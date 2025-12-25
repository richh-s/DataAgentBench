code = """import json
import pandas as pd

# load full result
path = var_call_u7LwvtP9An54K2vttyrB6z4T
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['vs', 'defeats', 'beats', 'victory', 'defeat', 'win', 'loses', 'loss', 'quarterback', 'coach', 'league', 'tournament', 'final', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'olympic', 'olympics', 'world cup', 'nfl', 'nba', 'mlb', 'nhl']

max_len = -1
max_title = None

for art in data:
    text = (art.get('title','') + ' ' + art.get('description','')).lower()
    if any(k in text for k in sports_keywords):
        desc = art.get('description') or ''
        l = len(desc)
        if l > max_len:
            max_len = l
            max_title = art.get('title')

result = max_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_u7LwvtP9An54K2vttyrB6z4T': 'file_storage/call_u7LwvtP9An54K2vttyrB6z4T.json'}

exec(code, env_args)
