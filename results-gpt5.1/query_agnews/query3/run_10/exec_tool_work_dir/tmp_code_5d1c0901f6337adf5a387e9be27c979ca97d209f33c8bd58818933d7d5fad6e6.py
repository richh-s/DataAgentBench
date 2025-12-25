code = """import json, pandas as pd

# Load full results if stored in files
articles_path = var_call_vhBlRTyTCnkMUO84Xj3378t2
meta_path = var_call_LIkCRj2A9IuUl2ubGYiod7bg

with open(articles_path, 'r') as f:
    articles = json.load(f)
with open(meta_path, 'r') as f:
    meta = json.load(f)

# Convert to DataFrames
df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(meta)

# Ensure article_id is int in both
df_articles['article_id'] = df_articles['article_id'].astype(int)
df_meta['article_id'] = df_meta['article_id'].astype(int)

# Merge on article_id for Europe 2010-2020
merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Simple keyword-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'oil', 'economy', 'economic', 'trade', 'business', 'company', 'companies', 'firm', 'fund', 'funds', 'bank', 'banks', 'investment', 'investor', 'investors', 'finance', 'financial', 'ipo', 'shares', 'share', 'profit', 'profits', 'revenue', 'growth', 'price', 'prices', 'merger', 'acquisition', 'loan', 'loans', 'debt', 'budget', 'tax', 'currency', 'currencies', 'export', 'exports', 'import', 'imports', 'sales', 'retail']

text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()
pattern = '|'.join(sorted(set(business_keywords), key=len, reverse=True))

is_business = text.str.contains(pattern, regex=True)

merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

business_by_year = merged[is_business].groupby('year')['article_id'].nunique()

# Ensure all years 2010-2020 are present (even if zero)
years = list(range(2010, 2021))
counts = [int(business_by_year.get(y, 0)) for y in years]

avg_business_per_year = float(sum(counts) / len(years))

result = {
  'years': years,
  'business_counts_per_year': counts,
  'average_business_articles_per_year_europe_2010_2020': avg_business_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_vhBlRTyTCnkMUO84Xj3378t2': 'file_storage/call_vhBlRTyTCnkMUO84Xj3378t2.json', 'var_call_LIkCRj2A9IuUl2ubGYiod7bg': 'file_storage/call_LIkCRj2A9IuUl2ubGYiod7bg.json'}

exec(code, env_args)
