code = """import json

# Load the articles data
path = var_call_qcBPNVw1FwCBKuMx2mlOYhsk
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

sports_keywords = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'cricket', 'rugby', 'hockey',
    'tennis', 'golf', 'match', 'tournament', 'cup', 'league', 'season', 'coach', 'manager', 'player',
    'team', 'teams', 'scored', 'defeat', 'defeated', 'beat', 'beats', 'win', 'wins', 'won', 'inning',
    'penalty', 'goal', 'goals', 'nba', 'nfl', 'mlb', 'fifa', 'olympic', 'olympics', 'boxing', 'fight', 'racing', 'track', 'race'
]

sports_articles = []
for a in articles:
    title = a.get('title') or ''
    desc = a.get('description') or ''
    combined = (title + ' ' + desc).lower()
    if any(kw in combined for kw in sports_keywords):
        sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description': desc, 'description_length': len(desc)})

if not sports_articles:
    result = {'title': None, 'article_id': None, 'description_length': 0}
else:
    max_len = max(x['description_length'] for x in sports_articles)
    for x in sports_articles:
        if x['description_length'] == max_len:
            result = {'title': x['title'], 'article_id': x['article_id'], 'description_length': x['description_length']}
            break

# Prepare output in the required PRINT FORMAT
json_text = json.dumps(result)
py_literal = json.dumps(json_text)

print("----BEGIN PRINT FORMAT----")
print('print("__RESULT__:")')
print('print(' + py_literal + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_qcBPNVw1FwCBKuMx2mlOYhsk': 'file_storage/call_qcBPNVw1FwCBKuMx2mlOYhsk.json'}

exec(code, env_args)
