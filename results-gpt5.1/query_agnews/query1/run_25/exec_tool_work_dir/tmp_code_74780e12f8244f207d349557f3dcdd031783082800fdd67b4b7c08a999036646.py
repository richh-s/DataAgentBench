code = """import json, pandas as pd
import os

path = var_call_WcXbXdZUCH2YmxFp0wiGWrz5
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'game', 'team', 'match', 'tournament', 'league', 'cup', 'olympic', 'nfl', 'nba', 'mlb', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'hockey', 'cricket']

sports_articles = []
for doc in data:
    text = (doc.get('title','') + ' ' + doc.get('description','')).lower()
    if any(k in text for k in sports_keywords):
        sports_articles.append(doc)

max_doc = None
max_len = -1
for doc in sports_articles:
    desc = doc.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_doc = doc

result = max_doc['title'] if max_doc else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WcXbXdZUCH2YmxFp0wiGWrz5': 'file_storage/call_WcXbXdZUCH2YmxFp0wiGWrz5.json'}

exec(code, env_args)
