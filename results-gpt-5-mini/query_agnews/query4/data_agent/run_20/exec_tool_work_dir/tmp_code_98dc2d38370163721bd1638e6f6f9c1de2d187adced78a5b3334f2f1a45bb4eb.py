code = """import json
import pandas as pd

# Load metadata from the JSON file path provided in var_call_f6xJBzSJhOHxJM42g4hHBKdo
metadata_path = var_call_f6xJBzSJhOHxJM42g4hHBKdo
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# Load articles from the in-memory variable
articles = var_call_NKGYQ0mYfFmQV2bgYDdzA6j8

# Create DataFrames
md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

# Ensure article_id are strings for join
md['article_id'] = md['article_id'].astype(str)
art['article_id'] = art['article_id'].astype(str)

# Merge metadata for 2015 with articles
md_2015 = md[md['publication_date'].str.startswith('2015-')].copy()
merged = md_2015.merge(art, on='article_id', how='left')

# Fill NaNs
merged['title'] = merged['title'].fillna('')
merged['description'] = merged['description'].fillna('')

# Define keyword lists
sports_kw = ['match','goal','tournament','season','coach','score','win','defeat','olympic','world cup','football','soccer','nba','nfl','mlb','cricket','tennis','golf','league','cup','bat','innings','home run']
business_kw = ['stock','market','economy','economies','invest','investment','bank','commercial','shares','bonds','ipo','earnings','finance','wall st','carlyle','oil prices','oil price','oil prices soar','company','companies','merger','acquisition']
sci_kw = ['science','technology','tech','scientist','research','nasa','space','study','scientific','robot','ai','artificial intelligence','software','internet','gadget','startup','biotech','dna','gene','lab','experiment']

# Classification function
import re

def classify_text(text):
    t = text.lower()
    # Sports
    for kw in sports_kw:
        if kw in t:
            return 'Sports'
    # Business
    for kw in business_kw:
        if kw in t:
            return 'Business'
    # Science/Technology
    for kw in sci_kw:
        if kw in t:
            return 'Science/Technology'
    # Default to World
    return 'World'

# Apply classification
merged['combined'] = merged['title'] + ' ' + merged['description']
merged['category'] = merged['combined'].apply(classify_text)

# Count World articles by region
world_by_region = merged[merged['category'] == 'World'].groupby('region').size().reset_index(name='count')

if world_by_region.empty:
    result = {'regions': [], 'count': 0}
else:
    max_count = int(world_by_region['count'].max())
    top_regions = world_by_region[world_by_region['count'] == max_count]['region'].tolist()
    result = {'regions': top_regions, 'count': max_count}

# Print result in required format as JSON string
print("----BEGIN PRINT FORMAT----")
print('__RESULT__:')
print(json.dumps(result))
print("----END PRINT FORMAT----")"""

env_args = {'var_call_f6xJBzSJhOHxJM42g4hHBKdo': 'file_storage/call_f6xJBzSJhOHxJM42g4hHBKdo.json', 'var_call_NKGYQ0mYfFmQV2bgYDdzA6j8': [{'_id': '6959a6bf74ce4eecfe44d653', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a6bf74ce4eecfe44d654', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a6bf74ce4eecfe44d655', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a6bf74ce4eecfe44d656', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a6bf74ce4eecfe44d657', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
