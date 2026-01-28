code = """import json
import re

# Load data from the storage variable (file path)
file_path = var_call_DOq1Xu2e67egJjNURc97sEqn
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Helper: normalize text
def norm(s):
    return s.lower() if s else ''

# Keywords for categories
sports_keywords = [
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket',
    'rugby', 'hockey', 'nba', 'mlb', 'nhl', 'nfl', 'olympic', 'olympics', 'medal', 'coach',
    'player', 'players', 'match', 'season', 'scored', 'goal', 'goals', 'score', 'scores',
    'win', 'wins', 'defeat', 'defeated', 'tournament', 'cup', 'league', 'pitch', 'bat', 'run', 'runs'
]
science_keywords = [
    'scientist', 'research', 'researchers', 'technology', 'tech', 'computer', 'internet', 'software', 'ibm', 'google', 'nasa'
]
business_keywords = [
    'economy', 'economic', 'stocks', 'stock', 'market', 'markets', 'shares', 'investment', 'oil', 'business', 'bank', 'trade', 'company', 'firm', 'profit', 'profits'
]

# Classification function
def classify(rec):
    t = norm(rec.get('title', ''))
    d = norm(rec.get('description', ''))
    combined = t + ' ' + d
    # Sports first
    for kw in sports_keywords:
        if kw in combined:
            return 'Sports'
    for kw in science_keywords:
        if kw in combined:
            return 'Science/Technology'
    for kw in business_keywords:
        if kw in combined:
            return 'Business'
    return 'World'

# Process records
sports_records = []
for rec in records:
    # Ensure description exists
    desc = rec.get('description') or ''
    cat = classify(rec)
    if cat == 'Sports':
        sports_records.append({
            'article_id': rec.get('article_id'),
            'title': rec.get('title'),
            'description': desc,
            'desc_len': len(desc)
        })

# Find the sports article with the longest description
if not sports_records:
    result = None
else:
    sports_records.sort(key=lambda x: x['desc_len'], reverse=True)
    top = sports_records[0]
    result = top['title']

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DOq1Xu2e67egJjNURc97sEqn': 'file_storage/call_DOq1Xu2e67egJjNURc97sEqn.json'}

exec(code, env_args)
