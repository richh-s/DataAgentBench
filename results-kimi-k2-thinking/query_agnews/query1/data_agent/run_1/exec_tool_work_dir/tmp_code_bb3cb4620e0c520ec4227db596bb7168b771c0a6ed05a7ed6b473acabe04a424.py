code = """import json

# Get the articles data from storage
articles_data = locals()['var_functions.query_db:8']

# Check if we need to load from file
if isinstance(articles_data, str) and articles_data.endswith('.json'):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_data

# Analyze the articles we have and look for sports-related content
sports_keywords = ['sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympic', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl']
sports_articles = []

for article in articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    # Check if any sports keyword appears
    has_sports_keyword = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
    
    sports_articles.append({
        'article_id': article['article_id'],
        'title': article['title'],
        'description': article['description'],
        'desc_length': len(article['description']),
        'appears_sports': has_sports_keyword
    })

print('__RESULT__:')
print(json.dumps(sports_articles, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969634fcb9584e5a9a9cd5c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969634fcb9584e5a9a9cd5d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969634fcb9584e5a9a9cd5e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'type': "<class 'list'>", 'is_string': False, 'preview': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_functions.query_db:8': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969634fcb9584e5a9a9cd5c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969634fcb9584e5a9a9cd5d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969634fcb9584e5a9a9cd5e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
