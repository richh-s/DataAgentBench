code = """import json
import pandas as pd

# Load full results from files
with open(var_call_agaNUoweFpJpZS4Hob5lUHmp, 'r') as f:
    pub_data = json.load(f)
with open(var_call_pqM6m0fsJvImEDmjWZeiiMW8, 'r') as f:
    cpc_def_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

def extract_year(date_str):
    for token in str(date_str).split():
        if token.strip(',').isdigit() and len(token.strip(',')) == 4:
            y = int(token.strip(',').replace(',', ''))
            if 2000 <= y <= 2100:
                return y
    return None

pub_df['year'] = pub_df['publication_date'].apply(extract_year)

pub_df = pub_df[pub_df['year'].isin([2020, 2021, 2022])]

records = []
for _, row in pub_df.iterrows():
    year = row['year']
    try:
        cpcs = json.loads(row['cpc'])
    except Exception:
        continue
    codes = set([c.get('code') for c in cpcs if isinstance(c, dict) and c.get('code')])
    for code in codes:
        records.append({'code': code, 'year': year})

codes_df = pd.DataFrame(records)
if codes_df.empty:
    result = []
else:
    counts = codes_df.groupby(['code', 'year']).size().reset_index(name='count')

    years = [2020, 2021, 2022]
    alpha = 0.2
    ema_records = []

    for code, grp in counts.groupby('code'):
        year_counts = {y: 0 for y in years}
        for _, r in grp.iterrows():
            year_counts[r['year']] = r['count']
        ema_prev = year_counts[2020]
        ema_vals = {2020: ema_prev}
        for y in [2021, 2022]:
            ema_prev = alpha * year_counts[y] + (1-alpha) * ema_prev
            ema_vals[y] = ema_prev
        best_year = max(ema_vals, key=lambda y: ema_vals[y])
        if best_year == 2022:
            ema_records.append({'code': code, 'ema_2020': ema_vals[2020], 'ema_2021': ema_vals[2021], 'ema_2022': ema_vals[2022]})

    ema_df = pd.DataFrame(ema_records)

    cpc_def_df = pd.DataFrame(cpc_def_data)
    level5 = set(cpc_def_df['symbol'].astype(str).tolist())

    ema_df = ema_df[ema_df['code'].isin(level5)]

    ema_df = ema_df.sort_values('ema_2022', ascending=False)

    result = ema_df['code'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_agaNUoweFpJpZS4Hob5lUHmp': 'file_storage/call_agaNUoweFpJpZS4Hob5lUHmp.json', 'var_call_pqM6m0fsJvImEDmjWZeiiMW8': 'file_storage/call_pqM6m0fsJvImEDmjWZeiiMW8.json', 'var_call_0rDbwvEvRRhRTgvg0Z5D218g': 'file_storage/call_0rDbwvEvRRhRTgvg0Z5D218g.json'}

exec(code, env_args)
