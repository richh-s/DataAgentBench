code = """import json
import pandas as pd

path = var_call_SoSVaKsI0dwC0XsUvpc5eizF
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Heuristic: classify sports by keywords in title/description
sports_keywords = ['sport', 'sports', 'game', 'games', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'cricket', 'rugby', 'tournament', 'match', 'league', 'athlete', 'athletic']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
mask_sports = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[mask_sports].copy()

sports_df['desc_len'] = sports_df['description'].fillna('').str.len()
max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]

result = json.dumps({'title': max_row['title']})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_SoSVaKsI0dwC0XsUvpc5eizF': 'file_storage/call_SoSVaKsI0dwC0XsUvpc5eizF.json'}

exec(code, env_args)
