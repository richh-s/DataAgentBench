code = """import json, pandas as pd

# Load full results from files
with open(var_call_3pzPtBD4EufpCUKDwp5MIZ8Z, 'r') as f:
    europe_meta = json.load(f)
with open(var_call_7XGVLT9hmwoCSyT3219IHzkn, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to get titles/descriptions for European articles 2010-2020
merged = meta_df.merge(articles_df, on='article_id', how='left')

# Simple rule-based classifier for Business vs other categories
business_keywords = [
    'stock', 'stocks', 'wall st', 'dow', 'nasdaq', 's&p', 'bond', 'bonds',
    'market', 'markets', 'ipo', 'merger', 'acquisition', 'm&a', 'profit',
    'profits', 'earning', 'earnings', 'revenue', 'revenues', 'sales',
    'company', 'companies', 'shares', 'share', 'corporate', 'economy',
    'economic', 'trade', 'bank', 'banks', 'banking', 'finance', 'financial',
    'business', 'firm', 'firms', 'investment', 'investor', 'investors',
    'oil', 'price', 'prices', 'retail', 'jobless', 'unemployment', 'deficit',
    'loan', 'loans', 'deal', 'deals', 'eurozone', 'euro', 'interest rate',
    'interest rates', 'fund', 'funds', 'mutual fund'
]

sports_keywords = ['football', 'soccer', 'tennis', 'basketball', 'cricket', 'olympics', 'tournament', 'cup', 'league', 'goal', 'match']
science_keywords = ['research', 'study', 'scientist', 'nasa', 'space', 'galaxy', 'physics', 'chemistry', 'biology', 'technology', 'tech', 'software', 'computer', 'scientific']

business_kw = set(business_keywords)
sports_kw = set(sports_keywords)
science_kw = set(science_keywords)

def classify(title, desc):
    text = (str(title) + ' ' + str(desc)).lower()
    # simple token-based contains
    if any(kw in text for kw in sports_kw):
        return 'Sports'
    if any(kw in text for kw in science_kw):
        return 'Science/Technology'
    if any(kw in text for kw in business_kw):
        return 'Business'
    return 'World'

merged['category'] = merged.apply(lambda r: classify(r.get('title', ''), r.get('description', '')), axis=1)

# Filter to Business
biz = merged[merged['category'] == 'Business'].copy()

# Extract year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# Count per year 2010-2020
counts = biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts.mean()

result = {
    'counts_per_year': counts.to_dict(),
    'average_business_articles_per_year_2010_2020_Europe': avg_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3pzPtBD4EufpCUKDwp5MIZ8Z': 'file_storage/call_3pzPtBD4EufpCUKDwp5MIZ8Z.json', 'var_call_7XGVLT9hmwoCSyT3219IHzkn': 'file_storage/call_7XGVLT9hmwoCSyT3219IHzkn.json', 'var_call_CNKSaxF58Ph2RgMX1rTQ5wEw': ['articles']}

exec(code, env_args)
