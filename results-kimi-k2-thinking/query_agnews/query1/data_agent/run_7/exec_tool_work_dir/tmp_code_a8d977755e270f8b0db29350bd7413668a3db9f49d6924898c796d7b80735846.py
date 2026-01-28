code = """import json
import os

# Load articles data
stored_data = locals()['var_functions.query_db:2']

# Check if it's a file path or direct data
if isinstance(stored_data, str) and os.path.exists(stored_data):
    with open(stored_data, 'r') as f:
        articles = json.load(f)
else:
    articles = stored_data

# Count total articles
print(f"Total articles: {len(articles)}")

# Create list of sports-related keywords
sports_keywords = [
    'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis',
    'golf', 'olympics', 'athlete', 'game', 'team', 'league', 'cup',
    'championship', 'tournament', 'match', 'player', 'coach', 'season',
    'race', 'racing', 'marathon', 'medal', 'score', 'win', 'lose', 'victory'
]

# Find sports articles
sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    # Check if any sports keyword appears
    for keyword in sports_keywords:
        if keyword in title or keyword in description:
            sports_articles.append({
                'title': article.get('title'),
                'description': article.get('description'),
                'desc_length': len(article.get('description', ''))
            })
            break

print(f"Found {len(sports_articles)} potential sports articles")

if sports_articles:
    # Sort by description length
    sports_articles.sort(key=lambda x: x['desc_length'], reverse=True)
    
    # Get the article with longest description
    longest_article = sports_articles[0]
    
    print(f"\nArticle with longest description:")
    print(f"Title: {longest_article['title']}")
    print(f"Description length: {longest_article['desc_length']}")
    
    # Print result in required format
    result = longest_article['title']
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
