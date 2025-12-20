code = """import json, pandas as pd

# Load metadata: if it's a file path (string), open it; otherwise treat as data
if isinstance(var_call_rM22KBbJVIE3ngtwMbPABpwT, str):
    with open(var_call_rM22KBbJVIE3ngtwMbPABpwT, 'r') as f:
        metadata = json.load(f)
else:
    metadata = var_call_rM22KBbJVIE3ngtwMbPABpwT

# Load full articles from JSON file path
if isinstance(var_call_yeV4zmi5Rm3bVjmG3Dc5btoe, str):
    with open(var_call_yeV4zmi5Rm3bVjmG3Dc5btoe, 'r') as f:
        articles = json.load(f)
else:
    articles = var_call_yeV4zmi5Rm3bVjmG3Dc5btoe

meta_df = pd.DataFrame(metadata)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

merged = meta_df.merge(articles_df, on='article_id', how='inner')

business_keywords = [
    'stock', 'stocks', 'market', 'markets', 'shares', 'share', 'bond', 'bonds',
    'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking',
    'trade', 'trading', 'business', 'company', 'companies', 'corporate',
    'investment', 'investor', 'investors', 'ipo', 'merger', 'acquisition',
    'earnings', 'profit', 'profits', 'losses', 'revenue', 'sales', 'retail',
    'jobless', 'jobs', 'unemployment', 'oil', 'energy', 'currency', 'currencies',
    'dollar', 'euro', 'yen', 'price', 'prices', 'inflation', 'deficit', 'growth',
    'industry', 'industries', 'businesses', 'economies', 'fund', 'funds', 'loan', 'loans'
]

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(k in text for k in business_keywords)

merged['is_business'] = merged.apply(is_business, axis=1)

merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

business_by_year = merged[merged['is_business']].groupby('year').size()

years = list(range(2010, 2021))
counts = [int(business_by_year.get(y, 0)) for y in years]

avg_business_per_year = sum(counts) / len(years)

result = {
    'years': years,
    'business_counts_per_year': counts,
    'average_business_articles_per_year_2010_2020_Europe': avg_business_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rM22KBbJVIE3ngtwMbPABpwT': 'file_storage/call_rM22KBbJVIE3ngtwMbPABpwT.json', 'var_call_yeV4zmi5Rm3bVjmG3Dc5btoe': 'file_storage/call_yeV4zmi5Rm3bVjmG3Dc5btoe.json'}

exec(code, env_args)
