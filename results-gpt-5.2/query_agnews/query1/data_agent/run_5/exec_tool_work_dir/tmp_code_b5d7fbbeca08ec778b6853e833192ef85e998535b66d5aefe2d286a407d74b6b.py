code = """import json, pandas as pd

# load full mongo export
path = var_call_ai6TfhABzd7boPsNx9ZsDlFX
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def is_sports(title, desc):
    t = ((title or '') + ' ' + (desc or '')).lower()
    sports_kw = [
        'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey',
        'tennis','golf','olympic','olympics','fifa','uefa','world cup','cup final',
        'match','tournament','coach','quarterback','touchdown','home run','goal','goals',
        'season','playoff','playoffs','league','championship','grand slam','race','prix',
        'driver','cricket','rugby','boxing','ufc','wimbledon','super bowl'
    ]
    return any(k in t for k in sports_kw)

sports = []
for r in recs:
    title = r.get('title')
    desc = r.get('description')
    if title is None or desc is None:
        continue
    if is_sports(title, desc):
        sports.append({
            'article_id': r.get('article_id'),
            'title': title,
            'description': desc,
            'desc_len': len(desc)
        })

if not sports:
    out = {'title': None}
else:
    best = max(sports, key=lambda x: x['desc_len'])
    out = {'title': best['title'], 'article_id': best.get('article_id'), 'description_length': best['desc_len']}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ai6TfhABzd7boPsNx9ZsDlFX': 'file_storage/call_ai6TfhABzd7boPsNx9ZsDlFX.json'}

exec(code, env_args)
