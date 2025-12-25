code = """import json, pandas as pd
from collections import Counter

# Load full Europe metadata from file path
with open(var_call_oIl0RNvfYzmoiBAw1il9pMI9, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_qBeZTv0zFVAV8q8q7qPCFgdi

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure correct types
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Join metadata with articles text
df = meta_df.merge(articles_df, on='article_id', how='left')

# Simple rule-based classifier for Business vs other categories using title+description
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'ftse', 'dax',
    'market', 'markets', 'trading', 'shares', 'share', 'bond', 'bonds', 'treasury',
    'fed', 'ecb', 'interest rate', 'interest rates', 'rate hike', 'rate cut',
    'economy', 'economic', 'recession', 'growth', 'gdp', 'inflation', 'deflation',
    'unemployment', 'jobs report', 'payrolls',
    'company', 'companies', 'corporate', 'business', 'merger', 'acquisition', 'm&a',
    'profit', 'profits', 'earnings', 'revenue', 'sales', 'forecast', 'outlook',
    'ipo', 'initial public offering', 'listing',
    'bank', 'banks', 'banking', 'credit', 'loan', 'loans', 'mortgage', 'debt',
    'currency', 'currencies', 'forex', 'euro', 'yen', 'dollar',
    'oil', 'crude', 'gold', 'commodity', 'commodities',
    'trade', 'tariff', 'tariffs', 'export', 'exports', 'import', 'imports'
]

biz_kw = [k.lower() for k in business_keywords]

texts = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

def is_business(text):
    return any(k in text for k in biz_kw)

df['is_business'] = texts.apply(is_business)

# Filter to business articles only
biz_df = df[df['is_business']]

# Extract year and compute counts per year
biz_df['year'] = biz_df['publication_date'].str.slice(0,4).astype(int)
counts_per_year = biz_df.groupby('year').size()

# Ensure all years 2010-2020 present with 0 if missing
all_years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in all_years]

avg_per_year = float(sum(counts) / len(all_years))

result = {
    'years': all_years,
    'business_article_counts_per_year_in_europe': counts,
    'average_business_articles_per_year_in_europe_2010_2020_inclusive': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oIl0RNvfYzmoiBAw1il9pMI9': 'file_storage/call_oIl0RNvfYzmoiBAw1il9pMI9.json', 'var_call_qBeZTv0zFVAV8q8q7qPCFgdi': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
