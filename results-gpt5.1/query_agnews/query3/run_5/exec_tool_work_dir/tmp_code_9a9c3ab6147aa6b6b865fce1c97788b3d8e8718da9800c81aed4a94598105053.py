code = """import json, pandas as pd
from pathlib import Path

# Load tool results
meta_file = var_call_8cuLbMfzREszoe683nNQvLT2
articles_file = var_call_5ALqP0Sbojz2TbCrmMqT4MXa

with open(meta_file, 'r') as f:
    meta = json.load(f)
with open(articles_file, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id types align
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join on article_id for European 2010-2020 articles
merged = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple heuristic classifier for Business vs others using title+description keywords
text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

business_keywords = [
    'stock', 'stocks', 'market', 'markets', 'share', 'shares', 'ipo', 'investment', 'investor', 'investors',
    'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'loan', 'loans', 'credit',
    'trade deficit', 'trade gap', 'trade', 'exports', 'import', 'imports', 'oil prices', 'oil price', 'crude',
    'company', 'companies', 'corporate', 'profit', 'profits', 'losses', 'earnings', 'revenue', 'sales',
    'business', 'firm', 'firms', 'merger', 'acquisition', 'takeover', 'job cuts', 'jobs', 'unemployment',
    'retail', 'commercial real estate', 'real estate', 'mutual fund', 'mutual funds', 'funds', 'bonds',
    'currency', 'currencies', 'dollar', 'euro', 'yen', 'pound', 'tariff', 'tariffs', 'interest rate', 'interest rates'
]

# classify as business if any keyword present
def is_business(t):
    return any(kw in t for kw in business_keywords)

merged['is_business'] = text.apply(is_business)

business_df = merged[merged['is_business']].copy()

# Extract year
business_df['year'] = business_df['publication_date'].str.slice(0,4).astype(int)

# Filter explicitly between 2010 and 2020 inclusive (should already be, but for safety)
business_df = business_df[(business_df['year']>=2010) & (business_df['year']<=2020)]

counts_per_year = business_df.groupby('year').size()

# Compute average over the 11 years 2010-2020 inclusive
years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in years]
avg = sum(counts) / len(years)

result = {
    'years': years,
    'business_counts_per_year': counts,
    'average_business_articles_per_year_europe_2010_2020': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8cuLbMfzREszoe683nNQvLT2': 'file_storage/call_8cuLbMfzREszoe683nNQvLT2.json', 'var_call_5ALqP0Sbojz2TbCrmMqT4MXa': 'file_storage/call_5ALqP0Sbojz2TbCrmMqT4MXa.json'}

exec(code, env_args)
