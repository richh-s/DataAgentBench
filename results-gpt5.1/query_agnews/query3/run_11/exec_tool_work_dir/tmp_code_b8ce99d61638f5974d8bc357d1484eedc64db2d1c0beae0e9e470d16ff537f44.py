code = """import json, pandas as pd

# Load Europe metadata
with open(var_call_4APftiFU6hZIv8hZfyb75MlT, 'r') as f:
    europe_meta = json.load(f)

# Load all articles
with open(var_call_KwIemDTcKODscxxK9rvpmLJU, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure proper dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge on article_id for Europe-only articles
merged = meta_df.merge(articles_df, on='article_id', how='inner')

# Simple rule-based classifier for Business category
business_keywords = [
    'stock', 'stocks', 'market', 'markets', 'shares', 'wall st', 'wall street', 'bond', 'bonds',
    'economy', 'economic', 'economics', 'trade deficit', 'trade gap', 'trade', 'growth', 'recession',
    'company', 'companies', 'firm', 'corporate', 'profits', 'earnings', 'ipo', 'float', 'merger',
    'acquisition', 'm&a', 'shares', 'equity', 'fund', 'funds', 'investment', 'investor', 'loan',
    'interest rate', 'interest rates', 'central bank', 'bank', 'banks', 'currency', 'currencies',
    'eurozone', 'oil prices', 'oil price', 'oil', 'commodities', 'salary', 'wage', 'wages', 'unemployment',
    'jobless', 'retail sales', 'real estate', 'commercial', 'business', 'industry', 'industries'
]

bk = '|'.join(business_keywords)
text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()
merged['is_business'] = text.str.contains(bk, case=False, regex=True)

business = merged[merged['is_business']]

# Extract year and filter 2010-2020 explicitly (though query already did)
business['year'] = business['publication_date'].str.slice(0,4).astype(int)

# Count per year and compute average
counts_per_year = business.groupby('year')['article_id'].nunique()

# Ensure all years 2010-2020 represented (with 0 if missing)
years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in years]
avg_per_year = sum(counts) / len(years)

result = {
    'years': years,
    'business_article_counts_per_year_europe': counts,
    'average_business_articles_per_year_europe_2010_2020': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4APftiFU6hZIv8hZfyb75MlT': 'file_storage/call_4APftiFU6hZIv8hZfyb75MlT.json', 'var_call_KwIemDTcKODscxxK9rvpmLJU': 'file_storage/call_KwIemDTcKODscxxK9rvpmLJU.json'}

exec(code, env_args)
