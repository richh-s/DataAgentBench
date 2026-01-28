code = """import json
# Load the list of 2015 article IDs from previous query (path provided in var_call_u8cYs7K5Y5wAqEYYHbIgvLcL)
path_ids = var_call_u8cYs7K5Y5wAqEYYHbIgvLcL
with open(path_ids, 'r') as f:
    ids = json.load(f)
# Load the full articles data (path in var_call_y2B9a3m5T1vFFOtAuW2YmZFZ)
path_articles = var_call_y2B9a3m5T1vFFOtAuW2YmZFZ
with open(path_articles, 'r') as f:
    articles = json.load(f)
# Build mapping from int article_id to article record
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    article_map[aid] = a
# We'll also need the metadata records from the first query to get region per article
# The original metadata query result file path is var_call_kO1HUmuJfOqZvh05wh4xaIAu
path_meta = var_call_kO1HUmuJfOqZvh05wh4xaIAu
with open(path_meta, 'r') as f:
    meta = json.load(f)
# Build mapping article_id -> region for 2015 articles
region_map = {int(m['article_id']): m['region'] for m in meta}

# Define keyword lists
sports_kw = ['game','match','season','football','soccer','basketball','nba','mlb','world cup','tournament','scored','defeated','beat','loses','win','wins','goal','innings','coach','coach','olympic','olympics','rugby','tennis','golf','fired','score','cup']
business_kw = ['market','stocks','investment','economy','trade','company','shares','profit','bank','ipo','merger','acquisition','business','firm','dollar','oil prices','stock','economy','investor','investors','reuters','bloomberg']
tech_kw = ['technology','scientist','research','nasa','space','scientists','experiment','tech','software','internet','google','microsoft','apple','iphone','android','robot','nuclear','phone','device','samsung','ai','robotics']

# Classify function
import re

def contains_kw(text, kwlist):
    text_l = text.lower()
    for kw in kwlist:
        if kw in text_l:
            return True
    return False

# Count world category per region
from collections import Counter
world_counts = Counter()
processed = 0
not_found = 0
for aid in ids:
    aid = int(aid)
    region = region_map.get(aid)
    if region is None:
        continue
    art = article_map.get(aid)
    if not art:
        not_found += 1
        continue
    title = art.get('title','') or ''
    desc = art.get('description','') or ''
    text = title + ' ' + desc
    # classification priority: sports, business, tech, else world
    if contains_kw(text, sports_kw):
        cat = 'Sports'
    elif contains_kw(text, business_kw):
        cat = 'Business'
    elif contains_kw(text, tech_kw):
        cat = 'Science/Technology'
    else:
        cat = 'World'
    if cat == 'World':
        world_counts[region] += 1
    processed += 1

# Determine region with max count
if world_counts:
    max_region, max_count = world_counts.most_common(1)[0]
else:
    max_region, max_count = None, 0

result = {'region': max_region, 'count': max_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kO1HUmuJfOqZvh05wh4xaIAu': 'file_storage/call_kO1HUmuJfOqZvh05wh4xaIAu.json', 'var_call_u8cYs7K5Y5wAqEYYHbIgvLcL': 'file_storage/call_u8cYs7K5Y5wAqEYYHbIgvLcL.json', 'var_call_y2B9a3m5T1vFFOtAuW2YmZFZ': 'file_storage/call_y2B9a3m5T1vFFOtAuW2YmZFZ.json'}

exec(code, env_args)
