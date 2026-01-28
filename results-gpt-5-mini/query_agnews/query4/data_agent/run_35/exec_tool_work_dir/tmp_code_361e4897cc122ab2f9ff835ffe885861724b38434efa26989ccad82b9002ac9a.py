code = """import json
import pandas as pd

# Load data from previous tool outputs (file paths are provided in variables)
with open(var_call_36eCPtR0iYYjmgbysxpnISUP, 'r', encoding='utf-8') as f:
    articles = json.load(f)
with open(var_call_HmZXMn7JrEtDVZ6jo9bkLjah, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

df_a = pd.DataFrame(articles)
df_m = pd.DataFrame(metadata)

# Normalize article_id types
if 'article_id' in df_a.columns:
    df_a['article_id'] = df_a['article_id'].astype(str)
if 'article_id' in df_m.columns:
    df_m['article_id'] = df_m['article_id'].astype(str)

# Merge
df = pd.merge(df_m, df_a, on='article_id', how='left')

# Filter for year 2015
df['publication_date'] = df['publication_date'].astype(str)
df_2015 = df[df['publication_date'].str.startswith('2015')].copy()

# Classification rules
sports_kw = ['match','beat','defeat','defeated','win','wins','won','goal','season','club','football','soccer','basketball','olympic','olympics','serie','league','tournament','scored','penalty','coach','manager','fans','cup','vs.','vs ']
scitech_kw = ['technology','tech','scientist','research','nasa','space','robot','software','computer','internet','novel','study','lab','scientific','science','nuclear','ai','artificial intelligence']
business_kw = ['stocks','shares','ipo','market','markets','economy','economic','reuters -','wall st','investment','bank','earnings','profit','trade deficit','trade','dollar','oil prices','oil and economy','merger','acquisition']

import re

def classify_text(row):
    title = '' if pd.isna(row.get('title')) else str(row.get('title'))
    desc = '' if pd.isna(row.get('description')) else str(row.get('description'))
    text = (title + ' ' + desc).lower()
    # simple token check
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in scitech_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    return 'World'

# Apply classification
if df_2015.shape[0] == 0:
    result = {'top_region': None, 'count': 0, 'counts_by_region': {}}
else:
    df_2015['category'] = df_2015.apply(classify_text, axis=1)
    world_df = df_2015[df_2015['category'] == 'World']
    counts = world_df['region'].value_counts().to_dict()
    if len(counts) == 0:
        result = {'top_region': None, 'count': 0, 'counts_by_region': {}}
    else:
        # determine top region (if tie, list all)
        max_count = max(counts.values())
        top_regions = [r for r,c in counts.items() if c==max_count]
        result = {'top_region': top_regions if len(top_regions)>1 else top_regions[0], 'count': max_count, 'counts_by_region': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FI2ZJ6xitn7GNx2lfIM1Dkz7': ['articles'], 'var_call_36eCPtR0iYYjmgbysxpnISUP': 'file_storage/call_36eCPtR0iYYjmgbysxpnISUP.json', 'var_call_Wyal0vAWlPopU08kwxHO9RP5': ['authors', 'article_metadata'], 'var_call_HmZXMn7JrEtDVZ6jo9bkLjah': 'file_storage/call_HmZXMn7JrEtDVZ6jo9bkLjah.json'}

exec(code, env_args)
