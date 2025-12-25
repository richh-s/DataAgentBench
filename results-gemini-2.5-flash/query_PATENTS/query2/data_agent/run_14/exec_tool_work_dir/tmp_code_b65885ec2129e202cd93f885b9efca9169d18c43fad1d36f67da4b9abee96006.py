code = """import pandas as pd
import json

data = pd.read_json(locals()['var_function-call-12286119263325599604'])

def parse_date(date_str):
    if isinstance(date_str, str):
        date_str = date_str.replace("th", "").replace("rd", "").replace("nd", "").replace("st", "").replace("on ", "").replace(",", "")
        try:
            return pd.to_datetime(date_str, format="%B %d %Y", errors='coerce')
        except ValueError:
            try:
                return pd.to_datetime(date_str, format="%d %B %Y", errors='coerce')
            except ValueError:
                try:
                    return pd.to_datetime(date_str, format="%Y %B %d", errors='coerce')
                except ValueError:
                    return pd.to_datetime(date_str, errors='coerce')
    return pd.NaT

data['parsed_grant_date'] = data['grant_date'].apply(parse_date)
data['parsed_filing_date'] = data['filing_date'].apply(parse_date)

filtered_data = data[
    (data['parsed_grant_date'].dt.year == 2019) &
    (data['parsed_grant_date'].dt.month >= 7) &
    (data['Patents_info'].str.contains('from DE', na=False))
]

cpc_filings = []
for _, row in filtered_data.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group = code[:4]
                filing_year = row['parsed_filing_date'].year
                if not pd.isna(filing_year):
                    cpc_filings.append({'cpc_group': cpc_group, 'filing_year': int(filing_year)})
    except (json.JSONDecodeError, TypeError):
        continue

filings_df = pd.DataFrame(cpc_filings)

# Group by CPC group and filing year to count patents
yearly_filings = filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='count')

# Pivot to have years as columns for easier EMA calculation
pivot_df = yearly_filings.pivot(index='cpc_group', columns='filing_year', values='count').fillna(0)

alpha = 0.1
ema_results = {}

for cpc_group in pivot_df.index:
    ema_values = {}
    current_ema = 0
    for year in sorted(pivot_df.columns):
        if year in pivot_df.columns:
            value = pivot_df.loc[cpc_group, year]
        else:
            value = 0
        current_ema = alpha * value + (1 - alpha) * current_ema
        ema_values[year] = current_ema
    ema_results[cpc_group] = ema_values

best_cpc_groups = []
for cpc_group, emas in ema_results.items():
    if emas:
        best_year = max(emas, key=emas.get)
        highest_ema = emas[best_year]
        best_cpc_groups.append({'cpc_group': cpc_group, 'best_year': best_year, 'highest_ema': highest_ema})

best_cpc_df = pd.DataFrame(best_cpc_groups).sort_values(by='highest_ema', ascending=False)

print("__RESULT__:")
print(best_cpc_df.to_json(orient='records'))"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json'}

exec(code, env_args)
