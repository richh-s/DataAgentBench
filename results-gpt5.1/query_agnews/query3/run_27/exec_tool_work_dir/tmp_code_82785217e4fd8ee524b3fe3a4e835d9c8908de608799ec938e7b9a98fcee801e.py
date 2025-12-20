code = """import json, pandas as pd

# Load full results from files
with open(var_call_EdKWM7LSg8xFHpuAtGFAHjNY, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_ZurbhZAlXdw799Lt6pPlPhEs, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Join metadata with articles
joined = meta_df.merge(articles_df, on='article_id', how='inner')

# Simple keyword-based classification for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'business', 'trade', 'trading', 'oil', 'bank', 'banks', 'finance', 'financial', 'fund', 'funds', 'investment', 'investor', 'investors', 'ipo', 'shares', 'profits', 'revenue', 'growth', 'loan', 'loans', 'interest rate', 'interest rates', 'currency', 'currencies', 'euro', 'dollar', 'yen', 'company', 'companies', 'corporate']

text = (joined['title'].fillna('') + ' ' + joined['description'].fillna('')).str.lower()

pattern = '|'.join([k.replace(' ', ' ') for k in business_keywords])
joined['is_business'] = text.str.contains(pattern, regex=True)

# Filter to business articles
business = joined[joined['is_business']].copy()

# Extract year
business['year'] = business['publication_date'].str.slice(0, 4).astype(int)

# Count per year 2010-2020
counts = business.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)

average_per_year = counts.mean()

result = {
    'counts_per_year': counts.to_dict(),
    'average_business_articles_per_year_europe_2010_2020': average_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EdKWM7LSg8xFHpuAtGFAHjNY': 'file_storage/call_EdKWM7LSg8xFHpuAtGFAHjNY.json', 'var_call_ZurbhZAlXdw799Lt6pPlPhEs': 'file_storage/call_ZurbhZAlXdw799Lt6pPlPhEs.json'}

exec(code, env_args)
