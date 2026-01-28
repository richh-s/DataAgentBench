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

meta_df['article_id_num'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id_num'] = pd.to_numeric(arts_df['article_id'], errors='coerce')

meta_ids = set(meta_df.dropna(subset=['article_id_num'])['article_id_num'].astype(int).head(5000).tolist())
arts_ids = set(arts_df.dropna(subset=['article_id_num'])['article_id_num'].astype(int).head(5000).tolist())

inter = sorted(list(meta_ids.intersection(arts_ids)))

print('__RESULT__:')
print(json.dumps({'meta_ids_sample_minmax': [int(meta_df.article_id_num.min()), int(meta_df.article_id_num.max())],
                  'arts_ids_sample_minmax': [int(arts_df.article_id_num.min()), int(arts_df.article_id_num.max())],
                  'meta_n': int(meta_df.shape[0]), 'arts_n': int(arts_df.shape[0]),
                  'intersection_sample': inter[:20], 'intersection_size_sampled': len(inter)}))"""

env_args = {'var_call_ycD5Tn2PvYb9A119GxQY5n9w': 'file_storage/call_ycD5Tn2PvYb9A119GxQY5n9w.json', 'var_call_YXGYT2sREtdoS9rXJDNwnswl': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_QAEJioMBHRwZND3u71PQv6O6': {'meta_cols': ['region', 'article_id'], 'arts_cols': ['article_id', 'title', 'description'], 'meta_head': [{'region': 'Europe', 'article_id': '13'}, {'region': 'South America', 'article_id': '18'}, {'region': 'Africa', 'article_id': '26'}], 'arts_head': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_call_JvQ2GOU7xWxyvLLFE0N53gug': {'columns': ['region', 'article_id', 'title', 'description'], 'head': []}, 'var_call_7t7HkyvKz92Pze5LYBX6t8eS': {'df_cols': ['region', 'article_id', 'title', 'description'], 'df_len': 0, 'meta_cols': ['region', 'article_id'], 'arts_cols': ['article_id', 'title', 'description']}}

exec(code, env_args)
