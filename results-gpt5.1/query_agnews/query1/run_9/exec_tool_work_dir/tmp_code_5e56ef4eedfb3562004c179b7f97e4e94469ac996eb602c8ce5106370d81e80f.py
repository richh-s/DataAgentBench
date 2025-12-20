code = """import json
import pandas as pd

path = var_call_JJtnQ59j9AGg3a3NWwQ6yzGW
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['game', 'games', 'match', 'matches', 'tournament', 'league', 'season', 'team', 'teams', 'coach', 'player', 'players', 'score', 'scored', 'scoring', 'victory', 'win', 'wins', 'won', 'loss', 'lost', 'defeat', 'beat', 'beats', 'beaten', 'cup', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'cricket', 'hockey', 'racing', 'nascar', 'formula one', 'f1', 'track and field', 'athletics', 'world series', 'super bowl', 'playoffs']

sports_articles = []
for art in data:
    text = (art.get('title','') + ' ' + art.get('description','')).lower()
    if any(k in text for k in sports_keywords):
        sports_articles.append(art)

max_title = None
max_len = -1
for art in sports_articles:
    desc = art.get('description') or ''
    l = len(desc)
    if l > max_len:
        max_len = l
        max_title = art.get('title')

result = max_title

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JJtnQ59j9AGg3a3NWwQ6yzGW': 'file_storage/call_JJtnQ59j9AGg3a3NWwQ6yzGW.json'}

exec(code, env_args)
