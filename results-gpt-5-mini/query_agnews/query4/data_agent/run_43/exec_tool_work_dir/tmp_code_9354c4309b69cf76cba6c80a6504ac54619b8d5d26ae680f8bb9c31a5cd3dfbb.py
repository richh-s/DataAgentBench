code = """import json
import pandas as pd

# Read the large JSON results from the previous query_db calls
with open(var_call_O1dYqdKzyKEYimmlxR72LZHz, 'r') as f:
    metadata_records = json.load(f)
with open(var_call_rFomZx1sgaeYPPHzHfeDPQJW, 'r') as f:
    articles_records = json.load(f)

# Create DataFrames
md = pd.DataFrame(metadata_records)
arts = pd.DataFrame(articles_records)

# Normalize types
md['article_id'] = md['article_id'].astype(str).astype(int)
arts['article_id'] = arts['article_id'].astype(str).astype(int)

# Merge metadata for 2015 with articles
merged = pd.merge(md, arts[['article_id', 'title', 'description']], on='article_id', how='left')

# Classification keywords
business_kw = ['market','stock','stocks','shares','trade deficit','trade','economy','ipo','investment','investor','bank','profit','earnings','revenue','company','companies','oil','crude','merger','acquir','bond','fed','u.s. economy','dollar']
sports_kw = ['game','match','season','goal','scores','scored','tournament','world cup','olympic','player','league','coach','football','soccer','basketball','tennis','baseball','rugby','score','fifa','nhl','nba','mlb']
sci_kw = ['scientist','research','nasa','space','technology','tech','robot','robotics','computer','internet','software','hardware','cyber','spacecraft','physics','biology','genetic','virus','disease','study']

# Helper to count keyword hits
import re

def count_hits(text, keywords):
    if not isinstance(text, str):
        return 0
    text = text.lower()
    hits = 0
    for kw in keywords:
        # use word boundary for single words, but allow spaces in multi-word keywords
        if ' ' in kw:
            if kw in text:
                hits += 1
        else:
            # simple word search
            # escape kw
            if re.search(r"\b" + re.escape(kw) + r"\b", text):
                hits += 1
    return hits

# Classify each article
cats = []
for _, row in merged.iterrows():
    text = ' '.join([str(row.get('title','') or ''), str(row.get('description','') or '')])
    b = count_hits(text, business_kw)
    s = count_hits(text, sports_kw)
    c = count_hits(text, sci_kw)
    # Determine category by highest hits; ties or zero -> World
    scores = {'Business': b, 'Sports': s, 'Science/Technology': c}
    mx = max(scores.values())
    if mx == 0:
        cat = 'World'
    else:
        # if unique max and greater than others
        max_keys = [k for k,v in scores.items() if v == mx]
        if len(max_keys) == 1:
            cat = max_keys[0]
        else:
            # tie -> World as fallback
            cat = 'World'
    cats.append(cat)

merged['category'] = cats

# Filter World category
world = merged[merged['category'] == 'World']
# Count by region
counts = world['region'].value_counts().to_dict()

# Determine top region
if counts:
    top_region = max(counts.items(), key=lambda x: x[1])[0]
    top_count = int(max(counts.items(), key=lambda x: x[1])[1])
else:
    top_region = None
    top_count = 0

result = {'top_region': top_region, 'count': top_count, 'counts': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jX4hasSUtBEhqYn9gKLGCRxz': ['articles'], 'var_call_O1dYqdKzyKEYimmlxR72LZHz': 'file_storage/call_O1dYqdKzyKEYimmlxR72LZHz.json', 'var_call_rFomZx1sgaeYPPHzHfeDPQJW': 'file_storage/call_rFomZx1sgaeYPPHzHfeDPQJW.json'}

exec(code, env_args)
