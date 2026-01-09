code = """import json, pandas as pd

meta_path = var_call_hvAFSoxu426dQ5z94Yt4vDMi
with open(meta_path, 'r') as f:
    meta_list = json.load(f)
meta_df = pd.DataFrame(meta_list)
meta_df['article_id'] = meta_df['article_id'].astype(int)

articles = pd.DataFrame(var_call_4OlB5V3gnxAnDPibobVsNMtK)
articles['article_id'] = articles['article_id'].astype(int)

meta_ids = set(meta_df['article_id'])
matched = articles[articles['article_id'].isin(meta_ids)]

out = {
    'meta_count': int(len(meta_df)),
    'articles_count': int(len(articles)),
    'matched_count': int(len(matched)),
    'meta_id_min': int(meta_df['article_id'].min()),
    'meta_id_max': int(meta_df['article_id'].max()),
    'articles_id_min': int(articles['article_id'].min()),
    'articles_id_max': int(articles['article_id'].max())
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BYEYRTbp8MVVlsKwooJZTNUl': [{'cnt': '14860'}], 'var_call_b7HeGfRV4nk9z9C07TIuGo9Q': 'file_storage/call_b7HeGfRV4nk9z9C07TIuGo9Q.json', 'var_call_4OlB5V3gnxAnDPibobVsNMtK': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_hvAFSoxu426dQ5z94Yt4vDMi': 'file_storage/call_hvAFSoxu426dQ5z94Yt4vDMi.json', 'var_call_w4Fzci6MVDXzDhpxbS44uqXx': {'average_business_articles_per_year_europe_2010_2020': 0.0, 'total_business_articles_2010_2020': 0, 'yearly_business_article_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}}}

exec(code, env_args)
