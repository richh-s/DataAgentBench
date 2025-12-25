code = """import json, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_4xNwjzSQoHDQscrZwoPk5Tq9, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_vkpofMEyO8Mz0bmwqPclE5qO, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# merge
merged = meta_df.merge(articles_df, on='article_id', how='inner')

# simple keyword-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'trade', 'trading', 'business', 'finance', 'financial', 'bank', 'banks', 'banking', 'loan', 'loans', 'company', 'companies', 'corporate', 'oil', 'earnings', 'shares', 'investor', 'investors', 'investment', 'investments', 'ipo', 'merger', 'acquisition', 'profit', 'profits', 'revenue', 'sales', 'growth', 'interest rate', 'interest rates', 'currency', 'currencies']

import re
pattern = re.compile(r'(' + '|'.join(re.escape(k) for k in business_keywords) + r')', re.IGNORECASE)

texts = (merged['title'].fillna('') + ' ' + merged['description'].fillna(''))
merged['is_business'] = texts.apply(lambda x: bool(pattern.search(x)))

# filter to business
biz = merged[merged['is_business']].copy()

# extract year
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# filter years 2010-2020 inclusive (should already be)
biz = biz[(biz['year'] >= 2010) & (biz['year'] <= 2020)]

counts_by_year = biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts_by_year.mean()

result = {
    'counts_by_year': counts_by_year.to_dict(),
    'average_business_articles_per_year_2010_2020_Europe': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4xNwjzSQoHDQscrZwoPk5Tq9': 'file_storage/call_4xNwjzSQoHDQscrZwoPk5Tq9.json', 'var_call_vkpofMEyO8Mz0bmwqPclE5qO': 'file_storage/call_vkpofMEyO8Mz0bmwqPclE5qO.json'}

exec(code, env_args)
