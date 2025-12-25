code = """import json, pandas as pd

# Load full results from files
with open(var_call_sSVjOQePKENQ0mldVSJNlI1X, 'r') as f:
    meta = json.load(f)
with open(var_call_UAKBCI8fIyT14drm34ySvBja, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id types are consistent
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge to get titles/descriptions for European articles 2010-2020
merged = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'shares', 'trade deficit', 'economy', 'economic', 'ipo', 'loan', 'rates', 'interest rate', 'import', 'export', 'exports', 'oil', 'growth', 'profits', 'earnings', 'funds', 'price', 'prices', 'revenue', 'sales', 'investment', 'investors', 'bank', 'banks', 'central bank', 'currency', 'currencies', 'euro', 'dollar', 'yen', 'nasdaq', 'nyse', 'dow', 'bond', 'bonds', 'merger', 'acquisition', 'jobs', 'unemployment', 'inflation', 'deflation', 'gdp', 'budget', 'deficit', 'surplus']

bk_set = set(business_keywords)

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    for kw in bk_set:
        if kw in text:
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter to business articles
biz = merged[merged['is_business']]

# Extract year
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# Filter years 2010-2020 inclusive (should already be, but to be safe)
biz = biz[(biz['year'] >= 2010) & (biz['year'] <= 2020)]

counts_per_year = biz.groupby('year').size()

# Compute average over the 11 years (2010-2020 inclusive)
all_years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in all_years]
avg = sum(counts) / len(all_years)

result = {
    'counts_per_year': {str(y): counts_per_year.get(y, 0) for y in all_years},
    'average_business_articles_per_year_europe_2010_2020': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sSVjOQePKENQ0mldVSJNlI1X': 'file_storage/call_sSVjOQePKENQ0mldVSJNlI1X.json', 'var_call_UAKBCI8fIyT14drm34ySvBja': 'file_storage/call_UAKBCI8fIyT14drm34ySvBja.json'}

exec(code, env_args)
