code = """import json
import pandas as pd

# Load results from previous tool calls
# var_call_DFX1BxGWIt4XkrrNELEWf776 is a file path to the metadata JSON
metadata_path = var_call_DFX1BxGWIt4XkrrNELEWf776
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# var_call_lPcgEIF325BU3H7mwjckN5V5 is the articles list
articles = var_call_lPcgEIF325BU3H7mwjckN5V5

# Create DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id types align (strings)
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge on article_id
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Define keyword sets for categories
world_kw = ['president', 'prime minister', 'election', 'elected', 'government', 'minister', 'killed', 'attack', 'terror', 'conflict', 'war', 'military', 'diplomat', 'refugee', 'sanction', 'united nations', 'un ', 'iraq', 'syria', 'afghanistan', 'border', 'protest', 'protests', 'russia', 'china', 'ukraine', 'police']
sports_kw = ['match', 'season', 'goal', 'score', 'scored', 'defeat', 'beat', 'won', 'wins', 'tournament', 'league', 'cup', 'world cup', 'olympic', 'coach', 'coach', 'player', 'players']
business_kw = ['market', 'stocks', 'shares', 'oil', 'economy', 'business', 'company', 'companies', 'revenue', 'earnings', 'investment', 'investors', 'bank', 'merger', 'acquisition', 'firm', 'firm', 'carlyle']
sci_kw = ['scientist', 'research', 'technology', 'tech', 'nasa', 'study', 'scientists', 'space', 'discovery', 'scientific', 'software', 'internet']

# Function to classify
import re

def score_text(text, keywords):
    if not isinstance(text, str):
        return 0
    text = text.lower()
    score = 0
    for kw in keywords:
        # count occurrences
        score += text.count(kw)
    return score

categories = []
for _, row in df.iterrows():
    text = ''
    if pd.notna(row.get('title')):
        text += row['title'] + ' '
    if pd.notna(row.get('description')):
        text += row['description']
    s_world = score_text(text, world_kw)
    s_sports = score_text(text, sports_kw)
    s_business = score_text(text, business_kw)
    s_sci = score_text(text, sci_kw)
    scores = {'World': s_world, 'Sports': s_sports, 'Business': s_business, 'Science/Technology': s_sci}
    # pick category with highest score; if tie or all zero, prefer World, then Business, then Sports, then Science/Technology
    max_score = max(scores.values())
    if max_score == 0:
        cat = 'World'
    else:
        # get categories with max score
        winners = [k for k, v in scores.items() if v == max_score]
        if len(winners) == 1:
            cat = winners[0]
        else:
            # tie-breaker order
            for pref in ['World', 'Business', 'Sports', 'Science/Technology']:
                if pref in winners:
                    cat = pref
                    break
    categories.append(cat)

df['category'] = categories

# Filter only 2015 entries (they already are) and category == 'World'
df_2015_world = df[df['category'] == 'World']

# Count by region
counts = df_2015_world['region'].value_counts().to_dict()

# Determine top region
if counts:
    top_region = max(counts.items(), key=lambda x: (x[1], x[0]))[0]
    top_count = counts[top_region]
else:
    top_region = None
    top_count = 0

result = {'top_region': top_region, 'count': int(top_count), 'counts_by_region': counts}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DFX1BxGWIt4XkrrNELEWf776': 'file_storage/call_DFX1BxGWIt4XkrrNELEWf776.json', 'var_call_lPcgEIF325BU3H7mwjckN5V5': [{'_id': '6959aa4321e0c9d9a6b14066', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959aa4321e0c9d9a6b14067', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959aa4321e0c9d9a6b14068', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959aa4321e0c9d9a6b14069', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959aa4321e0c9d9a6b1406a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
