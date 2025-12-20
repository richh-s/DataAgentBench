code = """import json, pandas as pd, os

# Load full Europe metadata from file
path = var_call_L4nN5UacjwR4y7HTSwQCGeV0
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_ciPgQCEXhZBi2xhHthmKWFZB

# Build lookup for article_id -> (title, description)
art_df = pd.DataFrame(articles)
art_df['article_id'] = art_df['article_id'].astype(int)

meta_df = pd.DataFrame(europe_meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Join
df = meta_df.merge(art_df, on='article_id', how='left')

# Very simple rule-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'shares', 'profit', 'profits', 'losses', 'earnings', 'revenue', 'revenues', 'business', 'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'trade', 'trading', 'merger', 'acquisition', 'deal', 'deals', 'investment', 'investor', 'investors', 'oil', 'crude', 'gas', 'company', 'companies', 'corporate', 'industry', 'industries', 'retail', 'sales', 'jobs', 'jobless', 'unemployment', 'bond', 'bonds', 'currency', 'currencies']

kw_pattern = '|'.join(business_keywords)

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(k in text for k in business_keywords)

df['is_business'] = df.apply(is_business, axis=1)

# Filter to business articles
bdf = df[df['is_business']]

# Count per year 2010-2020 and compute average
counts = bdf.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg = counts.mean()

result = {
    'counts_per_year': counts.to_dict(),
    'average_business_articles_per_year_2010_2020_Europe': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_L4nN5UacjwR4y7HTSwQCGeV0': 'file_storage/call_L4nN5UacjwR4y7HTSwQCGeV0.json', 'var_call_q47lqRO3Vf7J0tQkQW1NEUrr': ['articles'], 'var_call_ciPgQCEXhZBi2xhHthmKWFZB': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
