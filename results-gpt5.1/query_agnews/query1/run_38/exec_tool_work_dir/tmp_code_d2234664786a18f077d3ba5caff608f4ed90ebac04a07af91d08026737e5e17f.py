code = """import json, pandas as pd, os

path = var_call_w4dwht0aK9krO8gPSqpQGfWE
with open(path, 'r') as f:
    data = json.load(f)

# rudimentary sports classifier based on keywords in title/description
sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'matches', 'tournament', 'league', 'cup', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'cricket', 'rugby', 'hockey']

sports_articles = []
for doc in data:
    text = ((doc.get('title') or '') + ' ' + (doc.get('description') or '')).lower()
    if any(k in text for k in sports_keywords):
        sports_articles.append(doc)

max_article = None
max_len = -1
for doc in sports_articles:
    desc = doc.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_article = doc

result = max_article['title'] if max_article else None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_w4dwht0aK9krO8gPSqpQGfWE': 'file_storage/call_w4dwht0aK9krO8gPSqpQGfWE.json'}

exec(code, env_args)
