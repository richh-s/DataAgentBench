code = """import json
import pandas as pd

# Load the Mongo query result from storage
path = var_call_nAjioQjyVIhk1OOtDTsRK3mw
with open(path, 'r') as f:
    articles = json.load(f)

# Load the list of article_ids for Amy Jones
amy_articles = var_call_GT0bjKW6ELkXaCzgT8dtiiSC
amy_article_ids = [int(r['article_id']) for r in amy_articles]

# Create DataFrame
df = pd.DataFrame(articles)
# ensure article_id numeric
df['article_id'] = df['article_id'].astype(int)

# Filter to Amy's articles (in case Mongo returned only subset)
df_amy = df[df['article_id'].isin(amy_article_ids)].copy()

# Simple keyword-based classifier for categories based on title+description
# Categories: World, Sports, Business, Science/Technology
import re

def classify(text):
    t = (text or '').lower()
    # Science/Technology keywords
    sci_keywords = ['science', 'scientist', 'research', 'technology', 'tech', 'nasa', 'space', 'intel', 'microsoft', 'computer', 'engineering', 'lab', 'physics', 'chemistry']
    sports_keywords = ['game', 'olympic', 'olympics', 'score', 'win', 'defeat', 'tournament', 'season', 'coach', 'goal', 'match', 'u.s. open', 'capriati', 'serena', 'championship']
    business_keywords = ['company', 'profit', 'profits', 'revenue', 'stock', 'stocks', 'market', 'trading', 'trade', 'wto', 'economy', 'earnings', 'microsoft', 'intel', 'bhp']
    world_keywords = ['president', 'prime minister', 'country', 'city', 'election', 'militant', 'gaza', 'iraq', 'nepal', 'israeli', 'somalia', 'belgian', 'france', 'geneva']

    # count matches
    scores = {'Science/Technology':0, 'Sports':0, 'Business':0, 'World':0}
    for kw in sci_keywords:
        if kw in t:
            scores['Science/Technology'] += 1
    for kw in sports_keywords:
        if kw in t:
            scores['Sports'] += 1
    for kw in business_keywords:
        if kw in t:
            scores['Business'] += 1
    for kw in world_keywords:
        if kw in t:
            scores['World'] += 1
    # special handling: if 'space', 'nasa', 'science' strong indicator of Science/Technology
    # if tie, pick highest by predefined priority Science/Technology > Sports > Business > World
    max_score = max(scores.values())
    if max_score == 0:
        return 'World'  # default
    # get categories with max score
    best = [k for k,v in scores.items() if v==max_score]
    priority = ['Science/Technology','Sports','Business','World']
    for p in priority:
        if p in best:
            return p

# Apply classification to Amy's articles
cats = []
for _, row in df_amy.iterrows():
    text = (row.get('title','') or '') + ' ' + (row.get('description','') or '')
    c = classify(text)
    cats.append({'article_id': row['article_id'], 'title': row.get('title',''), 'category': c})

cats_df = pd.DataFrame(cats)

# Compute fraction belonging to Science/Technology
total = len(amy_article_ids)
# Note: some of Amy's article_ids might not be present in the Mongo result; use total based on ids from metadata
sci_count = (cats_df['category']=='Science/Technology').sum()

fraction = sci_count / total if total>0 else 0

result = {'total_articles_by_amy': total, 'science_tech_articles': int(sci_count), 'fraction': fraction}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BNRz5jphbab2OC2uYVOcJIt9': [{'author_id': '218'}], 'var_call_GT0bjKW6ELkXaCzgT8dtiiSC': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_nAjioQjyVIhk1OOtDTsRK3mw': 'file_storage/call_nAjioQjyVIhk1OOtDTsRK3mw.json'}

exec(code, env_args)
