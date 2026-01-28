code = """import json
from collections import defaultdict

# Load metadata records
m = var_call_0DRPXBYbhRuzxDy2ieFdONjy
if isinstance(m, str) and m.endswith('.json'):
    with open(m, 'r') as f:
        metadata = json.load(f)
else:
    metadata = m
# Build id -> year mapping
id_to_year = {}
for r in metadata:
    try:
        aid = int(r['article_id'])
    except:
        aid = int(r['article_id'])
    pub = r.get('publication_date')
    year = int(pub[:4]) if pub and len(pub) >= 4 else None
    id_to_year[aid] = year

# Load articles collection
a = var_call_wlT7mKOtb310biE3wHfIjZEt
if isinstance(a, str) and a.endswith('.json'):
    with open(a, 'r') as f:
        articles = json.load(f)
else:
    articles = a

# Convert articles list to dict by article_id
articles_by_id = {}
for art in articles:
    try:
        aid = int(art.get('article_id'))
    except:
        aid = int(art['article_id'])
    title = art.get('title','') or ''
    desc = art.get('description','') or ''
    articles_by_id[aid] = {'title': title, 'description': desc}

# Define business keywords
biz_keywords = [
    'econom', 'market', 'stock', 'stocks', 'share', 'shares', 'ipo', 'earnings', 'profit', 'profits',
    'company', 'companies', 'business', 'bank', 'banks', 'investment', 'investor', 'investors', 'revenue',
    'merger', 'acquisition', 'acquisitions', 'trade', 'oil prices', 'oil price', 'oil', 'unemployment', 'inflation',
    'dow', 'nasdaq', 'ftse', 'eurozone', 'euro', 'dollar', 'bond', 'bonds', 'tax', 'taxes'
]

# Count business articles per year among metadata (Europe, 2010-2020)
counts = defaultdict(int)
for aid, year in id_to_year.items():
    if year is None:
        continue
    if 2010 <= year <= 2020:
        art = articles_by_id.get(aid)
        if not art:
            continue
        text = (art['title'] + ' ' + art['description']).lower()
        is_biz = False
        for kw in biz_keywords:
            if kw in text:
                is_biz = True
                break
        if is_biz:
            counts[year] += 1

# Ensure all years present
years = list(range(2010, 2021))
per_year = {str(y): counts.get(y, 0) for y in years}
total = sum(per_year.values())
avg = total / len(years) if len(years) > 0 else 0

result = {'per_year': per_year, 'total_business_articles': total, 'average_per_year': avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0DRPXBYbhRuzxDy2ieFdONjy': 'file_storage/call_0DRPXBYbhRuzxDy2ieFdONjy.json', 'var_call_e2xOTmHXWvOvvDUYyk9kRdta': 'file_storage/call_e2xOTmHXWvOvvDUYyk9kRdta.json', 'var_call_wlT7mKOtb310biE3wHfIjZEt': 'file_storage/call_wlT7mKOtb310biE3wHfIjZEt.json'}

exec(code, env_args)
