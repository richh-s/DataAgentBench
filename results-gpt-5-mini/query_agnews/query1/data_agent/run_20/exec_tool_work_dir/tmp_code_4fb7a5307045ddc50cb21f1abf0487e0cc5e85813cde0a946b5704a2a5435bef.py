code = """import json
from pathlib import Path
import re

# Load original articles data
data_path = Path(var_call_v3avNa2MXFKLvL5ulBW5M8GJ)
with data_path.open('r', encoding='utf-8') as f:
    records = json.load(f)

sports_terms = ['olympic','olympics','football','soccer','basketball','baseball','tennis','golf','cricket',
                'nba','mlb','nhl','fifa','rugby','boxing','wrestle','wrestles','wrestling','swimmer','swimming',
                'skateboard','skateboarding','athlete','athletes','coach','team','season','match','tournament',
                'goal','score','innings','pitcher','home run','hat-trick','striker','goalkeeper','padres','reds','reds knock','indian beat','nba stars','al lead']

sports_records = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    combined = (title + ' ' + desc).lower()
    found = False
    for term in sports_terms:
        # use simple substring for multiword terms, word boundary for single words
        if ' ' in term:
            if term in combined:
                found = True
                break
        else:
            if re.search(r"\b" + re.escape(term) + r"\b", combined):
                found = True
                break
    if found:
        sports_records.append({'article_id': r.get('article_id'), 'title': title, 'description_len': len(desc)})

if not sports_records:
    result = None
else:
    best = max(sports_records, key=lambda x: x['description_len'])
    result = best['title']

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_v3avNa2MXFKLvL5ulBW5M8GJ': 'file_storage/call_v3avNa2MXFKLvL5ulBW5M8GJ.json', 'var_call_SYQwGPDeleCPLeQwEQognVGt': None, 'var_call_nINtKGSq8v2t3qpxB4QJekfP': 'file_storage/call_nINtKGSq8v2t3qpxB4QJekfP.json', 'var_call_EPJwmeGHzuqJP47L9qDroW3b': None, 'var_call_wQdK2cOB0lnqYTh3IGHXcXEq': None}

exec(code, env_args)
