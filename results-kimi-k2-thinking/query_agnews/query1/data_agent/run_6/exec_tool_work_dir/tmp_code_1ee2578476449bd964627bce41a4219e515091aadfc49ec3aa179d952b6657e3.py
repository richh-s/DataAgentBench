code = """import json

# Read the articles from the file
data_file = locals()['var_functions.query_db:10']
with open(data_file, 'r') as f:
    articles = json.load(f)

# Define sports keywords
sports_keywords = [
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'olympic', 'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'fifa', 'world cup',
    'athlete', 'race', 'marathon', 'championship', 'medal', 'coach', 'team',
    'player', 'game', 'match', 'score', 'season', 'league', 'tournament',
    'hockey', 'cricket', 'rugby', 'boxing', 'wrestling', 'cycling', 'skiing',
    'running', 'swimming', 'volleyball', 'handball', 'badminton', 'table tennis',
    'bowling', 'skating', ' gymnastics', 'track', 'field', 'ski', 'snowboard',
    ' surfing', 'skateboard', 'karate', 'judo', 'taekwondo', 'fencing',
    'archery', 'shooting', 'equestrian', 'rowing', 'canoe', 'kayak', 'sailing',
    'diving', 'water polo', 'polo', 'lacrosse', 'cricket', 'snooker', 'pool',
    'darts', 'billiards', 'bowls', 'curling', 'softball', 'rounders'
]

# Function to check if article is about sports
def is_sports_article(title, description):
    combined = (title + ' ' + description).lower()
    for keyword in sports_keywords:
        if keyword in combined:
            return True
    return False

# Find all sports articles and track the one with longest description
sports_articles = []
longest_desc_length = 0
longest_sports_article = None

for article in articles:
    if is_sports_article(article['title'], article['description']):
        desc_length = len(article['description'])
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description_length': desc_length
        })
        
        if desc_length > longest_desc_length:
            longest_desc_length = desc_length
            longest_sports_article = article

# Prepare result
if longest_sports_article:
    result = {
        'title': longest_sports_article['title'],
        'description_length': longest_desc_length,
        'total_sports_articles_found': len(sports_articles)
    }
else:
    result = {
        'title': None,
        'message': 'No sports articles found',
        'total_sports_articles_found': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969666e3efec42e10016862', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969666e3efec42e10016863', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969666e3efec42e10016864', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969666e3efec42e10016865', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969666e3efec42e10016866', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'found_sports_articles': 0, 'message': 'No sports articles found'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 1000}}

exec(code, env_args)
