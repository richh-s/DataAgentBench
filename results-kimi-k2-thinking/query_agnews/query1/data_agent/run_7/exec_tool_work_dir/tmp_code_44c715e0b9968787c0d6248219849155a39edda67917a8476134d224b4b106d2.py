code = """import json
import os

# Load articles data
articles = locals()['var_functions.query_db:2']
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

# Comprehensive sports keywords
sports_keywords = [
    'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
    'cricket', 'hockey', 'rugby', 'athletic', 'athlete', 'olympics', 'olympic',
    'world cup', 'super bowl', 'game', 'team', 'player', 'coach', 'season',
    'match', 'tournament', 'championship', 'league', 'race', 'racing', 'marathon',
    'medal', 'gold', 'silver', 'bronze', 'score', 'win', 'won', 'victory',
    'lose', 'loses', 'lost', 'defeat', 'title', 'defending', 'champion'
]

# Check each article
sports_candidates = []

for article in articles:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    # Check for sports keywords
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            sports_candidates.append({
                'title': article.get('title'),
                'description': article.get('description'),
                'desc_length': len(article.get('description', ''))
            })
            break

if sports_candidates:
    # Sort by description length
    sports_candidates.sort(key=lambda x: x['desc_length'], reverse=True)
    
    # Get top 5 for verification
    top_5 = sports_candidates[:5]
    
    # Print some debug info
    print("Top 5 sports articles by description length:")
    for i, article in enumerate(top_5):
        print(f"{i+1}. Title: {article['title']}")
        print(f"   Length: {article['desc_length']}")
        print(f"   Start: {article['description'][:60]}...")
        print()
    
    # Return the title with max length
    result = top_5[0]['title']
else:
    result = "No sports articles found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': "Why Windows isn't Unix"}

exec(code, env_args)
