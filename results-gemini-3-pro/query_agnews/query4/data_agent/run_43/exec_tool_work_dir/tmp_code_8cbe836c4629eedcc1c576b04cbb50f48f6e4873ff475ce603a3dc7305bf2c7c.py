code = """import json
import re

with open(locals()['var_function-call-14621584579191841765'], 'r') as f:
    meta_list = json.load(f)

target_ids = set()
for m in meta_list:
    target_ids.add(int(m['article_id']))

with open(locals()['var_function-call-9425048213146947809'], 'r') as f:
    all_articles = json.load(f)

# Filter for intersection
sample_articles = []
count = 0
for a in all_articles:
    try:
        aid = int(a['article_id'])
    except:
        continue
    if aid in target_ids:
        sample_articles.append(a)
        count += 1
        if count >= 5:
            break

print("__RESULT__:")
print(json.dumps(sample_articles))"""

env_args = {'var_function-call-14621584579191841765': 'file_storage/function-call-14621584579191841765.json', 'var_function-call-7803509644995873515': 6696, 'var_function-call-6632200024076563961': 'file_storage/function-call-6632200024076563961.json', 'var_function-call-11326914846194858501': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14573584342887086246': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9425048213146947809': 'file_storage/function-call-9425048213146947809.json', 'var_function-call-14825555218432229196': {'counts': {}, 'total_world': 0, 'debug': []}}

exec(code, env_args)
