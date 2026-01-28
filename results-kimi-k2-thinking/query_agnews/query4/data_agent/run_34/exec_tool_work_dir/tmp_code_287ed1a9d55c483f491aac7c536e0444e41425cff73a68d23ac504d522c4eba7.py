code = """import json
import pandas as pd
import re

# Load articles data
articles_data = locals()['var_functions.query_db:0']

# Load metadata data - it's a file path
metadata_file_path = locals()['var_functions.query_db:2']
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles_data)
df_metadata = pd.DataFrame(metadata_2015)

# Merge the DataFrames on article_id
df_merged = pd.merge(df_metadata, df_articles, on='article_id', how='inner')

# Convert publication_date to datetime
df_merged['publication_date'] = pd.to_datetime(df_merged['publication_date'])

# Ensure we're only looking at 2015 data (should already be filtered, but just in case)
df_2015 = df_merged[df_merged['publication_date'].dt.year == 2015]

# Define keywords for World category
world_keywords = [
    'world', 'global', 'international', 'nation', 'president', 'government', 
    'war', 'peace', 'conflict', 'treaty', 'diplomatic', 'foreign', 'policy',
    'united nations', 'un', 'european union', 'eu', 'nato', 'africa', 'asia',
    'europe', 'america', 'middle east', 'afghanistan', 'iraq', 'iran', 'north korea',
    'south korea', 'china', 'japan', 'russia', 'ukraine', 'syria', 'israel',
    'palestine', 'military', 'army', 'soldier', 'terror', 'terrorist', 'attack'
]

# Function to classify article category
def classify_category(title, description):
    text = f"{title} {description}".lower()
    
    # Check for World category keywords
    for keyword in world_keywords:
        if keyword in text:
            return 'World'
    
    # Check for Sports
    if any(word in text for word in ['sport', 'game', 'team', 'player', 'coach', 'league', 'tournament', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic']):
        return 'Sports'
    
    # Check for Business
    if any(word in text for word in ['business', 'economy', 'stock', 'market', 'company', 'corporation', 'profit', 'loss', 'revenue', 'wall st', 'wall street', 'finance', 'financial']):
        return 'Business'
    
    # Check for Science/Technology
    if any(word in text for word in ['science', 'technology', 'tech', 'research', 'study', 'scientist', 'computer', 'internet', 'software', 'hardware', 'digital', 'innovation']):
        return 'Science/Technology'
    
    # Default to World if uncertain (many news articles are world news)
    return 'World'

# Apply classification
df_2015['category'] = df_2015.apply(lambda row: classify_category(row['title'], row['description']), axis=1)

# Filter for World category articles
world_articles = df_2015[df_2015['category'] == 'World']

# Group by region and count
region_counts = world_articles.groupby('region').size().reset_index(name='article_count')

# Sort by count descending
region_counts_sorted = region_counts.sort_values('article_count', ascending=False)

# Find the region with the most articles
if not region_counts_sorted.empty:
    top_region = region_counts_sorted.iloc[0]
    result = {
        'region': top_region['region'],
        'article_count': int(top_region['article_count'])
    }
else:
    result = {'region': None, 'article_count': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969eb4faa75f1e99b0a7c8f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969eb4faa75f1e99b0a7c90', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969eb4faa75f1e99b0a7c91', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969eb4faa75f1e99b0a7c92', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969eb4faa75f1e99b0a7c93', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
