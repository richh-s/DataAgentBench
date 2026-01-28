code = """import json

# Load the articles data from the stored JSON file path variable
path = var_call_qcBPNVw1FwCBKuMx2mlOYhsk
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define sports-related keywords for simple heuristic classification
sports_keywords = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'cricket', 'rugby', 'hockey',
    'tennis', 'golf', 'match', 'tournament', 'cup', 'league', 'season', 'coach', 'manager', 'player',
    'team', 'teams', 'scored', 'defeat', 'defeated', 'beat', 'beats', 'win', 'wins', 'won', 'inning',
    'penalty', 'goal', 'goals', 'nba', 'nfl', 'mlb', 'fifa', 'olympic', 'olympics', 'boxing', 'fight', 'racing', 'track', 'race'
]

sports_articles = []
for a in articles:
    title = (a.get('title') or '')
    desc = (a.get('description') or '')
    combined = (title + ' ' + desc).lower()
    if any(kw in combined for kw in sports_keywords):
        desc_len = len(desc)
        sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description': desc, 'description_length': desc_len})

# If no sports articles found, return empty result
if not sports_articles:
    result = {'title': None, 'article_id': None, 'description_length': 0}
else:
    # Find the article(s) with maximum description length
    max_len = max(a['description_length'] for a in sports_articles)
    # Choose the first article with that max length (stable order from file)
    chosen = None
    for a in sports_articles:
        if a['description_length'] == max_len:
            chosen = a
            break
    result = {'title': chosen['title'], 'article_id': chosen['article_id'], 'description_length': chosen['description_length']}

# Prepare the JSON string to embed as a Python string literal
json_text = json.dumps(result)

print("----BEGIN PRINT FORMAT----")
print('print("__RESULT__:")')
print('print(' + json.dumps(json_text) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_qcBPNVw1FwCBKuMx2mlOYhsk': 'file_storage/call_qcBPNVw1FwCBKuMx2mlOYhsk.json'}

exec(code, env_args)
