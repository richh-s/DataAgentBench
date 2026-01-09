code = """import json, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_maybe_path(var_call_ycD5Tn2PvYb9A119GxQY5n9w)
arts = load_maybe_path(var_call_YXGYT2sREtdoS9rXJDNwnswl)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)
meta_df.columns = [c.strip() for c in meta_df.columns]
arts_df.columns = [c.strip() for c in arts_df.columns]

meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'], errors='coerce')
meta_df = meta_df.dropna(subset=['article_id']).copy()
arts_df = arts_df.dropna(subset=['article_id']).copy()
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

df = meta_df.merge(arts_df, on='article_id', how='inner')

print('__RESULT__:')
print(json.dumps({'df_cols': list(df.columns), 'df_len': int(len(df)), 'meta_cols': list(meta_df.columns), 'arts_cols': list(arts_df.columns)}))"""

env_args = {'var_call_ycD5Tn2PvYb9A119GxQY5n9w': 'file_storage/call_ycD5Tn2PvYb9A119GxQY5n9w.json', 'var_call_YXGYT2sREtdoS9rXJDNwnswl': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_QAEJioMBHRwZND3u71PQv6O6': {'meta_cols': ['region', 'article_id'], 'arts_cols': ['article_id', 'title', 'description'], 'meta_head': [{'region': 'Europe', 'article_id': '13'}, {'region': 'South America', 'article_id': '18'}, {'region': 'Africa', 'article_id': '26'}], 'arts_head': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_call_JvQ2GOU7xWxyvLLFE0N53gug': {'columns': ['region', 'article_id', 'title', 'description'], 'head': []}}

exec(code, env_args)
