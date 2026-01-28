code = """import json

# Load the Mongo query result from the provided storage key file path
path = var_call_9wZHcrEI7YjpVlw6E6qLW0W9
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Ensure consistent fields and compute description lengths
for r in records:
    # Normalize missing fields
    if 'description' not in r or r['description'] is None:
        r['description'] = ''
    if 'title' not in r or r['title'] is None:
        r['title'] = ''
    # compute length
    r['desc_len'] = len(r['description'])

# Define sports-related keywords (lowercase)
sports_keywords = [
    'match', 'beat', 'defeat', 'defeated', 'win', 'wins', 'won', 'score', 'goal', 'goals',
    'season', 'coach', 'manager', 'league', 'cup', 'tournament', 'olympic', 'olympics',
    'race', 'racing', 'final', 'semifinal', 'quarterfinal', 'playoff', 'playoffs',
    'nba', 'mlb', 'nfl', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'tennis',
    'golf', 'hockey', 'boxer', 'boxing', 'fell short', 'draw', 'striker', 'midfielder',
    'goalkeeper', 'coach', 'pitcher', 'batting', 'innings', 'scored', 'scoring', 'tackle',
    'try', 'tries', 'wicket', 'bat', 'cricket', 'rugby', 'fifa'
]

def is_sports(rec):
    txt = (rec.get('title','') + ' ' + rec.get('description','')).lower()
    for kw in sports_keywords:
        if kw in txt:
            return True
    return False

# Filter sports articles
sports_articles = [r for r in records if is_sports(r)]

# If none found via keywords, attempt simple heuristic: titles containing known sports outlets or sections (e.g., 'Sports')
if not sports_articles:
    for r in records:
        if 'sports' in (r.get('title','') + ' ' + r.get('description','')).lower():
            sports_articles.append(r)

# Select the sports article with maximum description length
if sports_articles:
    best = max(sports_articles, key=lambda x: x['desc_len'])
    result_title = best.get('title','')
else:
    result_title = ''

import json as _json
print("__RESULT__:")
print(_json.dumps(result_title))"""

env_args = {'var_call_TBBPglvXuM6UgsuWtAguBNil': ['articles'], 'var_call_9wZHcrEI7YjpVlw6E6qLW0W9': 'file_storage/call_9wZHcrEI7YjpVlw6E6qLW0W9.json'}

exec(code, env_args)
