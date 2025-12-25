code = """import json, pandas as pd, os

# Load Europe metadata from file
path = var_call_TbUotq9SoiVRSIxGFdU2Doat
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_lJcTnXNcKh9ATJ0uj3Aoh1SX

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to get titles/descriptions for Europe articles
merged = meta_df.merge(articles_df, on='article_id', how='left')

# Simple keyword-based classifier for Business category
business_keywords = ['market', 'markets', 'stock', 'stocks', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'bond', 'bonds', 'treasury', 'fund', 'funds', 'investment', 'investor', 'investors', 'bank', 'banks', 'banking', 'loan', 'loans', 'merger', 'acquisition', 'm&a', 'deal', 'deals', 'profit', 'profits', 'loss', 'revenue', 'sales', 'earning', 'earnings', 'ipo', 'company', 'companies', 'corp', 'corporation', 'business', 'economy', 'economic', 'finance', 'financial', 'industry', 'industries', 'oil', 'crude', 'retail', 'consumer', 'trade', 'trading']

bk_set = set(business_keywords)

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    for kw in bk_set:
        if kw in text:
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter to business articles
biz = merged[merged['is_business']]

# Extract year and filter 2010-2020 inclusive (already done, but ensure)
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

biz_per_year = biz.groupby(merged.loc[biz.index, 'year']).size().reindex(range(2010, 2021), fill_value=0)

avg_business_per_year = biz_per_year.mean()

result = {"average_business_articles_per_year_europe_2010_2020": avg_business_per_year,
          "business_articles_per_year": biz_per_year.to_dict()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TbUotq9SoiVRSIxGFdU2Doat': 'file_storage/call_TbUotq9SoiVRSIxGFdU2Doat.json', 'var_call_lJcTnXNcKh9ATJ0uj3Aoh1SX': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
