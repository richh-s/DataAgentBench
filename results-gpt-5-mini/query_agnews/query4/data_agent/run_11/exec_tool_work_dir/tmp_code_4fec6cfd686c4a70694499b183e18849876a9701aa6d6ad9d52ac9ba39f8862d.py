code = """import json
import re

# Load data from stored JSON files
with open(var_call_BQWfRKVk77JJmyAnJEQEtxFQ, 'r', encoding='utf-8') as f:
    metadata = json.load(f)
with open(var_call_ytJ7w3JMKEzVYOuVUTxTqWIm, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Build article text map
article_text = {}
for a in articles:
    aid = str(a.get('article_id'))
    title = a.get('title') or ''
    desc = a.get('description') or ''
    combined = (title + ' ' + desc).lower()
    article_text[aid] = combined

# Keyword lists for simple rule-based classification
sports_kw = [
    'match', 'cup', 'goal', 'goals', 'league', 'season', 'score', 'scores', 'tournament', 'win', 'wins', 'defeat', 'defeated', 'draw', 'coach', 'coach', 'olympic', 'olympics', 'fifa', 'premier', 'world cup', 'nba', 'nfl', 'mlb', 'soccer', 'football', 'cricket', 'bat', 'innings', 'try', 'tries'
]
science_kw = [
    'scientist', 'research', 'study', 'researchers', 'experiment', 'lab', 'technology', 'tech', 'software', 'computer', 'nasa', 'space', 'scientific', 'drug', 'medical', 'disease', 'virus', 'genetic', 'ai ', 'artificial intelligence', 'robot', 'robotic'
]
business_kw = [
    'stock', 'stocks', 'market', 'shares', 'ipo', 'company', 'companies', 'firm', 'bank', 'banks', 'profit', 'loss', 'earnings', 'revenue', 'merger', 'acquisition', 'trade deficit', 'economy', 'economy', 'oil', 'oil prices', 'investment', 'financial', 'finance', 'bond', 'currency'
]

# Lowercase keywords
sports_kw = [k.lower() for k in sports_kw]
science_kw = [k.lower() for k in science_kw]
business_kw = [k.lower() for k in business_kw]

# Classification function: priority Sports -> Science/Tech -> Business -> World

def classify(text):
    if not text:
        return 'World'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    return 'World'

# Count world articles per region
from collections import Counter
region_counts = Counter()
missing_articles = 0
for m in metadata:
    aid = str(m.get('article_id'))
    region = m.get('region')
    text = article_text.get(aid)
    if text is None:
        missing_articles += 1
        continue
    cat = classify(text)
    if cat == 'World':
        region_counts[region] += 1

# Determine top region(s)
if region_counts:
    max_count = max(region_counts.values())
    top_regions = sorted([r for r,c in region_counts.items() if c == max_count])
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'top_count': max_count,
    'counts': dict(region_counts),
    'missing_articles': missing_articles
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BQWfRKVk77JJmyAnJEQEtxFQ': 'file_storage/call_BQWfRKVk77JJmyAnJEQEtxFQ.json', 'var_call_ytJ7w3JMKEzVYOuVUTxTqWIm': 'file_storage/call_ytJ7w3JMKEzVYOuVUTxTqWIm.json'}

exec(code, env_args)
