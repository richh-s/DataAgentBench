code = """import json, pandas as pd

# Load full metadata
with open(var_call_sae3Hn4lrcpgZ5WlhRpwFmdY, 'r') as f:
    meta = json.load(f)

# Load full articles
with open(var_call_5qQv1beOU1SWGG6p8RXUsBwp, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter year 2015
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Join
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Simple rule-based classifier for categories
world_keywords = ['iraq','election','president','government','war','united nations','un','prime minister','israel','palestinian','palestine','conflict','troops','terror','bomb','attack','afghanistan','nuclear','diplomat','embassy','summit','minister','parliament','border','refugee','protest','russia','china','european union','eu','policy','world','global']

sports_keywords = ['game','games','match','tournament','league','cup','olympics','nfl','nba','mlb','nhl','soccer','football','basketball','baseball','tennis','golf','cricket','coach','team','season','playoff','athlete','score','goal']

business_keywords = ['stock','stocks','market','shares','ipo','wall st','wall street','nasdaq','dow','economy','economic','funds','bank','banks','investor','investors','investment','invest','finance','financial','merger','acquisition','profit','loss','earnings','revenue','sales','price','prices','oil','trade deficit','trade','loan','jobless','unemployment','retail','company','companies','corporate','industry']

sci_tech_keywords = ['science','scientist','research','study','studies','technology','tech','software','internet','web','online','computer','computers','nuclear plant','nuclear','space','nasa','biology','physics','chemistry','engineer','engineering','cell','genome','medical','medicine','drug','drugs','disease','diseases']

import re

def classify(text):
    if not isinstance(text,str):
        return 'Other'
    t = text.lower()
    def has(keys):
        return any(k in t for k in keys)
    # Prioritize sports, business, sci/tech, then world to reduce overlap bias
    if has(sports_keywords):
        return 'Sports'
    if has(business_keywords):
        return 'Business'
    if has(sci_tech_keywords):
        return 'Science/Technology'
    if has(world_keywords):
        return 'World'
    return 'Other'

# Use title+description
df['text'] = df['title'].fillna('') + ' ' + df['description'].fillna('')
df['category'] = df['text'].apply(classify)

world_2015 = df[df['category'] == 'World']
counts = world_2015.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sae3Hn4lrcpgZ5WlhRpwFmdY': 'file_storage/call_sae3Hn4lrcpgZ5WlhRpwFmdY.json', 'var_call_5qQv1beOU1SWGG6p8RXUsBwp': 'file_storage/call_5qQv1beOU1SWGG6p8RXUsBwp.json'}

exec(code, env_args)
