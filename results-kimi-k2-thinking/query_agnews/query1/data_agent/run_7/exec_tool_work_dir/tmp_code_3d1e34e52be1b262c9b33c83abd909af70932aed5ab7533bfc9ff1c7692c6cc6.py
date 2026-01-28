code = """import json
import os

# Load articles data
articles = locals()['var_functions.query_db:2']
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

print("Total articles: %d" % len(articles))

# Sports keywords
sports_keywords = [
    'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 
    'golf', 'cricket', 'hockey', 'race', 'athlete', 'olympics', 
    'game', 'team', 'player', 'match', 'championship', 'tournament'
]

sports_articles = []

# Process articles
for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    
    is_sports = any(keyword in title or keyword in desc for keyword in sports_keywords)
    
    if is_sports:
        sports_articles.append({
            'title': article.get('title'),
            'desc': article.get('description'),
            'length': len(article.get('description', ''))
        })

if sports_articles:
    sports_articles.sort(key=lambda x: x['length'], reverse=True)
    
    print("Sports articles found: %d" % len(sports_articles))
    
    # Show top 3
    for i in range(min(3, len(sports_articles))):
        print("%d. %s (length: %d)" % (i+1, sports_articles[i]['title'], sports_articles[i]['length']))
    
    result = sports_articles[0]['title']
else:
    result = "No sports articles found"

# Output in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': "Why Windows isn't Unix", 'var_functions.execute_python:20': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.list_db:22': ['authors', 'article_metadata']}

exec(code, env_args)
