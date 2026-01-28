code = """import json
import re

# Access the articles data from previous query
articles_data = locals()['var_functions.query_db:2']

# Define sports-related keywords to identify sports articles
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis',
    'golf', 'cricket', 'rugby', 'volleyball', 'swimming', 'cycling',
    'olympic', 'world cup', 'championship', 'tournament', 'league',
    'game', 'match', 'player', 'team', 'score', 'victory', 'defeat',
    'coach', 'season', 'sport', 'athlete', 'medal', 'title', 'cup',
    'final', 'quarter', 'semifinal', 'quarterfinal', 'racing', 'marathon'
]

# Function to check if an article is about sports
def is_sports_article(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    # Check if any sports keyword appears in title or description
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            return True
    return False

# Process articles to find sports articles and their description lengths
sports_articles = []

for article in articles_data:
    title = article.get('title', '')
    description = article.get('description', '')
    
    if is_sports_article(title, description):
        desc_length = len(description)
        sports_articles.append({
            'title': title,
            'description': description,
            'desc_length': desc_length,
            'article_id': article.get('article_id')
        })

# Sort sports articles by description length (descending)
sports_articles_sorted = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)

# Get the sports article with the longest description
if sports_articles_sorted:
    longest_article = sports_articles_sorted[0]
    result = {
        'title': longest_article['title'],
        'description_length': longest_article['desc_length'],
        'total_sports_articles_found': len(sports_articles)
    }
else:
    result = {
        'message': 'No sports articles found',
        'total_sports_articles_found': 0
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata']}

exec(code, env_args)
