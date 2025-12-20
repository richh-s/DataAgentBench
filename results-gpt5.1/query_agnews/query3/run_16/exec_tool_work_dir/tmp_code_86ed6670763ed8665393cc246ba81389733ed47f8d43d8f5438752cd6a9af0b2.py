code = """import json, pandas as pd
from collections import defaultdict

# Load metadata (may be file path if large)
meta_source = var_call_cN8wmSquxuQsDjPPPLQKuach
if isinstance(meta_source, str):
    with open(meta_source, 'r') as f:
        meta_records = json.load(f)
else:
    meta_records = meta_source

articles_records = var_call_m9AbauotgHoTYFl3yoQNTLxj

meta_df = pd.DataFrame(meta_records)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

articles_df = pd.DataFrame(articles_records)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Simple rule-based classifier for Business category using title+description keywords
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economic', 'economy', 'finance', 'financial', 'bank', 'banks', 'banking', 'wall st', 'nasdaq', 'dow', 'profit', 'profits', 'earnings', 'revenue', 'ipo', 'merger', 'acquisition', 'corporate', 'business', 'trade', 'trading', 'oil', 'prices', 'crude', 'investment', 'investors', 'fund', 'funds', 'currency', 'currencies', 'euro', 'dollar']

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(kw in text for kw in business_keywords)

articles_df['is_business'] = articles_df.apply(is_business, axis=1)

# Join Europe meta with article texts
merged = meta_df.merge(articles_df[['article_id','is_business']], on='article_id', how='left')

# Filter to business articles
biz = merged[merged['is_business'] == True]

# Count per year 2010-2020
counts = biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)

avg_per_year = counts.mean()

result = {
  'counts_per_year': counts.to_dict(),
  'average_business_articles_per_year_2010_2020_Europe': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cN8wmSquxuQsDjPPPLQKuach': 'file_storage/call_cN8wmSquxuQsDjPPPLQKuach.json', 'var_call_m9AbauotgHoTYFl3yoQNTLxj': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
