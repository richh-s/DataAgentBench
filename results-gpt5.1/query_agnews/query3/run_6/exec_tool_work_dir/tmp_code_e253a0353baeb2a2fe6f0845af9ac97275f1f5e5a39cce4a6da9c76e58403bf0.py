code = """import json, pandas as pd

# Load full results from files
with open(var_call_M2o2ZBn0LjOkg4mYl3MkNiBT, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_0l34abV81hiRkbXBC0jMpq6s, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Join metadata with articles on article_id
merged = meta_df.merge(articles_df, on='article_id', how='inner')

# Very naive business classifier based on presence of finance/economy keywords in title/description
business_keywords = ['stock', 'stocks', 'wall st', 'wall street', 'market', 'markets', 'economy', 'economic', 'business', 'trade deficit', 'trade gap', 'gdp', 'revenue', 'profit', 'profits', 'shares', 'ipo', 'loan', 'interest rate', 'interest rates', 'central bank', 'oil prices', 'crude', 'corporate', 'merger', 'acquisition', 'jobs', 'unemployment', 'investor', 'investment', 'fund', 'funds']

text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

def is_business(txt):
    return any(k in txt for k in business_keywords)

merged['is_business'] = text.apply(is_business)

# Filter to business articles
business_df = merged[merged['is_business']]

# Extract year
business_df['year'] = business_df['publication_date'].str.slice(0,4).astype(int)

# Filter years 2010-2020 inclusive (should already be, but just in case)
business_df = business_df[(business_df['year'] >= 2010) & (business_df['year'] <= 2020)]

# Count per year and compute average
counts_per_year = business_df.groupby('year').size()

# Ensure all years 2010-2020 represented (with 0 if missing)
all_years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in all_years]

avg_business_per_year = sum(counts) / len(all_years) if all_years else 0

result = {
    'counts_per_year': {str(y): counts_per_year.get(y, 0) for y in all_years},
    'average_business_articles_per_year_2010_2020_inclusive': avg_business_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_M2o2ZBn0LjOkg4mYl3MkNiBT': 'file_storage/call_M2o2ZBn0LjOkg4mYl3MkNiBT.json', 'var_call_0l34abV81hiRkbXBC0jMpq6s': 'file_storage/call_0l34abV81hiRkbXBC0jMpq6s.json'}

exec(code, env_args)
