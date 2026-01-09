code = """import json, pandas as pd

# Load full mongo export
path = var_call_3f1mVxLAvVSUKNCurjsgdyUD
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def is_sports(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d
    sports_terms = [
        'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','cricket',
        'olympic','grand slam','tournament','match','game','season','coach','quarterback','touchdown','home run',
        'goal','league','championship','world cup','uefa','fifa','premier league','la liga','serie a','bundesliga',
        'formula 1','f1','nascar','motogp','driver','race','gp','boxing','ufc','mma','wrestling','injury','trade',
        'playoffs','final','semifinal','quarterfinal','cup','open','pga','atp','wta'
    ]
    # require at least 2 term hits OR 1 strong league term
    strong = ['nba','nfl','mlb','nhl','fifa','uefa','world cup','olympic','formula 1','nascar','ufc']
    hit_strong = any(s in text for s in strong)
    hits = sum(1 for s in sports_terms if s in text)
    return hit_strong or hits >= 2

sports = []
for r in records:
    title = r.get('title')
    desc = r.get('description')
    if is_sports(title, desc):
        sports.append({
            'article_id': r.get('article_id'),
            'title': title,
            'desc_len': 0 if desc is None else len(desc)
        })

if not sports:
    out = {'error':'No sports articles detected'}
else:
    best = max(sports, key=lambda x: x['desc_len'])
    out = {'title': best['title'], 'article_id': best['article_id'], 'description_length': best['desc_len']}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3f1mVxLAvVSUKNCurjsgdyUD': 'file_storage/call_3f1mVxLAvVSUKNCurjsgdyUD.json'}

exec(code, env_args)
