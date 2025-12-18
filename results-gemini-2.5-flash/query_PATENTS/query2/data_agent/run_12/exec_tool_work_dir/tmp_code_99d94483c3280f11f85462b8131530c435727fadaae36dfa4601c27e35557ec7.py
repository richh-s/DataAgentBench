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

df = pd.DataFrame(data)

df["grant_date_parsed"] = df["grant_date"].apply(parse_date_robust)
df["filing_date_parsed"] = df["filing_date"].apply(parse_date_robust)
df["country_code"] = df["Patents_info"].apply(extract_country_code_optimized)

filtered_df = df[
    (df["grant_date_parsed"].dt.year == 2019) &
    (df["grant_date_parsed"].dt.month >= 7) &
    (df["country_code"] == "DE")
].copy()

processed_data = []
for _, row in filtered_df.iterrows():
    filing_year = row["filing_date_parsed"].year if pd.notna(row["filing_date_parsed"]) else None
    if filing_year is None:
        continue

    cpc_list = []
    try:
        cpc_list = json.loads(row["cpc"])
    except (json.JSONDecodeError, TypeError):
        pass

    title_parsed = []
    try:
        title_parsed = json.loads(row["title_localized"])
    except (json.JSONDecodeError, TypeError):
        pass
    
    full_title = None
    if title_parsed:
        for title_item in title_parsed:
            if isinstance(title_item, dict) and title_item.get('language') == 'en' and 'text' in title_item:
                full_title = title_item['text']
                break
        if full_title is None and isinstance(title_parsed[0], dict) and 'text' in title_parsed[0]:
            full_title = title_parsed[0]['text']

    if full_title is None:
        continue

    for cpc_item in cpc_list:
        cpc_code = cpc_item.get("code")
        if cpc_code and len(cpc_code) >= 4:
            processed_data.append({
                "cpc_group": cpc_code[:4],
                "filing_year": filing_year,
                "full_title": full_title
            })

cpc_processed_df = pd.DataFrame(processed_data)

print("__RESULT__:")
print(cpc_processed_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)
