code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data from file
with open(var_call_fR2bszF9aE6CEYfiiPXYHOAj, 'r') as f:
    pubs = json.load(f)

# Filter to German patents by country code "DE" in Patents_info
pattern_country = re.compile(r'\bDE\b')

records = []
for row in pubs:
    info = row.get('Patents_info') or ''
    if not pattern_country.search(info):
        continue
    grant = row.get('grant_date') or ''
    m = re.search(r'(\d{1,2}(st|nd|rd|th)?\s+\w+\s+\d{4}|\w+\s+\d{1,2}(st|nd|rd|th)?,\s*\d{4}|\d{1,2}\.\d{1,2}\.\d{4}|\w+\s+\d{4}|\d{4})', grant)
    if not m:
        continue
    date_str = m.group(0).replace('of ', '')
    date_str = re.sub(r'(st|nd|rd|th)', '', date_str)
    dt = None
    for fmt in ['%d %B %Y','%B %d, %Y','%d.%m.%Y','%B %Y','%Y']:
        try:
            dt = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue
    if dt is None:
        continue
    if not (dt.year == 2019 and dt.month >= 7):
        continue
    cpc_raw = row.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    year = dt.year
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        group = re.match(r'^[A-Z]\d{2}', code)
        if not group:
            continue
        group_code = group.group(0)
        records.append({'group_code': group_code, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['group_code','year']).size().reset_index(name='count')
    # Build full year range for EMA per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    ema_rows = []
    alpha = 0.1
    for g, sub in counts.groupby('group_code'):
        year_counts = {int(r['year']): int(r['count']) for _, r in sub.iterrows()}
        ema = None
        for y in sorted(all_years):
            c = year_counts.get(y, 0)
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'group_code': g, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    idx = ema_df.groupby('group_code')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    best = best.sort_values('ema', ascending=False).head(50)
    result = best.to_dict(orient='records')

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_fR2bszF9aE6CEYfiiPXYHOAj': 'file_storage/call_fR2bszF9aE6CEYfiiPXYHOAj.json', 'var_call_YKoxP2LhTwhHVrrCDmn19j2s': 'file_storage/call_YKoxP2LhTwhHVrrCDmn19j2s.json'}

exec(code, env_args)
