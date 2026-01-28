code = """import json
import pandas as pd

# Load the articles from the query using locals()
articles = locals()['var_functions.query_db:0']

print("Total articles loaded:", len(articles))
print("First 5 articles:")
for i, article in enumerate(articles[:5]):
    print(i+1, ". Title:", article['title'])
    print("   Article ID:", article['article_id'])
    print()

# Check if there are sports articles by looking for keywords
sports_keywords = ['sports', 'sport', 'game', 'olympic', 'athlete', 'football', 'basketball', 'soccer', 'baseball', 'tennis', 'golf']
sports_articles = []

for article in articles:
    title = article['title'].lower()
    desc = article['description'].lower()
    title_has_sports = any(keyword in title for keyword in sports_keywords)
    desc_has_sports = any(keyword in desc for keyword in sports_keywords)
    
    if title_has_sports or desc_has_sports:
        sports_articles.append(article)

print("Found", len(sports_articles), "potential sports articles based on keywords")
if sports_articles:
    print("Sample sports articles:")
    for i, article in enumerate(sports_articles[:5]):
        print(i+1, ". Title:", article['title'])
        print("   Article ID:", article['article_id'])

result = json.dumps("Total: " + str(len(articles)) + ", Sports: " + str(len(sports_articles)))
print('__RESULT__:', result)"""

env_args = {'var_functions.query_db:0': [{'_id': '69696c6a0c41ae9ae8ecd6d1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696c6a0c41ae9ae8ecd6d2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696c6a0c41ae9ae8ecd6d3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696c6a0c41ae9ae8ecd6d4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696c6a0c41ae9ae8ecd6d5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
