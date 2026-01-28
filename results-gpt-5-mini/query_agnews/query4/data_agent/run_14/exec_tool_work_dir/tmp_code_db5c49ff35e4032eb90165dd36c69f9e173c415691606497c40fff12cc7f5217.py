code = """import json
import pandas as pd

# Load the large results from files provided by previous tool calls
with open(var_call_de68GDOaNFq9FhCBGN5ghgAO, 'r') as f:
    metadata = json.load(f)
with open(var_call_2BGF6SSwp4gxtkcsoFwIA9gc, 'r') as f:
    articles = json.load(f)

md = pd.DataFrame(metadata)
arts = pd.DataFrame(articles)

# Ensure article_id types are consistent
md['article_id'] = md['article_id'].astype(str)
arts['article_id'] = arts['article_id'].astype(str)

# Merge metadata for 2015 with article content
df = pd.merge(md, arts, on='article_id', how='inner')

# Simple keyword-based classifier for categories
sports_kw = [
    'score','match','cup','league','season','goal','bat','batting','pitcher','quarterback',
    'touchdown','tournament','olympic','olympics','world cup','fifa','nba','mlb','nfl',
    'soccer','football','basketball','tennis','golf','cricket','goalkeeper','coach','scored',
    'defeat','beat','wins','loss','draw','inning','home run','homers'
]
business_kw = [
    'stock','stocks','market','shares','ipo','investment','investors','economy','economic',
    'finance','bank','profit','profits','earnings','dollar','bond','merger','acquisition',
    'reuters - financial','wall st','wall street','fed','interest rate'
]
tech_kw = [
    'scientist','research','technology','scientists','nasa','space','software','computer',
    'internet','ai','artificial intelligence','robot','drugs','drug','vaccine','researchers',
    'experiment','scientific','nuclear','tech','mobile','iphone','android'
]
world_kw = [
    'president','election','attack','war','military','government','border','conflict','minister',
    'reuters','afp','ap','washington','tehran','london','moscow','china','india','russia','europe',
    'africa','asia','north america','south america','country','countries'
]

import re

def contains_any(text, keywords):
    if not isinstance(text, str):
        return False
    text = text.lower()
    for kw in keywords:
        if kw in text:
            return True
    return False

def classify_row(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    # Priority: sports, business, tech, world
    if contains_any(text, sports_kw):
        return 'Sports'
    if contains_any(text, business_kw):
        return 'Business'
    if contains_any(text, tech_kw):
        return 'Science/Technology'
    if contains_any(text, world_kw):
        return 'World'
    # Default to World if none matched
    return 'World'

# Apply classifier
df['category'] = df.apply(classify_row, axis=1)

# Count World articles by region
world_df = df[df['category']=='World']
counts = world_df['region'].value_counts().to_dict()

if len(counts)==0:
    result = {"region": None, "count": 0, "counts": counts}
else:
    # get region with max count (if tie, pick the first)
    max_region = max(counts.items(), key=lambda x: (x[1], x[0]))[0]
    result = {"region": max_region, "count": counts[max_region], "counts": counts}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NvJkSqQCeNGn9eBAl0HXKGhx': ['articles'], 'var_call_QKvKdpde5ftBXk9YQl0rpQhR': ['authors', 'article_metadata'], 'var_call_de68GDOaNFq9FhCBGN5ghgAO': 'file_storage/call_de68GDOaNFq9FhCBGN5ghgAO.json', 'var_call_2BGF6SSwp4gxtkcsoFwIA9gc': 'file_storage/call_2BGF6SSwp4gxtkcsoFwIA9gc.json'}

exec(code, env_args)
