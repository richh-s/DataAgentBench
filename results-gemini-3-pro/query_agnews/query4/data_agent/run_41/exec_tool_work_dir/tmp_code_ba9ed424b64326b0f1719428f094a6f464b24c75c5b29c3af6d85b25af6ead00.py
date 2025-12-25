code = """import json
import pandas as pd

file_path = locals()['var_function-call-1582016694630583511']
with open(file_path, 'r') as f:
    articles_2015 = json.load(f)

df = pd.DataFrame(articles_2015)
ids = df['article_id'].astype(int)

print("__RESULT__:")
print(json.dumps({"min": int(ids.min()), "max": int(ids.max()), "count": len(ids)}))"""

env_args = {'var_function-call-1582016694630583511': 'file_storage/function-call-1582016694630583511.json', 'var_function-call-8744902824758175518': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_function-call-607457671861550025': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13447300378826587909': {'sample': [], 'total_merged': 0}, 'var_function-call-139548067748344674': {'count': 5, 'first_ids': ['0', '1', '2', '3', '4']}}

exec(code, env_args)
