code = """import json

# Load articles data from the stored JSON file path variable
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
    title_result = None
else:
    max_len = max(x['description_length'] for x in sports_articles)
    # choose first with max length
    chosen = next(x for x in sports_articles if x['description_length'] == max_len)
    title_result = chosen['title']

# Print in required format: two lines
print("__RESULT__:")
print(json.dumps(title_result))"""

env_args = {'var_call_qcBPNVw1FwCBKuMx2mlOYhsk': 'file_storage/call_qcBPNVw1FwCBKuMx2mlOYhsk.json'}

exec(code, env_args)
