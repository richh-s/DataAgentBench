code = """import json

# Load the articles data
articles = locals()['var_functions.query_db:0']

# Search for sports articles by checking for sports-related keywords
sports_articles = []
sports_keywords = ['game', 'football', 'basketball', 'soccer', 'baseball', 'tennis', 'golf', 'olympic', 'champion', 'league', 'sport', 'athlete', 'win', 'lose', 'match', 'score', 'team', 'player', 'coach', 'season', 'cup']

for article in articles:
    title = article['title'].lower()
    desc = article['description'].lower()
    
    for keyword in sports_keywords:
        if keyword in title or keyword in desc:
            sports_articles.append(article)
            break

# Find the sports article with the longest description
if sports_articles:
    longest_sports_article = max(sports_articles, key=lambda x: len(x['description']))
    result = {
        'title': longest_sports_article['title'],
        'description_length': len(longest_sports_article['description']),
        'description': longest_sports_article['description'],
        'total_sports_articles_found': len(sports_articles)
    }
else:
    # If no sports articles found by keywords, check all articles
    longest_article = max(articles, key=lambda x: len(x['description']))
    result = {
        'title': longest_article['title'],
        'description_length': len(longest_article['description']),
        'description': longest_article['description'],
        'note': 'No sports articles found by keyword search'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '696972f8e1f960ac8c37d44b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696972f8e1f960ac8c37d44c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696972f8e1f960ac8c37d44d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696972f8e1f960ac8c37d44e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696972f8e1f960ac8c37d44f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
