code = """import json
from pathlib import Path
import re

data_path = Path(var_call_v3avNa2MXFKLvL5ulBW5M8GJ)
with data_path.open('r', encoding='utf-8') as f:
    records = json.load(f)

sports_terms = ['football','soccer','basketball','baseball','hockey','tennis','golf','cricket',
                'match','tournament','season','coach','goal','score','scored','won','win','beat',
                'defeat','draw','cup','olympic','nba','mlb','nhl','fifa','rugby','boxing','athlete',
                'goalkeeper','striker','inning','innings','home run','hat-trick','matchday','pitch','bat']

matches = []
for r in records:
    txt = (r.get('title','') + ' ' + r.get('description','')).lower()
    for term in sports_terms:
        if term in txt:
            matches.append({'article_id': r.get('article_id'), 'title': r.get('title'), 'term': term, 'description_len': len(r.get('description',''))})
            break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_v3avNa2MXFKLvL5ulBW5M8GJ': 'file_storage/call_v3avNa2MXFKLvL5ulBW5M8GJ.json', 'var_call_SYQwGPDeleCPLeQwEQognVGt': None}

exec(code, env_args)
