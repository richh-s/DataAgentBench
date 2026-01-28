code = """import json
import pandas as pd

# Load previous query results from storage file paths
with open(var_call_z3Nl8MRG5xApky3QBku1Qh3G, 'r') as f:
    metadata_2015 = json.load(f)
with open(var_call_gDKPAd5GrWGlbuY72ErfWuCJ, 'r') as f:
    articles = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(metadata_2015)
df_articles = pd.DataFrame(articles)

# Ensure article_id types are strings for safe merge
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge on article_id
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Drop rows without text
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Simple rule-based classifier
sports_kw = [
    'score','scores','beat','beats','defeat','defeats','defeated','match','tournament','league',
    'season','goal','goals','touchdown','inning','bat','pitcher','coach','player','players',
    'olympic','world cup','cup','fifa','nba','mlb','nfl','soccer','football','basketball','tennis'
]
business_kw = [
    'stock','stocks','shares','market','markets','economy','economic','revenue','profit','profits',
    'ipo','investment','investor','investors','company','companies','bank','banks','dollar','trade',
    'trading','oil prices','oil','crude','billion','million'
]
sci_kw = [
    'scientist','scientists','research','study','studies','technology','tech','computer','software',
    'nasa','experiment','scientific','iphone','android','smartphone','robot','drugs','virus'
]

import re

def classify(text):
    t = text.lower()
    # sports
    for kw in sports_kw:
        if kw in t:
            return 'Sports'
    # business
    for kw in business_kw:
        if kw in t:
            return 'Business'
    # science/tech
    for kw in sci_kw:
        if kw in t:
            return 'Science/Technology'
    # default to World
    return 'World'

# Combine title and description
df['full_text'] = (df['title'] + ' ' + df['description']).astype(str)

# Classify
df['category'] = df['full_text'].apply(classify)

# Filter for World category
df_world = df[df['category'] == 'World']

# Count by region
counts = df_world['region'].value_counts().to_dict()

# Determine top region(s)
if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'count_by_region': counts,
    'max_count': max_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_z3Nl8MRG5xApky3QBku1Qh3G': 'file_storage/call_z3Nl8MRG5xApky3QBku1Qh3G.json', 'var_call_gDKPAd5GrWGlbuY72ErfWuCJ': 'file_storage/call_gDKPAd5GrWGlbuY72ErfWuCJ.json'}

exec(code, env_args)
