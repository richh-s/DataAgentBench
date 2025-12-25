code = """import json
import pandas as pd

path = var_call_MBgrrtKjLGUd4MdrJrdWhBxw
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['sport', 'sports', 'game', 'games', 'team', 'teams', 'match', 'league', 'tournament', 'athlete', 'athletes', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl']

sports_articles = []
for doc in data:
    title = doc.get('title', '') or ''
    desc = doc.get('description', '') or ''
    full_text = (title + ' ' + desc).lower()
    if any(k in full_text for k in sports_keywords):
        sports_articles.append({
            'title': title,
            'description': desc,
            'desc_len': len(desc)
        })

if sports_articles:
    df = pd.DataFrame(sports_articles)
    max_row = df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MBgrrtKjLGUd4MdrJrdWhBxw': 'file_storage/call_MBgrrtKjLGUd4MdrJrdWhBxw.json'}

exec(code, env_args)
