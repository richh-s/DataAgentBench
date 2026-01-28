code = """import json
import pandas as pd

# Load metadata (large result stored in a JSON file path)
meta_path = var_call_8jhTkxYSdlW1Ghb90gocUotU
with open(meta_path, 'r') as f:
    meta = json.load(f)

articles = var_call_0hXdhO7mqQVNpI8zEfYHbf2S

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id are strings for joining
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata for 2015 with articles
# (meta already filtered in the query, but ensure publication_date startswith 2015-)
df_meta = df_meta[df_meta['publication_date'].str.startswith('2015-')]

df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Fill NaNs with empty strings
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Simple keyword-based classifier
sports_kw = ['score','season','match','goal','tournament','league','player','win','defeat','coach','olympic','fifa','nba','mlb','nhl','touchdown','penalty','striker','pitch','cup','final','draw','race','race','scored','inning']
business_kw = ['market','stocks','shares','economy','investment','firm','company','bank','business','merger','acquisition','billion','million','profit','loss','ipo','ceo','revenue']
scitech_kw = ['technology','scientist','research','nasa','space','software','ai','robot','tech','device','scientific','study','researchers','computer','internet','satellite']
world_kw = ['president','election','protest','conflict','war','attacked','bomb','killed','diplomat','government','minister','country','countries','united nations','refugee','peace','treaty','border','sanction','crisis','police','court','trial','accused']

import re

def classify(text):
    t = text.lower()
    # Check sports
    for kw in sports_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', t):
            return 'Sports'
    for kw in business_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', t):
            return 'Business'
    for kw in scitech_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', t):
            return 'Science/Technology'
    # If world-specific keywords present, mark World
    for kw in world_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', t):
            return 'World'
    # Default to World if no other category matched
    return 'World'

# Apply classifier
df['combined_text'] = (df['title'] + ' ' + df['description']).astype(str)
df['category'] = df['combined_text'].apply(classify)

# Filter World
df_world = df[df['category'] == 'World']

# Count by region
counts = df_world['region'].value_counts().to_dict()

if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'top_count': max_count,
    'counts': counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8jhTkxYSdlW1Ghb90gocUotU': 'file_storage/call_8jhTkxYSdlW1Ghb90gocUotU.json', 'var_call_0hXdhO7mqQVNpI8zEfYHbf2S': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
