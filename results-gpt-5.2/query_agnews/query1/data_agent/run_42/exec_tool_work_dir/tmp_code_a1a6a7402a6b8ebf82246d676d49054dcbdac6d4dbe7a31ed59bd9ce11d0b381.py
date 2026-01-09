code = """import json, pandas as pd
path = var_call_6HTF3HvG7xeXRc4nzeSmAdu0
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def is_sports(title, desc):
    txt = ((title or '') + ' ' + (desc or '')).lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','pga','uefa','fifa','olympic','olympics','soccer','football','baseball','basketball','hockey','tennis','golf','cricket','rugby','formula','f1','nascar','grand prix',
        'match','tournament','season','playoffs','quarterback','touchdown','home run','goal','coach','league','championship','cup','open','slam','medal','athlete','win','lost','defeat','draw',
        'yankees','red sox','lakers','celtics','warriors','knicks','cowboys','patriots','packers','arsenal','chelsea','liverpool','manchester','barcelona','real madrid','juventus','milan'
    ]
    return any(t in txt for t in sports_terms)

sports = []
for r in data:
    title = r.get('title')
    desc = r.get('description')
    if is_sports(title, desc):
        sports.append({
            'article_id': r.get('article_id'),
            'title': title,
            'description': desc,
            'desc_len': len(desc) if isinstance(desc, str) else 0
        })

if sports:
    best = max(sports, key=lambda x: x['desc_len'])
    out = {'title': best['title'], 'article_id': best['article_id'], 'description_length': best['desc_len']}
else:
    out = None

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6HTF3HvG7xeXRc4nzeSmAdu0': 'file_storage/call_6HTF3HvG7xeXRc4nzeSmAdu0.json'}

exec(code, env_args)
