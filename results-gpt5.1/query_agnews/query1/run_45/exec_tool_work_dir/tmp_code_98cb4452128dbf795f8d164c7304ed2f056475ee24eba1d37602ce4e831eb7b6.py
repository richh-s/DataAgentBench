code = """import json
import pandas as pd

path = var_call_0zduyfyNmnDEFhGxRIUZ0rvv
with open(path, 'r') as f:
    data = json.load(f)

# Heuristic categorization: mark sports articles
sports_keywords = ['sport', 'sports', 'game', 'games', 'tournament', 'league', 'cup', 'match', 'olympic', 'olympics', 'soccer', 'football', 'nba', 'nfl', 'mlb', 'nhl', 'tennis', 'golf', 'cricket', 'baseball', 'basketball', 'hockey']

def is_sports(rec):
    text = ((rec.get('title') or '') + ' ' + (rec.get('description') or '')).lower()
    return any(k in text for k in sports_keywords)

sports_articles = [r for r in data if is_sports(r)]

max_title = None
max_len = -1
for r in sports_articles:
    desc = r.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_title = r.get('title')

result = json.dumps({'title': max_title, 'description_length': max_len})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_0zduyfyNmnDEFhGxRIUZ0rvv': 'file_storage/call_0zduyfyNmnDEFhGxRIUZ0rvv.json'}

exec(code, env_args)
