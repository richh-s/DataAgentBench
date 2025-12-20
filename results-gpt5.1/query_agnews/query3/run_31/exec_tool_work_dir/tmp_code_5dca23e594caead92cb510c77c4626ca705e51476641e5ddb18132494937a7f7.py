code = """import json, pandas as pd

# Load metadata from file path
with open(var_call_QACbBhom0SZNP0B3U4yPLuEU, 'r') as f:
    metadata = json.load(f)

articles = var_call_h5nIv2pPwXTOgmjjrvuAz3XE

meta_df = pd.DataFrame(metadata)
arts_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

merged = pd.merge(meta_df, arts_df, on='article_id', how='left')

business_keywords = ['stock', 'stocks', 'market', 'markets', 'share', 'shares', 'bond', 'bonds', 'oil', 'economy', 'economic', 'business', 'company', 'companies', 'corporate', 'investor', 'investors', 'investment', 'investments', 'finance', 'financial', 'bank', 'banks', 'banking', 'trade', 'trading', 'profit', 'profits', 'loss', 'losses', 'revenue', 'earnings', 'merger', 'acquisition', 'deal', 'deals', 'loan', 'loans', 'credit', 'debt', 'crisis', 'fund', 'funds', 'currency', 'currencies', 'dollar', 'euro']

business_set = set(business_keywords)

def is_business(row):
    title = row['title'] if isinstance(row.get('title'), str) else ''
    desc = row['description'] if isinstance(row.get('description'), str) else ''
    text = (title + ' ' + desc).lower()
    return any(k in text for k in business_set)

merged['is_business'] = merged.apply(is_business, axis=1)

biz = merged[merged['is_business']]

biz['year'] = biz['publication_date'].astype(str).str.slice(0,4).astype(int)

counts_per_year = biz.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts_per_year.mean()

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_per_year': counts_per_year.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_QACbBhom0SZNP0B3U4yPLuEU': 'file_storage/call_QACbBhom0SZNP0B3U4yPLuEU.json', 'var_call_h5nIv2pPwXTOgmjjrvuAz3XE': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
