code = """import json, pandas as pd

# Load full results if they are file paths
meta_data = var_call_F7qnZ99fLUkMG7dE8QLNUqKy
articles_data = var_call_hoAjYuSMOSOPQdYvOrsLzyuw

if isinstance(meta_data, str):
    with open(meta_data, 'r') as f:
        meta_data = json.load(f)
if isinstance(articles_data, str):
    with open(articles_data, 'r') as f:
        articles_data = json.load(f)

meta_df = pd.DataFrame(meta_data)
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df = pd.DataFrame(articles_data)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Simple keyword-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'business', 'finance', 'financial',
                     'trade', 'trading', 'company', 'companies', 'corporate', 'profit', 'profits', 'loss', 'losses',
                     'shares', 'share', 'investment', 'investor', 'investors', 'ipo', 'merger', 'acquisition',
                     'oil', 'bank', 'banks', 'loan', 'loans', 'interest rate', 'interest rates', 'currency', 'currencies',
                     'euro', 'dollar', 'yen', 'bond', 'bonds', 'fund', 'funds', 'revenue', 'sales', 'earnings',
                     'dividend', 'tax', 'tariff', 'exports', 'imports', 'unemployment', 'inflation']

business_keywords = [k.lower() for k in business_keywords]

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(kw in text for kw in business_keywords)

articles_df['is_business'] = articles_df.apply(is_business, axis=1)

# Join metadata with articles
merged = pd.merge(meta_df, articles_df[['article_id', 'is_business']], on='article_id', how='left')

# Filter to business articles only
business_meta = merged[merged['is_business']]

# Extract year
business_meta['year'] = business_meta['publication_date'].str.slice(0,4).astype(int)

# Count per year and compute average over 2010-2020 inclusive
counts_per_year = business_meta.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
average_per_year = counts_per_year.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': round(float(average_per_year), 2),
    'counts_per_year': counts_per_year.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_F7qnZ99fLUkMG7dE8QLNUqKy': 'file_storage/call_F7qnZ99fLUkMG7dE8QLNUqKy.json', 'var_call_hoAjYuSMOSOPQdYvOrsLzyuw': 'file_storage/call_hoAjYuSMOSOPQdYvOrsLzyuw.json'}

exec(code, env_args)
