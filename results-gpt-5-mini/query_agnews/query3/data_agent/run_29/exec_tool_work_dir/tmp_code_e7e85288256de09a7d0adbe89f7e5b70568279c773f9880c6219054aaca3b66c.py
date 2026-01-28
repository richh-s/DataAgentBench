code = """import json
from collections import defaultdict

# Load metadata (Europe articles filtered earlier)
meta_path = var_call_GyTzqACDcvIV3zGDKVIrK555
with open(meta_path, 'r') as f:
    meta = json.load(f)

# Load all articles data
arts_path = var_call_mr0jtZcgneDfrU1klGa0DLhU
with open(arts_path, 'r') as f:
    arts = json.load(f)

# Build mapping article_id -> title+description
art_map = {}
for a in arts:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    art_map[aid] = (title + ' ' + desc).lower()

# Keywords for business classification
business_keywords = [
    'econom', 'economy', 'stock', 'stocks', 'market', 'markets', 'bank', 'banks', 'dollar', 'euro',
    'finance', 'financial', 'investment', 'investor', 'investors', 'ipo', 'merger', 'acquir', 'buyout',
    'profit', 'profits', 'revenue', 'earnings', 'shares', 'share', 'oil prices', 'oil export', 'oil exports',
    'trade', 'commerce', 'commercial', 'industry', 'business', 'company', 'companies', 'corporate'
]

# Years range
years = list(range(2010, 2021))
counts = {str(y): 0 for y in years}

# Process metadata records
for r in meta:
    aid_raw = r.get('article_id')
    try:
        aid = int(aid_raw)
    except:
        try:
            aid = int(str(aid_raw).strip())
        except:
            continue
    pub = r.get('publication_date','')
    if not pub or len(pub) < 4:
        continue
    try:
        year = int(pub[:4])
    except:
        continue
    if year < 2010 or year > 2020:
        continue
    text = art_map.get(aid, '').lower()
    # If no text, skip classification
    if not text:
        continue
    is_business = False
    for kw in business_keywords:
        if kw in text:
            is_business = True
            break
    if is_business:
        counts[str(year)] += 1

# Compute average over the 11 years
total = sum(counts[str(y)] for y in years)
num_years = len(years)
avg = total / num_years if num_years else 0.0

result = {
    'counts_by_year': counts,
    'total_business_articles_2010_2020': total,
    'number_of_years': num_years,
    'average_business_articles_per_year': round(avg, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GyTzqACDcvIV3zGDKVIrK555': 'file_storage/call_GyTzqACDcvIV3zGDKVIrK555.json', 'var_call_tGVA907GjKRDbTQyKyeuKl9d': 'file_storage/call_tGVA907GjKRDbTQyKyeuKl9d.json', 'var_call_AMORTeqymlFqLxH1Ab3UUCoF': 'file_storage/call_AMORTeqymlFqLxH1Ab3UUCoF.json', 'var_call_mr0jtZcgneDfrU1klGa0DLhU': 'file_storage/call_mr0jtZcgneDfrU1klGa0DLhU.json'}

exec(code, env_args)
