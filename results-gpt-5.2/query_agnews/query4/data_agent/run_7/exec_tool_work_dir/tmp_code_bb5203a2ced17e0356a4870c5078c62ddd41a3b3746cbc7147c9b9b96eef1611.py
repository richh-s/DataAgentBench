code = """import json, pandas as pd

meta_src = var_call_smSVMN9cKDVUnyrQMYxy4rXv
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src
arts = var_call_bv2CnHsMIXHWODP6MPLURA3N

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df.columns = [c.strip() for c in meta_df.columns]
arts_df.columns = [c.strip() for c in arts_df.columns]

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

j = meta_df.merge(arts_df, on='article_id', how='inner', suffixes=('_meta','_art'))

res = {
  'meta_cols': list(meta_df.columns),
  'joined_cols': list(j.columns),
  'rows': int(len(j))
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_smSVMN9cKDVUnyrQMYxy4rXv': 'file_storage/call_smSVMN9cKDVUnyrQMYxy4rXv.json', 'var_call_bv2CnHsMIXHWODP6MPLURA3N': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
