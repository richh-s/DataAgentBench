code = """import json, pandas as pd
from collections import Counter

# Load full Europe metadata
path = var_call_HkxMXAFiwLI9Tj5DewXsdE3Z
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_iGUMVXd6zzY2BII2PPedgHc1

# Build DataFrame
meta_df = pd.DataFrame(europe_meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

art_df = pd.DataFrame(articles)
art_df['article_id'] = art_df['article_id'].astype(int)

# Simple keyword-based classifier for Business vs others
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'business', 'company', 'companies', 'corporate', 'bank', 'banks', 'finance', 'financial', 'trade', 'trading', 'oil', 'merger', 'deal', 'shares', 'investor', 'investment', 'investors']

def is_business(title, desc):
    text = f"{title} {desc}".lower()
    return any(k in text for k in business_keywords)

art_df['is_business'] = art_df.apply(lambda r: is_business(r['title'], r['description']), axis=1)

# Join metadata with articles, keep only those we have content for
joined = meta_df.merge(art_df[['article_id','is_business']], on='article_id', how='inner')

# Count business articles per year
biz_per_year = joined[joined['is_business']].groupby('year').size().to_dict()

# Average from 2010 to 2020 inclusive
years = list(range(2010, 2021))
counts = [biz_per_year.get(y, 0) for y in years]
avg = sum(counts) / len(years) if years else 0

result = {"business_articles_per_year": biz_per_year, "average_2010_2020": avg}

j = json.dumps(result)
print("__RESULT__:")
print(j)"""

env_args = {'var_call_HkxMXAFiwLI9Tj5DewXsdE3Z': 'file_storage/call_HkxMXAFiwLI9Tj5DewXsdE3Z.json', 'var_call_iGUMVXd6zzY2BII2PPedgHc1': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_arF6PTef8yv80ivvx5CRQpI2': ['articles'], 'var_call_g6qfgbijmLk2Zdok4TKkmngP': ['authors', 'article_metadata']}

exec(code, env_args)
