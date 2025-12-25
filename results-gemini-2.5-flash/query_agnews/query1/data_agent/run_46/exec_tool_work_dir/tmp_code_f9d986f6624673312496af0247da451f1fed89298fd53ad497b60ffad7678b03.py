code = """import json
import pandas as pd

articles = json.loads(locals()['var_function-call-1935282102866927201']['query_db_response']['results'][0])
df = pd.DataFrame(articles)
sports_articles = df[df['description'].str.contains('sports', case=False) | df['title'].str.contains('sports', case=False)]
sports_articles['description_length'] = sports_articles['description'].str.len()
max_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
result = max_description_article['title']
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-1935282102866927201': [{'_id': '6943d6f733843de1eae62a90', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d6f733843de1eae62a91', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d6f733843de1eae62a92', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d6f733843de1eae62a93', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d6f733843de1eae62a94', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
