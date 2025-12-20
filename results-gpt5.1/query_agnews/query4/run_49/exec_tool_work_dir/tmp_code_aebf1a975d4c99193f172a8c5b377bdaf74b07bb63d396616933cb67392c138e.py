code = """import json, pandas as pd
from collections import Counter

# Load full metadata
with open(var_call_D4rbVZO6sidEp9Yogif35xyL, 'r') as f:
    metadata = json.load(f)

articles = var_call_EG0mP651k5ezAQYNEdBjb9S2

# Build simple keyword-based classifier for World category
world_keywords = ['iraq','election','elections','war','terror','un','u.n.','president','government','prime minister','israel','palestinian','afghanistan','security council','diplomat','eu','european union','nato','summit']

world_ids = set()
for art in articles:
    text = (art.get('title','') + ' ' + art.get('description','')).lower()
    if any(kw in text for kw in world_keywords):
        world_ids.add(str(art['article_id']))

# Filter metadata for 2015 and world articles
counts = Counter()
for row in metadata:
    aid = str(row['article_id'])
    if not row['publication_date'].startswith('2015-'):
        continue
    if aid in world_ids:
        counts[row['region']] += 1

if counts:
    region_2015 = max(counts.items(), key=lambda x: x[1])[0]
else:
    region_2015 = None

import json as _json
result = _json.dumps(region_2015)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_EG0mP651k5ezAQYNEdBjb9S2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_D4rbVZO6sidEp9Yogif35xyL': 'file_storage/call_D4rbVZO6sidEp9Yogif35xyL.json'}

exec(code, env_args)
