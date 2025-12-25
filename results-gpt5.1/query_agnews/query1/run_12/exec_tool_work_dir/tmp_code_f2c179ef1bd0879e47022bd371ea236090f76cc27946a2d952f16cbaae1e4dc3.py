code = """import json
import pandas as pd

path = var_call_QRVsq6c9LzjG9gmaVlIBko9D
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'tournament', 'match', 'league', 'olympic', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'tennis', 'golf', 'cricket', 'baseball', 'football', 'hockey']

max_len = -1
max_title = None

for doc in data:
    title = (doc.get('title') or '').lower()
    desc = doc.get('description') or ''
    text = title + ' ' + desc.lower()
    if any(k in text for k in sports_keywords):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_title = doc.get('title')

result = max_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QRVsq6c9LzjG9gmaVlIBko9D': 'file_storage/call_QRVsq6c9LzjG9gmaVlIBko9D.json'}

exec(code, env_args)
