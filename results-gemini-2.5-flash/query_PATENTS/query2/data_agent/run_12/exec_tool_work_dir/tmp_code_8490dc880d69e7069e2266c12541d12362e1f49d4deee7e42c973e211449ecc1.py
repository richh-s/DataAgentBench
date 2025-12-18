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

file_path = locals()["var_function-call-12873615387478038273"]
with open(file_path, 'r') as f:
    data = json.load(f)

# Step 1: Initial Filtering and Data Extraction
# Iterate through records and filter/extract only necessary data points directly.
processed_records_step1 = []

for record in data:
    grant_date_str = record.get("grant_date")
    filing_date_str = record.get("filing_date")
    patents_info_str = record.get("Patents_info")
    cpc_raw = record.get("cpc")
    title_localized_raw = record.get("title_localized")

    grant_date_parsed = parse_date_robust(grant_date_str)
    filing_date_parsed = parse_date_robust(filing_date_str)
    country_code = extract_country_code_optimized(patents_info_str)

    # Apply filtering conditions immediately
    if pd.notna(grant_date_parsed) and pd.notna(filing_date_parsed) and country_code == "DE":
        if grant_date_parsed.year == 2019 and grant_date_parsed.month >= 7:
            # Append only the essential raw data for further processing
            processed_records_step1.append({
                "cpc": cpc_raw,
                "filing_year": filing_date_parsed.year, # Store year directly
                "title_localized": title_localized_raw
            })

# Convert the filtered and partially processed data to a DataFrame
intermediate_df = pd.DataFrame(processed_records_step1)

print("__RESULT__:")
print(intermediate_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)
