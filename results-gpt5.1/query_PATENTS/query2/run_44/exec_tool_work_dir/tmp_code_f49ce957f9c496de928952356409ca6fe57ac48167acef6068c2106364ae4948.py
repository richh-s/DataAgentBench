code = """import json, re, pandas as pd
from datetime import datetime

# Load full patent data from file
path = var_call_P8HH7HXAZmt7GGdSTeyI1bj1
with open(path, 'r') as f:
    patents = json.load(f)

# Filter to Germany using country_code in Patents_info
country_patents = []
for rec in patents:
    info = rec.get('Patents_info','') or ''
    if re.search(r'\bDE\b', info):
        country_patents.append(rec)

# Helper to parse natural-language grant_date to year
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    if not date_str:
        return None
    # extract year as 4 digits
    m = re.search(r'(20\d{2})', date_str)
    if m:
        return int(m.group(1))
    return None

# Extract year and CPC codes
rows = []
for rec in country_patents:
    year = parse_year(rec.get('grant_date',''))
    if not year:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # CPC group at level 4 ~ first three characters (section+class)?? but better approximate by first 3 chars before any slash
        grp = re.match(r'^[A-Z]\d\d', code)
        if grp:
            group_code = grp.group(0)
        else:
            group_code = code.split('/')[0][:4]
        rows.append({'year': year, 'group_code': group_code})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Count filings per year per group
    counts = df.groupby(['group_code','year']).size().reset_index(name='count')
    # Build full year range per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    groups = []
    for g, sub in counts.groupby('group_code'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0).reset_index()
        sub = sub.rename(columns={'index':'year'})
        # compute EMA with alpha=0.1
        alpha = 0.1
        ema = []
        prev = None
        for _, r in sub.iterrows():
            x = r['count']
            if prev is None:
                prev = x
            else:
                prev = alpha*x + (1-alpha)*prev
            ema.append(prev)
        sub['ema'] = ema
        # best year (max ema)
        idxmax = sub['ema'].idxmax()
        best_year = int(sub.loc[idxmax, 'year'])
        best_ema = float(sub.loc[idxmax, 'ema'])
        groups.append({'group_code': g, 'best_year': best_year, 'best_ema': best_ema})
    best_df = pd.DataFrame(groups)
    # For each year, find group with highest EMA
    # Actually problem: "Find the CPC technology areas in Germany with the highest exponential moving average of patent filings each year" -> so for each year, pick group with max EMA
    records = []
    for year in all_years:
        year_rows = []
        for g, sub in counts.groupby('group_code'):
            sub = sub.set_index('year').reindex(all_years, fill_value=0)
            alpha = 0.1
            prev = None
            for y in all_years:
                x = sub.loc[y, 'count'] if y in sub.index else 0
                if prev is None:
                    prev = x
                else:
                    prev = alpha*x + (1-alpha)*prev
                if y == year:
                    year_rows.append({'group_code': g, 'year': year, 'ema': float(prev)})
                    break
        if year_rows:
            year_df = pd.DataFrame(year_rows)
            idx = year_df['ema'].idxmax()
            row = year_df.loc[idx]
            records.append({'year': int(row['year']), 'group_code': row['group_code'], 'ema': float(row['ema'])})
    result = records

# Load CPC level-4 titles
path2 = var_call_LJ69UAtpJBtyVKEw1hjnndTE
with open(path2, 'r') as f:
    cpc_defs = json.load(f)

cpc_df = pd.DataFrame(cpc_defs)

# Merge titles by matching first 3 chars of group_code to symbol (which is section+class like A61)
if result:
    res_df = pd.DataFrame(result)
    res_df['symbol_key'] = res_df['group_code'].str[:3]
    cpc_df['symbol_key'] = cpc_df['symbol'].str[:3]
    merged = res_df.merge(cpc_df[['symbol_key','titleFull']], on='symbol_key', how='left')
    merged = merged.rename(columns={'titleFull':'titleFull'})
    out = merged[['year','group_code','titleFull','ema']].sort_values(['year'])
    answer = out.to_dict(orient='records')
else:
    answer = []

import json as _json
s = _json.dumps(answer)
print("__RESULT__:")
print(s)"""

env_args = {'var_call_P8HH7HXAZmt7GGdSTeyI1bj1': 'file_storage/call_P8HH7HXAZmt7GGdSTeyI1bj1.json', 'var_call_LJ69UAtpJBtyVKEw1hjnndTE': 'file_storage/call_LJ69UAtpJBtyVKEw1hjnndTE.json', 'var_call_zywejmWXaoxgielqsydyxPY6': ['publicationinfo'], 'var_call_vpmtx0qBYcvS2dtxTDz4CW29': ['cpc_definition']}

exec(code, env_args)
