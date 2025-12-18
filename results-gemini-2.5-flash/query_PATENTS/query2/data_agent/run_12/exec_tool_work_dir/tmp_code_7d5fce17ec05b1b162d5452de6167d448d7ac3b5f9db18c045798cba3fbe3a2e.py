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

file_path = locals()["var_function-call-3734399808846831582"]
with open(file_path, 'r') as f:
    data = json.load(f)

# --- Step 1: Filter records and extract basic information efficiently ---
# Instead of creating a large DataFrame immediately, process records in a loop
# and store only necessary, already parsed information.

initial_processed_records = []

for record in data:
    grant_date_str = record.get("grant_date")
    filing_date_str = record.get("filing_date")
    patents_info_str = record.get("Patents_info")

    grant_date_parsed = parse_date_robust(grant_date_str)
    filing_date_parsed = parse_date_robust(filing_date_str)
    country_code = extract_country_code_optimized(patents_info_str)

    # Filter records early based on grant date and country code
    if (pd.notna(grant_date_parsed) and grant_date_parsed.year == 2019 and grant_date_parsed.month >= 7) and \
       (pd.notna(filing_date_parsed)) and (country_code == "DE"):
        
        # Now, safely parse CPC and title_localized for this specific record
        cpc_list = []
        try:
            cpc_list = json.loads(record.get("cpc"))
        except (json.JSONDecodeError, TypeError):
            pass

        title_list = []
        try:
            title_list = json.loads(record.get("title_localized"))
        except (json.JSONDecodeError, TypeError):
            pass

        full_title = None
        if title_list:
            for title_item in title_list:
                if isinstance(title_item, dict) and title_item.get('language') == 'en' and 'text' in title_item:
                    full_title = title_item['text']
                    break
            if full_title is None and isinstance(title_list[0], dict) and 'text' in title_list[0]:
                full_title = title_list[0]['text']

        if full_title is None:
            continue # Skip if no suitable title is found

        for cpc_item in cpc_list:
            cpc_code = cpc_item.get("code")
            if cpc_code and len(cpc_code) >= 4:
                initial_processed_records.append({
                    "cpc_group": cpc_code[:4],
                    "filing_year": filing_date_parsed.year,
                    "full_title": full_title
                })

# Create a DataFrame from the carefully filtered and processed records
cpc_processed_df = pd.DataFrame(initial_processed_records)

# --- Step 2: Calculate yearly filings and EMA ---
yearly_filings = cpc_processed_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

alpha = 0.1
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# --- Step 3: Find the best year for each CPC group based on EMA ---
best_years_ema = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# --- Step 4: Get the most frequent full title for each CPC group ---
title_map = cpc_processed_df.groupby('cpc_group')['full_title'].apply(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index(name='most_frequent_title')

# --- Step 5: Merge results and format for final output ---
final_result_df = pd.merge(best_years_ema, title_map, on='cpc_group', how='left')

final_result_df = final_result_df[['cpc_group', 'most_frequent_title', 'filing_year']]
final_result_df = final_result_df.rename(columns={
    'cpc_group': 'CPC group code',
    'most_frequent_title': 'Full Title',
    'filing_year': 'Best Year'
})

print("__RESULT__:")
print(final_result_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json', 'var_function-call-3734399808846831582': 'file_storage/function-call-3734399808846831582.json'}

exec(code, env_args)
