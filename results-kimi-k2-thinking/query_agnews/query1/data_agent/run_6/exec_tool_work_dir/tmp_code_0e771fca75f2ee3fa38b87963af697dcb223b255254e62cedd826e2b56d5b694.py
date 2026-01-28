code = """import json

# Get the articles from the storage variable
articles = locals()['var_functions.query_db:2']

# Function to classify sports articles
def is_sports_article(title, description):
    sport_keywords = ['sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'nfl', 'nba', 'mlb', 'nhl', 'athlete', 'race', 'marathon', 'world cup', 'championship', 'medal', 'coach', 'team', 'player', 'game', 'season', 'league', 'tournament']
    combined_text = (title + ' ' + description).lower()
    for keyword in sport_keywords:
        if keyword in combined_text:
            return True
    return False

# Find all sports articles and their description lengths
sports_articles = []
for article in articles:
    if is_sports_article(article['title'], article['description']):
        desc_length = len(article['description'])
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'description_length': desc_length
        })

# Find the one with longest description
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    result = {
        'found_sports_articles': len(sports_articles),
        'longest_sports_article_title': longest_article['title']
    }
else:
    result = {'found_sports_articles': 0, 'message': 'No sports articles found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969666e3efec42e10016862', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969666e3efec42e10016863', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969666e3efec42e10016864', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969666e3efec42e10016865', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969666e3efec42e10016866', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
