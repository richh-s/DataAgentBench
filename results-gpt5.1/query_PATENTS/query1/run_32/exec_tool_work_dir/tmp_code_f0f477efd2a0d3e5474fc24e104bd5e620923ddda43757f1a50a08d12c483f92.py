code = """import json, pandas as pd, re, datetime
from datetime import datetime

# Load full results from files
with open(var_call_jA0ONeP22wVdv6r8PI2bC5RN, 'r') as f:
    pub_data = json.load(f)
with open(var_call_fPJM9bvSQ2hCsURVJ49wpMmI, 'r') as f:
    cpc5_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural language publication_date
months = {m: i for i, m in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], start=1)}

def parse_year(date_str):
    if not isinstance(date_str, str):
        return None
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}[^,]*,?\s*(\d{4})', date_str)
    if not m:
        m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}\w*,?\s*(\d{4})', date_str)
    if m:
        return int(m.group(2))
    m = re.search(r'(\d{4})', date_str)
    if m:
        return int(m.group(1))
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)

# Filter for reasonable years
pub_df = pub_df[(pub_df['year'] >= 2000) & (pub_df['year'] <= 2024)]

# Expand CPC codes
records = []
for _, row in pub_df.iterrows():
    year = row['year']
    cpc_raw = row['cpc']
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        records.append({'year': year, 'code': code})

codes_df = pd.DataFrame(records)
if codes_df.empty:
    result = []
else:
    # Count filings per year per CPC code
    counts = codes_df.groupby(['code','year']).size().reset_index(name='filings')

    # Compute EMA (alpha=0.2) per code across years ordered chronologically
    alpha = 0.2
    ema_records = []
    for code, grp in counts.groupby('code'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            if ema is None:
                ema = r['filings']  # seed with first value
            else:
                ema = alpha * r['filings'] + (1-alpha) * ema
            ema_records.append({'code': code, 'year': int(r['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    # For each code, find year with max EMA and that max value
    idx = ema_df.groupby('code')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)

    # Filter to best year == 2022
    best_2022 = best_df[best_df['year'] == 2022]

    # Now restrict to CPC level 5 codes
    cpc5_df = pd.DataFrame(cpc5_data)
    cpc5_symbols = set(cpc5_df['symbol'].astype(str))

    best_2022_lvl5 = best_2022[best_2022['code'].isin(cpc5_symbols)]

    result = sorted(best_2022_lvl5['code'].unique().tolist())

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_jA0ONeP22wVdv6r8PI2bC5RN': 'file_storage/call_jA0ONeP22wVdv6r8PI2bC5RN.json', 'var_call_fPJM9bvSQ2hCsURVJ49wpMmI': 'file_storage/call_fPJM9bvSQ2hCsURVJ49wpMmI.json'}

exec(code, env_args)
