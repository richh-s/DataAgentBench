code = """import json, pandas as pd

# Load metadata result
path_meta = var_call_WPe0imwhARFrdlCCDHjn1re9
with open(path_meta, 'r') as f:
    meta = json.load(f)

# Load articles result
path_art = var_call_vrdTsYlaoXDoEtvKzpuDpJdp
with open(path_art, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id is int in both
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join to get titles/descriptions only for Europe 2010-2020
merged = meta_df.merge(arts_df, on='article_id', how='left')

# Very naive classifier for Business vs others using keywords
business_keywords = ['stock', 'stocks', 'market', 'markets', 'share', 'shares', 'trading', 'trade', 'trader', 'fund', 'funds', 'bank', 'banks', 'economy', 'economic', 'finance', 'financial', 'business', 'company', 'companies', 'oil', 'profit', 'profits', 'growth', 'loan', 'loans', 'price', 'prices', ' ipo', 'investment', 'investor', 'investors', 'revenue', 'sales', 'earnings']

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(k in text for k in business_keywords)

merged['is_business'] = merged.apply(is_business, axis=1)

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

# Filter to business
biz = merged[merged['is_business']]

# Count per year
counts = biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)

avg_per_year = counts.mean()

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_per_year': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_WPe0imwhARFrdlCCDHjn1re9': 'file_storage/call_WPe0imwhARFrdlCCDHjn1re9.json', 'var_call_vrdTsYlaoXDoEtvKzpuDpJdp': 'file_storage/call_vrdTsYlaoXDoEtvKzpuDpJdp.json'}

exec(code, env_args)
