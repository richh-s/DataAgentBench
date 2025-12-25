code = """import json, pandas as pd

# Load full results if stored in files
import os

def load_results(var):
    if isinstance(var, str) and os.path.isfile(var):
        with open(var, 'r') as f:
            return json.load(f)
    return var

meta = load_results(var_call_mKP9ThjQFvya7ugRxrHgyBIj)
arts = load_results(var_call_ciIczXwNoK5k1NKwmo2eIYcu)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge to get titles/descriptions for Europe 2010-2020
merged = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple rule-based classifier for Business category
business_keywords = [
    'stock', 'stocks', 'market', 'markets', 'shares', 'share', 'profit', 'profits',
    'trade', 'trading', 'economy', 'economic', 'business', 'company', 'companies',
    'corporate', 'bank', 'banks', 'finance', 'financial', 'investment', 'investor',
    'investors', 'oil', 'earnings', 'merger', 'acquisition', 'ipo', 'revenue',
    'sales', 'dollar', 'euro', 'yen', 'job', 'jobs', 'unemployment', 'growth',
    'industry', 'industries', 'firm', 'fund', 'funds', 'loan', 'loans', 'budget',
    'deficit', 'tariff', 'tariffs', 'bond', 'bonds', 'economies', 'currency',
    'currencies'
]

bk_set = set(business_keywords)

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    tokens = ''.join(ch if ch.isalnum() else ' ' for ch in text).split()
    return any(tok in bk_set for tok in tokens)

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter business articles
biz = merged[merged['is_business']]

# Extract year
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

counts_per_year = biz.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)

average_per_year = counts_per_year.mean()

result = {
    'counts_per_year': counts_per_year.to_dict(),
    'average_business_articles_per_year_europe_2010_2020': average_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mKP9ThjQFvya7ugRxrHgyBIj': 'file_storage/call_mKP9ThjQFvya7ugRxrHgyBIj.json', 'var_call_ciIczXwNoK5k1NKwmo2eIYcu': 'file_storage/call_ciIczXwNoK5k1NKwmo2eIYcu.json'}

exec(code, env_args)
