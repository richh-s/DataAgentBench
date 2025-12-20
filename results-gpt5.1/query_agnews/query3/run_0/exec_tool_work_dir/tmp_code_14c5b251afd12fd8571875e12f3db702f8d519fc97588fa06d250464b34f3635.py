code = """import json, pandas as pd

# Load full results from files
with open(var_call_L8GUfkcdTvGDqiHplv5L1eet, 'r') as f:
    articles = json.load(f)
with open(var_call_l7b4C8MTsmcnft7qehsTPFUR, 'r') as f:
    meta = json.load(f)

art_df = pd.DataFrame(articles)[['article_id', 'title', 'description']]
meta_df = pd.DataFrame(meta)[['article_id', 'region', 'publication_date']]

# Ensure article_id types match
art_df['article_id'] = art_df['article_id'].astype(int)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# Filter Europe 2010-2020 already done in SQL; just merge
merged = meta_df.merge(art_df, on='article_id', how='left')

# Simple heuristic to classify Business vs others using keywords
business_keywords = ['market', 'markets', 'stock', 'stocks', 'wall st', 'dow', 'nasdaq', 'bond', 'bonds', 'fund', 'funds', 'trade', 'trading', 'economy', 'economic', 'loan', 'loans', 'bank', 'banks', 'banking', 'ipo', 'shares', 'share', 'oil', 'price', 'prices', 'finance', 'financial', 'money', 'business', 'corporate', 'merger', 'acquisition', 'earnings', 'revenue', 'profit', 'loss', 'sales', 'retail', 'company', 'companies', 'firm', 'firms', 'investment', 'investor', 'investors', 'eurozone']

import re

def is_business(row):
    text = f"{row['title']} {row['description']}".lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

# Keep only business articles
biz = merged[merged['is_business']]

# Extract year
biz['year'] = biz['publication_date'].str[:4].astype(int)

# Filter 2010-2020 just in case
biz = biz[(biz['year'] >= 2010) & (biz['year'] <= 2020)]

# Count per year then average over the 11 years
counts_per_year = biz.groupby('year').size()
# Ensure all years present
for y in range(2010, 2021):
    if y not in counts_per_year.index:
        counts_per_year.loc[y] = 0
counts_per_year = counts_per_year.sort_index()
avg_per_year = counts_per_year.mean()

result = {
    'counts_per_year': counts_per_year.to_dict(),
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_L8GUfkcdTvGDqiHplv5L1eet': 'file_storage/call_L8GUfkcdTvGDqiHplv5L1eet.json', 'var_call_l7b4C8MTsmcnft7qehsTPFUR': 'file_storage/call_l7b4C8MTsmcnft7qehsTPFUR.json'}

exec(code, env_args)
