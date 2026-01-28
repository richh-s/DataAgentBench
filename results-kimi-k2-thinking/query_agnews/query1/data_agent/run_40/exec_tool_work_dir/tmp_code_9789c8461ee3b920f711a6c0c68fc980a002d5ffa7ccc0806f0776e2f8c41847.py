code = """import json
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

sports_articles = []
for i, article in enumerate(articles_data):
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    # Check for strong sports indicators
    strong_sports_terms = ['nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'coach', 'player', 'team', 'game', 'match', 'season', 'championship', 'tournament']
    
    if any(term in title_lower or term in desc_lower for term in strong_sports_terms):
        sports_articles.append({
            'title': article.get('title'),
            'desc': article.get('description'),
            'desc_length': len(article.get('description', ''))
        })

# Find sports article with longest description
if sports_articles:
    longest = max(sports_articles, key=lambda x: x['desc_length'])
    output = longest['title']
else:
    output = None

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': "Why Windows isn't Unix", 'var_functions.execute_python:12': 1000, 'var_functions.execute_python:16': "Why Windows isn't Unix"}

exec(code, env_args)
