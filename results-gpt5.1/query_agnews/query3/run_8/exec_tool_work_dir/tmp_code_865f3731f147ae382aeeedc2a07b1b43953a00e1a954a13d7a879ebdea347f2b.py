code = """import json, pandas as pd

# Load full metadata result
with open(var_call_i5LEZzUxPikTwdmQtIeNvpO1, 'r') as f:
    europe_meta = json.load(f)

# Load full articles result
with open(var_call_XWwmzMi9vAJHif5JPikClZ5t, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to get titles/descriptions for European articles 2010-2020
merged = meta_df.merge(articles_df, on='article_id', how='inner')

# Simple rule-based classifier for Business category using keywords
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'market', 'markets', 'share', 'shares',
    'oil', 'economy', 'economic', 'trade', 'deficit', 'loan', 'interest rate', 'interest rates',
    'bank', 'banks', 'fund', 'funds', 'investment', 'investor', 'investors', 'ipo', 'float',
    'company', 'companies', 'firm', 'corporate', 'business', 'industry', 'industries',
    'profit', 'profits', 'revenue', 'sales', 'job', 'jobs', 'unemployment', 'wage', 'wages',
    'currency', 'dollar', 'euro', 'yen', 'merger', 'acquisition', 'takeover', 'price', 'prices'
]

import re
pattern = re.compile('|'.join(re.escape(k) for k in business_keywords), re.IGNORECASE)

texts = (merged['title'].fillna('') + ' ' + merged['description'].fillna(''))
merged['is_business'] = texts.apply(lambda x: bool(pattern.search(x)))

business_articles = merged[merged['is_business']].copy()

# Extract year
business_articles['year'] = business_articles['publication_date'].str.slice(0,4).astype(int)

# Filter years 2010-2020 explicitly (though query already did)
business_articles = business_articles[(business_articles['year'] >= 2010) & (business_articles['year'] <= 2020)]

counts_per_year = business_articles.groupby('year').size()

# Compute average over all 11 years (including years with zero by reindexing)
years = list(range(2010, 2021))
counts_per_year = counts_per_year.reindex(years, fill_value=0)
avg_per_year = counts_per_year.mean()

result = {
    'counts_per_year': counts_per_year.to_dict(),
    'average_business_articles_per_year_2010_2020_europe': avg_per_year
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_i5LEZzUxPikTwdmQtIeNvpO1': 'file_storage/call_i5LEZzUxPikTwdmQtIeNvpO1.json', 'var_call_XWwmzMi9vAJHif5JPikClZ5t': 'file_storage/call_XWwmzMi9vAJHif5JPikClZ5t.json'}

exec(code, env_args)
