code = """import pandas as pd
import json

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
    import re
    # Match two uppercase letters directly before a publication/application number pattern
    match = re.search(r'([A-Z]{2})[- ]\d{2,}', patent_info) # e.g., US-2019... or DE 12345
    if match:
        return match.group(1)
    # Check for specific country mentions in the string
    if "US patent" in patent_info: return "US"
    if "DE patent" in patent_info or "German patent" in patent_info: return "DE"
    if "EP patent" in patent_info: return "EP"
    if "WO patent" in patent_info: return "WO"
    return None


file_path = locals()["var_function-call-12873615387478038273"]
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Step 1: Initial parsing of dates and country codes
df["grant_date_parsed"] = df["grant_date"].apply(parse_date_robust)
df["filing_date_parsed"] = df["filing_date"].apply(parse_date_robust)
df["country_code"] = df["Patents_info"].apply(extract_country_code_optimized)

# Step 2: Filter for relevant patents
filtered_df = df[
    (df["grant_date_parsed"].dt.year == 2019) &
    (df["grant_date_parsed"].dt.month >= 7) &
    (df["country_code"] == "DE")
].copy()

# Step 3: Extract CPC groups and titles more efficiently
# Apply json.loads to cpc and title_localized columns first
filtered_df['cpc_parsed'] = filtered_df['cpc'].apply(lambda x: json.loads(x) if pd.notna(x) else [])
filtered_df['title_parsed'] = filtered_df['title_localized'].apply(lambda x: json.loads(x) if pd.notna(x) else [])


# Explode the cpc_parsed column to get one row per CPC code
cpc_data = filtered_df.explode('cpc_parsed')

# Extract CPC group (first 4 characters) and filter for valid codes
cpc_data['cpc_group'] = cpc_data['cpc_parsed'].apply(lambda x: x['code'][:4] if isinstance(x, dict) and 'code' in x and len(x['code']) >= 4 else None)
cpc_data = cpc_data.dropna(subset=['cpc_group'])

# Extract English titles, or the first available title if English is not present
cpc_data['full_title'] = cpc_data['title_parsed'].apply(lambda x: next((item['text'] for item in x if item.get('language') == 'en'), x[0]['text'] if x else None) if isinstance(x, list) else None)

# Keep only necessary columns for further processing
final_cpc_data = cpc_data[['cpc_group', 'filing_date_parsed', 'full_title']].copy()
final_cpc_data['filing_year'] = final_cpc_data['filing_date_parsed'].dt.year

# Step 4: Calculate yearly filings
yearly_filings = final_cpc_data.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# Step 5: Calculate EMA
alpha = 0.1
# Sort by year within each group to ensure correct EMA calculation
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Step 6: Find the best year for each CPC group based on EMA
best_years = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# Step 7: Get the most frequent full title for each CPC group
# Group by cpc_group and find the mode of 'full_title'
# Ensure 'full_title' is not None before finding mode
title_mapping = final_cpc_data[final_cpc_data['full_title'].notna()].groupby('cpc_group')['full_title'].apply(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index(name='most_frequent_title')

# Merge with the best_years DataFrame
result_df = pd.merge(best_years, title_mapping, on='cpc_group', how='left')

# Format the final output
result_df = result_df[['cpc_group', 'most_frequent_title', 'filing_year', 'ema']]
result_df = result_df.rename(columns={'cpc_group': 'CPC group code', 'most_frequent_title': 'Full Title', 'filing_year': 'Best Year'})

print("__RESULT__:")
print(result_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)
