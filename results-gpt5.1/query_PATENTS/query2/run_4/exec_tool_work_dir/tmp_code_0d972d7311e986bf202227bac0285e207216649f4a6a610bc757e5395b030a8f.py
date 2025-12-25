code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data
with open(var_call_XdrUf8wkxD8lgLzVRI2OEHLR, 'r') as f:
    pubs = json.load(f)

# Filter for German patents and parse dates
records = []
for row in pubs:
    info = row.get('Patents_info') or ''
    if ' country_code: DE' not in info and 'country_code: DE' not in info and ' DE ' not in info:
        continue
    gdate = row.get('grant_date') or ''
    # Normalize and parse year and date, look for 2019 and second half
    # We just extract year and month via regex for digits
    nums = re.findall(r'\d{1,2}|\d{4}', gdate)
    year = None
    month = None
    if nums:
        # year is 4-digit
        for n in nums:
            if len(n) == 4:
                year = int(n)
        # month: try to infer from month names
    # Fallback: try datetime parsing with common patterns
    if year is None:
        try:
            dt = datetime.strptime(gdate, '%d %B %Y')
            year = dt.year
            month = dt.month
        except Exception:
            year = None
    if year != 2019:
        continue
    # second half of year: months 7-12, but month often missing; skip if unknown
    if month is None:
        # attempt to detect month names
        m = None
        for i, name in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1):
            if name.lower() in gdate.lower():
                m = i
                break
        month = m
    if month is None or month < 7:
        continue
    cpc_raw = row.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # collapse to level-4 group: first three chars (section+class) or up to first non-alnum?
        m = re.match(r'([A-Z]\d{2})', code)
        if not m:
            continue
        group = m.group(1)
        records.append({'year': year, 'group': group})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count filings per year and group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # generate annual range for EMA; here only 2019 so EMA==count
    # compute EMA with alpha=0.1 assuming years sorted ascending
    ema_rows = []
    alpha = 0.1
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha)*ema
            ema_rows.append({'group': g, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # best year per group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # Load CPC level-4 definitions into DataFrame
    with open(var_call_QOxxbdqmRt8E6j2ApHNLyMf2, 'r') as f:
        defs = json.load(f)
    defs_df = pd.DataFrame(defs)
    defs_df['symbol'] = defs_df['symbol'].astype(str)
    # join on group code
    merged = best.merge(defs_df, left_on='group', right_on='symbol', how='left')
    merged = merged[['group','titleFull','year','ema']]
    merged = merged.sort_values('ema', ascending=False).head(20)
    result = merged.to_dict(orient='records')

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_XdrUf8wkxD8lgLzVRI2OEHLR': 'file_storage/call_XdrUf8wkxD8lgLzVRI2OEHLR.json', 'var_call_QOxxbdqmRt8E6j2ApHNLyMf2': 'file_storage/call_QOxxbdqmRt8E6j2ApHNLyMf2.json'}

exec(code, env_args)
