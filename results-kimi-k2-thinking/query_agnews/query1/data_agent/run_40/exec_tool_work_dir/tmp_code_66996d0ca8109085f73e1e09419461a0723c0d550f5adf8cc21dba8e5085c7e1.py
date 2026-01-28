code = """import json

# Read the full result from the file
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

# Define sports keywords to identify sports articles
sports_keywords = ['sports', 'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'olympics', 'world cup', 'championship', 'game', 'match', 'player', 'team', 'coach', 'league', 'cup', 'racing', 'nfl', 'nba', 'mlb', 'nhl', 'golf']

# Find sports articles and track the one with longest description
sports_articles = []
longest_desc_length = 0
longest_sports_article = None

for article in articles_data:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    # Check if this is a sports article
    is_sports = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
    
    if is_sports:
        desc_length = len(article.get('description', ''))
        sports_articles.append({
            'title': article.get('title'),
            'desc_length': desc_length
        })
        
        # Track the article with longest description
        if desc_length > longest_desc_length:
            longest_desc_length = desc_length
            longest_sports_article = article

# Print result in required format
result = longest_sports_article.get('title') if longest_sports_article else None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
