code = """import json
import re

# Load the articles data from the file path stored in the variable
articles_file_path = var_functions.query_db:8

# Read the articles data
with open(articles_file_path, 'r') as f:
    articles = json.load(f)

# Define sports keywords to identify sports articles
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
    'olympics', 'championship', 'league', 'team', 'player', 'coach',
    'game', 'match', 'score', 'victory', 'defeat', 'win', 'loss',
    'tournament', 'season', 'record', 'sport', 'sports', 'racing',
    'hockey', 'cricket', 'rugby', 'athlete', 'athletic', 'medal',
    'final', 'quarterfinal', 'semifinal', 'bronze', 'silver', 'gold',
    'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'world cup'
]

# Function to check if an article is sports-related
def is_sports_article(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            return True
    return False

# Filter sports articles and find the one with longest description
sports_articles = []
max_length = 0
longest_desc_article = None

for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    
    if is_sports_article(title, description):
        sports_articles.append(article)
        desc_length = len(description)
        if desc_length > max_length:
            max_length = desc_length
            longest_desc_article = article

# Sort sports articles by description length to verify
sports_articles_sorted = sorted(sports_articles, key=lambda x: len(x.get('description', '')), reverse=True)

# Get the top 10 sports articles by description length for verification
top_10_sports = sports_articles_sorted[:10]

result = {
    'total_articles': len(articles),
    'sports_articles_count': len(sports_articles),
    'longest_description_article': longest_desc_article,
    'max_description_length': max_length,
    'top_10_sports_articles': top_10_sports
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
