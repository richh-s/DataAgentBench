code = """import json, pandas as pd, os

# Load Europe metadata
path_meta = var_call_5wHqtmsVdpP3KiZgebIEbMfE
with open(path_meta, 'r') as f:
    europe_meta = json.load(f)

# Load all articles
path_articles = var_call_xZqGFdVLgdzqBM4rScBYdrnq
with open(path_articles, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
art_df = pd.DataFrame(articles)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Simple rule-based classifier for Business category using keywords
business_keywords = ['stock', 'stocks', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'market', 'markets', 'shares', 'share price', 'ipo', 'merger', 'acquisition', 'deal', 'profit', 'profits', 'losses', 'earnings', 'revenue', 'sales', 'economy', 'economic', 'trade', 'oil', 'crude', 'bank', 'banking', 'interest rate', 'rates', 'currency', 'currencies', 'dollar', 'euro', 'yen', 'inflation', 'deflation', 'investment', 'investor', 'fund', 'funds', 'business', 'company', 'companies', 'corp', 'corporation', 'group plc', 'plc', 'industrial', 'industry', 'job cuts', 'jobs', 'unemployment', 'housing market', 'real estate']

business_keywords = [k.lower() for k in business_keywords]

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(kw in text for kw in business_keywords)

art_df['is_business'] = art_df.apply(is_business, axis=1)

# Join Europe metadata with articles
merged = meta_df.merge(art_df[['article_id', 'is_business']], on='article_id', how='left')

# Filter to business articles
biz = merged[merged['is_business']]

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

biz_per_year = biz.groupby(merged.loc[biz.index, 'year']).size()

# Compute average from 2010 to 2020 inclusive
years = list(range(2010, 2021))
counts = [int(biz_per_year.get(y, 0)) for y in years]
avg = sum(counts) / len(years)

result = {
    'business_counts_per_year': {str(y): counts[i] for i, y in enumerate(years)},
    'average_business_articles_per_year_2010_2020_Europe': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5wHqtmsVdpP3KiZgebIEbMfE': 'file_storage/call_5wHqtmsVdpP3KiZgebIEbMfE.json', 'var_call_xZqGFdVLgdzqBM4rScBYdrnq': 'file_storage/call_xZqGFdVLgdzqBM4rScBYdrnq.json', 'var_call_Ux2CSP2kkwaBmbimMa5OdCEf': ['articles']}

exec(code, env_args)
