code = """import json

# Load articles data from the file
file_path = 'file_storage/functions.query_db:10.json'
with open(file_path, 'r') as f:
    articles_data = json.load(f)

print('Total articles loaded:', len(articles_data))

# Function to identify sports articles
def is_sports_article(title, description):
    """Determine if an article is about sports based on title and description"""
    sports_keywords = [
        'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis',
        'golf', 'cricket', 'rugby', 'hockey', 'olympics', 'olympic',
        'game', 'team', 'player', 'players', 'league', 'season', 'coach',
        'championship', 'tournament', 'match', 'matches', 'score', 'goal',
        'athlete', 'athletes', 'competition', 'stadium', 'quarterback',
        'pitcher', 'batter', 'goalie', 'footballer', 'world cup',
        'nba', 'nfl', 'mlb', 'nhl', 'ncaa', 'fifa', 'uefa',
        'premier league', 'bundesliga', 'la liga', 'serie a',
        'basketball', 'soccer', 'football', 'running', 'marathon',
        'cycling', 'swimming', 'boxing', 'mma', 'ufc', 'wrestling',
        'racing', 'formula one', 'nascar', 'indycar', 'tour de france'
    ]
    
    text = (title + ' ' + description).lower()
    
    for keyword in sports_keywords:
        if keyword in text:
            return True
    return False

# Find sports articles and their description lengths
sports_articles = []
for article in articles_data:
    title = article['title']
    description = article['description']
    
    if is_sports_article(title, description):
        desc_length = len(description)
        sports_articles.append({
            'article_id': article['article_id'],
            'title': title,
            'description': description,
            'desc_length': desc_length
        })

print('Sports articles found:', len(sports_articles))

result = 'No sports articles found'
if sports_articles:
    # Find the article with the longest description
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    result = longest_article['title']
    print('Longest sports article:', result)
    print('Description length:', longest_article['desc_length'])

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'_id': '696969edc7924738c51171a0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696969edc7924738c51171a1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696969edc7924738c51171a2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696969edc7924738c51171a3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696969edc7924738c51171a4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'_id': '696969edc7924738c51171a0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696969edc7924738c51171a1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696969edc7924738c51171a2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696969edc7924738c51171a3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696969edc7924738c51171a4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'_id': '696969edc7924738c51171a0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696969edc7924738c51171a1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696969edc7924738c51171a2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696969edc7924738c51171a3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696969edc7924738c51171a4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:16': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
