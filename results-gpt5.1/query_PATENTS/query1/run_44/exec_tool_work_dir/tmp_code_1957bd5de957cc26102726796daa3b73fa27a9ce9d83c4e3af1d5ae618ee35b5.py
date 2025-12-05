code = """import json, pandas as pd

file_path_pub = var_call_vUnhcYy7ruX2NJeUrALEw6s3

with open(file_path_pub, 'r') as f:
    pub_data = json.load(f)

# Sample a subset to avoid timeout
pub_data_sample = pub_data  # assuming manageable size now

df_pub = pd.DataFrame(pub_data_sample)

from datetime import datetime

def get_year_simple(date_str):
    try:
        return datetime.strptime(date_str.split(',')[-1].strip(), '%Y').year
    except Exception:
        parts = date_str.strip().split(' ')
        for p in reversed(parts):
            if p.rstrip('stndrh,').isdigit():
                y = int(p.rstrip('stndrh,'))
                if 1900 <= y <= 2100:
                    return y
        return None

df_pub['year'] = df_pub['publication_date'].apply(get_year_simple)
df_pub = df_pub.dropna(subset=['year'])
df_pub['year'] = df_pub['year'].astype(int)

records = []
for _, row in df_pub.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    year = row['year']
    for entry in cpc_list:
        code = entry.get('code')
        if code:
            records.append({'code': code, 'year': year})

codes_df = pd.DataFrame(records)

annual_counts = codes_df.groupby(['code', 'year']).size().reset_index(name='count')

alpha = 0.2
ema_records = []
for code, grp in annual_counts.groupby('code'):
    grp = grp.sort_values('year')
    ema = None
    for _, r in grp.iterrows():
        if ema is None:
            ema = r['count']
        else:
            ema = alpha * r['count'] + (1 - alpha) * ema
        ema_records.append({'code': code, 'year': int(r['year']), 'ema': float(ema)})

ema_df = pd.DataFrame(ema_records)

best_years = ema_df.sort_values(['code', 'ema', 'year'], ascending=[True, False, True]).groupby('code').first().reset_index()

best_2022_codes = best_years[best_years['year'] == 2022]['code'].tolist()

file_path_cpc = var_call_ZdvC1SOIoljQWH4ZpNNeusDu
with open(file_path_cpc, 'r') as f:
    cpc_defs = json.load(f)

cpc_df = pd.DataFrame(cpc_defs)
level5_symbols = set(cpc_df['symbol'].tolist())

result_codes = [c for c in best_2022_codes if c in level5_symbols]

result = json.dumps(result_codes)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_vUnhcYy7ruX2NJeUrALEw6s3': 'file_storage/call_vUnhcYy7ruX2NJeUrALEw6s3.json', 'var_call_ZdvC1SOIoljQWH4ZpNNeusDu': 'file_storage/call_ZdvC1SOIoljQWH4ZpNNeusDu.json'}

exec(code, env_args)
