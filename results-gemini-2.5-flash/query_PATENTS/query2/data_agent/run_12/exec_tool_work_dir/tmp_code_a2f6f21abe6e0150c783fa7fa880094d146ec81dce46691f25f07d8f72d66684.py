code = """import pandas as pd
import json
import re

def parse_date_robust(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    date_str = date_str.lower()
    date_str = date_str.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
    month_replacements = {
        "january": "jan", "february": "feb", "march": "mar", "april": "apr", "may": "may", "june": "jun",
        "july": "jul", "august": "aug", "september": "sep", "october": "oct", "november": "nov", "december": "dec"
    }
    for full, abbr in month_replacements.items():
        date_str = date_str.replace(full, abbr)
    date_str = date_str.replace("dated", "").replace("of", "").replace(",", "").replace(".", "").strip()

    for fmt in ["%d %b %Y", "%b %d %Y", "%Y %b %d", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%b %Y", "%Y"]:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            pass
    return pd.NaT

def extract_country_code_optimized(patent_info):
    if not isinstance(patent_info, str):
        return None
    match = re.search(r'\b([A-Z]{2})[\s-]\d{4,}', patent_info)
    if match:
        return match.group(1)
    if "Germany" in patent_info or "German patent" in patent_info: return "DE"
    if "US patent" in patent_info: return "US"
    if "EP patent" in patent_info: return "EP"
    if "WO patent" in patent_info: return "WO"
    return None

# Load the full data once
file_path = locals()["var_function-call-10977132411253422251"]
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Step 1: Parse dates and extract country codes
df["grant_date_parsed"] = df["grant_date"].apply(parse_date_robust)
df["filing_date_parsed"] = df["filing_date"].apply(parse_date_robust)
df["country_code"] = df["Patents_info"].apply(extract_country_code_optimized)

# Step 2: Filter for relevant patents based on grant date and country code
filtered_df = df[
    (df["grant_date_parsed"].dt.year == 2019) &
    (df["grant_date_parsed"].dt.month >= 7) &
    (df["country_code"] == "DE")
].copy()

# Drop original raw date and patent info columns to save memory early
filtered_df = filtered_df.drop(columns=['grant_date', 'filing_date', 'Patents_info', 'grant_date_parsed', 'country_code'], errors='ignore')

# Step 3: Process CPC codes and titles
# Safely parse JSON strings into lists of dictionaries for CPC and titles
filtered_df['cpc_parsed'] = filtered_df['cpc'].apply(lambda x: json.loads(x) if isinstance(x, str) else [])
filtered_df['titles_parsed'] = filtered_df['title_localized'].apply(lambda x: json.loads(x) if isinstance(x, str) else [])

# Explode the 'cpc_parsed' column to have one row per CPC code
exploded_df = filtered_df.explode('cpc_parsed')

# Extract CPC group (first 4 characters) and filter for valid entries
exploded_df['cpc_group'] = exploded_df['cpc_parsed'].apply(lambda x: x.get('code')[:4] if isinstance(x, dict) and x.get('code') and len(x['code']) >= 4 else None)
exploded_df = exploded_df.dropna(subset=['cpc_group'])

# Extract filing year and drop rows with missing filing year (should be minimal after initial filtering)
exploded_df['filing_year'] = exploded_df['filing_date_parsed'].dt.year.astype(int, errors='ignore') # Cast to int
exploded_df = exploded_df.dropna(subset=['filing_year'])

# Extract the most suitable title (English first, then first available)
exploded_df['full_title'] = exploded_df['titles_parsed'].apply(lambda x:
    next((item['text'] for item in x if item.get('language') == 'en' and 'text' in item), 
         x[0]['text'] if x and isinstance(x[0], dict) and 'text' in x[0] else None)
)
exploded_df = exploded_df.dropna(subset=['full_title'])

# Drop intermediate parsing columns and original raw columns no longer needed
exploded_df = exploded_df.drop(columns=['cpc', 'title_localized', 'cpc_parsed', 'titles_parsed', 'filing_date_parsed'], errors='ignore')

# Step 4: Calculate yearly filings for EMA
yearly_filings = exploded_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# Step 5: Calculate EMA
alpha = 0.1
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Step 6: Find the best year for each CPC group based on EMA
best_years_ema = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# Step 7: Get the most frequent full title for each CPC group
title_map = exploded_df.groupby('cpc_group')['full_title'].apply(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index(name='most_frequent_title')

# Step 8: Merge results and format for final output
final_result_df = pd.merge(best_years_ema, title_map, on='cpc_group', how='left')

# Select and rename columns for final output
final_result_df = final_result_df[['cpc_group', 'most_frequent_title', 'filing_year']]
final_result_df = final_result_df.rename(columns={
    'cpc_group': 'CPC group code',
    'most_frequent_title': 'Full Title',
    'filing_year': 'Best Year'
})

print("__RESULT__:
" + final_result_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json', 'var_function-call-3734399808846831582': 'file_storage/function-call-3734399808846831582.json', 'var_function-call-10977132411253422251': 'file_storage/function-call-10977132411253422251.json'}

exec(code, env_args)
