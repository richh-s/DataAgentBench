code = """import json
import pandas as pd

articles_data = locals()['var_function-call-1929457005846210006']['query_db_response']['results'][0]
articles_list = json.loads(articles_data)

sports_articles = []
for article in articles_list:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    if "sport" in title or "sports" in title or "sport" in description or "sports" in description:
        sports_articles.append({
            'title': article.get('title'),
            'description_length': len(article.get('description', ''))
        })

if not sports_articles:
    result = {"answer": "No sports articles found."}
else:
    max_desc_article = max(sports_articles, key=lambda x: x['description_length'])
    result = {"title": max_desc_article['title']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-1929457005846210006': [{'_id': '6943b8dfbc7d37409567f447', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b8dfbc7d37409567f448', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b8dfbc7d37409567f449', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b8dfbc7d37409567f44a', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b8dfbc7d37409567f44b', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
