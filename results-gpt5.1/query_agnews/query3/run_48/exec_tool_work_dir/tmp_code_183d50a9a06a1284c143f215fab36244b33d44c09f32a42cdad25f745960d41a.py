code = """import json, pandas as pd
from collections import defaultdict

# Load Europe metadata from file path in var_call_tHGrmiZFTzk5WAVqFzadmC6v
with open(var_call_tHGrmiZFTzk5WAVqFzadmC6v, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_G4D5TSVthgxT0m02JbSv57Uv

# Convert to DataFrames
meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge on article_id to get titles/descriptions only for Europe+2010-2020
merged = meta_df.merge(articles_df, on='article_id', how='left')

# Simple keyword-based classifier into 4 categories
world_kw = ['world', 'country', 'countries', 'war', 'election', 'government', 'iraq', 'u.n.', 'united nations']
sports_kw = ['game', 'team', 'match', 'season', 'league', 'cup', 'championship', 'coach', 'player', 'nba', 'nfl', 'soccer', 'tennis', 'olympics']
business_kw = ['stock', 'stocks', 'wall st', 'market', 'markets', 'shares', 'investor', 'investors', 'company', 'companies', 'oil', 'economy', 'economic', 'earnings', 'deal', 'merger', 'bank', 'banks', 'trade', 'trading', 'corporate', 'business']
scitech_kw = ['science', 'scientist', 'research', 'study', 'technology', 'tech', 'space', 'nasa', 'computer', 'internet', 'software', 'hardware']

def classify(title, desc):
    text = f"{title} {desc}".lower()
    # Count matches by category
    scores = defaultdict(int)
    for w in world_kw:
        if w in text: scores['World'] += 1
    for w in sports_kw:
        if w in text: scores['Sports'] += 1
    for w in business_kw:
        if w in text: scores['Business'] += 1
    for w in scitech_kw:
        if w in text: scores['Science/Technology'] += 1
    if not scores:
        # default to World if nothing matches
        return 'World'
    # pick category with max score; tie-breaker by fixed order
    order = ['Business', 'World', 'Sports', 'Science/Technology']
    max_score = max(scores.values())
    candidates = [k for k,v in scores.items() if v == max_score]
    for cat in order:
        if cat in candidates:
            return cat
    return candidates[0]

merged['category'] = merged.apply(lambda r: classify(r.get('title', ''), r.get('description', '')), axis=1)

# Filter to Business
business = merged[merged['category'] == 'Business'].copy()

# Extract year
business['year'] = business['publication_date'].str.slice(0,4).astype(int)

# Count per year
counts = business.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

# Average over 2010-2020 inclusive (11 years)
avg = counts.mean()

result = round(float(avg), 2)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tHGrmiZFTzk5WAVqFzadmC6v': 'file_storage/call_tHGrmiZFTzk5WAVqFzadmC6v.json', 'var_call_G4D5TSVthgxT0m02JbSv57Uv': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
