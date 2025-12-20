code = """import json, pandas as pd
from datetime import datetime

# Load full results from files
with open(var_call_H7FVXBUJS2FzZaD6pAv2NDYp, 'r') as f:
    meta = json.load(f)
with open(var_call_lCzqo5o1m4oQ5XAI4OUIhwUa, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter metadata to 2015 only
meta_df['year'] = meta_df['publication_date'].str[:4].astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Join with articles to get text
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Very simple keyword-based classifier for categories
world_keywords = ['iraq','war','election','president','government','minister','united nations','u.n.','u.n','terror','bomb','peace','conflict','korea','taliban','gaza','israel','palestinian','afghanistan','nato','parliament','vote','rebel','military','troop','summit','embassy','diplomat','crisis']

sports_keywords = ['game','season','team','win','victory','defeat','coach','player','league','tournament','soccer','football','nba','nfl','mlb','nhl','goal','score','match','olympic','olympics','tennis','golf','cricket','basketball','baseball','playoffs']

business_keywords = ['stock','market','share','shares','bond','bonds','profit','loss','economy','economic','index','investor','investment','bank','banks','fund','funds','trade','trading','company','corporate','merger','acquisition','ipo','revenue','earnings']

scitech_keywords = ['research','scientist','scientists','study','studies','technology','software','hardware','internet','computer','computing','physics','chemistry','biology','space','nasa','genetic','genetics','engineer','engineering','medical','medicine','disease','drug','drugs','phone','mobile','smartphone']


def classify(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    def has(keys):
        return any(k in text for k in keys)
    # Priority order: Sports, Business, Sci/Tech, then World as default if it has worldish keywords, else None
    if has(sports_keywords):
        return 'Sports'
    if has(business_keywords):
        return 'Business'
    if has(scitech_keywords):
        return 'Science/Technology'
    if has(world_keywords):
        return 'World'
    return None


df['category'] = df.apply(classify, axis=1)

world_df = df[df['category'] == 'World']

counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = None
else:
    result = counts.index[0]

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_H7FVXBUJS2FzZaD6pAv2NDYp': 'file_storage/call_H7FVXBUJS2FzZaD6pAv2NDYp.json', 'var_call_lCzqo5o1m4oQ5XAI4OUIhwUa': 'file_storage/call_lCzqo5o1m4oQ5XAI4OUIhwUa.json'}

exec(code, env_args)
