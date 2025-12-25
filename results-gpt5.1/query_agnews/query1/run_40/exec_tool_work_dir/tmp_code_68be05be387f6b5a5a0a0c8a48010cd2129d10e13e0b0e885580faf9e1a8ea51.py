code = """import json, pandas as pd, os

path = var_call_8F71DbZX4GOK72Hz0NpMJ29j
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['vs', 'defeat', 'defeats', 'beat', 'beats', 'victory', 'win', 'wins', 'loses', 'loss', 'draw', 'cup', 'league', 'tournament', 'final', 'quarterfinal', 'semifinal', 'coach', 'manager', 'team', 'teams', 'goal', 'goals', 'score', 'scored', 'scoring', 'nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'olympic', 'olympics', 'cricket', 'rugby', 'fifa', 'uefa']

sports_articles = []
for art in data:
    text = (art.get('title','') + ' ' + art.get('description','')).lower()
    if any(k in text for k in sports_keywords):
        sports_articles.append(art)

max_art = None
max_len = -1
for art in sports_articles:
    desc = art.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_art = art

result = max_art.get('title') if max_art else None

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_8F71DbZX4GOK72Hz0NpMJ29j': 'file_storage/call_8F71DbZX4GOK72Hz0NpMJ29j.json'}

exec(code, env_args)
