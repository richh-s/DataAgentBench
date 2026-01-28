code = """import json
from pathlib import Path
# Load metadata (large file path)
meta_path = var_call_4k9wroUinQQ9xAhohQ3PeNhb
with open(meta_path, 'r') as f:
    meta = json.load(f)
# Load articles list
articles = var_call_o5TyGtwy2HeeHTpvgnwlrcxu
# Normalize types and build dict for fast lookup
meta_records = []
for item in meta:
    try:
        aid = int(item['article_id'])
    except:
        continue
    pub = item.get('publication_date')
    meta_records.append({'article_id': aid, 'publication_date': pub})

articles_by_id = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    articles_by_id[aid] = {'title': a.get('title','') or '', 'description': a.get('description','') or ''}

# Merge: keep only those metadata entries which have article content available
merged = []
for m in meta_records:
    aid = m['article_id']
    if aid in articles_by_id:
        rec = {'article_id': aid, 'publication_date': m['publication_date'], 'title': articles_by_id[aid]['title'], 'description': articles_by_id[aid]['description']}
        merged.append(rec)

# Define business keywords
kw = [
    'market','markets','stock','stocks','economy','economic','business','firm','company','companies',
    'investment','investments','investor','investors','bank','banks','shares','revenue','profit','loss',
    'ipo','merger','acquisition','acquires','oil prices','oil price','wall st','wall street','private','aerospace',
    'trade','trading','bourse','financial','finance','financially','inflation','deflation','interest rate','interest rates'
]

import re
pattern = re.compile('|'.join(re.escape(x) for x in kw), re.IGNORECASE)

# Count Business articles per year 2010-2020
counts = {str(y): 0 for y in range(2010, 2021)}
for r in merged:
    pub = r.get('publication_date')
    if not pub or len(pub) < 4:
        continue
    year = int(pub[:4])
    if year < 2010 or year > 2020:
        continue
    text = (r.get('title','') + ' ' + r.get('description',''))
    if pattern.search(text):
        counts[str(year)] += 1

# Compute average over the 11 years
total = sum(counts.values())
num_years = 2020 - 2010 + 1
average = total / num_years if num_years else None

result = {'counts_per_year': counts, 'total_business_articles': total, 'years': num_years, 'average_per_year': average}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4k9wroUinQQ9xAhohQ3PeNhb': 'file_storage/call_4k9wroUinQQ9xAhohQ3PeNhb.json', 'var_call_nCNfbEqe6bSlq2hXLdJLejOU': 'file_storage/call_nCNfbEqe6bSlq2hXLdJLejOU.json', 'var_call_o5TyGtwy2HeeHTpvgnwlrcxu': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
