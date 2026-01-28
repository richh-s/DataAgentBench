code = """import json
import pandas as pd

# Load metadata (file path stored in var_call_nkfCKSPjPVepzwRsXkOjZ1eu)
with open(var_call_nkfCKSPjPVepzwRsXkOjZ1eu, 'r') as f:
    meta = json.load(f)

df_meta = pd.DataFrame(meta)
# Load articles list (already in variable var_call_ZilkLbOMniGvP4nPIB65ty3f)
df_articles = pd.DataFrame(var_call_ZilkLbOMniGvP4nPIB65ty3f)

# Ensure article_id are strings
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Fill NaN title/description with empty strings
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Classification keywords
business_kw = ['stock','stocks','market','markets','shares','earnings','oil prices','oil','economy','investment','investor','billion','dow','nasdaq','wall st','carlyle','private investment','merger','ipo','revenue','profits','company','companies','firm']
sports_kw = ['beat','defeat','win','wins','match','goal','season','tournament','cup','olympic','nba','mlb','nfl','soccer','football','tennis','score','scored','race','players','league']
tech_kw = ['nasa','scientist','research','technology','tech','software','google','apple','robot','scientists','study','space','scientific','internet','facebook','microsoft','ai','artificial intelligence']
world_kw = ['president','election','elections','war','conflict','attack','attacked','minister','parliament','government','united nations','militia','rebel','pipeline','pipelines','export','exports','border','diplomacy','summit','country','countries','iraq','china','russia','syria','ceasefire','refugee','refugees','foreign','attack','protest','protests']

import re

def classify(row):
    text = (row.get('title','') + ' ' + row.get('description','')).lower()
    # Check business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in world_kw:
        if kw in text:
            return 'World'
    # default to World
    return 'World'

# Apply classification
df['category'] = df.apply(classify, axis=1)

# Filter for World
df_world = df[df['category'] == 'World']

# Count by region
counts = df_world.groupby('region').size().to_dict()

# Determine top region
if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'max_count': max_count,
    'counts_by_region': counts
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_La62qtbvIU0KPmifZ3mQEL5K': ['articles'], 'var_call_nkfCKSPjPVepzwRsXkOjZ1eu': 'file_storage/call_nkfCKSPjPVepzwRsXkOjZ1eu.json', 'var_call_ZilkLbOMniGvP4nPIB65ty3f': [{'_id': '6959a971562a97b0f4822095', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a971562a97b0f4822096', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a971562a97b0f4822097', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a971562a97b0f4822098', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a971562a97b0f4822099', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
