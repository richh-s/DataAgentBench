code = """import json
from pathlib import Path
import re

# load records
data_path = Path(var_call_v3avNa2MXFKLvL5ulBW5M8GJ)
with data_path.open('r', encoding='utf-8') as f:
    records = json.load(f)

# keyword lists
sports_kw = ['olympic','olympics','football','soccer','basketball','baseball','hockey','tennis','golf','cricket',
             'match','tournament','season','coach','goal','score','scored','won','win','beat','beats','defeat',
             'draw','cup','nba','mlb','nhl','fifa','rugby','boxing','athlete','athletes','pitcher','inning','innings',
             'home run','strike','striker','wrestle','wrestles','swimmer','swimming','skateboarding','olympian']
tech_kw = ['scientist','scientists','research','technology','tech','computer','ibm','software','nuclear','drug','experiment',
           'scientific','researchers','internet','online','email','e-mail','microsoft','windows','xp','server','linux']
business_kw = ['stock','stocks','market','shares','ipo','investment','investor','economy','economics','trade deficit','profits',
               'profit','oil prices','oil','barrel','dollar','rate cut','interest rates','company','firm','revenue','earnings']

# helper
def count_kw(text, kw_list):
    t = text.lower()
    cnt = 0
    for kw in kw_list:
        # word boundary for alpha keywords, else simple in
        pattern = r"\b" + re.escape(kw) + r"\b"
        if re.search(pattern, t):
            cnt += 1
    return cnt

# classify and compute description length
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    combined = (title + ' ' + desc).lower()
    s_count = count_kw(combined, sports_kw)
    t_count = count_kw(combined, tech_kw)
    b_count = count_kw(combined, business_kw)
    # choose max, tie-breaker: sports > tech > business > world
    counts = {'Sports': s_count, 'Science/Technology': t_count, 'Business': b_count}
    max_cat = max(counts, key=lambda k: (counts[k], 1 if k=='Sports' else 0 if k!='Sports' else 0))
    # But ensure that tie-breaker makes Sports priority if equal
    # We'll implement explicit logic
    max_val = max(counts.values())
    if max_val == 0:
        category = 'World'
    else:
        # get all with max_val
        best = [k for k,v in counts.items() if v==max_val]
        if 'Sports' in best:
            category = 'Sports'
        elif 'Science/Technology' in best:
            category = 'Science/Technology'
        else:
            category = 'Business'
    r['category'] = category
    r['description_len'] = len(desc)

# filter sports
sports = [r for r in records if r['category']=='Sports']
if not sports:
    result = None
else:
    max_r = max(sports, key=lambda x: x['description_len'])
    result = max_r.get('title')

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_v3avNa2MXFKLvL5ulBW5M8GJ': 'file_storage/call_v3avNa2MXFKLvL5ulBW5M8GJ.json', 'var_call_SYQwGPDeleCPLeQwEQognVGt': None, 'var_call_nINtKGSq8v2t3qpxB4QJekfP': 'file_storage/call_nINtKGSq8v2t3qpxB4QJekfP.json'}

exec(code, env_args)
