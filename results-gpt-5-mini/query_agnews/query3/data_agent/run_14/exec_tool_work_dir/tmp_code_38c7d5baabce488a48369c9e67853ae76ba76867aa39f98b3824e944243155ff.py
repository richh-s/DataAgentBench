code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_HaXAoKYyVMULcYpGlnbOm8V2, 'r') as f:
    metadata = json.load(f)
with open(var_call_eBO4PhUuIK8HqLUJ2V9Rvw0K, 'r') as f:
    articles = json.load(f)

md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

# Ensure correct types
md['article_id'] = md['article_id'].astype(int)
md['publication_date'] = pd.to_datetime(md['publication_date'])
art['article_id'] = art['article_id'].astype(int)

# Merge metadata (Europe) with articles
df = md.merge(art, on='article_id', how='left')

# Restrict to years 2010-2020 inclusive (though query already filtered)
df['year'] = df['publication_date'].dt.year
mask = (df['year'] >= 2010) & (df['year'] <= 2020)
df = df[mask].copy()

# Classification heuristics
import re

def classify_row(title, desc):
    text = ' '.join(filter(None, [str(title), str(desc)])).lower()
    # Sports keywords
    sports_kw = ['football', 'soccer', 'basketball', 'tennis', 'golf', 'cricket', 'match', 'league', 'cup', 'scored', 'coach', 'player', 'season', 'wins', 'defeat']
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    # Science/Technology keywords
    tech_kw = ['technology', 'tech', 'scientist', 'research', 'nasa', 'computer', 'software', 'internet', 'robot', 'science', 'ai']
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    # Business keywords
    biz_kw = ['economy', 'economic', 'market', 'stock', 'stocks', 'shares', 'ipo', 'bank', 'finance', 'financial', 'business', 'firm', 'company', 'profit', 'investment', 'investor', 'oil', 'dollar', 'euro', 'money', 'fund']
    for kw in biz_kw:
        if kw in text:
            return 'Business'
    # Default to World
    return 'World'

# Apply classification
df['category'] = df.apply(lambda r: classify_row(r.get('title',''), r.get('description','')), axis=1)

# Count business articles per year
years = list(range(2010, 2021))
counts = {str(y): int(df[(df['year']==y) & (df['category']=='Business')].shape[0]) for y in years}

total_business = sum(counts.values())
average_per_year = total_business / len(years) if len(years)>0 else 0.0

result = {
    'yearly_business_counts': counts,
    'total_business_articles_2010_2020': int(total_business),
    'average_business_articles_per_year_2010_2020': round(average_per_year, 2)
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HaXAoKYyVMULcYpGlnbOm8V2': 'file_storage/call_HaXAoKYyVMULcYpGlnbOm8V2.json', 'var_call_eBO4PhUuIK8HqLUJ2V9Rvw0K': 'file_storage/call_eBO4PhUuIK8HqLUJ2V9Rvw0K.json'}

exec(code, env_args)
