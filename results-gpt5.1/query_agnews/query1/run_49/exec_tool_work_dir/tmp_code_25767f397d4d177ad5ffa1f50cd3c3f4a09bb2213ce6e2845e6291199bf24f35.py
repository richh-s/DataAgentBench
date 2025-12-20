code = """import json, pandas as pd

# load full data from file
path = var_call_eXZffnTLK4mCjesVWEuWssiH
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'team', 'teams', 'league', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'olympic', 'olympics', 'tournament', 'match', 'cup', 'championship', 'coach', 'player', 'players']

def is_sports(title, desc):
    text = f"{title} {desc}".lower()
    return any(k in text for k in sports_keywords)

max_len = -1
max_title = None
for art in data:
    title = art.get('title') or ''
    desc = art.get('description') or ''
    if not is_sports(title, desc):
        continue
    dlen = len(desc)
    if dlen > max_len:
        max_len = dlen
        max_title = title

result = max_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eXZffnTLK4mCjesVWEuWssiH': 'file_storage/call_eXZffnTLK4mCjesVWEuWssiH.json'}

exec(code, env_args)
