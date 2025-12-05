code = """import json, pandas as pd, re, datetime
from datetime import datetime

# Load full publication data
with open(var_call_N3Vs8onEbTv2FBoT4BAPN1z5, 'r') as f:
    pub_data = json.load(f)

# Load CPC level 5 symbols
with open(var_call_89jFA38yLRbmrDgz7j7ViNx7, 'r') as f:
    cpc_def = json.load(f)

level5_symbols = set([r['symbol'] for r in cpc_def])

# Helper to parse natural language dates to year
def parse_year(date_str):
    if not date_str:
        return None
    try:
        # Remove ordinal suffixes
        cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
        return datetime.strptime(cleaned, '%b %d, %Y').year
    except Exception:
        try:
            cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
            return datetime.strptime(cleaned, '%B %d, %Y').year
        except Exception:
            return None

rows = []
for rec in pub_data:
    year = parse_year(rec.get('publication_date'))
    if not year:
        continue
    try:
        cpc_list = json.loads(rec.get('cpc'))
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if code in level5_symbols:
            rows.append({'year': year, 'code': code})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Count filings per year per code
    counts = df.groupby(['code','year']).size().reset_index(name='count')
    # Ensure years sorted per code and compute EMA with alpha=0.2
    alpha = 0.2
    ema_records = []
    for code, grp in counts.sort_values('year').groupby('code'):
        ema = None
        for _, r in grp.iterrows():
            y = int(r['year'])
            cnt = r['count']
            if ema is None:
                ema = cnt
            else:
                ema = alpha*cnt + (1-alpha)*ema
            ema_records.append({'code': code, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    # For each code, find year with max EMA
    idx = ema_df.groupby('code')['ema'].idxmax()
    best = ema_df.loc[idx, ['code','year','ema']]
    # Filter to best year == 2022
    best_2022 = best[best['year'] == 2022]
    result = sorted(best_2022['code'].unique().tolist())

import json as jsonlib
out = jsonlib.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_N3Vs8onEbTv2FBoT4BAPN1z5': 'file_storage/call_N3Vs8onEbTv2FBoT4BAPN1z5.json', 'var_call_89jFA38yLRbmrDgz7j7ViNx7': 'file_storage/call_89jFA38yLRbmrDgz7j7ViNx7.json'}

exec(code, env_args)
