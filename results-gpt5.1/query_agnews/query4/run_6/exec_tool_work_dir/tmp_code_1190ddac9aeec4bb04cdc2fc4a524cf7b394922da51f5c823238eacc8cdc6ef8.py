code = """import json, pandas as pd

# Load full metadata result from file
with open(var_call_6ySKfY5FRPMd5wAmvXCyaAGJ, 'r') as f:
    meta = json.load(f)

articles = var_call_ZCvBqUBspztVGE7FSToOHSru

meta_df = pd.DataFrame(meta)
art_df = pd.DataFrame(articles)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Filter year 2015
meta_df['year'] = meta_df['publication_date'].str[:4].astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Simple heuristic classifier for World category
# We'll classify as Business if words like 'stock, oil, earn, profit, market, share, wall st, investors' appear
# Sports if words like 'game, team, season, coach, win, loss, football, soccer, basketball, baseball' appear
# Sci/Tech if words like 'research, study, scientists, technology, software, internet, computer, space, nasa' appear
# Otherwise World

business_kw = ['stock', 'stocks', 'wall st', 'wall street', 'oil', 'economy', 'economic', 'earnings', 'profit', 'profits', 'market', 'markets', 'investor', 'investors', 'trade', 'trading', 'fund', 'funds', 'bank', 'banks', 'shares']
sports_kw = ['game', 'games', 'team', 'teams', 'season', 'coach', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympics', 'olympic', 'tournament', 'league', 'mlb', 'nfl', 'nba', 'nhl']
scitech_kw = ['research', 'study', 'studies', 'scientist', 'scientists', 'technology', 'software', 'internet', 'computer', 'computers', 'space', 'nasa', 'science', 'sciences', 'tech', 'online']

def classify(row):
    text = (str(row['title']) + ' ' + str(row['description'])).lower()
    if any(k in text for k in sports_kw):
        return 'Sports'
    if any(k in text for k in scitech_kw):
        return 'Science/Technology'
    if any(k in text for k in business_kw):
        return 'Business'
    return 'World'

art_df['category'] = art_df.apply(classify, axis=1)

# Keep only World
world_df = art_df[art_df['category'] == 'World']

# Join with 2015 metadata
merged = pd.merge(meta_2015, world_df[['article_id']], on='article_id', how='inner')

# Count by region
counts = merged.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    answer = None
else:
    answer = counts.idxmax()

import json as _json
res = _json.dumps({'region_with_most_world_articles_2015': answer})
print("__RESULT__:")
print(res)"""

env_args = {'var_call_6ySKfY5FRPMd5wAmvXCyaAGJ': 'file_storage/call_6ySKfY5FRPMd5wAmvXCyaAGJ.json', 'var_call_ZCvBqUBspztVGE7FSToOHSru': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
