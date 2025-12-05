code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data
with open(var_call_TYd04Y5ZFl4Omd6zhPeB4W7p, 'r') as f:
    pubs = json.load(f)

# Filter to Germany via Patents_info country_code DE
country_re = re.compile(r'country_code\s*([A-Z]{2})')
records = []
for row in pubs:
    info = row.get('Patents_info') or ''
    m = country_re.search(info)
    if not m or m.group(1) != 'DE':
        continue
    gd = row.get('grant_date') or ''
    # parse year and month from natural language date, looking for 2019 and months Jul-Dec
    # Rough parse: search for 2019
    if '2019' not in gd:
        continue
    # find month name
    month_names = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month = None
    for i, mn in enumerate(month_names, start=1):
        if mn.lower() in gd.lower():
            month = i
            break
    if not month or month < 7:
        continue
    # good: grant in second half 2019
    # parse year more robustly
    year = 2019
    cpc_json = row.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_json)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # level-4 group approximated as first 4 characters before slash or space
        main = code.split()[0]
        base = main.split('/')[0]
        # take first 4 chars of base if length>=4 else whole base
        g4 = base[:4]
        records.append({'year': year, 'cpc4': g4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count per year, per cpc4
    counts = df.groupby(['cpc4','year']).size().reset_index(name='count')
    # since we only have 2019, EMA over years degenerates; but we'll still compute assuming single year
    # To be safe, generate years from min to max and fill missing with 0
    out_rows = []
    alpha = 0.1
    for cpc4, grp in counts.groupby('cpc4'):
        years = list(range(grp['year'].min(), grp['year'].max()+1))
        ema = None
        best_year = None
        best_ema = None
        for y in years:
            c = int(grp.loc[grp['year']==y, 'count'].iloc[0]) if y in set(grp['year']) else 0
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        out_rows.append({'cpc4': cpc4, 'best_year': best_year, 'best_ema': float(best_ema)})
    top = pd.DataFrame(out_rows)
    # keep groups with highest EMA, say top 20
    top = top.sort_values('best_ema', ascending=False).head(20)
    result = top.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TYd04Y5ZFl4Omd6zhPeB4W7p': 'file_storage/call_TYd04Y5ZFl4Omd6zhPeB4W7p.json', 'var_call_c5AgfjVc5YxaU94xfJJnuW3p': 'file_storage/call_c5AgfjVc5YxaU94xfJJnuW3p.json'}

exec(code, env_args)
