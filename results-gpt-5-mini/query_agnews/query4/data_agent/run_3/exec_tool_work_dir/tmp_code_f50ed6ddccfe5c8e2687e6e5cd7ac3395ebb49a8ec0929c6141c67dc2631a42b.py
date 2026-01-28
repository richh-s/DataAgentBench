code = """import json
from collections import Counter

# Load data from previous query_db calls stored in provided file paths
# var_call_PlPpWltl1ivj6lTKeELRWpcB -> articles data (JSON list)
# var_call_4AW5CveX2r7QZmVtxjN40Tei -> metadata 2015 data (JSON list)

with open(var_call_PlPpWltl1ivj6lTKeELRWpcB, 'r') as f:
    articles = json.load(f)
with open(var_call_4AW5CveX2r7QZmVtxjN40Tei, 'r') as f:
    metadata_2015 = json.load(f)

# Build mapping from article_id to combined text
article_text = {}
for a in articles:
    aid = str(a.get('article_id'))
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid] = (title + ' ' + desc).lower()

# Define keyword sets for categories
sports_kw = [
    'match','goal','score','season','win','beat','defeat','draw','league',
    'cup','fifa','championship','tournament','olympic','olympics','nba','mlb',
    'nfl','goalkeeper','striker','midfielder','coach','manager','hat-trick',
    'penalty','injury','transfer','race','rally','grand prix','formula 1'
]

business_kw = [
    'stock','stocks','shares','market','ipo','earnings','profits','revenue',
    'investment','economy','trade deficit','dollar','bond','index','bank',
    'million','billion','merger','acquisition','revenue','profit','investor',
    'dow','nasdaq','reuters -','afp -','bloomberg'
]

tech_kw = [
    'technology','tech','computer','google','apple','microsoft','hp','ibm',
    'software','hardware','nasa','space','research','scientist','nuclear',
    'robot','ai ','artificial intelligence','ipad','iphone','android'
]

# Lowercase keywords
sports_kw = [k.lower() for k in sports_kw]
business_kw = [k.lower() for k in business_kw]
tech_kw = [k.lower() for k in tech_kw]

# Function to classify text
def classify(text):
    t = text.lower()
    # sports
    for k in sports_kw:
        if k in t:
            return 'Sports'
    # business
    for k in business_kw:
        if k in t:
            return 'Business'
    # tech / science
    for k in tech_kw:
        if k in t:
            return 'Science/Technology'
    # default
    return 'World'

# Count World articles by region for metadata entries
region_counts = Counter()
missing = 0
for m in metadata_2015:
    aid = str(m.get('article_id'))
    region = m.get('region')
    if aid in article_text:
        cat = classify(article_text[aid])
        if cat == 'World':
            region_counts[region] += 1
    else:
        missing += 1

# Determine top region
if region_counts:
    top_region, top_count = region_counts.most_common(1)[0]
else:
    top_region, top_count = None, 0

result = {
    'top_region': top_region,
    'top_count': top_count,
    'counts_by_region': dict(region_counts),
    'missing_metadata_article_texts': missing
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PlPpWltl1ivj6lTKeELRWpcB': 'file_storage/call_PlPpWltl1ivj6lTKeELRWpcB.json', 'var_call_4AW5CveX2r7QZmVtxjN40Tei': 'file_storage/call_4AW5CveX2r7QZmVtxjN40Tei.json'}

exec(code, env_args)
