code = """import json, pandas as pd

path = var_call_MGRSCjdFpf5UzApTh3ehLHyN
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

def is_sports(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','ncaa','uefa','fifa','world cup','olympic','olympics',
        'tennis','golf','soccer','football','basketball','baseball','hockey','cricket','rugby',
        'formula 1','f1','nascar','grand slam','atp','wta','pga','goal','touchdown','home run',
        'coach','quarterback','playoff','tournament','match','season','league','championship'
    ]
    return any(term in text for term in sports_terms)

best = None
for a in articles:
    title = a.get('title')
    desc = a.get('description')
    if desc is None:
        continue
    if not is_sports(title, desc):
        continue
    n = len(desc)
    if (best is None) or (n > best['desc_len']):
        best = {'article_id': a.get('article_id'), 'title': title, 'desc_len': n}

out = {'title': None, 'article_id': None, 'description_length': None}
if best:
    out = {'title': best['title'], 'article_id': best['article_id'], 'description_length': best['desc_len']}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MGRSCjdFpf5UzApTh3ehLHyN': 'file_storage/call_MGRSCjdFpf5UzApTh3ehLHyN.json'}

exec(code, env_args)
