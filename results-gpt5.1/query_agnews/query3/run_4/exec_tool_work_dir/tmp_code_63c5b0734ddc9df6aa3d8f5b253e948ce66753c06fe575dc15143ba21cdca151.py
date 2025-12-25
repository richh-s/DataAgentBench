code = """import json, pandas as pd

# Load Europe metadata
meta_file = var_call_oLP9zcp1eLmfep3QFGKp5OV1
with open(meta_file, 'r') as f:
    europe_meta = json.load(f)

# Load all articles
articles_file = var_call_32fIZHZQ9Q9GQSz9AW2NGmK2
with open(articles_file, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
art_df = pd.DataFrame(articles)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Join to get title and description for European articles in 2010-2020
merged = meta_df.merge(art_df, on='article_id', how='inner')

# Simple rule-based classifier for Business category
business_keywords = [
    'stock', 'stocks', 'market', 'markets', 'share', 'shares', 'bond', 'bonds', 'investor', 'investors',
    'investment', 'bank', 'banks', 'banking', 'loan', 'loans', 'finance', 'financial', 'economy', 'economic',
    'trade', 'trading', 'ipo', 'merger', 'acquisition', 'profits', 'profit', 'earnings', 'revenue', 'sales',
    'company', 'companies', 'corporate', 'business', 'businesses', 'firm', 'firms', 'industry', 'industries',
    'oil', 'gas', 'energy', 'price', 'prices', 'currency', 'currencies', 'euro', 'dollar', 'yen', 'fund', 'funds',
    'retail', 'unemployment', 'jobs', 'jobless', 'growth', 'gdp', 'exports', 'imports'
]

kw_set = set(business_keywords)

def is_business(row):
    text = f"{row['title']} {row['description']}".lower()
    # crude tokenization
    tokens = ''.join(ch if ch.isalpha() else ' ' for ch in text).split()
    return any(tok in kw_set for tok in tokens)

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter to business articles
biz = merged[merged['is_business']]

# Extract year and restrict 2010-2020 inclusive (already from query, but be safe)
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)
biz = biz[(biz['year'] >= 2010) & (biz['year'] <= 2020)]

# Count per year
counts = biz.groupby('year').size()

# Compute average over all 11 years (include years with zero by reindexing)
years = list(range(2010, 2021))
counts = counts.reindex(years, fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles_2010_2020_europe': int(counts.sum()),
    'per_year_counts': counts.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oLP9zcp1eLmfep3QFGKp5OV1': 'file_storage/call_oLP9zcp1eLmfep3QFGKp5OV1.json', 'var_call_32fIZHZQ9Q9GQSz9AW2NGmK2': 'file_storage/call_32fIZHZQ9Q9GQSz9AW2NGmK2.json'}

exec(code, env_args)
