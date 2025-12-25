code = """import json
import pandas as pd

path = var_call_sOWtdVfiFUAM2CzYDmqp5CC7
with open(path, 'r') as f:
    data = json.load(f)

# Simple keyword-based classifier for sports titles/descriptions
sports_keywords = ['sport', 'sports', 'game', 'games', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'tournament', 'league', 'cup', 'final', 'coach', 'team', 'teams', 'player', 'players', 'match', 'score', 'scored', 'scoring', 'win', 'victory', 'defeat']

sports_articles = []
for doc in data:
    title = (doc.get('title') or '').lower()
    desc = (doc.get('description') or '').lower()
    text = title + ' ' + desc
    if any(k in text for k in sports_keywords):
        sports_articles.append(doc)

# Find sports article with max description length
max_doc = None
max_len = -1
for doc in sports_articles:
    desc = doc.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_doc = doc

result = max_doc.get('title') if max_doc else None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sOWtdVfiFUAM2CzYDmqp5CC7': 'file_storage/call_sOWtdVfiFUAM2CzYDmqp5CC7.json'}

exec(code, env_args)
