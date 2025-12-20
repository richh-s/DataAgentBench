code = """import json, pandas as pd

# Load full results from files
with open(var_call_st1HFvzXzOaDoHGbMBd8ieYA, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_eGM5YTWzkMSr39l0CAXxK6QC, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
art_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Merge to get title and description for European articles
merged = pd.merge(meta_df, art_df, on='article_id', how='inner')

# Simple keyword-based classifier for Business category
business_keywords = ['stock', 'stocks', 'market', 'markets', 'wall st', 'wall street', 'dow', 'nasdaq', 'ftse', 'dax', 'nikkei',
                     'share', 'shares', 'equity', 'equities', 'bond', 'bonds', 'fund', 'funds', 'mutual fund', 'hedge fund',
                     'ipo', 'merger', 'acquisition', 'm&a', 'profit', 'profits', 'earnings', 'revenue', 'sales', 'forecast',
                     'economy', 'economic', 'trade', 'tariff', 'gdp', 'unemployment', 'inflation', 'interest rate', 'central bank',
                     'ecb', 'federal reserve', 'bank of england', 'loan', 'loans', 'mortgage', 'credit', 'debt', 'deficit',
                     'surplus', 'currency', 'currencies', 'dollar', 'euro', 'yen', 'pound',
                     'business', 'company', 'companies', 'corporate', 'industry', 'industries', 'firm', 'firms', 'enterprise',
                     'startup', 'start-up', 'venture capital', 'investment', 'investor', 'investors', 'finance', 'financial',
                     'oil', 'gas', 'energy', 'retail', 'consumer', 'manufacturing', 'export', 'imports', 'import', 'exporter',
                     'budget', 'tax', 'taxes', 'taxation', 'bankruptcy', 'billion', 'million']

business_keywords = [k.lower() for k in business_keywords]

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(k in text for k in business_keywords)

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter to business articles
biz = merged[merged['is_business']]

# Extract year
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# Filter to 2010-2020 inclusive just in case
biz = biz[(biz['year'] >= 2010) & (biz['year'] <= 2020)]

counts_per_year = biz.groupby('year')['article_id'].nunique()

# Compute average over all 11 years (2010-2020 inclusive)
years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in years]
avg = sum(counts) / len(years)

result = {
    'counts_per_year': {str(y): counts_per_year.get(y, 0) for y in years},
    'average_business_articles_per_year_2010_2020_Europe': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_st1HFvzXzOaDoHGbMBd8ieYA': 'file_storage/call_st1HFvzXzOaDoHGbMBd8ieYA.json', 'var_call_eGM5YTWzkMSr39l0CAXxK6QC': 'file_storage/call_eGM5YTWzkMSr39l0CAXxK6QC.json'}

exec(code, env_args)
