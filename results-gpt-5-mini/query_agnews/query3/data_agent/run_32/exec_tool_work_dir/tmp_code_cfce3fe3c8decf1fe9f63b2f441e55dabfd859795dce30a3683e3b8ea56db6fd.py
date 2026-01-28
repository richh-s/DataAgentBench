code = """import json
from collections import defaultdict
# Load metadata records (European articles 2010-01-01 to 2020-12-31)
meta_path = var_call_KdEPq9ih9xbeyXXRjzKp75qz
with open(meta_path, 'r') as f:
    meta_records = json.load(f)
# Load articles collection
arts_path = var_call_cY96RhSH6ioOscmGWNr0tzh0
with open(arts_path, 'r') as f:
    articles = json.load(f)
# Build article_id -> content map
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    art_map[aid] = (title, desc)
# Define business keywords
bk = [
    'business','economy','economic','economics','market','markets','stock','stocks','share','shares',
    'company','companies','bank','banks','finance','financial','investment','investor','ipo','merger',
    'acquisit','profit','loss','revenue','trade','trading','firm','corporate','commerce','retail','inflation',
    'interest rate','interest rates'
]
# classify and count per year
counts = {str(y): 0 for y in range(2010, 2021)}
for r in meta_records:
    try:
        aid = int(r.get('article_id'))
        pub = r.get('publication_date')
        year = int(pub[:4])
    except:
        continue
    if year < 2010 or year > 2020:
        continue
    content = ''
    if aid in art_map:
        title, desc = art_map[aid]
        content = (title + ' ' + desc).lower()
    else:
        # missing article content; skip classification
        continue
    is_business = False
    for kw in bk:
        if kw in content:
            is_business = True
            break
    if is_business:
        counts[str(year)] += 1
# compute average over 11 years
total = sum(counts.values())
avg = total / 11.0
output = {'counts_per_year': counts, 'total_business_articles': total, 'average_per_year': round(avg, 2)}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_7JiWDAT31e3Wk6vFOsyX4w2C': ['articles'], 'var_call_lScxeEEpq8xQx4Mbf73gwpIo': ['authors', 'article_metadata'], 'var_call_KdEPq9ih9xbeyXXRjzKp75qz': 'file_storage/call_KdEPq9ih9xbeyXXRjzKp75qz.json', 'var_call_WBUGmlbklopY2muc9d8kkVTO': 'file_storage/call_WBUGmlbklopY2muc9d8kkVTO.json', 'var_call_cY96RhSH6ioOscmGWNr0tzh0': 'file_storage/call_cY96RhSH6ioOscmGWNr0tzh0.json'}

exec(code, env_args)
