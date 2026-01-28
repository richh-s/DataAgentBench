code = """import json

result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

print('Total number of articles:', len(articles_data))

sports_keywords = ['sports', 'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'olympics', 'world cup', 'championship', 'game', 'match', 'player', 'team', 'coach', 'league']

sports_articles = []
for article in articles_data:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    has_sports_keyword = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
    
    if has_sports_keyword:
        sports_articles.append({
            'article_id': article.get('article_id'),
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': len(article.get('description', ''))
        })

print('Found', len(sports_articles), 'potentially sports-related articles')

if sports_articles:
    longest_sports = max(sports_articles, key=lambda x: x['desc_length'])
    print('Longest sports article:')
    print('Title:', longest_sports['title'])
    print('Description length:', longest_sports['desc_length'])"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
