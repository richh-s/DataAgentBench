code = """import json, pandas as pd

path_meta = var_call_WPe0imwhARFrdlCCDHjn1re9
with open(path_meta, 'r') as f:
    meta = json.load(f)

path_art = var_call_vrdTsYlaoXDoEtvKzpuDpJdp
with open(path_art, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# coerce article_id to numeric, errors to NaN then drop
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'], errors='coerce')
meta_df = meta_df.dropna(subset=['article_id'])
arts_df = arts_df.dropna(subset=['article_id'])
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

merged = meta_df.merge(arts_df, on='article_id', how='left')

business_keywords = ['stock', 'stocks', 'market', 'markets', 'share', 'shares', 'trading', 'trade', 'trader', 'fund', 'funds', 'bank', 'banks', 'economy', 'economic', 'finance', 'financial', 'business', 'company', 'companies', 'oil', 'profit', 'profits', 'growth', 'loan', 'loans', 'price', 'prices', ' ipo', 'investment', 'investor', 'investors', 'revenue', 'sales', 'earnings']

# Ensure title/description are strings
merged['title'] = merged['title'].astype(str)
merged['description'] = merged['description'].astype(str)

lower_keywords = [k.lower() for k in business_keywords]

import numpy as np

def is_business(text):
    if not isinstance(text, str):
        text = ''
    t = text.lower()
    return any(k in t for k in lower_keywords)

texts = merged['title'].fillna('') + ' ' + merged['description'].fillna('')
merged['is_business'] = texts.apply(is_business)

merged['year'] = merged['publication_date'].astype(str).str.slice(0,4).astype(int)

biz = merged[merged['is_business']]

counts = biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)

avg_per_year = float(counts.mean())

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_per_year': {str(int(k)): int(v) for k,v in counts.to_dict().items()}})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_WPe0imwhARFrdlCCDHjn1re9': 'file_storage/call_WPe0imwhARFrdlCCDHjn1re9.json', 'var_call_vrdTsYlaoXDoEtvKzpuDpJdp': 'file_storage/call_vrdTsYlaoXDoEtvKzpuDpJdp.json'}

exec(code, env_args)
