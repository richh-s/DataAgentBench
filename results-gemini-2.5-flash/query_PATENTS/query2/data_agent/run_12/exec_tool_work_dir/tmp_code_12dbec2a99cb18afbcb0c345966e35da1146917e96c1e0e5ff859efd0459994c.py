code = """import pandas as pd
import json
import re
from collections import defaultdict, Counter

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

file_path = locals()["var_function-call-1303477139949817039"]

yearly_filings_counts = defaultdict(lambda: defaultdict(int))
cpc_group_titles_counter = defaultdict(Counter)

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

    if pd.isna(grant_date_parsed) or pd.isna(filing_date_parsed) or country_code != "DE":
        continue

    if not (grant_date_parsed.year == 2019 and grant_date_parsed.month >= 7):
        continue

    filing_year = filing_date_parsed.year

    cpc_list = []
    try:
        cpc_list = json.loads(cpc_raw)
    except (json.JSONDecodeError, TypeError):
        pass

    title_parsed = []
    try:
        title_parsed = json.loads(title_localized_raw)
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
            cpc_group = cpc_code[:4]
            yearly_filings_counts[cpc_group][filing_year] += 1
            cpc_group_titles_counter[cpc_group][full_title] += 1

yearly_filings_data = []
for cpc_group, years_data in yearly_filings_counts.items():
    for year, count in years_data.items():
        yearly_filings_data.append({"cpc_group": cpc_group, "filing_year": year, "filings": count})

yearly_filings_df = pd.DataFrame(yearly_filings_data)

alpha = 0.1
yearly_filings_df = yearly_filings_df.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings_df["ema"] = yearly_filings_df.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

best_years_ema = yearly_filings_df.loc[yearly_filings_df.groupby("cpc_group")["ema"].idxmax()].reset_index(drop=True)

most_frequent_titles = []
for cpc_group, counter in cpc_group_titles_counter.items():
    if counter:
        most_frequent_title = counter.most_common(1)[0][0]
        most_frequent_titles.append({"cpc_group": cpc_group, "most_frequent_title": most_frequent_title})

title_map_df = pd.DataFrame(most_frequent_titles)

final_result_df = pd.merge(best_years_ema, title_map_df, on='cpc_group', how='left')

final_result_df = final_result_df[['cpc_group', 'most_frequent_title', 'filing_year']]
final_result_df = final_result_df.rename(columns={
    'cpc_group': 'CPC group code',
    'most_frequent_title': 'Full Title',
    'filing_year': 'Best Year'
})

print("__RESULT__:")
print(final_result_df.to_json(orient="records"))"""

env_args = {'var_function-call-254829674187600523': ['cpc_definition'], 'var_function-call-12873615387478038273': 'file_storage/function-call-12873615387478038273.json', 'var_function-call-3734399808846831582': 'file_storage/function-call-3734399808846831582.json', 'var_function-call-10977132411253422251': 'file_storage/function-call-10977132411253422251.json', 'var_function-call-1303477139949817039': 'file_storage/function-call-1303477139949817039.json'}

exec(code, env_args)
