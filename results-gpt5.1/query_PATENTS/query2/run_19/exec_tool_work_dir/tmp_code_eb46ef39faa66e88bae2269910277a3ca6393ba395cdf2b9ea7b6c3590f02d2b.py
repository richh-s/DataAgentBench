code = """import json, re, pandas as pd

# Load full datasets from files
with open(var_call_ymOKMGQIL7DiaPoDUyMyNIl7, 'r') as f:
    half2019_records = json.load(f)
with open(var_call_yJmHj3rechWwxAaz6VDckSRh, 'r') as f:
    cpc_defs = json.load(f)
with open(var_call_2J5QayNDPs6wuowUX1XAPFTT, 'r') as f:
    all2019_records = json.load(f)

# Helper to extract country code from Patents_info (pattern " from DE," or " (no. DE-" etc.)
cc_pattern = re.compile(r'\bfrom\s+([A-Z]{2})\b|\bno\.\s+([A-Z]{2})-|\bnumber\s+([A-Z]{2})-', re.IGNORECASE)

def extract_cc(text):
    m = cc_pattern.search(text)
    if not m:
        return None
    for g in m.groups():
        if g:
            return g.upper()
    return None

# Filter to Germany patents in second half 2019 by grant_date and country code DE
second_half = []
for rec in half2019_records:
    cc = extract_cc(rec.get('Patents_info', '') or '')
    if cc != 'DE':
        continue
    second_half.append(rec)

# Parse CPC JSON-like string into list of codes and reduce to level-4 group (section+2 digits, e.g., "A61")

def parse_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
    except Exception:
        return []
    codes = []
    for item in data:
        code = item.get('code')
        if not code:
            continue
        # Normalize: strip spaces, take leading letter plus next two digits (if present)
        m = re.match(r'([A-HY])\s*(\d\d)', code)
        if m:
            grp = m.group(1) + m.group(2)
            codes.append(grp)
    return list(set(codes))

# Build yearly counts per CPC level-4 group for DE patents (all 2019, to compute EMA over years)

# First, collect all DE 2019 grants with a year parsed from grant_date

def parse_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(20\d{2})', date_str)
    return int(m.group(1)) if m else None

all_de_2019 = []
for rec in all2019_records:
    year = parse_year(rec.get('grant_date', '') or '')
    if year != 2019:
        continue
    cc = extract_cc(rec.get('Patents_info', '') or '')
    if cc != 'DE':
        continue
    all_de_2019.append(rec)

# If we only have 2019 in this dataset, EMA by year degenerates to that single year
# Count filings per group per (single) year
rows = []
for rec in all_de_2019:
    year = 2019
    for grp in parse_cpc_codes(rec.get('cpc', '') or ''):
        rows.append({'year': year, 'group': grp})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # Compute EMA per group across years (here likely just 2019)
    alpha = 0.1
    ema_rows = []
    for grp, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            y = r['year']
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'group': grp, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)

    # Now restrict to groups that appear in second-half 2019 DE grants
    sh_groups = set()
    for rec in second_half:
        for grp in parse_cpc_codes(rec.get('cpc', '') or ''):
            sh_groups.add(grp)

    ema_df = ema_df[ema_df['group'].isin(sh_groups)]

    # For each group, find the year with highest EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].copy()

    # Attach CPC titles from level-4 definitions
    defs_df = pd.DataFrame(cpc_defs)
    defs_df['symbol'] = defs_df['symbol'].astype(str).str.strip()
    defs_df['titleFull'] = defs_df['titleFull']

    best['group_code'] = best['group']
    merged = best.merge(defs_df, left_on='group_code', right_on='symbol', how='left')

    merged = merged[['group_code','titleFull','year','ema']]
    merged = merged.sort_values('ema', ascending=False)

    result = merged.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ymOKMGQIL7DiaPoDUyMyNIl7': 'file_storage/call_ymOKMGQIL7DiaPoDUyMyNIl7.json', 'var_call_yJmHj3rechWwxAaz6VDckSRh': 'file_storage/call_yJmHj3rechWwxAaz6VDckSRh.json', 'var_call_2J5QayNDPs6wuowUX1XAPFTT': 'file_storage/call_2J5QayNDPs6wuowUX1XAPFTT.json'}

exec(code, env_args)
