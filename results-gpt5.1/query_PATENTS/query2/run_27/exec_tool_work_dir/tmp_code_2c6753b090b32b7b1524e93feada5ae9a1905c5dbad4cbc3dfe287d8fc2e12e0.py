code = """import json, re, pandas as pd

# Load full CPC def file if path
cpc_defs_path = var_call_mIE6JQxrfs2mcT5bQA9YcrBC
with open(cpc_defs_path, 'r') as f:
    cpc_defs = json.load(f)

# Load full publication data
pub_path = var_call_u3INibwuJtcIv2AYjIho8E2i
with open(pub_path, 'r') as f:
    pubs = json.load(f)

# Filter to Germany via Patents_info containing ' DE' or ' In DE,' etc. We look for ' DE-' publication or application numbers.
country_re = re.compile(r'\bDE-')

de_pubs = [p for p in pubs if country_re.search(p.get('Patents_info',''))]

# Parse grant year from grant_date natural language
month_map = {m: i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

import datetime

def parse_year(date_str):
    if not date_str:
        return None
    # Extract 4-digit year
    m = re.search(r'(20\d{2})', date_str)
    if m:
        return int(m.group(1))
    return None

# we will need ordering of years, so compute year and count per CPC group code (level 4 section code, i.e., first 3 chars like 'A61')

rows = []
for p in de_pubs:
    y = parse_year(p.get('grant_date',''))
    if y is None:
        continue
    cpc_json = p.get('cpc')
    if not cpc_json:
        continue
    try:
        cpcs = json.loads(cpc_json)
    except Exception:
        continue
    codes = set()
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        # Normalise to section+2-digit class, e.g. A61, B60
        m = re.match(r'([A-HY]\d\d)', code)
        if not m:
            continue
        grp = m.group(1)
        codes.add(grp)
    for grp in codes:
        rows.append({'year': y, 'group': grp})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Count patents per year-group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # For stability, ensure continuous years per group from min to max
    results = []
    alpha = 0.1
    for grp, gdf in counts.groupby('group'):
        years = list(range(int(gdf['year'].min()), int(gdf['year'].max())+1))
        year_to_cnt = dict(zip(gdf['year'], gdf['count']))
        ema = None
        best_year = None
        best_ema = None
        for y in years:
            c = year_to_cnt.get(y, 0)
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            if best_ema is None or ema>best_ema:
                best_ema = ema
                best_year = y
        results.append({'group': grp, 'best_year': best_year, 'max_ema': best_ema})
    res_df = pd.DataFrame(results)
    # Attach titles from cpc_defs
    defs_df = pd.DataFrame(cpc_defs)
    defs_df = defs_df[['symbol','titleFull']]
    merged = res_df.merge(defs_df, left_on='group', right_on='symbol', how='left')
    merged = merged.sort_values('max_ema', ascending=False)
    # Keep groups that have at least one patent in 2019 with grant in H2 2019 (already ensured by original filter), but we want highest EMA overall, so take top 10
    top = merged.head(20)
    result = []
    for _, r in top.iterrows():
        result.append({'cpc_group_code': r['group'], 'titleFull': r.get('titleFull'), 'best_year': int(r['best_year']), 'max_ema': float(r['max_ema'])})

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_u3INibwuJtcIv2AYjIho8E2i': 'file_storage/call_u3INibwuJtcIv2AYjIho8E2i.json', 'var_call_mIE6JQxrfs2mcT5bQA9YcrBC': 'file_storage/call_mIE6JQxrfs2mcT5bQA9YcrBC.json', 'var_call_RQ0dhxB8zFtQwbS060ndKIRU': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
