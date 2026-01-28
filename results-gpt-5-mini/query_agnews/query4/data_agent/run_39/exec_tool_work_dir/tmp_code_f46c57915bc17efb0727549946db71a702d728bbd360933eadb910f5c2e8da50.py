code = """import json
import pandas as pd

# Load metadata result from file path variable
path = var_call_tLQkzDMv3d6LeAcraaMdwzah
with open(path, 'r') as f:
    metadata_records = json.load(f)

articles_records = var_call_GvJOuhsauIvk4a7BpZc5aNlc

md = pd.DataFrame(metadata_records)
art = pd.DataFrame(articles_records)

# Ensure article_id types are consistent strings
md['article_id'] = md['article_id'].astype(str)
art['article_id'] = art['article_id'].astype(str)

# Merge metadata (2015) with articles
df = pd.merge(md, art, on='article_id', how='left')

# Prepare keyword lists for category classification
sports_kw = ['match','cup','league','goal','scored','penalty','season','tournament','win','won','defeat','coach','player','quarterback','football','soccer','basketball','tennis','olympic','olympics','fifa','nba','mlb','rugby','cricket','score','innings','goalkeeper']
business_kw = ['market','markets','stock','stocks','share','shares','economy','business','invest','investment','wall st','wall-st','profit','revenue','earnings','bank','financial','billion','million','ipo','merger','acquisition','commerce','trade']
science_kw = ['technology','tech','scientist','research','nasa','space','scientists','computer','internet','software','hardware','ai','artificial intelligence','robot','robotics','smartphone','drug','vaccine','study','research','scientific','science','biotech']

# Function to classify category
import re

def contains_any(text, keywords):
    if not isinstance(text, str):
        return False
    t = text.lower()
    for kw in keywords:
        if kw in t:
            return True
    return False

def classify_row(row):
    text = ''
    if isinstance(row.get('title'), str):
        text += row['title'] + ' '
    if isinstance(row.get('description'), str):
        text += row['description']
    # Priority: Sports -> Science/Tech -> Business -> World (default)
    if contains_any(text, sports_kw):
        return 'Sports'
    if contains_any(text, science_kw):
        return 'Science/Technology'
    if contains_any(text, business_kw):
        return 'Business'
    # Otherwise, classify as World
    return 'World'

# Classify all rows
df['category'] = df.apply(classify_row, axis=1)

# Filter to World category
world_df = df[df['category'] == 'World']

# Count by region
counts = world_df.groupby('region').size().reset_index(name='count')
if counts.empty:
    result_region = None
    result_count = 0
else:
    counts_sorted = counts.sort_values(by='count', ascending=False)
    top = counts_sorted.iloc[0]
    result_region = top['region']
    result_count = int(top['count'])

# Print result in required format
print("__RESULT__:")
print(json.dumps({"region": result_region, "count": result_count}))"""

env_args = {'var_call_tLQkzDMv3d6LeAcraaMdwzah': 'file_storage/call_tLQkzDMv3d6LeAcraaMdwzah.json', 'var_call_GvJOuhsauIvk4a7BpZc5aNlc': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
