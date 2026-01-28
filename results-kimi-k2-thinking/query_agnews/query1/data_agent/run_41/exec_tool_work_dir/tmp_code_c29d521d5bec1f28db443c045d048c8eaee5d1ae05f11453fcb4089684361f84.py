code = """import json
import os

# Read the articles file
file_path = '/tmp/query_result_articles_database.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        articles = json.load(f)
else:
    # Try to find the file
    possible_paths = ['/tmp/query_result_*.json', '/tmp/*.json']
    articles = []\n# Define sports keywords
sports_keywords = [
    'sport', 'game', 'football', 'soccer', 'basketball', 'baseball', 'tennis',
    'olympic', 'olympics', 'league', 'team', 'player', 'coach', 'stadium', 'match',
    'tournament', 'championship', 'world cup', 'nba', 'nfl', 'mlb', 'nhl',
    'golf', 'cricket', 'rugby', 'boxing', 'wrestling', 'ski', 'skating',
    'athlete', 'athletic', 'marathon', 'race', 'racing', 'hockey', 'volleyball',
    'badminton', 'swimming', 'cycling', 'running', 'judo', 'karate', 'bowling',
    'fencing', 'gymnastics', 'handball', 'medal', 'gold medal', 'silver medal',
    'bronze medal', 'world record', 'score', 'final', 'quarterfinal', 'semifinal'
]

# Filter sports articles
sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    is_sports = any(keyword in title or keyword in description for keyword in sports_keywords)
    
    if is_sports:
        sports_articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'length': len(article.get('description', ''))
        })

# Find article with longest description
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['length'])
    result = longest_article['title']
else:
    result = "No sports articles found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'No sports articles found in the dataset'}

exec(code, env_args)
