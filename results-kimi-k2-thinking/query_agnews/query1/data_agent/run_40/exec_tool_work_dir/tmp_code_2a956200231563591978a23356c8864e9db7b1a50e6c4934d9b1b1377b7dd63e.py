code = """import json
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

sports_articles = []
sports_keywords = ['sport', 'game', 'team', 'player', 'coach', 'season', 'championship', 'tournament', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'racing', 'olympics', 'world cup', 'nfl', 'nba', 'mlb', 'nhl']

for article in articles_data:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    if any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords):
        sports_articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': len(article.get('description', ''))
        })

if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    result = longest_article['title']
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': "Why Windows isn't Unix", 'var_functions.execute_python:12': 1000}

exec(code, env_args)
