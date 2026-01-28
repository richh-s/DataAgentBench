code = """import json

# Read the articles from the file
data_file = locals()['var_functions.query_db:10']
with open(data_file, 'r') as f:
    articles = json.load(f)

# More specific sports keywords to reduce false positives
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'world cup', 'fifa', 'uefa',
    'olympics', 'olympic games', 'athlete', 'marathon', 'championship',
    'gold medal', 'silver medal', 'bronze medal', 'coach', 'quarterback',
    'touchdown', 'goal', 'points', 'season', 'league', 'tournament',
    'hockey', 'cricket', 'rugby', 'boxing', 'wrestling', 'cycling',
    'running', 'swimming', 'volleyball', 'gymnastics', 'track and field',
    'skiing', 'snowboarding', 'ski jumping', 'figure skating',
    'motor racing', 'formula one', 'f1', 'nascar', 'indycar',
    'basketball court', 'football field', 'soccer stadium',
    'playoff', 'semifinal', 'final match', 'quarterfinal'
]

# Tech-related terms that indicate NOT a sports article
tech_keywords = ['windows', 'unix', 'linux', 'software', 'computer', 'internet', 'google', 'microsoft', 'apple', 'technology', 'tech', 'digital', 'online', 'data', 'server', 'website']

# Function to check if article is about sports
def is_sports_article(title, description):
    combined = (title + ' ' + description).lower()
    
    # First check if it's a tech article (to eliminate false positives)
    tech_score = sum(1 for keyword in tech_keywords if keyword in combined)
    if tech_score > 1:  # If multiple tech keywords found, likely not sports
        return False
    
    # Check for sports keywords
    sport_score = sum(1 for keyword in sports_keywords if keyword in combined)
    
    # More stringent requirement - need at least 1 sports keyword
    # and the article shouldn't be primarily about technology
    return sport_score >= 1

# Find the sports article with the longest description
longest_desc_length = 0
longest_sports_article = None
sports_articles_count = 0

for article in articles:
    if is_sports_article(article['title'], article['description']):
        sports_articles_count += 1
        desc_length = len(article['description'])
        
        if desc_length > longest_desc_length:
            longest_desc_length = desc_length
            longest_sports_article = article

# Prepare result
if longest_sports_article:
    result = {
        'title': longest_sports_article['title'],
        'description_length': longest_desc_length,
        'total_sports_articles_found': sports_articles_count,
        'article_id': longest_sports_article['article_id']
    }
else:
    result = {
        'title': None,
        'message': 'No sports articles found',
        'total_sports_articles_found': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969666e3efec42e10016862', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969666e3efec42e10016863', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969666e3efec42e10016864', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969666e3efec42e10016865', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969666e3efec42e10016866', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'found_sports_articles': 0, 'message': 'No sports articles found'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 1000}, 'var_functions.execute_python:14': {'title': "Why Windows isn't Unix", 'description_length': 708, 'total_sports_articles_found': 268}}

exec(code, env_args)
