code = """import json

# Get the articles from the previous query (using string key)
articles = var_functions.query_db:2

# Calculate description lengths
for article in articles:
    article['desc_length'] = len(article.get('description', ''))

# Sort by description length (descending)
articles_sorted = sorted(articles, key=lambda x: x['desc_length'], reverse=True)

# Print some debug info
for i, a in enumerate(articles_sorted[:3]):
    print(f"Article {i}: {a['title']}")
    print(f"Desc length: {a['desc_length']}")
    print()

# Convert to JSON-serializable format
result = json.dumps(articles_sorted, default=str)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69696a7443295558a7f48161', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696a7443295558a7f48162', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696a7443295558a7f48163', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696a7443295558a7f48164', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696a7443295558a7f48165', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
