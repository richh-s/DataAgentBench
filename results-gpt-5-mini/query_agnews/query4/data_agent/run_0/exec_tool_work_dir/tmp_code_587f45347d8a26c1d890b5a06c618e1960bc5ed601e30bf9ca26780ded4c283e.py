code = """import json
import pandas as pd

# Load previous tool results from storage variables
p_meta = var_call_2LUiUeReFC2WGoAP2lgV2r3F
p_articles = var_call_qD8uzcVYco6okhCyUZd4ZVT2

# helper to load if path
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_var(p_meta)
articles = load_var(p_articles)

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Normalize article_id to int for safe merge
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata (2015) with article texts
df = pd.merge(df_meta, df_articles[['article_id','title','description']], on='article_id', how='left')

# Define keyword-based classifier
sports_kw = ['goal','match','season','team','score','wins','defeat','draw','tournament','league','season','cup','olympic','fifa','nba','mlb','nfl','football','soccer','tennis','cricket','goalkeeper','midfielder','forward']
business_kw = ['stocks','stock','market','shares','profit','profits','revenue','invest','investment','bank','economy','economic','trade','trading','oil','barrel','prices','price','dollar','market','firm','company','ipo','shares','bourse']
tech_kw = ['technology','tech','scientist','nasa','computer','software','internet','google','hp','microsoft','apple','device','robot','ai','artificial intelligence','space','research','science']

import re

def classify(title, desc):
    text = ' '.join([str(title or ''), str(desc or '')]).lower()
    # simple word match
    for kw in sports_kw:
        if re.search(r"\b"+re.escape(kw)+r"\b", text):
            return 'Sports'
    for kw in business_kw:
        if re.search(r"\b"+re.escape(kw)+r"\b", text):
            return 'Business'
    for kw in tech_kw:
        if re.search(r"\b"+re.escape(kw)+r"\b", text):
            return 'Science/Technology'
    return 'World'

# Apply classifier
df['category'] = df.apply(lambda r: classify(r.get('title',''), r.get('description','')), axis=1)

# Count World articles by region
world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().to_dict()

if counts:
    # find region with max count (ties broken by alphabetical order)
    max_count = max(counts.values())
    top_regions = sorted([k for k,v in counts.items() if v==max_count])
    top_region = top_regions[0]
else:
    top_region = None
    max_count = 0

result = {"region": top_region, "world_article_count": int(max_count), "counts_by_region": counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2LUiUeReFC2WGoAP2lgV2r3F': 'file_storage/call_2LUiUeReFC2WGoAP2lgV2r3F.json', 'var_call_qD8uzcVYco6okhCyUZd4ZVT2': 'file_storage/call_qD8uzcVYco6okhCyUZd4ZVT2.json'}

exec(code, env_args)
