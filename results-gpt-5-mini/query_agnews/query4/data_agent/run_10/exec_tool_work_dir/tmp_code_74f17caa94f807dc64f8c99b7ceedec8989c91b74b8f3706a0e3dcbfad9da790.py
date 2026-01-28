code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_jyHzbUOwaZQm4RfO91nVrBM6, 'r', encoding='utf-8') as f:
    articles = json.load(f)
with open(var_call_jxleeD71CtHzBAE38icuyxXZ, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# Create DataFrames
df_a = pd.DataFrame(articles)
df_m = pd.DataFrame(metadata)

# Normalize article_id to string for reliable merge
df_a['article_id'] = df_a['article_id'].astype(str).str.strip()
df_m['article_id'] = df_m['article_id'].astype(str).str.strip()

# Merge
df = pd.merge(df_m, df_a, on='article_id', how='left')

# Simple rule-based classifier for categories
sports_kw = ['game','match','tournament','league','scored','goal','runs','season','coach','player','olympic','superbowl','nba','mlb','nfl','soccer','cricket','tennis','golf','score','bat','pitch','boxing','ufc']
business_kw = ['stock','stocks','market','economy','share','ipo','investment','investor','bank','dollar','oil price','oil prices','revenue','earnings','profit','business','acquisition','merger','company','firm','finance','invest','bond']
science_kw = ['research','scientists','technology','tech','computer','software','internet','nasa','scientific','study','researchers','nuclear','drug','medical','ai','algorithm','engineer','space','robot','science']

def classify(row):
    text = ''
    if pd.notna(row.get('title')):
        text += ' ' + str(row['title'])
    if pd.notna(row.get('description')):
        text += ' ' + str(row['description'])
    text = text.lower()
    # check sports first
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply classification
df['category'] = df.apply(classify, axis=1)

# Filter to year 2015
df['publication_date'] = df['publication_date'].astype(str)
df_2015 = df[df['publication_date'].str.startswith('2015')].copy()

# Count World category articles by region
world_2015 = df_2015[df_2015['category'] == 'World']
counts = world_2015.groupby('region').size().reset_index(name='count')

if counts.empty:
    result = {'region': None, 'count': 0}
else:
    counts = counts.sort_values('count', ascending=False)
    top = counts.iloc[0]
    result = {'region': top['region'], 'count': int(top['count'])}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0BWcHPYHbYtm4KFexPtzuWSl': ['articles'], 'var_call_jyHzbUOwaZQm4RfO91nVrBM6': 'file_storage/call_jyHzbUOwaZQm4RfO91nVrBM6.json', 'var_call_8u5Ea8LqaPAgkZM0I0UuvQvL': ['authors', 'article_metadata'], 'var_call_jxleeD71CtHzBAE38icuyxXZ': 'file_storage/call_jxleeD71CtHzBAE38icuyxXZ.json'}

exec(code, env_args)
