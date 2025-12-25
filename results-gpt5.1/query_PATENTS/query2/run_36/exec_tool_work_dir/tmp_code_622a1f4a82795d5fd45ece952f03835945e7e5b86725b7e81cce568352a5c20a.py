code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication results
with open(var_call_73hECfYL7lDWNEIynVqtvvzj, 'r') as f:
    pubs = json.load(f)

# Filter for Germany using country code "DE" in Patents_info
pattern = re.compile(r'\bDE\b')

de_pubs = [r for r in pubs if r.get('grant_date') and r.get('cpc') and pattern.search(r.get('Patents_info',''))]

# Parse grant year
months_map = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    s = date_str.replace('on ','').replace('the ','')
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', s)
    y = re.search(r'(20\d{2})', s)
    if not m or not y:
        return None
    return int(y.group(1))

# Extract CPC codes and years
rows = []
for r in de_pubs:
    year = parse_year(r['grant_date'])
    if year is None:
        continue
    try:
        cpc_list = json.loads(r['cpc'])
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # level-4 group: take main class or group prefix before first '/'; for simplicity, use first 4 chars of main section+class if present
        main = code.split('/')[0]
        # normalize to first 4 characters or full main if shorter
        lvl4 = main[:4]
        rows.append({'cpc_level4': lvl4, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['cpc_level4','year']).size().reset_index(name='count')

    # For EMA we need years per group sorted; assume full range from min to max, fill missing with 0
    alpha = 0.1
    best_rows = []
    for code, grp in counts.groupby('cpc_level4'):
        years = list(range(grp['year'].min(), grp['year'].max()+1))
        year_counts = {y:0 for y in years}
        year_counts.update({int(row['year']): int(row['count']) for _, row in grp.iterrows()})
        ema = None
        best_year = None
        best_ema = -1
        for y in sorted(years):
            x = year_counts[y]
            if ema is None:
                ema = x
            else:
                ema = alpha*x + (1-alpha)*ema
            if ema > best_ema:
                best_ema = ema
                best_year = y
        best_rows.append({'cpc_level4': code, 'best_year': best_year, 'best_ema': best_ema})

    best_df = pd.DataFrame(best_rows)
    # Get those with highest EMA overall
    max_ema = best_df['best_ema'].max() if not best_df.empty else None
    if max_ema is None:
        top = []
    else:
        top = best_df[best_df['best_ema'] == max_ema]

    result = top.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_73hECfYL7lDWNEIynVqtvvzj': 'file_storage/call_73hECfYL7lDWNEIynVqtvvzj.json', 'var_call_0ZV6ilAr6T0GgyulkGiBYzwb': 'file_storage/call_0ZV6ilAr6T0GgyulkGiBYzwb.json', 'var_call_5QFI4er5X2ubjaLzSoMactte': ['publicationinfo'], 'var_call_cGg95xvWJ1mlCuFe2qbODnGr': ['cpc_definition']}

exec(code, env_args)
