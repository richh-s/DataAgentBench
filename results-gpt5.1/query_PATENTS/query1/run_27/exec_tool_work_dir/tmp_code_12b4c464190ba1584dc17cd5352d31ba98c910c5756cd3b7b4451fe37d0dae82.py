code = """import json, pandas as pd, datetime as dt

# Load full publication data
with open(var_call_n6QpmquHkibhcJA3ZY7kSMRL, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    parts = s.replace(',', '').split()
    if len(parts) < 3:
        return None
    mon = parts[0][:3]
    year = parts[-1]
    try:
        return int(year)
    except:
        return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Extract CPC codes per publication
codes_rows = []
for _, row in pub_df.iterrows():
    year = row['year']
    cpc_raw = row['cpc']
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        codes_rows.append({'symbol': code, 'year': year})

codes_df = pd.DataFrame(codes_rows)

# Aggregate counts per symbol-year
counts = codes_df.groupby(['symbol','year']).size().reset_index(name='count')

# Pivot to have years as rows, symbols as columns for EMA
years_sorted = sorted(counts['year'].unique())

# Compute EMA per symbol over years
alpha = 0.2

ema_records = []
for symbol, grp in counts.groupby('symbol'):
    grp = grp.set_index('year').reindex(years_sorted, fill_value=0).sort_index()
    ema = None
    for y, cnt in grp['count'].items():
        if ema is None:
            ema = cnt
        else:
            ema = alpha*cnt + (1-alpha)*ema
        ema_records.append({'symbol': symbol, 'year': int(y), 'ema': float(ema)})

ema_df = pd.DataFrame(ema_records)

# Determine best EMA year for each symbol
idx = ema_df.groupby('symbol')['ema'].idxmax()
best_df = ema_df.loc[idx].reset_index(drop=True)

# Filter to best year = 2022
best_2022 = best_df[best_df['year'] == 2022]

symbols_2022 = sorted(best_2022['symbol'].unique())

import json as _json
result = _json.dumps(symbols_2022)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_n6QpmquHkibhcJA3ZY7kSMRL': 'file_storage/call_n6QpmquHkibhcJA3ZY7kSMRL.json', 'var_call_UG8NvhbjbktTG8UhVablTj1j': 'file_storage/call_UG8NvhbjbktTG8UhVablTj1j.json'}

exec(code, env_args)
