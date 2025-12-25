code = """import json, re, pandas as pd
from datetime import datetime

# Load full patent data
with open(var_call_M9g9PRV6dJucIUDdBnvHkxEl, 'r') as f:
    patents = json.load(f)

# Load CPC level-4 definitions
with open(var_call_Aw4Gsdd0hRh9J2p12XSzzNzl, 'r') as f:
    cpc_defs = json.load(f)

pat_df = pd.DataFrame(patents)

def extract_country(info):
    m = re.search(r'\b([A-Z]{2})\b patent application', info)
    if not m:
        m = re.search(r'Application \(ID [A-Z]{2}-', info)
        if m:
            return info[m.start()+13:m.start()+15]
    return m.group(1) if m else None

pat_df['country'] = pat_df['Patents_info'].astype(str).apply(extract_country)
pat_df = pat_df[pat_df['country'] == 'DE']

# Parse grant year (though all are 2019, we generalize)

month_map = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'],1)}

def parse_year(date_str):
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', date_str)
    y = re.search(r'(20\d{2})', date_str)
    if not y:
        return None
    return int(y.group(1))

pat_df['year'] = pat_df['grant_date'].astype(str).apply(parse_year)
pat_df = pat_df.dropna(subset=['year'])

# Extract CPC codes and roll up to level-4 technology area (first 3 chars, e.g., A61)

records = []
for _, row in pat_df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        tech = code[:3]
        records.append({'year': int(row['year']), 'tech': tech})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['tech','year']).size().reset_index(name='count')

    # Build complete yearly series per tech
    all_years = sorted(counts['year'].unique())
    tech_results = []
    alpha = 0.1
    for tech, grp in counts.groupby('tech'):
        series = {y:0 for y in all_years}
        for _, r in grp.iterrows():
            series[r['year']] = r['count']
        ema = None
        best_year = None
        best_ema = None
        for y in all_years:
            x = series[y]
            if ema is None:
                ema = x
            else:
                ema = alpha*x + (1-alpha)*ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        tech_results.append({'tech': tech, 'best_year': best_year, 'best_ema': best_ema})

    res_df = pd.DataFrame(tech_results)

    # Map to titles via cpc_defs
    defs_df = pd.DataFrame(cpc_defs)
    defs_df = defs_df[['symbol','titleFull']].drop_duplicates()

    res_df = res_df.merge(defs_df, left_on='tech', right_on='symbol', how='left')
    res_df = res_df.sort_values('best_ema', ascending=False).head(20)

    result = []
    for _, r in res_df.iterrows():
        result.append({
            'CPC_group_code_level4': r['tech'],
            'titleFull': r.get('titleFull'),
            'best_year': int(r['best_year']),
            'best_EMA_of_filings': float(r['best_ema'])
        })

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_M9g9PRV6dJucIUDdBnvHkxEl': 'file_storage/call_M9g9PRV6dJucIUDdBnvHkxEl.json', 'var_call_Aw4Gsdd0hRh9J2p12XSzzNzl': 'file_storage/call_Aw4Gsdd0hRh9J2p12XSzzNzl.json'}

exec(code, env_args)
