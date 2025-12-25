code = """import json, pandas as pd

# Load metadata (Europe 2010-2020)
meta_path = var_call_dvuukWGB1ezyql1ohQayJPuJ
with open(meta_path, 'r') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Load articles
arts_path = var_call_EwELEuONARa8NUIYhYADcy73
with open(arts_path, 'r') as f:
    arts = json.load(f)
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Fill NaNs in text columns and lowercase
for col in ['title','description']:
    if col in arts_df.columns:
        arts_df[col] = arts_df[col].fillna('').astype(str).str.lower()

business_keywords = ['stock', 'stocks', 'market', 'business', 'economy', 'economic', 'finance', 'financial', 'trade', 'trading', 'company', 'companies', 'corporate', 'shares', 'investor', 'investors', 'investment', 'bank', 'banks', 'banking', 'ipo', 'merger', 'acquisition', 'profits', 'earnings', 'revenue', 'deficit', 'budget', 'oil', 'price', 'prices', 'commerce', 'sales', 'retail', 'fund', 'funds']
pattern = '|'.join(business_keywords)

arts_df['is_business'] = False
mask = arts_df['title'].str.contains(pattern, na=False) | arts_df['description'].str.contains(pattern, na=False)
arts_df.loc[mask, 'is_business'] = True

merged = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='left')
merged['is_business'] = merged['is_business'].fillna(False)

biz = merged[merged['is_business'] == True]

counts_per_year = biz.groupby('year')['article_id'].nunique()

years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in years]
avg = sum(counts) / len(years) if years else 0

result = {
    'years': years,
    'business_counts_per_year': counts,
    'average_business_articles_per_year_Europe_2010_2020': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dvuukWGB1ezyql1ohQayJPuJ': 'file_storage/call_dvuukWGB1ezyql1ohQayJPuJ.json', 'var_call_EwELEuONARa8NUIYhYADcy73': 'file_storage/call_EwELEuONARa8NUIYhYADcy73.json'}

exec(code, env_args)
