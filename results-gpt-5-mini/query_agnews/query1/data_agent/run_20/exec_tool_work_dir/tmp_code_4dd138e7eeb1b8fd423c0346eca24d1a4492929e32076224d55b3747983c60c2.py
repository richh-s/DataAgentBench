code = """import json
from pathlib import Path
import re

data_path = Path(var_call_v3avNa2MXFKLvL5ulBW5M8GJ)
with data_path.open('r', encoding='utf-8') as f:
    records = json.load(f)

sports_terms = ['football','soccer','basketball','baseball','hockey','tennis','golf','cricket',
                'olympic','olympics','nba','mlb','nhl','boxing','wrestle','wrestles','wrestling',
                'swimmer','swimming','skateboard','skateboarding','coach','team','season','match','tournament',
                'score','goal','innings','pitcher','athlete','athletes','goalkeeper','striker']

sports_records = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    combined = (title + ' ' + desc).lower()
    for term in sports_terms:
        if re.search(r"\b" + re.escape(term) + r"\b", combined):
            sports_records.append({'article_id': r.get('article_id'), 'title': title, 'description_len': len(desc)})
            break

if not sports_records:
    result = None
else:
    best = max(sports_records, key=lambda x: x['description_len'])
    result = best['title']

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_v3avNa2MXFKLvL5ulBW5M8GJ': 'file_storage/call_v3avNa2MXFKLvL5ulBW5M8GJ.json', 'var_call_SYQwGPDeleCPLeQwEQognVGt': None, 'var_call_nINtKGSq8v2t3qpxB4QJekfP': 'file_storage/call_nINtKGSq8v2t3qpxB4QJekfP.json', 'var_call_EPJwmeGHzuqJP47L9qDroW3b': None}

exec(code, env_args)
