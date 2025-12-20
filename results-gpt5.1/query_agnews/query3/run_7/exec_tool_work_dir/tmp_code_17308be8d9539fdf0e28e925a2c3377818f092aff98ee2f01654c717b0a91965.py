code = """import json, pandas as pd

# Load Europe metadata
meta = var_call_r6Oas5SWc0kbD0PcviFQI8ZP
if isinstance(meta, str) and meta.endswith('.json'):
    with open(meta, 'r') as f:
        meta = json.load(f)

# Load all articles
arts = var_call_xVFaoswvyHkf9t02ZVcEb94c
if isinstance(arts, str) and arts.endswith('.json'):
    with open(arts, 'r') as f:
        arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join on article_id to get title/description for Europe 2010-2020
merged = meta_df.merge(arts_df, on='article_id', how='left')

# Simple business categorization heuristic based on keywords
business_keywords = ['stock', 'stocks', 'market', 'markets', 'shares', 'profit', 'profits', 'trade', 'trading', 'economy', 'economic', 'business', 'company', 'companies', 'oil', 'price', 'prices', 'bank', 'banks', 'loan', 'loans', 'fund', 'funds', 'investment', 'investors', 'ipo', 'merger', 'acquisition', 'corporate', 'earnings', 'revenue', 'sales', 'financial', 'finance', 'budget']

import re
pattern = re.compile(r"(" + "|".join(business_keywords) + r")", re.IGNORECASE)

texts = (merged['title'].fillna('') + ' ' + merged['description'].fillna(''))
merged['is_business'] = texts.apply(lambda x: bool(pattern.search(x)))

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

# Filter business articles
biz = merged[merged['is_business']]

# Count per year 2010-2020
counts = biz.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts.mean()

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_per_year': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_r6Oas5SWc0kbD0PcviFQI8ZP': 'file_storage/call_r6Oas5SWc0kbD0PcviFQI8ZP.json', 'var_call_xVFaoswvyHkf9t02ZVcEb94c': 'file_storage/call_xVFaoswvyHkf9t02ZVcEb94c.json'}

exec(code, env_args)
