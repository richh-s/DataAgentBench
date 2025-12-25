code = """import json, pandas as pd
from collections import defaultdict

# Load full metadata result from file
with open(var_call_BixES22lyZ3hMdNBkNS0xiIV, 'r') as f:
    meta = json.load(f)

arts = var_call_tkOOedsOI3kBvEEeyS2TluQQ

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

merged = meta_df.merge(arts_df, on='article_id', how='inner')

# Very simple rule-based classifier for Business category
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'dow ', 'nasdaq', 's&p', 'bond', 'bonds', 'treasury', 'market', 'markets',
    'shares', 'share', 'investor', 'investors', 'investment', 'fund', 'funds', 'profit', 'profits', 'earnings', 'revenue',
    'sales', 'merger', 'acquisition', 'm&a', 'ipo', 'float', 'company', 'companies', 'corporate', 'business', 'commerce',
    'trade', 'trading', 'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'loan', 'loans',
    'credit', 'debt', 'currency', 'currencies', 'forex', 'oil', 'crude', 'energy', 'gas', 'commodit', 'retail', 'consumer',
    'industry', 'industries', 'jobless', 'unemployment', 'housing', 'real estate', 'quarter', 'q1', 'q2', 'q3', 'q4'
]

bk_set = set(business_keywords)

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    return any(k in text for k in bk_set)

merged['is_business'] = merged.apply(is_business, axis=1)

business = merged[merged['is_business']].copy()

business['year'] = business['publication_date'].str.slice(0,4).astype(int)

counts = business.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts.mean()

result = {
    'counts_per_year': counts.to_dict(),
    'average_business_articles_per_year_2010_2020_europe': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BixES22lyZ3hMdNBkNS0xiIV': 'file_storage/call_BixES22lyZ3hMdNBkNS0xiIV.json', 'var_call_tkOOedsOI3kBvEEeyS2TluQQ': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
