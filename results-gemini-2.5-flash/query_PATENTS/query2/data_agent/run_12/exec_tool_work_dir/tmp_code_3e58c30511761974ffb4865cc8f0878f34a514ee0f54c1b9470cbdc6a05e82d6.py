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

def safe_json_loads(json_str):
    try:
        return json.loads(json_str) if pd.notna(json_str) else []
    except (json.JSONDecodeError, TypeError):
        return []

def get_best_title(title_list):
    if not isinstance(title_list, list):
        return None
    for title_item in title_list:
        if isinstance(title_item, dict) and title_item.get('language') == 'en' and 'text' in title_item:
            return title_item['text']
    if title_list and isinstance(title_list[0], dict) and 'text' in title_list[0]:
        return title_list[0]['text']
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

filtered_df['cpc_parsed'] = filtered_df['cpc'].apply(safe_json_loads)
filtered_df['titles_parsed'] = filtered_df['title_localized'].apply(safe_json_loads)

exploded_cpc_df = filtered_df.explode('cpc_parsed')
exploded_cpc_df = exploded_cpc_df[exploded_cpc_df['cpc_parsed'].apply(lambda x: isinstance(x, dict) and 'code' in x)]
exploded_cpc_df['cpc_group'] = exploded_cpc_df['cpc_parsed'].apply(lambda x: x['code'][:4] if len(x['code']) >= 4 else None)
exploded_cpc_df = exploded_cpc_df.dropna(subset=['cpc_group'])

exploded_cpc_df['filing_year'] = exploded_cpc_df['filing_date_parsed'].dt.year
exploded_cpc_df = exploded_cpc_df.dropna(subset=['filing_year'])

exploded_cpc_df['full_title'] = exploded_cpc_df['titles_parsed'].apply(get_best_title)
exploded_cpc_df = exploded_cpc_df.dropna(subset=['full_title'])

yearly_filings = exploded_cpc_df.groupby(["cpc_group", "filing_year"]).size().reset_index(name="filings")

alpha = 0.1
yearly_filings = yearly_filings.sort_values(by=['cpc_group', 'filing_year'])
yearly_filings["ema"] = yearly_filings.groupby("cpc_group")["filings"].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

best_years_ema = yearly_filings.loc[yearly_filings.groupby("cpc_group")["ema"].idxmax()]

title_map = exploded_cpc_df.groupby('cpc_group')['full_title'].apply(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index(name='most_frequent_title')

final_result_df = pd.merge(best_years_ema, title_map, on='cpc_group', how='left')

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
