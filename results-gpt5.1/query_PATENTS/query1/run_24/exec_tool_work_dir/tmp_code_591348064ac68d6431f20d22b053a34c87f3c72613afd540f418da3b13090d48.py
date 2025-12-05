code = """import json, pandas as pd

# Load a subset of publication data to reduce processing
with open(var_call_8yfQNBECApkiGyQZabmS785J, 'r') as f:
    pub_data = json.load(f)

# Limit to records with publication dates from 2010 onwards to reduce size
from datetime import datetime

def parse_year_quick(s):
    try:
        parts = s.replace('st','').replace('nd','').replace('rd','').replace('th','')
        return datetime.strptime(parts.strip(), '%b %d, %Y').year
    except Exception:
        try:
            return datetime.strptime(parts.strip(), '%B %d, %Y').year
        except Exception:
            return None

filtered = []
for rec in pub_data:
    y = parse_year_quick(rec.get('publication_date',''))
    if y is not None and y <= 2022:
        rec['year'] = y
        filtered.append(rec)

pub_df = pd.DataFrame(filtered)

records = []
for _, row in pub_df.iterrows():
    year = int(row['year'])
    cpc_raw = row['cpc']
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if code:
            records.append({'year': year, 'symbol': code})

cpc_df = pd.DataFrame(records)

# Aggregate counts
yearly_counts = cpc_df.groupby(['symbol','year']).size().reset_index(name='count')

alpha = 0.2
results = []
for sym, sub in yearly_counts.groupby('symbol'):
    sub = sub.sort_values('year').set_index('year')
    years = range(sub.index.min(), sub.index.max()+1)
    sub = sub.reindex(years).fillna(0)
    ema = None
    for y, v in sub['count'].items():
        if ema is None:
            ema = v
        else:
            ema = alpha*v + (1-alpha)*ema
        results.append({'symbol': sym, 'year': int(y), 'ema': float(ema)})

ema_df = pd.DataFrame(results)

best_per_year = ema_df.loc[ema_df.groupby('year')['ema'].idxmax()].copy()

best_2022 = best_per_year[best_per_year['year']==2022]

with open(var_call_hmgZFiJtipf5XZEPOZEY4ohT, 'r') as f:
    lvl5_data = json.load(f)

lvl5_df = pd.DataFrame(lvl5_data)
lvl5_symbols = set(lvl5_df['symbol'])

best_2022_lvl5 = best_2022[best_2022['symbol'].isin(lvl5_symbols)]

result_symbols = sorted(best_2022_lvl5['symbol'].unique())

import json as _json
out = _json.dumps(result_symbols)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8yfQNBECApkiGyQZabmS785J': 'file_storage/call_8yfQNBECApkiGyQZabmS785J.json', 'var_call_hmgZFiJtipf5XZEPOZEY4ohT': 'file_storage/call_hmgZFiJtipf5XZEPOZEY4ohT.json', 'var_call_QwMXpMPf4V3SpbwPHsUXWmRS': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}]}

exec(code, env_args)
