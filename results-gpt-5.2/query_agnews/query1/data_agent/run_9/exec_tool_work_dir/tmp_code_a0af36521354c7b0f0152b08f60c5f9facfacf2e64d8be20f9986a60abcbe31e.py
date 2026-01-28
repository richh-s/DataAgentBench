code = """import json, pandas as pd

# Load full articles result
p = var_call_0AvjMpnH0BJ9XwnTagYCbpZk
with open(p, 'r', encoding='utf-8') as f:
    articles = json.load(f)

def is_sports(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d
    sports_terms = [
        'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics',
        'fifa','uefa','premier league','champions league','world cup','super bowl','touchdown','quarterback','coach',
        'rookie','season','playoff','final','tournament','match','game','wins','win','loss','defeat','league','cup',
        'yankees','red sox','lakers','celtics','arsenal','chelsea','barcelona','real madrid','manchester','juventus'
    ]
    return any(term in text for term in sports_terms)

sports_articles = []
for a in articles:
    title = a.get('title')
    desc = a.get('description')
    if desc is None:
        continue
    if is_sports(title, desc):
        sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

# Pick greatest description length
if sports_articles:
    best = max(sports_articles, key=lambda x: x['desc_len'])
    out = best['title']
else:
    out = None

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0AvjMpnH0BJ9XwnTagYCbpZk': 'file_storage/call_0AvjMpnH0BJ9XwnTagYCbpZk.json'}

exec(code, env_args)
