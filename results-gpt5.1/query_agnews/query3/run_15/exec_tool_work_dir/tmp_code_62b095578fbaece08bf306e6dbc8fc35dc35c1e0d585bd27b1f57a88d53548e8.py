code = """import json, pandas as pd

# Load full results from files
with open(var_call_JPjXxp7MLT2ZLbVD1AbHGyG0, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_kouJiytlgrxBnH168nyHuE43, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

merged = meta_df.merge(articles_df, on='article_id', how='inner')

# Simple keyword-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'ipo', 'loan', 'loans', 'trade', 'trading', 'investment', 'investor', 'investors', 'business', 'shares', 'profits', 'revenue', 'growth', 'prices', 'oil', 'merger', 'acquisition', 'fund', 'funds', 'deficit', 'rates', 'interest rate', 'corporate', 'company', 'companies', 'firm', 'firms', 'jobless', 'unemployment', 'earnings', 'currency', 'currencies']

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(k in text for k in business_keywords)

merged['is_business'] = merged.apply(is_business, axis=1)

business_articles = merged[merged['is_business']].copy()

business_articles['year'] = business_articles['publication_date'].str.slice(0,4).astype(int)

counts_per_year = business_articles.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

average_per_year = counts_per_year.mean()

result = round(float(average_per_year), 2)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JPjXxp7MLT2ZLbVD1AbHGyG0': 'file_storage/call_JPjXxp7MLT2ZLbVD1AbHGyG0.json', 'var_call_kouJiytlgrxBnH168nyHuE43': 'file_storage/call_kouJiytlgrxBnH168nyHuE43.json'}

exec(code, env_args)
