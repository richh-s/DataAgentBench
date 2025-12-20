code = """import json, pandas as pd
from pathlib import Path

# Load metadata (Europe, 2010-2020)
meta_file = var_call_Q1yqZph6XZAo67zadKJv8iQ6
with open(meta_file, 'r') as f:
    meta_records = json.load(f)
meta_df = pd.DataFrame(meta_records)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Load all articles
articles_file = var_call_ilFUgEIQJGeRbfmAaaD5VQP2
with open(articles_file, 'r') as f:
    article_records = json.load(f)
articles_df = pd.DataFrame(article_records)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Simple rule-based classifier for Business vs other
# Keywords indicative of business/economy/finance
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'ftse', 'dax',
    'share', 'shares', 'ipo', 'market', 'markets', 'bond', 'bonds', 'fund', 'funds',
    'mutual fund', 'oil', 'crude', 'economy', 'economic', 'trade deficit', 'trade gap',
    'gdp', 'interest rate', 'interest rates', 'loan', 'loans', 'bank', 'banks', 'central bank',
    'fed ', 'federal reserve', 'ecb', 'eurozone', 'finance', 'financial', 'earnings',
    'profit', 'profits', 'loss', 'losses', 'revenue', 'merger', 'acquisition', 'm&a',
    'corporate', 'business', 'commerce', 'retail', 'sales', 'company', 'companies',
    'firm', 'firms', 'industry', 'industries', 'jobless', 'unemployment', 'housing market',
]

text_cols = (articles_df['title'].fillna('') + ' ' + articles_df['description'].fillna('')).str.lower()

import numpy as np
pat = '|'.join([k.replace(' ', '\\s+') for k in business_keywords])
mask_business = text_cols.str.contains(pat, regex=True)
articles_df['is_business'] = mask_business

# Join Europe metadata with articles and filter to Business
merged = meta_df.merge(articles_df[['article_id','is_business']], on='article_id', how='left')

business_europe = merged[merged['is_business']]

# Count per year and compute average over 2010-2020 inclusive
counts_per_year = business_europe.groupby('year').size()
# Ensure all years present
for y in range(2010, 2021):
    if y not in counts_per_year.index:
        counts_per_year.loc[y] = 0
counts_per_year = counts_per_year.sort_index()

average_per_year = counts_per_year.mean()

import math
avg_rounded = float(round(average_per_year, 2))

result = {
    'average_business_articles_per_year_europe_2010_2020': avg_rounded,
    'counts_per_year': counts_per_year.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Q1yqZph6XZAo67zadKJv8iQ6': 'file_storage/call_Q1yqZph6XZAo67zadKJv8iQ6.json', 'var_call_ilFUgEIQJGeRbfmAaaD5VQP2': 'file_storage/call_ilFUgEIQJGeRbfmAaaD5VQP2.json'}

exec(code, env_args)
