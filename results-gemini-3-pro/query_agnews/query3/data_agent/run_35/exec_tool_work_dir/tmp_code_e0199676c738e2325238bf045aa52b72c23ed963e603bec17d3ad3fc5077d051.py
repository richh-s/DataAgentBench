code = """# Debugging counts
import json
import re

metadata_key = 'var_function-call-3785327814520365478'
metadata_file = locals()[metadata_key]
with open(metadata_file, 'r') as f:
    metadata_list = json.load(f)

article_years = set()
for entry in metadata_list:
    aid = str(entry['article_id'])
    article_years.add(aid)

articles_key = 'var_function-call-10461147015258945080'
articles_file = locals()[articles_key]
with open(articles_file, 'r') as f:
    articles_list = json.load(f)

matched_count = 0
for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_years:
        matched_count += 1

print("__RESULT__:")
print(json.dumps({"total_metadata": len(metadata_list), "total_articles": len(articles_list), "matched": matched_count}))"""

env_args = {'var_function-call-3785327814520365478': 'file_storage/function-call-3785327814520365478.json', 'var_function-call-10425828837385434801': 14860, 'var_function-call-14030611635613635526': ['articles'], 'var_function-call-14105563126826159578': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8122656162104347158': 5, 'var_function-call-10461147015258945080': 'file_storage/function-call-10461147015258945080.json', 'var_function-call-16342635927272023977': {'yearly_counts': {'2010': 50, '2011': 68, '2012': 47, '2013': 61, '2014': 59, '2015': 55, '2016': 63, '2017': 62, '2018': 73, '2019': 51, '2020': 64}, 'average': 59.36363636363637}, 'var_function-call-14388110284107897755': {'yearly_counts': {'2010': 1, '2011': 4, '2012': 4, '2013': 6, '2014': 1, '2015': 1, '2016': 7, '2017': 3, '2018': 4, '2019': 3, '2020': 3}, 'average': 3.3636363636363638}}

exec(code, env_args)
