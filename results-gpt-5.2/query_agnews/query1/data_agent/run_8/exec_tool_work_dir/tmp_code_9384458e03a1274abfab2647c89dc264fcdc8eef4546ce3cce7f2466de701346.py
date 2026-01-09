code = """import json, pandas as pd
path = var_call_lahIzzS7kqaWbBdablj1pFiG
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def is_sports(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    sports_kw = [
        'nba','nfl','mlb','nhl','ncaa','uefa','fifa','olympic','olympics','grand slam',
        'tennis','golf','soccer','football','baseball','basketball','hockey','cricket',
        'rugby','formula one','f1','nascar','motogp','cycling','tour de france','wimbledon',
        'super bowl','world series','stanley cup','playoffs','coach','quarterback',
        'goal','touchdown','home run','pitcher','golfer','striker','midfielder','defender',
        'match','tournament','league','championship','cup','seed','ranked','innings','tee'
    ]
    return any(k in text for k in sports_kw)

sports = []
for r in data:
    title = r.get('title')
    desc = r.get('description')
    if is_sports(title, desc):
        sports.append({
            'article_id': r.get('article_id'),
            'title': title,
            'desc_len': len(desc) if isinstance(desc, str) else 0
        })

# if heuristic found none, fall back to longest overall
if not sports:
    best = max(data, key=lambda r: len(r.get('description') or ''))
    out = {'title': best.get('title')}
else:
    best = max(sports, key=lambda r: r['desc_len'])
    out = {'title': best['title']}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lahIzzS7kqaWbBdablj1pFiG': 'file_storage/call_lahIzzS7kqaWbBdablj1pFiG.json'}

exec(code, env_args)
