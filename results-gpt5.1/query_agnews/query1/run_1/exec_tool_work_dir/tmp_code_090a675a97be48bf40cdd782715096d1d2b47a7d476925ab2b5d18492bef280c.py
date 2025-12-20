code = """import json, pandas as pd

path = var_call_7EdV3aCXAyGKEVAFYwstOCaE
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'matches', 'tournament', 'league', 'cup', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'soccer', 'football', 'cricket', 'tennis', 'golf', 'baseball', 'basketball', 'hockey']

sports_articles = []
for art in data:
    text = ((art.get('title') or '') + ' ' + (art.get('description') or '')).lower()
    if any(k in text for k in sports_keywords):
        desc = art.get('description') or ''
        sports_articles.append({'title': art.get('title'), 'desc_len': len(desc)})

if sports_articles:
    max_article = max(sports_articles, key=lambda x: x['desc_len'])
    result = max_article['title']
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7EdV3aCXAyGKEVAFYwstOCaE': 'file_storage/call_7EdV3aCXAyGKEVAFYwstOCaE.json'}

exec(code, env_args)
