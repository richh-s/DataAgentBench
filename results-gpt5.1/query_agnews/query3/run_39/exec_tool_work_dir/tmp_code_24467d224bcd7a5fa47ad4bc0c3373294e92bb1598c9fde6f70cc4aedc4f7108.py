code = """import json, pandas as pd

# Load metadata (Europe 2010-2020)
with open(var_call_5z7Vcmwx91oUuI0YWXOueMaT, 'r') as f:
    europe_meta = json.load(f)

# Load all articles
with open(var_call_ApIPJJ8IgmAAWzyKLLLF0uTq, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
art_df = pd.DataFrame(articles)

# Ensure integer article_id for join
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Join to get titles/descriptions for Europe 2010-2020
merged = meta_df.merge(art_df, on='article_id', how='left')

# Simple rule-based classifier for Business category based on title+description keywords
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'share', 'shares',
    'market', 'markets', 'trading', 'ipo', 'merger', 'acquisition', 'deal', 'profit',
    'losses', 'earnings', 'revenue', 'investment', 'fund', 'funds', 'mutual fund',
    'bond', 'bonds', 'currency', 'currencies', 'dollar', 'euro', 'yen', 'oil', 'crude',
    'economy', 'economic', 'finance', 'financial', 'business', 'company', 'companies',
    'firm', 'firms', 'corporate', 'bank', 'banks', 'banking', 'loan', 'loans', 'credit',
    'retail', 'sales', 'jobless', 'trade deficit', 'trade gap', 'unemployment',
    'industry', 'industries', 'output', 'exports', 'imports', 'price', 'prices',
    'rate', 'rates', 'interest rate', 'central bank', 'budget', 'tax', 'taxes'
]

business_keywords = [k.lower() for k in business_keywords]

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(k in text for k in business_keywords)

merged['is_business'] = merged.apply(is_business, axis=1)

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

# Filter to business articles
biz = merged[merged['is_business']]

# Count per year 2010-2020
counts_per_year = biz.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts_per_year.mean()

result = {
    'counts_per_year': counts_per_year.to_dict(),
    'average_business_articles_per_year_europe_2010_2020': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5z7Vcmwx91oUuI0YWXOueMaT': 'file_storage/call_5z7Vcmwx91oUuI0YWXOueMaT.json', 'var_call_ApIPJJ8IgmAAWzyKLLLF0uTq': 'file_storage/call_ApIPJJ8IgmAAWzyKLLLF0uTq.json'}

exec(code, env_args)
