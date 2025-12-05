code = """import json, pandas as pd, re, datetime as dt

# Load full data from file paths
pub_path = var_call_4qHXUsa805Doyw2LSC72F4sT
cpcdef_path = var_call_r2N3BQuEEKv9k790gFBaEJMx

with open(pub_path, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from publication_date like 'Aug 3rd, 2021'
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    # Extract 4-digit year
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        return int(m.group(0))
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Expand CPC JSON list per publication

def extract_codes(cpc_str):
    if not isinstance(cpc_str, str) or not cpc_str.strip():
        return []
    try:
        data = json.loads(cpc_str)
    except Exception:
        return []
    codes = []
    for obj in data:
        code = obj.get('code')
        if isinstance(code, str):
            codes.append(code.strip())
    return codes

pub_df['codes'] = pub_df['cpc'].apply(extract_codes)

rows = []
for _, r in pub_df.iterrows():
    y = r['year']
    for code in r['codes']:
        rows.append({'year': y, 'code': code})

codes_df = pd.DataFrame(rows)
if codes_df.empty:
    result = []
else:
    # Filter to level-5 symbols
    cpcdef_df = pd.DataFrame(cpcdef_data)
    level5 = set(cpcdef_df['symbol'].astype(str).unique())
    codes_df = codes_df[codes_df['code'].isin(level5)]

    if codes_df.empty:
        result = []
    else:
        # Count filings per code-year
        counts = codes_df.groupby(['code','year']).size().reset_index(name='count')
        # Compute EMA per code across years sorted chronologically
        alpha = 0.2
        ema_rows = []
        for code, grp in counts.groupby('code'):
            grp = grp.sort_values('year')
            ema = None
            for _, row in grp.iterrows():
                c = row['count']
                if ema is None:
                    ema = c
                else:
                    ema = alpha * c + (1-alpha) * ema
                ema_rows.append({'code': code, 'year': int(row['year']), 'ema': float(ema)})
        ema_df = pd.DataFrame(ema_rows)
        # For each code, find best year (max EMA). If multiple, take latest.
        ema_df['rank'] = ema_df.groupby('code')['ema'].rank(method='max', ascending=False)
        best = ema_df[ema_df['rank'] == 1.0].copy()
        # In case of ties, keep latest year per code
        best = best.sort_values(['code','year']).groupby('code').tail(1)
        # Keep only codes whose best year is 2022
        best_2022 = best[best['year'] == 2022]
        result = sorted(best_2022['code'].unique().tolist())

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4qHXUsa805Doyw2LSC72F4sT': 'file_storage/call_4qHXUsa805Doyw2LSC72F4sT.json', 'var_call_r2N3BQuEEKv9k790gFBaEJMx': 'file_storage/call_r2N3BQuEEKv9k790gFBaEJMx.json'}

exec(code, env_args)
