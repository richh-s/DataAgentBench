code = """import json, pandas as pd

# Load full results from files
with open(var_call_DGNOsyiWxFtiVylBU20Fc9In, 'r') as f:
    meta = json.load(f)
with open(var_call_5Fq6KRD3qt6YcWvtTZ8Q6X1Y, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter for 2015
meta_2015 = meta_df[meta_df['publication_date'].str.startswith('2015-')].copy()

# Merge with article text
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Very simple classifier for World vs other categories, based mainly on Sports/Business/Sci-Tech cues
business_words = ['stock','stocks','wall st','wall street','market','markets','shares','profit','profits','trade deficit','economy','economic','oil','ipo','fund','funds','interest rate','interest rates','loan','business','company','companies','bank','banks','merger','acquisition','investment','investors','earnings','revenue','sales']
sports_words = ['football','soccer','nba','nfl','nhl','mlb','cricket','tennis','golf','olympic','olympics','world cup','tournament','league','coach','goal','scored','match','game','games']
scitech_words = ['science','scientists','researchers','study','studies','technology','software','hardware','computer','computers','internet','online','space','nasa','astronaut','physics','chemistry','biology','genetics']

import re

def classify(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    # Heuristic: if sports/business/scitech words appear, assign those; else World
    for w in sports_words:
        if re.search(r'\b' + re.escape(w) + r'\b', text):
            return 'Sports'
    for w in business_words:
        if re.search(r'\b' + re.escape(w) + r'\b', text):
            return 'Business'
    for w in scitech_words:
        if re.search(r'\b' + re.escape(w) + r'\b', text):
            return 'Science/Technology'
    return 'World'

df['category'] = df.apply(classify, axis=1)

world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(counts)==0:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_DGNOsyiWxFtiVylBU20Fc9In': 'file_storage/call_DGNOsyiWxFtiVylBU20Fc9In.json', 'var_call_5Fq6KRD3qt6YcWvtTZ8Q6X1Y': 'file_storage/call_5Fq6KRD3qt6YcWvtTZ8Q6X1Y.json'}

exec(code, env_args)
