code = """import json

result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

# Let's be more strict about what qualifies as a sports article
sports_articles = []

for article in articles_data:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    
    # Very strict sports indicators to avoid false positives
    strict_sports_terms = [
        'nfl', 'nba', 'mlb', 'nhl',  # Major leagues
        'olympics', 'olympic', 'world cup', 'super bowl',  # Major events
        'football', 'basketball', 'baseball', 'hockey', 'soccer', 'tennis', 'golf'  # Sports names
    ]
    
    # Context indicators to ensure it's actually about sports
    sports_context_terms = ['coach', 'player', 'team', 'game', 'match', 'season', 'championship', 'tournament', 'league']
    
    # Check for strict sports terms
    has_strict_term = any(term in title or term in desc for term in strict_sports_terms)
    
    # Check for context
    has_context = any(term in title or term in desc for term in sports_context_terms)
    
    # Only classify as sports if it has a strict term AND context
    if has_strict_term or (has_context and ('sport' in title or 'sport' in desc)):
        sports_articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': len(article.get('description', ''))
        })

# Sort by description length to find the longest
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    result = longest_article['title']
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': "Why Windows isn't Unix", 'var_functions.execute_python:12': 1000, 'var_functions.execute_python:16': "Why Windows isn't Unix", 'var_functions.execute_python:20': "Why Windows isn't Unix", 'var_functions.execute_python:22': 'Examining 1000 articles for sports content', 'var_functions.execute_python:24': "Last Year's Flu Shot Imperfect But Effective"}

exec(code, env_args)
