code = """import json, pandas as pd, re
from collections import Counter

# Load full metadata from file
with open(var_call_UQiVmut6dNymku0jowBDhn9W, 'r') as f:
    meta = json.load(f)

articles = var_call_BNiipaMZWd5jOw2kOwqDz0UP

# Heuristic business classifier based on title+description keywords
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'nasdaq', 'dow', 's&p', 'ftse', 'dax', 'cac',
    'market', 'markets', 'share', 'shares', 'bond', 'bonds', 'treasury', 'treasuries',
    'oil', 'crude', 'gold', 'commodity', 'commodities',
    'economy', 'economic', 'gdp', 'inflation', 'deflation', 'recession', 'growth',
    'finance', 'financial', 'bank', 'banks', 'banking', 'loan', 'loans', 'credit', 'debt',
    'currency', 'currencies', 'euro', 'dollar', 'yen',
    'merger', 'acquisition', 'm&a', 'ipo', 'earnings', 'profit', 'profits', 'loss', 'losses',
    'revenue', 'revenues', 'turnover', 'dividend', 'dividends',
    'company', 'companies', 'corporate', 'business',
    'jobless', 'unemployment', 'employment', 'labor market',
]

sports_keywords = ['game','games','goal','goals','match','matches','tournament','league','cup','world cup','olympic','olympics','nfl','nba','mlb','nhl','soccer','football','basketball','baseball','tennis','golf','cricket','rugby','hockey','coach','player','team','teams']
science_keywords = ['space','nasa','galaxy','planet','planets','star','stars','astronomy','physics','chemical','chemistry','biology','biotech','genetic','genetics','researchers','scientists','laboratory','lab','experiment','experiments','technology','tech','software','hardware','internet','computer','computers','ai ','artificial intelligence','robot','robots','gadget','gadgets']
world_keywords = ['election','elections','government','president','prime minister','parliament','war','conflict','protest','protests','united nations','u.n.','un ','policy','policies','minister','ministers']

bk = [re.escape(k) for k in business_keywords]
sk = [re.escape(k) for k in sports_keywords]
sc = [re.escape(k) for k in science_keywords]
wk = [re.escape(k) for k in world_keywords]

b_re = re.compile(r'(' + '|'.join(bk) + r')', re.I)
s_re = re.compile(r'(' + '|'.join(sk) + r')', re.I)
sc_re = re.compile(r'(' + '|'.join(sc) + r')', re.I)
w_re = re.compile(r'(' + '|'.join(wk) + r')', re.I)

id_to_cat = {}
for a in articles:
    text = ((a.get('title') or '') + ' ' + (a.get('description') or '')).lower()
    scores = Counter()
    if b_re.search(text): scores['Business'] += 1
    if s_re.search(text): scores['Sports'] += 1
    if sc_re.search(text): scores['Science/Technology'] += 1
    if w_re.search(text): scores['World'] += 1
    if not scores:
        # default: World
        cat = 'World'
    else:
        cat = scores.most_common(1)[0][0]
    id_to_cat[int(a['article_id'])] = cat

# Build dataframe of European articles with years
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Filter to Business in Europe
meta_df['category'] = meta_df['article_id'].map(id_to_cat)
bus = meta_df[meta_df['category'] == 'Business']

per_year = bus.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)

avg = per_year.mean()

import math
avg_rounded = round(avg,2)

result = {"average_business_articles_per_year_europe_2010_2020": avg_rounded}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UQiVmut6dNymku0jowBDhn9W': 'file_storage/call_UQiVmut6dNymku0jowBDhn9W.json', 'var_call_BNiipaMZWd5jOw2kOwqDz0UP': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_q58FtgQf9kNUsPiyIX1q7arH': ['authors', 'article_metadata'], 'var_call_6zFnLFi6PMbCFrdMXWIsnGAi': ['articles']}

exec(code, env_args)
