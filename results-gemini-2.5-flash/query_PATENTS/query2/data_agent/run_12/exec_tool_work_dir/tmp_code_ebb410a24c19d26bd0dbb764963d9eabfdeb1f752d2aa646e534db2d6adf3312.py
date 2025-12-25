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
    import re
    match = re.search(r'\b([A-Z]{2})[\s-]\d{4,}', patent_info)
    if match:
        return match.group(1)
    if "Germany" in patent_info or "German patent" in patent_info: return "DE"
    if "US patent" in patent_info: return "US"
    if "EP patent" in patent_info: return "EP"
    if "WO patent" in patent_info: return "WO"
    return None

file_path = locals()["var_function-call-12873615387478038273"]
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df["grant_date_parsed"] = df["grant_date"].apply(parse_date_robust)
df["filing_date_parsed"] = df["filing_date"].apply(parse_date_robust)
df["country_code"] = df["Patents_info"].apply(extract_country_code_optimized)

filtered_df = df[
    (df["grant_date_parsed"].dt.year == 2019) &
    (df["grant_date_parsed"].dt.month >= 7) &
    (df["country_code"] == "DE")
].copy()

processed_records = []
for _, row in filtered_df.iterrows():
    try:
        cpc_list = json.loads(row["cpc"])
        filing_year = row["filing_date_parsed"].year if pd.notna(row["filing_date_parsed"]) else None
        title_localized = row["title_localized"]
        
        if filing_year is None:
            continue

        for cpc_item in cpc_list:
            cpc_code = cpc_item.get("code")
            if cpc_code and len(cpc_code) >= 4:
                # Parse title_localized to get the most suitable title here, reducing iterations later
                parsed_titles = json.loads(title_localized) if pd.notna(title_localized) else []
                full_title = next((item['text'] for item in parsed_titles if item.get('language') == 'en' and 'text' in item), 
                                  parsed_titles[0]['text'] if parsed_titles and isinstance(parsed_titles[0], dict) and 'text' in parsed_titles[0] else None)
                
                if full_title:
                    processed_records.append({
                        "cpc_group": cpc_code[:4],
                        "filing_year": filing_year,
                        "full_title": full_title
                    })
    except (json.JSONDecodeError, TypeError):
        continue

cpc_processed_df = pd.DataFrame(processed_records)

# Calculate yearly filings for EMA
yearly_filings = cpc_processed_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# Calculate EMA
alpha = 0.1
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Find the best year for each CPC group based on EMA
best_years_ema = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# Get the most frequent full title for each cpc_group from the processed data
title_map = cpc_processed_df.groupby('cpc_group')['full_title'].apply(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index(name='most_frequent_title')

# Merge with the best_years_ema DataFrame
final_result_df = pd.merge(best_years_ema, title_map, on='cpc_group', how='left')

# Select and rename columns for final output
final_result_df = final_result_df[['cpc_group', 'most_frequent_title', 'filing_year']]
final_result_df = final_result_df.rename(columns={
    'cpc_group': 'CPC group code',
    'most_frequent_title': 'Full Title',
    'filing_year': 'Best Year'
})

print("__RESULT__:")
print(final_result_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)
