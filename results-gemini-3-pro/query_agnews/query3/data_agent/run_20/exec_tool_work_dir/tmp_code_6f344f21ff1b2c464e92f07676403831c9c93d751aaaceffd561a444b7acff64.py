code = """import json
import pandas as pd

meta_path = locals()['var_function-call-7712258569316983833']
with open(meta_path, 'r') as f:
    meta_records = json.load(f)

df_meta = pd.DataFrame(meta_records)
try:
    ids = df_meta['article_id'].astype(int)
    print("__RESULT__:")
    print(json.dumps({"min": int(ids.min()), "max": int(ids.max()), "count": len(ids)}))
except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-7712258569316983833': 'file_storage/function-call-7712258569316983833.json', 'var_function-call-11963313759828392180': 'file_storage/function-call-11963313759828392180.json', 'var_function-call-17209390838595579310': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14274068418124532630': 5, 'var_function-call-6584692014692107885': 'file_storage/function-call-6584692014692107885.json', 'var_function-call-9657999728847516139': {'counts_per_year': {'2010': 47, '2011': 56, '2012': 47, '2013': 57, '2014': 54, '2015': 64, '2016': 55, '2017': 61, '2018': 63, '2019': 49, '2020': 63}, 'average': 56.0, 'total_articles': 2273, 'biz_articles': 616}, 'var_function-call-2979519728865069778': {'min': 0, 'max': 19999, 'count': 20000}}

exec(code, env_args)
