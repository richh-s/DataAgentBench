code = """import json, pandas as pd

# Load full metadata and articles results
with open(var_call_hGuMPfftvNWKwQu0eHHxTL3D, 'r') as f:
    meta = json.load(f)
with open(var_call_KGeErNAIO7HvwhQXz1NwAUod, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join on article_id to get titles and descriptions for European articles 2010-2020
merged = meta_df.merge(arts_df, on='article_id', how='left')

# Very simple rule-based classifier for Business category using keywords
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'earnings', 'ipo', 'oil', 'trade deficit', 'trade gap', 'merger', 'acquisition', 'shares', 'profit', 'profits', 'loan', 'interest rate', 'interest rates', 'central bank', 'funds', 'mutual fund', 'business', 'company', 'companies', 'corporate', 'industry', 'industries', 'investment', 'investor', 'investors', 'commercial', 'real estate', 'retail', 'tax', 'exports', 'imports', 'unemployment', 'jobs report', 'eurozone']

import re

pattern = re.compile('|'.join(re.escape(k) for k in business_keywords), flags=re.IGNORECASE)

texts = (merged['title'].fillna('') + ' ' + merged['description'].fillna(''))
merged['is_business'] = texts.apply(lambda x: bool(pattern.search(x)))

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

# Filter to business
biz = merged[merged['is_business']]

# Count per year 2010-2020
year_counts = biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = year_counts.mean()

result = {
    'year_counts': year_counts.to_dict(),
    'average_business_articles_per_year_europe_2010_2020': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_hGuMPfftvNWKwQu0eHHxTL3D': 'file_storage/call_hGuMPfftvNWKwQu0eHHxTL3D.json', 'var_call_KGeErNAIO7HvwhQXz1NwAUod': 'file_storage/call_KGeErNAIO7HvwhQXz1NwAUod.json'}

exec(code, env_args)
