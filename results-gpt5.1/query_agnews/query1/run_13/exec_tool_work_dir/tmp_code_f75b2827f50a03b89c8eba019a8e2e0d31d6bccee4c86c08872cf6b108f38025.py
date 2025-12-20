code = """import json
import pandas as pd

# Load full result from file
path = var_call_g6rdvbJgKzWuGTfd2n4Lea9N
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'team', 'teams', 'match', 'tournament', 'league', 'cup', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'cricket', 'hockey']

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

env_args = {'var_call_g6rdvbJgKzWuGTfd2n4Lea9N': 'file_storage/call_g6rdvbJgKzWuGTfd2n4Lea9N.json'}

exec(code, env_args)
