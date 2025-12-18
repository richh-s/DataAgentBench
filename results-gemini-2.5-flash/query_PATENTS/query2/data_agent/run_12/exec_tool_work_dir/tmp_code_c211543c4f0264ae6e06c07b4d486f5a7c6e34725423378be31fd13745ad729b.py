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

# Initial processing to filter and extract minimal necessary data
filtered_and_extracted_data = []

with open(file_path, 'r') as f:
    data = json.load(f)

for record in data:
    grant_date_str = record.get("grant_date")
    filing_date_str = record.get("filing_date")
    patents_info_str = record.get("Patents_info")

    grant_date_parsed = parse_date_robust(grant_date_str)
    filing_date_parsed = parse_date_robust(filing_date_str)
    country_code = extract_country_code_optimized(patents_info_str)

    if pd.isna(grant_date_parsed) or pd.isna(filing_date_parsed) or country_code != "DE":
        continue

    if not (grant_date_parsed.year == 2019 and grant_date_parsed.month >= 7):
        continue

    # Only store the raw cpc and title_localized, and the filing year
    filtered_and_extracted_data.append({
        "cpc_raw": record.get("cpc"),
        "filing_year": filing_date_parsed.year,
        "title_localized_raw": record.get("title_localized")
    })

print("__RESULT__:")
print(json.dumps(filtered_and_extracted_data))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json', 'var_function-call-3734399808846831582': 'file_storage/function-call-3734399808846831582.json'}

exec(code, env_args)
