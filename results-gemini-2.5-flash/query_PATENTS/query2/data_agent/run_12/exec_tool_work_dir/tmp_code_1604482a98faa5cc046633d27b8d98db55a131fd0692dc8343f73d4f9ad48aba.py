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

file_path = locals()["var_function-call-10977132411253422251"]

# --- Optimized Step 1: Filter and extract all necessary data in a single pass ---
final_cpc_data_list = []

with open(file_path, 'r') as f:
    data = json.load(f)

for record in data:
    grant_date_str = record.get("grant_date")
    filing_date_str = record.get("filing_date")
    patents_info_str = record.get("Patents_info")
    cpc_raw = record.get("cpc")
    title_localized_raw = record.get("title_localized")

    grant_date_parsed = parse_date_robust(grant_date_str)
    filing_date_parsed = parse_date_robust(filing_date_str)
    country_code = extract_country_code_optimized(patents_info_str)

    # Apply filtering conditions immediately to reduce data in memory
    if pd.isna(grant_date_parsed) or pd.isna(filing_date_parsed) or country_code != "DE":
        continue

    if not (grant_date_parsed.year == 2019 and grant_date_parsed.month >= 7):
        continue

    filing_year = filing_date_parsed.year

    # Safely parse CPC list
    cpc_list = []
    try:
        cpc_list = json.loads(cpc_raw)
    except (json.JSONDecodeError, TypeError):
        pass

    # Safely parse title_localized and extract the best available title
    title_parsed_list = []
    try:
        title_parsed_list = json.loads(title_localized_raw)
    except (json.JSONDecodeError, TypeError):
        pass
    
    full_title = None
    if title_parsed_list:
        for title_item in title_parsed_list:
            if isinstance(title_item, dict) and title_item.get('language') == 'en' and 'text' in title_item:
                full_title = title_item['text']
                break
        if full_title is None and isinstance(title_parsed_list[0], dict) and 'text' in title_parsed_list[0]:
            full_title = title_parsed_list[0]['text']

    if full_title is None:
        continue

    # Append each CPC group with its associated filing year and full title
    for cpc_item in cpc_list:
        cpc_code = cpc_item.get("code")
        if cpc_code and len(cpc_code) >= 4:
            final_cpc_data_list.append({
                "cpc_group": cpc_code[:4],
                "filing_year": filing_year,
                "full_title": full_title
            })

cpc_processed_df = pd.DataFrame(final_cpc_data_list)

# --- Step 2: Calculate yearly filings for EMA ---
yearly_filings = cpc_processed_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

# --- Step 3: Calculate EMA and find the best year ---
alpha = 0.1
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

best_years_ema = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

# --- Step 4: Get the most frequent full title for each CPC group ---
# This is done on the already filtered and processed `cpc_processed_df` for efficiency
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

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json', 'var_function-call-3734399808846831582': 'file_storage/function-call-3734399808846831582.json', 'var_function-call-10977132411253422251': 'file_storage/function-call-10977132411253422251.json'}

exec(code, env_args)
