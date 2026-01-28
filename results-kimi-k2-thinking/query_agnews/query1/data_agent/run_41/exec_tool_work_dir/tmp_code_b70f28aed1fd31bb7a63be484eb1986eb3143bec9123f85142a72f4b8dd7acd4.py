code = """import json
import os

# Read the articles data from the file stored in the variable
# The key is var_functions.query_db:0 but we need to access it with underscore
storage_key = 'var_functions.query_db_0'
if storage_key in locals():
    file_path = locals()[storage_key]
else:
    # Try alternative key format
    file_path = '/tmp/query_result_articles_database.json'

# If it's a file path string, read it
if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        articles = json.load(f)
else:
    # Fallback - try to read from preview or handle differently
    articles = []

# Define sports keywords to identify sports articles
sports_keywords = [
    'sport', 'game', 'football', 'soccer', 'basketball', 'baseball', 'tennis',
    'olympic', 'league', 'team', 'player', 'coach', 'stadium', 'match',
    'tournament', 'championship', 'world cup', 'nba', 'nfl', 'mlb', 'nhl',
    'golf', 'cricket', 'rugby', 'boxing', 'wrestling', 'ski', 'skating',
    'athlete', 'athletic', 'marathon', 'race', 'racing', 'hockey',
    'volleyball', 'badminton', 'swimming', 'cycling', 'running', 'judo',
    'karate', 'bowling', 'fencing', 'gymnastics', 'handball'
]

# Function to check if an article is about sports
def is_sports_article(title, description):
    if not title or not description:
        return False
        
    title_lower = title.lower()
    desc_lower = description.lower()
    
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            return True
    return False

# Filter sports articles and find the one with longest description
sports_articles = []
for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    
    if is_sports_article(title, description):
        desc_length = len(description)
        sports_articles.append({
            'article_id': article.get('article_id'),
            'title': title,
            'description': description,
            'desc_length': desc_length
        })

# If no sports articles found, return message
if not sports_articles:
    result = json.dumps("No sports articles found in the dataset")
else:
    # Find the sports article with the longest description
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    result = json.dumps(longest_article['title'])

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
