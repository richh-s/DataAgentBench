code = """import json
import os

path = var_call_Y74f7QGooo2uZPFmyKLWkcHK

with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'tournament', 'league', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'athlete', 'athletes', 'team', 'teams', 'coach', 'coaches', 'score', 'scored', 'scoring']

max_len = -1
max_title = None

for doc in data:
    desc = doc.get('description') or ''
    title = doc.get('title') or ''
    text = (title + ' ' + desc).lower()
    if any(k in text for k in sports_keywords):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_title = title

result = max_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Y74f7QGooo2uZPFmyKLWkcHK': 'file_storage/call_Y74f7QGooo2uZPFmyKLWkcHK.json'}

exec(code, env_args)
