code = """import json, pandas as pd, os

# Load full Europe metadata
path = var_call_x1B89PLxAVAkNHfFw7EgdZGE
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_3uhkTmUeDIdWQ4k6c6K1rHnx

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge
df = meta_df.merge(articles_df, on='article_id', how='left')

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_keywords = ['stock', 'stocks', 'market', 'markets', 'share', 'shares', 'profit', 'profits', 'loss', 'losses', 'bond', 'bonds', 'investor', 'investors', 'investment', 'investments', 'bank', 'banks', 'loan', 'loans', 'merger', 'acquisition', 'trade', 'trading', 'economy', 'economic', 'business', 'company', 'companies', 'corporate', 'financial', 'finance', 'earnings', 'revenue', 'sales', 'oil', 'currency', 'currencies', 'dollar', 'euro']

pattern = '|'.join(business_keywords)

business_mask = text.str.contains(pattern, regex=True)

business_df = df[business_mask].copy()

business_df['year'] = business_df['publication_date'].str.slice(0,4).astype(int)

counts = business_df.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts.mean()

result = {
    'counts_per_year': counts.to_dict(),
    'average_business_articles_per_year_2010_2020_europe': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_x1B89PLxAVAkNHfFw7EgdZGE': 'file_storage/call_x1B89PLxAVAkNHfFw7EgdZGE.json', 'var_call_3uhkTmUeDIdWQ4k6c6K1rHnx': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
