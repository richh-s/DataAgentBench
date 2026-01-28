code = """import json
import pandas as pd

# Load metadata (file path variable provided by previous query)
with open(var_call_MoBvMH9TpXa76DOQOubgLnuX, 'r') as f:
    meta = json.load(f)

articles = var_call_Ajmz7V20luIfGsMzpG3wu1Bw

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id types align
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge on article_id
df = df_meta.merge(df_articles, on='article_id', how='left')

# Classification keywords
world_kws = ['president','prime minister','government','election','killed','attack','bomb','protest','war','military','soldier','refugee','diplomat','united nations','un','gaza','israel','palestine','iraq','syria','russia','china','india','africa','europe','asia','north america','south america','britain','france','germany','uk','u.s.','us','u.k.','terror','ceasefire']
 sports_kws = ['match','beat','win','defeat','goal','league','season','cup','tournament','olympic','coach','scored','score','football','soccer','basketball','tennis','baseball','cricket','nba','nfl']
 business_kws = ['stock','stocks','market','economy','business','bank','oil','share','company','firm','investment','ipo','crude','wall st','reuters','forbes','bloomberg','economy']
 tech_kws = ['technology','scientist','research','nasa','space','software','device','internet','tech','scientists','study','computer','ai','robot']

import re

def score_text(text, kws):
    if not isinstance(text, str):
        return 0
    t = text.lower()
    s = 0
    for kw in kws:
        # count occurrences
        s += t.count(kw)
    return s

# Compute scores
texts = (df['title'].fillna('') + ' ' + df['description'].fillna('')).astype(str)
df['world_score'] = texts.apply(lambda x: score_text(x, world_kws))
df['sports_score'] = texts.apply(lambda x: score_text(x, sports_kws))
df['business_score'] = texts.apply(lambda x: score_text(x, business_kws))
df['tech_score'] = texts.apply(lambda x: score_text(x, tech_kws))

# Determine category by max score; tie-breaker priority: World, Sports, Business, Science/Technology
priority = ['World','Sports','Business','Science/Technology']

cats = []
for i,row in df.iterrows():
    scores = {'World': row['world_score'], 'Sports': row['sports_score'], 'Business': row['business_score'], 'Science/Technology': row['tech_score']}
    max_score = max(scores.values())
    if max_score == 0:
        # fallback: if title contains parentheses with news agency like (Reuters) and mentions country/region words, mark World
        txt = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
        if any(w in txt for w in ['(reuters)', 'reuters', 'afp', 'epa', 'country', 'minister', 'president']):
            cats.append('World')
        else:
            # default to Business if 'reuters' or 'wall' present else World
            if 'reuters' in txt or 'wall st' in txt or 'wall street' in txt:
                cats.append('Business')
            else:
                cats.append('World')
    else:
        # pick highest; if tie use priority
        top = [k for k,v in scores.items() if v==max_score]
        for p in priority:
            if p in top:
                cats.append(p)
                break

df['category'] = cats

# Filter for World in 2015 (df already from 2015 metadata)
df_world = df[df['category']=='World'].copy()

# Count by region
counts = df_world['region'].value_counts(dropna=True).to_dict()
if len(counts)==0:
    result = {'region': None, 'count': 0}
else:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c==max_count]
    if len(top_regions)==1:
        result = {'region': top_regions[0], 'count': max_count}
    else:
        result = {'regions': top_regions, 'count': max_count}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MoBvMH9TpXa76DOQOubgLnuX': 'file_storage/call_MoBvMH9TpXa76DOQOubgLnuX.json', 'var_call_Ajmz7V20luIfGsMzpG3wu1Bw': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
