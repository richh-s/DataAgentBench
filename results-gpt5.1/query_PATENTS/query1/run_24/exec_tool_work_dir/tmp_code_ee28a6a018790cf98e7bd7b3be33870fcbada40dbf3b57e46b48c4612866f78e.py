code = """import json, pandas as pd, datetime
from datetime import datetime

# Load full large results
with open(var_call_8yfQNBECApkiGyQZabmS785J, 'r') as f:
    pub_data = json.load(f)
with open(var_call_hmgZFiJtipf5XZEPOZEY4ohT, 'r') as f:
    lvl5_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    try:
        return datetime.strptime(s.strip(), '%b %dth, %Y').year
    except Exception:
        try:
            return datetime.strptime(s.strip(), '%B %dth, %Y').year
        except Exception:
            try:
                # handle st, nd, rd, th generically
                parts = s.replace('st','').replace('nd','').replace('rd','').replace('th','')
                return datetime.strptime(parts.strip(), '%b %d, %Y').year
            except Exception:
                try:
                    return datetime.strptime(parts.strip(), '%B %d, %Y').year
                except Exception:
                    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)

# Keep years up to 2022
pub_df = pub_df[pub_df['year'].notnull() & (pub_df['year'] <= 2022)]

# Explode CPC codes
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

# Aggregate counts per symbol per year
yearly_counts = cpc_df.groupby(['symbol','year']).size().reset_index(name='count')

# For EMA we need continuous years per symbol
symbols = yearly_counts['symbol'].unique()
results = []
alpha = 0.2

for sym in symbols:
    sub = yearly_counts[yearly_counts['symbol']==sym].set_index('year').sort_index()
    # reindex to continuous range
    years = range(sub.index.min(), sub.index.max()+1)
    sub = sub.reindex(years).fillna(0)
    ema = None
    for y, row in sub['count'].items():
        if ema is None:
            ema = row
        else:
            ema = alpha*row + (1-alpha)*ema
        results.append({'symbol': sym, 'year': int(y), 'ema': float(ema)})

ema_df = pd.DataFrame(results)

# For each year, find max EMA and symbols achieving it
best_per_year = ema_df.loc[ema_df.groupby('year')['ema'].idxmax()].copy()

# Restrict to year 2022
best_2022 = best_per_year[best_per_year['year']==2022]

# Level-5 symbols list
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
