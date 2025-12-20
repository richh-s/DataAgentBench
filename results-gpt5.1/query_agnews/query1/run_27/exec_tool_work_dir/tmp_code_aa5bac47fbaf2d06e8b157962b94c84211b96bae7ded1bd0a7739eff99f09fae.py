code = """import json, os

path = var_call_fkpYjBw0mmpB66rPLkrITtwz
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'tournament', 'match', 'league', 'cup', 'olympic', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'cricket']

max_len = -1
max_title = None

for doc in data:
    title = doc.get('title','') or ''
    desc = doc.get('description','') or ''
    text = (title + ' ' + desc).lower()
    if any(k in text for k in sports_keywords):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_title = title

result = {'title': max_title, 'description_length': max_len}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fkpYjBw0mmpB66rPLkrITtwz': 'file_storage/call_fkpYjBw0mmpB66rPLkrITtwz.json'}

exec(code, env_args)
