code = """import json, re, pandas as pd
from datetime import datetime

file_path = var_call_v2lLK5xVlBBKzJ1Gm4y3uBL8
with open(file_path, 'r') as f:
    grants = json.load(f)

# Filter to Germany via country code " DE" in Patents_info
def get_country(info):
    m = re.search(r'\b([A-Z]{2})\b', info)
    return m.group(1) if m else None

for g in grants:
    g['country'] = get_country(g['Patents_info'])

de_grants = [g for g in grants if g['country'] == 'DE']

# Parse year from grant_date
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', date_str)
    y = re.search(r'(20\d{2})', date_str)
    if y:
        return int(y.group(1))
    return None

for g in de_grants:
    g['year'] = parse_year(g['grant_date'])

# explode CPC codes
rows = []
for g in de_grants:
    if not g.get('cpc'):
        continue
    try:
        cpcs = json.loads(g['cpc'])
    except Exception:
        continue
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        # level 4 group: take up to first space or slash? CPCDefinition has symbols like "A61" so level4 is section+class
        group = re.match(r'^[A-Z]\d{2}', code)
        if not group:
            continue
        rows.append({'group': group.group(0), 'year': g['year']})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows).dropna()
    # count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # compute EMA per group sorted by year
    out_rows = []
    alpha = 0.1
    for grp, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        best_ema = None
        best_year = None
        for _, r in sub.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            if (best_ema is None) or (ema > best_ema):
                best_ema = ema
                best_year = int(r['year'])
        out_rows.append({'group': grp, 'best_year': best_year, 'best_ema': best_ema})
    result = out_rows

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_v2lLK5xVlBBKzJ1Gm4y3uBL8': 'file_storage/call_v2lLK5xVlBBKzJ1Gm4y3uBL8.json', 'var_call_ADw8ghL8FJaDbztlU1u2QVcD': 'file_storage/call_ADw8ghL8FJaDbztlU1u2QVcD.json', 'var_call_qsZvOYuGXcdIEgUIyJKMfqeJ': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
