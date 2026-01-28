code = """import json
import os
import re

# Load articles data
articles = locals()['var_functions.query_db:2']
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

print("Loaded " + str(len(articles)) + " articles")

# More comprehensive sports keywords
sports_keywords = [
    'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
    'cricket', 'hockey', 'rugby', 'volleyball', 'handball', 'boxing', 'wrestling',
    'athletic', 'athlete', 'olympics', 'olympic', 'world cup', 'super bowl', 
    'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'champions league',
    'game', 'team', 'player', 'coach', 'season', 'match', 'tournament', 
    'championship', 'league', 'race', 'racing', 'marathon', 'sprint',
    'medal', 'gold', 'silver', 'bronze', 'score', 'won', 'win', 'victory',
    'defeat', 'champion', 'title', 'final', 'semifinal', 'quarterfinal',
    'stadium', 'arena', 'court', 'field', 'pitch'
]

sports_articles = []

for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    
    # Check for sports context
    for keyword in sports_keywords:
        # Use word boundaries to avoid false positives (e.g., "game" in "game theory")
        pattern = r'\b' + re.escape(keyword) + r'\b'
        if re.search(pattern, title) or re.search(pattern, desc):
            sports_articles.append({
                'title': article.get('title'),
                'description': article.get('description'),
                'desc_length': len(article.get('description', ''))
            })
            break

if sports_articles:
    # Sort by description length
    sports_articles.sort(key=lambda x: x['desc_length'], reverse=True)
    
    print("Found " + str(len(sports_articles)) + " sports articles")
    print("\nTop 5 with longest descriptions:")
    for i in range(min(5, len(sports_articles))):
        article = sports_articles[i]
        print(str(i+1) + ". Title: " + article['title'])
        print("   Length: " + str(article['desc_length']))
        print("   Start: " + article['description'][:80])
        print()
    
    result_title = sports_articles[0]['title']
else:
    print("No clear sports articles found with keyword matching")
    result_title = "No sports articles identified"

print("__RESULT__:")
print(json.dumps(result_title))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': "Why Windows isn't Unix", 'var_functions.execute_python:20': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.list_db:22': ['authors', 'article_metadata']}

exec(code, env_args)
