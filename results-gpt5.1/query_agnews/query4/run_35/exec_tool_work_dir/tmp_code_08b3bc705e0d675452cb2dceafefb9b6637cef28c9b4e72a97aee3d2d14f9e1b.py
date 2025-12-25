code = """import json, pandas as pd

# Load full metadata and articles from files
with open(var_call_n642wGAaNVh8DviN5bwWGIwh, 'r') as f:
    meta = json.load(f)
with open(var_call_KfV3yUqO70fWRQsJbWOtP440, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter to 2015
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Merge
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based classifier for categories
world_keywords = ['iraq','election','government','minister','president','war','united nations','u.n.','u.n','peace','conflict','clashes','troops','attack','bomb','palestinian','israel','afghanistan','terror','militant','rebels','killed','security council','diplomat','foreign','summit','parliament','policy','nato','al-qaeda','al qaeda']

sports_keywords = ['football','soccer','nba','nfl','nhl','mlb','tennis','golf','olympics','cricket','baseball','basketball','hockey','athletics','grand slam','fifa','uefa','world cup','tournament','coach','player','goal','score','match','season opener']

business_keywords = ['stocks','stock','shares','wall st','wall street','ipo','market','trading','profit','losses','economy','economic','bank','fund','interest rates','inflation','deficit','treasury','bond','merger','acquisition','currency','dollar','yen','euro','nasdaq','dow','ftse','nikkei','loan','oil prices','crude','futures']

sci_tech_keywords = ['researchers','scientists','study','nasa','space','mission','planet','telescope','experiment','laboratory','technology','software','computer','internet','online','web site','website','cell phone','mobile phone','smartphone','genetic','dna','medical','vaccine','physics','chemistry','biology']


def to_lower(text):
    return text.lower() if isinstance(text,str) else ''

arts_df2 = df.copy()
arts_df2['text'] = (arts_df2['title'].fillna('') + ' ' + arts_df2['description'].fillna('')).apply(to_lower)

import numpy as np

cats = []
for txt in arts_df2['text']:
    scores = { 'World':0, 'Sports':0, 'Business':0, 'Science/Technology':0 }
    for w in world_keywords:
        if w in txt:
            scores['World'] += 1
    for w in sports_keywords:
        if w in txt:
            scores['Sports'] += 1
    for w in business_keywords:
        if w in txt:
            scores['Business'] += 1
    for w in sci_tech_keywords:
        if w in txt:
            scores['Science/Technology'] += 1
    # choose max, tie-breaker by fixed order
    max_score = max(scores.values())
    if max_score == 0:
        cat = 'World'  # default assumption
    else:
        for c in ['World','Sports','Business','Science/Technology']:
            if scores[c] == max_score:
                cat = c
                break
    cats.append(cat)

arts_df2['category'] = cats

world_2015 = arts_df2[arts_df2['category'] == 'World']

region_counts = world_2015.groupby('region').size().sort_values(ascending=False)

if len(region_counts) == 0:
    result = None
else:
    top_region = region_counts.idxmax()
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_n642wGAaNVh8DviN5bwWGIwh': 'file_storage/call_n642wGAaNVh8DviN5bwWGIwh.json', 'var_call_KfV3yUqO70fWRQsJbWOtP440': 'file_storage/call_KfV3yUqO70fWRQsJbWOtP440.json'}

exec(code, env_args)
