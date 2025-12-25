code = """import json, pandas as pd

# Load metadata for European articles 2010-2020
eu_meta = var_call_YkrobXUfEAzcJ2qbTLOv6n1i
if isinstance(eu_meta, str) and eu_meta.endswith('.json'):
    with open(eu_meta, 'r') as f:
        eu_meta = json.load(f)

# Load all articles
arts = var_call_vcNToBYaqdtwRWqONTEMCAeN
if isinstance(arts, str) and arts.endswith('.json'):
    with open(arts, 'r') as f:
        arts = json.load(f)

meta_df = pd.DataFrame(eu_meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id comparable
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Simple rule-based classifier for category based on title+description
BUSINESS_KEYWORDS = ['stock', 'stocks', 'wall st', 'wall street', 'market', 'markets', 'economy', 'economic', 'business', 'company', 'companies', 'shares', 'share', 'profit', 'profits', 'trade deficit', 'loan', 'ipo', 'investment', 'investors', 'fund', 'funds', 'oil prices', 'crude', 'merger', 'takeover', 'corporate', 'factory', 'factories', 'job cuts', 'unemployment', 'central bank', 'interest rate', 'interest rates', 'currency', 'currencies', 'dollar', 'euro', 'yen', 'export', 'exports', 'import', 'imports', 'deficit', 'tariff', 'tariffs', 'eurozone']
SPORTS_KEYWORDS = ['football', 'soccer', 'tennis', 'basketball', 'olympics', 'olympic', 'world cup', 'grand prix', 'formula one', 'f1', 'cricket', 'golf', 'baseball', 'nba', 'nfl', 'nhl', 'mlb', 'coach', 'coaches', 'tournament', 'league', 'cup final', 'goal', 'goals', 'score', 'scored', 'match', 'matches']
SCI_TECH_KEYWORDS = ['science', 'scientists', 'researchers', 'study', 'studies', 'technology', 'software', 'hardware', 'computer', 'computers', 'internet', 'online', 'web', 'mobile', 'phone', 'phones', 'nuclear', 'physics', 'biotech', 'drug', 'drugs', 'medical', 'medicine', 'research', 'space', 'satellite', 'satellites', 'mars', 'nasa', 'genetic', 'dna']

BUSINESS_KEYWORDS = [k.lower() for k in BUSINESS_KEYWORDS]
SPORTS_KEYWORDS = [k.lower() for k in SPORTS_KEYWORDS]
SCI_TECH_KEYWORDS = [k.lower() for k in SCI_TECH_KEYWORDS]

def classify(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    if any(k in text for k in SPORTS_KEYWORDS):
        return 'Sports'
    if any(k in text for k in SCI_TECH_KEYWORDS):
        return 'Science/Technology'
    if any(k in text for k in BUSINESS_KEYWORDS):
        return 'Business'
    return 'World'

arts_df['category'] = arts_df.apply(classify, axis=1)

# Merge articles with European metadata
merged = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='left')

# Filter to Business and years 2010-2020 (already filtered by query, but extract year)
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

business = merged[merged['category'] == 'Business']

# Count per year and compute average over the 11 years
counts_per_year = business.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts_per_year.mean()

import math
avg_per_year_rounded = round(float(avg_per_year), 2)

result = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year_rounded,
    'counts_per_year': counts_per_year.to_dict()
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_YkrobXUfEAzcJ2qbTLOv6n1i': 'file_storage/call_YkrobXUfEAzcJ2qbTLOv6n1i.json', 'var_call_vcNToBYaqdtwRWqONTEMCAeN': 'file_storage/call_vcNToBYaqdtwRWqONTEMCAeN.json'}

exec(code, env_args)
