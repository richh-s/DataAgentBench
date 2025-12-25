code = """import json, pandas as pd
from pathlib import Path

# Load Europe metadata
path_meta = Path(var_call_ntF1ZXxAJ0FalYvyMxIbcuXE)
with open(path_meta, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_d7GDH4erzQRSUVDbpVwX55R9

# Merge on article_id
meta_df = pd.DataFrame(europe_meta)
arts_df = pd.DataFrame(articles)
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

merged = meta_df.merge(arts_df, on='article_id', how='left')

# Simple rule-based categorization into Business vs others
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'business', 'earnings', 'revenue', 'profit', 'profits', 'trade', 'trading', 'oil', 'merger', 'acquisition', 'shares', 'bond', 'bonds', 'currency', 'currencies', 'forex', 'wall st', 'nasdaq', 'dow jones', 'ftse', 'dax']

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(kw in text for kw in business_keywords)

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter business articles
biz = merged[merged['is_business']]

# Extract year
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# Filter 2010-2020 inclusive (already, but just to be safe) and group
biz_period = biz[(biz['year']>=2010) & (biz['year']<=2020)]
counts = biz_period.groupby('year').size()

# Compute average number of business articles per year
avg_per_year = counts.mean() if len(counts)>0 else 0.0

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'yearly_counts': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_ntF1ZXxAJ0FalYvyMxIbcuXE': 'file_storage/call_ntF1ZXxAJ0FalYvyMxIbcuXE.json', 'var_call_d7GDH4erzQRSUVDbpVwX55R9': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
