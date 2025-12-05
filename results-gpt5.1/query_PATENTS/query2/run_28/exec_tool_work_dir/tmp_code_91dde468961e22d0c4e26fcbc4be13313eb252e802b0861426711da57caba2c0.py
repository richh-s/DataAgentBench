code = """import json, re, pandas as pd, datetime

# Load full publication data
with open(var_call_oIfLCnDS9X7Hraih704PxcCc, 'r') as f:
    pubs = json.load(f)

# Filter to Germany via country_code in Patents_info (look for 'DE-' pattern)
pat = re.compile(r'\bDE-')

records = []
for row in pubs:
    info = row.get('Patents_info') or ''
    if not pat.search(info):
        continue
    gd = row.get('grant_date') or ''
    # Parse year and month from natural language grant_date
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)\s+(\d{4})', gd)
    if not m:
        m = re.search(r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?\s+(\d{4})', gd)
    if not m:
        m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+of\s+([A-Za-z]+),?\s+(\d{4})', gd)
    if not m:
        continue
    day, month, year = None, None, None
    if len(m.groups())==3:
        if m.group(1).isalpha():
            month, day, year = m.group(1), int(m.group(2)), int(m.group(3))
        else:
            day, month, year = int(m.group(1)), m.group(2), int(m.group(3))
    month_str = month
    try:
        month_num = datetime.datetime.strptime(month_str, '%B').month
    except:
        try:
            month_num = datetime.datetime.strptime(month_str, '%b').month
        except:
            continue
    if year != 2019 or month_num < 7:
        continue
    # Now in Germany, granted in second half 2019
    cpc_raw = row.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # Use group at level 4: first 3 chars (section+class) as per provided defs
        group4 = code[:3]
        records.append({'year': year, 'cpc_group4': group4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per year per cpc_group4
    counts = df.groupby(['cpc_group4','year']).size().reset_index(name='count')
    # We have only 2019; to compute EMA by year over available years, we need full range per group
    # Build year range per group from min to max year (here likely only 2019)
    all_years = sorted(counts['year'].unique())
    groups = []
    for g, sub in counts.groupby('cpc_group4'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0)
        # compute EMA with alpha=0.1 over years in chronological order
        ema_vals = []
        prev = None
        for y in all_years:
            x = sub.loc[y, 'count']
            if prev is None:
                prev = x
            else:
                prev = 0.1*x + 0.9*prev
            ema_vals.append({'year': y, 'ema': float(prev)})
        # find best year (max ema)
        best = max(ema_vals, key=lambda r: r['ema'])
        groups.append({'cpc_group4': g, 'best_year': best['year'], 'max_ema': best['ema']})
    res_df = pd.DataFrame(groups)
    # sort by max_ema desc
    res_df = res_df.sort_values('max_ema', ascending=False)
    result = res_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_oIfLCnDS9X7Hraih704PxcCc': 'file_storage/call_oIfLCnDS9X7Hraih704PxcCc.json', 'var_call_ZDLhpK2kRlh0z6AUoGYNcrVO': 'file_storage/call_ZDLhpK2kRlh0z6AUoGYNcrVO.json'}

exec(code, env_args)
