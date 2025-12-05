code = """import json, pandas as pd, datetime as dt, re

# Load full results
pub_path = var_call_rsLR4inHjlZynKAipYdpmjRT
cpcdef_path = var_call_aIEDwcrdwiNPeICQgcADbBR0

with open(pub_path, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural language publication_date
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def extract_year(date_str):
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}..,\s*(\d{4})', date_str)
    if not m:
        m2 = re.search(r'(\d{4})', date_str)
        return int(m2.group(1)) if m2 else None
    return int(m.group(2))

pub_df['year'] = pub_df['publication_date'].map(extract_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# explode CPC codes
records = []
for _, row in pub_df.iterrows():
    year = row['year']
    cpc_raw = row['cpc']
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        codes = json.loads(cpc_raw)
    except Exception:
        continue
    for ent in codes:
        code = ent.get('code') if isinstance(ent, dict) else None
        if not code:
            continue
        records.append({'symbol': code, 'year': year})

cpc_year = pd.DataFrame(records)

# Keep only level 5 symbols
cpcdef_df = pd.DataFrame(cpcdef_data)
level5_syms = set(cpcdef_df['symbol'].astype(str).unique())

cpc_year = cpc_year[cpc_year['symbol'].isin(level5_syms)]

# Count filings per symbol-year
counts = cpc_year.groupby(['symbol','year']).size().reset_index(name='filings')

# Compute EMA per symbol over years with alpha=0.2
alpha = 0.2
ema_rows = []
for sym, grp in counts.groupby('symbol'):
    grp = grp.sort_values('year')
    ema = None
    for _, r in grp.iterrows():
        y = r['year']; f = r['filings']
        ema = f if ema is None else alpha*f + (1-alpha)*ema
        ema_rows.append({'symbol': sym, 'year': y, 'ema': ema})

ema_df = pd.DataFrame(ema_rows)

# Determine best year (max EMA) per symbol
idx = ema_df.groupby('symbol')['ema'].idxmax()
best = ema_df.loc[idx].reset_index(drop=True)

# Filter best year == 2022
best_2022 = best[best['year'] == 2022]

# Return only CPC group codes (symbols) at level 5 whose best year is 2022
result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rsLR4inHjlZynKAipYdpmjRT': 'file_storage/call_rsLR4inHjlZynKAipYdpmjRT.json', 'var_call_aIEDwcrdwiNPeICQgcADbBR0': 'file_storage/call_aIEDwcrdwiNPeICQgcADbBR0.json'}

exec(code, env_args)
