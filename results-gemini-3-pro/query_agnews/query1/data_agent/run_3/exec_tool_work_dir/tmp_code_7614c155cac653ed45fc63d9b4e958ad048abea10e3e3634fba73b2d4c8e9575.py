code = """import json
import re

with open(locals()['var_function-call-9674498384229145557'], 'r') as f:
    articles = json.load(f)

total = len(articles)
sample_sports = []
for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    if 'olympic' in text or 'football' in text or 'sport' in text or 'soccer' in text:
        sample_sports.append(art['title'])

result = {
    "total_articles": total,
    "potential_sports_count": len(sample_sports),
    "samples": sample_sports[:20]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17250944776855184585': ['articles'], 'var_function-call-17250944776855184316': ['authors', 'article_metadata'], 'var_function-call-13601084253976166638': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-13601084253976169751': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2953041677624993579': [{'author_id': '0', 'name': 'Felicia Miles'}], 'var_function-call-175646378764434338': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446509b7cb91ea91dd468c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446509b7cb91ea91dd468d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446509b7cb91ea91dd468e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446509b7cb91ea91dd468f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2720222771617662260': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446509b7cb91ea91dd468c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446509b7cb91ea91dd468d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446509b7cb91ea91dd468e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446509b7cb91ea91dd468f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9674498384229145557': 'file_storage/function-call-9674498384229145557.json', 'var_function-call-15251398799869609527': 'No sports articles found.'}

exec(code, env_args)
