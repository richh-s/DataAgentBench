code = """import json
import pandas as pd

# Load the large query results from the provided storage file paths
with open(var_call_3slgJBrmloTM9qzyarQJ9gZa, 'r') as f:
    articles = json.load(f)
with open(var_call_omI2nS9X385uXHHXpI3p2JNr, 'r') as f:
    metadata = json.load(f)

# DataFrames
df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(metadata)

# Ensure article_id as string for safe merge
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Filter for year 2015
df['year'] = df['publication_date'].str[:4]
df_2015 = df[df['year']=='2015'].copy()

# Classification rules
sports_kw = ['game','score','season','match','goal','bat','batting','innings','coach','league','nba','nfl','mlb','soccer','football','tennis','fifa','olympic','cup','tournament','boxing','win','defeat','draw']
business_kw = ['stock','stocks','market','wall st','ipo','earnings','profit','economy','dollar','shares','bank','business','revenue','investment','investor','oil prices']
sci_kw = ['scientist','research','study','researchers','technology','tech','computer','email','e-mail','nasa','ibm','google','software','drug','science','dna']

import re

def classify_row(title, desc):
    text = ''
    if not pd.isna(title):
        text += title + ' '
    if not pd.isna(desc):
        text += desc
    text = text.lower()
    # quick token search
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply classification
df_2015['category'] = df_2015.apply(lambda r: classify_row(r.get('title',''), r.get('description','')), axis=1)

# Count World articles by region
world_df = df_2015[df_2015['category']=='World']
counts = world_df.groupby('region').size().to_dict()

if counts:
    # determine top region
    top_region = max(counts.items(), key=lambda x: (x[1], x[0]))[0]
    top_count = int(counts[top_region])
else:
    top_region = None
    top_count = 0

result = {
    'top_region': top_region,
    'count': top_count,
    'counts_by_region': {k: int(v) for k,v in counts.items()}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6TvUNoifPFaGCxEi2yOKrIeV': ['articles'], 'var_call_3slgJBrmloTM9qzyarQJ9gZa': 'file_storage/call_3slgJBrmloTM9qzyarQJ9gZa.json', 'var_call_BvDq6aHIghcQJTzoNtneweAc': ['authors', 'article_metadata'], 'var_call_omI2nS9X385uXHHXpI3p2JNr': 'file_storage/call_omI2nS9X385uXHHXpI3p2JNr.json'}

exec(code, env_args)
