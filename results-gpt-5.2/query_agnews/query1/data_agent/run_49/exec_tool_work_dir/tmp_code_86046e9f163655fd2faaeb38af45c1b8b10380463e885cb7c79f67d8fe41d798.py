code = """import json, pandas as pd

path = var_call_8sAjXR7zjbFeHtpnUoWmpcgX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def is_sports(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','golf','tennis','olympic','olympics',
        'championship','tournament','match','season','coach','team','league','cup','grand slam','pga','fifa','uefa',
        'player','quarterback','touchdown','goal','strikeout','home run','run','inning','pitcher','ace','draft',
        'formula one','f1','nascar','motogp','cricket','rugby','wimbledon','us open','australian open','french open'
    ]
    return any(t in text for t in sports_terms)

best = None
for r in data:
    title = r.get('title')
    desc = r.get('description')
    if not desc:
        continue
    if is_sports(title, desc):
        l = len(desc)
        if best is None or l > best['len']:
            best = {'article_id': r.get('article_id'), 'title': title, 'len': l}

result = best if best else {}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8sAjXR7zjbFeHtpnUoWmpcgX': 'file_storage/call_8sAjXR7zjbFeHtpnUoWmpcgX.json'}

exec(code, env_args)
