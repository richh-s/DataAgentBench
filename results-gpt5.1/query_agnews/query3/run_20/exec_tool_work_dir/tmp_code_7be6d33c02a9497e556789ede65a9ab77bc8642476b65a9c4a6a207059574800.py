code = """import json, pandas as pd
from pathlib import Path

# Load full results from storage
meta_path = var_call_5dE2rBdAXpEEVnKOaiyNaP0w
arts_path = var_call_J74utXk8AyfEWHPckfTrcIKY

with open(meta_path, 'r') as f:
    meta = json.load(f)
with open(arts_path, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge to bring in text
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple business classifier based on keywords
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'business', 'finance', 'financial', 'oil', 'trade deficit', 'ipo', 'shares', 'interest rate', 'interest rates', 'bank', 'banks', 'loan', 'loans', 'growth', 'profits', 'revenue', 'investment', 'investor', 'investors', 'fund', 'funds', 'currency', 'currencies', 'euro', 'dollar', 'yen', 'price', 'prices', 'sales', 'jobless', 'unemployment']

import re
pattern = re.compile('|'.join(re.escape(k) for k in business_keywords), re.IGNORECASE)

texts = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
mask_business = texts.str.contains(pattern)

business_df = df[mask_business].copy()

# Extract year
business_df['year'] = business_df['publication_date'].str.slice(0,4).astype(int)

# Filter 2010-2020 (should already be but to be safe)
business_df = business_df[(business_df['year'] >= 2010) & (business_df['year'] <= 2020)]

counts = business_df.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

result = {
  'counts_per_year': counts.to_dict(),
  'average_per_year': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5dE2rBdAXpEEVnKOaiyNaP0w': 'file_storage/call_5dE2rBdAXpEEVnKOaiyNaP0w.json', 'var_call_J74utXk8AyfEWHPckfTrcIKY': 'file_storage/call_J74utXk8AyfEWHPckfTrcIKY.json', 'var_call_g95OEEF1SoUi4AoSvz6QbD0o': ['articles']}

exec(code, env_args)
