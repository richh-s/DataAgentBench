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

    # Attempt to parse common formats
    for fmt in ["%d %b %Y", "%b %d %Y", "%Y %b %d", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%b %Y"]:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            pass
    return pd.NaT

def extract_country_code_optimized(patent_info):
    if not isinstance(patent_info, str):
        return None
    # Optimized regex to capture two uppercase letters followed by a non-word character (space, hyphen) and digits
    import re
    match = re.search(r'\b([A-Z]{2})[\\s-]?\\d+', patent_info)
    if match: # This pattern often captures the country code for the publication number.
        return match.group(1)
    # Specific patterns for country mentions if the above fails to give the desired result consistently
    if "US patent" in patent_info: return "US"
    if "DE patent" in patent_info or "German patent" in patent_info: return "DE"
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

all_cpc_codes_and_titles = []
for index, row in filtered_df.iterrows():
    try:
        cpc_list = json.loads(row["cpc"])
        for cpc_item in cpc_list:
            cpc_code = cpc_item["code"]
            if len(cpc_code) >= 4:
                cpc_group = cpc_code[:4]
                all_cpc_codes_and_titles.append({
                    "cpc_group": cpc_group,
                    "filing_year": row["filing_date_parsed"].year,
                    "title_localized": row["title_localized"]
                })
    except (json.JSONDecodeError, TypeError):
        continue

cpc_data = pd.DataFrame(all_cpc_codes_and_titles)
print("__RESULT__:")
print(cpc_data.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json'}

exec(code, env_args)
