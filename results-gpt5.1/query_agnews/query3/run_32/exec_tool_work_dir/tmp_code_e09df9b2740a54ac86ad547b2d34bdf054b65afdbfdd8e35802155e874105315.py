code = """import json, pandas as pd
from collections import Counter

# Load full Europe metadata
path_meta = var_call_XPtFy8JBNBt4rYEIj2q1RKCx
with open(path_meta, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_GcNTfpnXsuqFubRBoulBssu1

# Build lookup for article text
df_articles = pd.DataFrame(articles)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge Europe subset with article texts
df_meta = pd.DataFrame(europe_meta)
df_meta['article_id'] = df_meta['article_id'].astype(int)

merged = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Simple keyword-based classifier into 4 categories
business_keywords = ['stock', 'stocks', 'market', 'markets', 'economy', 'economic', 'bank', 'banks', 'finance', 'financial', 'business', 'investor', 'investors', 'investment', 'investments', 'company', 'companies', 'corporate', 'wall st', 'wall street', 'oil', 'trade', 'trading', 'revenue', 'profit', 'profits', 'loss', 'shares']
sports_keywords = ['game', 'match', 'tournament', 'league', 'cup', 'olympic', 'olympics', 'football', 'soccer', 'basketball', 'tennis', 'cricket', 'baseball', 'golf', 'hockey', 'athletics', 'coach', 'team', 'teams', 'player', 'players', 'score', 'scored']
science_keywords = ['science', 'scientist', 'research', 'study', 'studies', 'technology', 'tech', 'space', 'nasa', 'quantum', 'physics', 'biology', 'medical', 'medicine', 'health', 'innovation', 'lab', 'laboratory']

business_kw = set(business_keywords)
sports_kw = set(sports_keywords)
science_kw = set(science_keywords)

import re

def classify(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    words = set(re.findall(r"[a-zA-Z']+", text))
    scores = {'Business': 0, 'Sports': 0, 'Science/Technology': 0, 'World': 0}
    for w in words:
        if w in business_kw:
            scores['Business'] += 1
        if w in sports_kw:
            scores['Sports'] += 1
        if w in science_kw:
            scores['Science/Technology'] += 1
    # default World if all zero
    if all(v == 0 for v in scores.values()):
        return 'World'
    # tie-breaker: choose max, if tie prefer non-World by order
    max_score = max(scores.values())
    best = [k for k,v in scores.items() if v==max_score]
    for cat in ['Business','Sports','Science/Technology','World']:
        if cat in best:
            return cat

merged['category'] = merged.apply(classify, axis=1)

# Filter to Business
business = merged[merged['category']=='Business'].copy()

# Extract year
business['year'] = business['publication_date'].str.slice(0,4).astype(int)

# Count by year 2010-2020
counts = business.groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = counts.mean()

result = {'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_by_year': counts.to_dict()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XPtFy8JBNBt4rYEIj2q1RKCx': 'file_storage/call_XPtFy8JBNBt4rYEIj2q1RKCx.json', 'var_call_GcNTfpnXsuqFubRBoulBssu1': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
