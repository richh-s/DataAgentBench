code = """import json, pandas as pd
path = var_call_XOu9Pi4vGi755IWFCcoTFJBM
with open(path, 'r') as f:
    data = json.load(f)

# Simple keyword-based sports classification in title or description
sports_keywords = ['sport', 'sports', 'game', 'games', 'tournament', 'league', 'soccer', 'football', 'baseball', 'basketball', 'olympic', 'olympics', 'tennis', 'golf', 'cricket', 'hockey', 'athletics', 'match', 'nba', 'nfl', 'mlb', 'nhl']

sports_articles = []
for doc in data:
    title = (doc.get('title') or '').lower()
    desc = (doc.get('description') or '').lower()
    text = title + ' ' + desc
    if any(k in text for k in sports_keywords):
        sports_articles.append(doc)

max_title = None
max_len = -1
for doc in sports_articles:
    desc = doc.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_title = doc.get('title')

result = max_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XOu9Pi4vGi755IWFCcoTFJBM': 'file_storage/call_XOu9Pi4vGi755IWFCcoTFJBM.json'}

exec(code, env_args)
