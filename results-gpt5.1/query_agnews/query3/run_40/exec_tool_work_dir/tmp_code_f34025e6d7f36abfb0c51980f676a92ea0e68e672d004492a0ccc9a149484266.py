code = """import json, pandas as pd

# Load full Europe metadata from file
with open(var_call_pCFxFjWlcmYGaiGu7WUDm2lf, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_Oz0HbuuZWemwBMOABkks852f

# Create DataFrames
meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Simple keyword-based classifier for Business category
business_keywords = ['market', 'markets', 'stock', 'stocks', 'wall st', 'wall street', 'dow', 'nasdaq', 'ftse', 'dax', 'nikkei', 'share', 'shares', 'bond', 'bonds', 'treasury', 'yield', 'oil', 'gold', 'crude', 'price', 'prices', 'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'fund', 'funds', 'investment', 'investor', 'investors', 'private equity', 'merger', 'acquisition', 'corporate', 'profit', 'profits', 'earnings', 'revenue', 'sales', 'trade', 'trading', 'business']

bk_set = set(business_keywords)

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(k in text for k in bk_set)

articles_df['is_business'] = articles_df.apply(is_business, axis=1)

# Join metadata with classified articles
merged = meta_df.merge(articles_df[['article_id', 'is_business']], on='article_id', how='left')

# Filter to business articles
biz = merged[merged['is_business']]

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# Count business articles per year 2010-2020
counts = biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts.mean()

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_per_year': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_pCFxFjWlcmYGaiGu7WUDm2lf': 'file_storage/call_pCFxFjWlcmYGaiGu7WUDm2lf.json', 'var_call_Oz0HbuuZWemwBMOABkks852f': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
