code = """import json
import pandas as pd

# Load the metadata results (may be a filepath or list)
meta_var = var_call_VimaS0jtldlL8gynh1PX6fEj
if isinstance(meta_var, str):
    with open(meta_var, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_var

# Load the articles results (already a list)
articles = var_call_UwBVouVdIW9YPI1Kw38f9iD0

# Convert to DataFrame
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id types are strings for merge
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Simple keyword-based classifier
import re

def classify(text):
    if not isinstance(text, str):
        text = ''
    t = text.lower()
    # sports keywords
    sports = ['match','season','goal','football','soccer','score','cup','tournament','player','coach','win','wins','beat','defeat','defeated','olympic','nba','mlb','nhl','fifa','league','race','tackle','pitch']
    business = ['stock','stocks','market','oil','economy','economics','shares','company','firm','investment','investor','bank','financial','merger','acquisition','ipo','reuters -','bloomberg','dow','nasdaq']
    science = ['scientist','research','study','space','nasa','technology','technolog','software','computer','internet','science','researchers','robot','ai','artificial intelligence']
    world = ['president','election','minister','war','attack','clash','refugee','diplomat','united nations','un ','u.n.','government','parliament','killed','police','soldier','protest','border','crisis','country','countries','syria','iraq','china','russia','europe','africa','asia','north america','south america']

    for kw in sports:
        if kw in t:
            return 'Sports'
    for kw in business:
        if kw in t:
            return 'Business'
    for kw in science:
        if kw in t:
            return 'Science/Technology'
    for kw in world:
        if kw in t:
            return 'World'
    # default to World if nothing matches (broad category)
    return 'World'

# Apply classifier to merged text
combined = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = combined.apply(classify)

# Filter to World category
df_world = df[df['category'] == 'World']

# Count by region
counts = df_world['region'].fillna('Unknown').value_counts().to_dict()

# Determine top region
if counts:
    top_region = max(counts.items(), key=lambda x: x[1])[0]
    top_count = counts[top_region]
else:
    top_region = None
    top_count = 0

result = {'top_region': top_region, 'count': int(top_count), 'counts_by_region': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VimaS0jtldlL8gynh1PX6fEj': 'file_storage/call_VimaS0jtldlL8gynh1PX6fEj.json', 'var_call_UwBVouVdIW9YPI1Kw38f9iD0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
