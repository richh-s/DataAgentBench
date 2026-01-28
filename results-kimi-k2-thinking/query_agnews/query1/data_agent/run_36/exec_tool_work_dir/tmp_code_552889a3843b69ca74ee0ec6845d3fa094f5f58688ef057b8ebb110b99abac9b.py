code = """import json

# Get the articles data
articles = locals()['var_functions.query_db:0']

# Count articles
total_articles = len(articles)

# Define sports keywords to identify sports articles
sports_keywords = ['sport', 'sports', 'game', 'games', 'team', 'teams', 'player', 'players', 'football', 'basketball', 'soccer', 'baseball', 'tennis', 'golf', 'hockey', 'league', 'match', 'championship', 'tournament', 'athlete', 'athletes', 'coach', 'coaching', 'olympic', 'olympics']

# Find sports articles
sports_articles = []

for article in articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    # Check for sports keywords
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            sports_articles.append(article)
            break

# Prepare result
if len(sports_articles) == 0:
    result = "No sports articles found"
else:
    # Find article with longest description
    longest_article = max(sports_articles, key=lambda x: len(x['description']))
    result = longest_article['title']

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969792c1611c676151fbe52', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969792c1611c676151fbe53', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969792c1611c676151fbe54', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969792c1611c676151fbe55', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969792c1611c676151fbe56', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
