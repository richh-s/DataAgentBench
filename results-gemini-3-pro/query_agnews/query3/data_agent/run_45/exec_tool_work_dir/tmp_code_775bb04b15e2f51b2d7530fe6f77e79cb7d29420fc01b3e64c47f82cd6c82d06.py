code = """import json
import pandas as pd

metadata_file = locals()['var_function-call-6625241908070332927']
articles_file = locals()['var_function-call-3790426654130503154']

with open(metadata_file, 'r') as f:
    meta = json.load(f)
with open(articles_file, 'r') as f:
    arts = json.load(f)

df_m = pd.DataFrame(meta)
df_a = pd.DataFrame(arts)
df_m['article_id'] = df_m['article_id'].astype(int)
df_a['article_id'] = df_a['article_id'].astype(int)

df = pd.merge(df_m, df_a, on='article_id', how='inner')

samples = df[['article_id', 'title', 'description']].head(20).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(samples))"""

env_args = {'var_function-call-6625241908070332927': 'file_storage/function-call-6625241908070332927.json', 'var_function-call-16753801428595803261': 'TOO_MANY', 'var_function-call-6611812941830838374': 14860, 'var_function-call-2647792999411181703': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1579965867563204147': [{'article_id': 3, 'publication_date': '2020-03-04', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}], 'var_function-call-9194869213981365014': {'metadata_count': 14860, 'articles_count': 5, 'articles_preview': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_function-call-3790426654130503154': 'file_storage/function-call-3790426654130503154.json', 'var_function-call-14099101923129492474': {'counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'average': 0.0, 'total_business': 0, 'total_merged': 5762}}

exec(code, env_args)
