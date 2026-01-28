code = """import json, re

# Load data from the storage file provided by the previous query_db call
with open(var_call_iJzLMo3mfDcWWgNlhP6fY6K0, 'r', encoding='utf-8') as f:
    articles = json.load(f)

sports_keywords = [
    'sport', 'sports', 'match', 'game', 'season', 'cup', 'league', 'tournament', 'score', 'scored',
    'defeat', 'win', 'won', 'lost', 'draw', 'coach', 'manager', 'football', 'soccer', 'baseball',
    'basketball', 'tennis', 'golf', 'cricket', 'olympic', 'racing', 'race', 'fifa', 'nba', 'nhl',
    'mlb', 'premiership', 'goal', 'goals', 'tries', 'hat-trick', 'pitch', 'kick', 'touchdown', 'innings'
]

def is_sports_article(title, description):
    combined = ((title or "") + " " + (description or "")).lower()
    # Use regex word boundary search for each keyword to reduce false positives
    for kw in sports_keywords:
        # escape keyword for regex
        pattern = r"\\b" + re.escape(kw) + r"\\b"
        if re.search(pattern, combined):
            return True
    return False

# Find sports articles and compute description lengths
sports_articles = []
for a in articles:
    title = a.get('title')
    description = a.get('description')
    if is_sports_article(title, description):
        desc_len = len(description) if description is not None else 0
        sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description_length': desc_len})

# If none found with strict keyword matching, fall back to a looser substring check
if not sports_articles:
    for a in articles:
        title = a.get('title')
        description = a.get('description')
        combined = ((title or "") + " " + (description or "")).lower()
        for kw in sports_keywords:
            if kw in combined:
                desc_len = len(description) if description is not None else 0
                sports_articles.append({'article_id': a.get('article_id'), 'title': title, 'description_length': desc_len})
                break

# Determine the sports article with the greatest description length
result = None
if sports_articles:
    result = max(sports_articles, key=lambda x: x['description_length'])
else:
    result = {'article_id': None, 'title': None, 'description_length': 0}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iJzLMo3mfDcWWgNlhP6fY6K0': 'file_storage/call_iJzLMo3mfDcWWgNlhP6fY6K0.json'}

exec(code, env_args)
