code = """import json
import pandas as pd

# Load metadata (stored as a JSON file path) and articles (list of records)
with open(var_call_kOb0bIQHtjY9q01SphjnAcTY, 'r') as f:
    meta = json.load(f)
articles = var_call_k5zNKJNQVC7VrCXrLiv4Mj1Y

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id types are strings for merging
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata with article content
df = pd.merge(df_meta, df_articles[['article_id', 'title', 'description']], on='article_id', how='left')

# Classification keywords
sports = ['game', 'player', 'season', 'match', 'goal', 'scored', 'tournament', 'coach', 'football', 'soccer', 'basketball', 'baseball', 'olympic', 'fifa', 'nba', 'nhl']
business = ['stock', 'stocks', 'market', 'markets', 'economy', 'economies', 'finance', 'company', 'companies', 'business', 'firm', 'investment', 'ipo', 'shares', 'bank']
sci = ['technology', 'tech', 'scientist', 'research', 'nasa', 'space', 'scientists', 'study', 'scientific', 'computer', 'software', 'google', 'apple', 'microsoft', 'robot', 'ai', 'robotics', 'digital']

# Helper to classify a single article
import re

def classify(text):
    if not isinstance(text, str):
        text = ''
    txt = text.lower()
    # check sports
    for w in sports:
        if re.search(r'\b' + re.escape(w) + r'\b', txt):
            return 'Sports'
    # check business
    for w in business:
        if re.search(r'\b' + re.escape(w) + r'\b', txt):
            return 'Business'
    # check science/tech
    for w in sci:
        if re.search(r'\b' + re.escape(w) + r'\b', txt):
            return 'Science/Technology'
    # default to World
    return 'World'

# Apply classification using title + description
combined = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = combined.apply(classify)

# Filter for year 2015 (metadata was already filtered but ensure)
df['year'] = df['publication_date'].str.slice(0,4)
df_2015 = df[df['year'] == '2015'].copy()

# Count World articles per region
world_df = df_2015[df_2015['category'] == 'World']
counts = world_df['region'].value_counts().to_dict()
# Determine top region(s)
if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
    # If multiple, join by comma
    top_region = ', '.join(top_regions)
else:
    top_region = None

result = {'top_region': top_region, 'counts': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kOb0bIQHtjY9q01SphjnAcTY': 'file_storage/call_kOb0bIQHtjY9q01SphjnAcTY.json', 'var_call_k5zNKJNQVC7VrCXrLiv4Mj1Y': [{'_id': '6959a9a77d70c23d0e2dabd2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a9a77d70c23d0e2dabd3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a9a77d70c23d0e2dabd4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a9a77d70c23d0e2dabd5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a9a77d70c23d0e2dabd6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
