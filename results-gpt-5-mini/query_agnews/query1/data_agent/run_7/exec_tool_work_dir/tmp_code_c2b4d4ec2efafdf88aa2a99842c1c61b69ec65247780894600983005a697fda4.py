code = """import json

# Load the full query_db result from the provided storage file path
file_path = var_call_G1sDr7cxVNwXNpAvw7BTORaO
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Define sports-related keywords for classification
sports_keywords = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'tennis', 'cricket', 'baseball', 'golf',
    'hockey', 'rugby', 'olympic', 'olympics', 'world cup', 'worldcup', 'cup', 'league', 'match',
    'season', 'coach', 'manager', 'player', 'team', 'score', 'goal', 'goals', 'won', 'win', 'defeat',
    'defeated', 'tackle', 'pitch', 'stadium', 'batting', 'innings', 'race', 'racing', 'motor', 'nba', 'mlb', 'nhl', 'nfl'
]

# Helper to determine if an article is sports-related
def is_sports(title, description):
    combined = ((title or '') + ' ' + (description or '')).lower()
    for kw in sports_keywords:
        if kw in combined:
            return True
    return False

# Process records: ensure fields exist and compute description lengths
sports_articles = []
for r in records:
    title = r.get('title') if isinstance(r.get('title'), str) else ''
    desc = r.get('description') if isinstance(r.get('description'), str) else ''
    if is_sports(title, desc):
        desc_len = len(desc)
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'desc_len': desc_len})

# Find the sports article with the maximum description length
if sports_articles:
    max_article = max(sports_articles, key=lambda x: x['desc_len'])
    result = max_article['title']
else:
    result = None

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_G1sDr7cxVNwXNpAvw7BTORaO': 'file_storage/call_G1sDr7cxVNwXNpAvw7BTORaO.json'}

exec(code, env_args)
