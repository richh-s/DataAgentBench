code = """import pandas as pd
import json

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce', dayfirst=True)
    except:
        try:
            return pd.to_datetime(date_str.replace('dated ', ''), errors='coerce', dayfirst=True)
        except:
            return pd.to_datetime(date_str, errors='coerce')


def extract_country_code(patent_info):
    if isinstance(patent_info, str):
        if "US patent" in patent_info or "US patent application" in patent_info:
            return "US"
        elif "German patent" in patent_info or "German patent application" in patent_info:
            return "DE"
        elif "GB patent" in patent_info or "GB patent application" in patent_info:
            return "GB"
        elif "JP patent" in patent_info or "JP patent application" in patent_info:
            return "JP"
        elif "KR patent" in patent_info or "KR patent application" in patent_info:
            return "KR"
        elif "CN patent" in patent_info or "CN patent application" in patent_info:
            return "CN"
        elif "EP patent" in patent_info or "EP patent application" in patent_info:
            return "EP"
        elif "WO patent" in patent_info or "WO patent application" in patent_info:
            return "WO"
    return None


results = pd.read_json(locals()['var_function-call-18001159190617317211'])

df = pd.DataFrame(results)

df['grant_date_parsed'] = df['grant_date'].apply(parse_date)
df['filing_date_parsed'] = df['filing_date'].apply(parse_date)
df['country_code'] = df['Patents_info'].apply(extract_country_code)

# Filter for patents granted in the second half of 2019 in Germany
start_date = pd.to_datetime('2019-07-01')
end_date = pd.to_datetime('2019-12-31')

filtered_df = df[(df['grant_date_parsed'] >= start_date) & (df['grant_date_parsed'] <= end_date) & (df['country_code'] == 'DE')].copy()

# Extract CPC level 4 codes and filing year
cpc_data = []
for index, row in filtered_df.iterrows():
    if row['cpc']:
        cpc_list = json.loads(row['cpc'])
        for cpc_entry in cpc_list:
            cpc_code = cpc_entry['code']
            if len(cpc_code) >= 4:
                cpc_group_level4 = cpc_code[:4]
                if pd.notna(row['filing_date_parsed']):
                    filing_year = row['filing_date_parsed'].year
                    cpc_data.append({'cpc_group_level4': cpc_group_level4, 'filing_year': filing_year})


cpc_df = pd.DataFrame(cpc_data)

# Calculate annual filing counts for each CPC group
filings_by_cpc_year = cpc_df.groupby(['cpc_group_level4', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.1
ema_results = []

for cpc_group in filings_by_cpc_year['cpc_group_level4'].unique():
    group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group_level4'] == cpc_group].sort_values(by='filing_year')
    group_df['ema'] = group_df['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    if not group_df.empty:
        best_year_row = group_df.loc[group_df['ema'].idxmax()]
        ema_results.append({
            'cpc_group_level4': cpc_group,
            'best_year': int(best_year_row['filing_year']),
            'highest_ema': best_year_row['ema']
        })

ema_df = pd.DataFrame(ema_results)

print("__RESULT__:")
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-18001159190617317211': 'file_storage/function-call-18001159190617317211.json'}

exec(code, env_args)
