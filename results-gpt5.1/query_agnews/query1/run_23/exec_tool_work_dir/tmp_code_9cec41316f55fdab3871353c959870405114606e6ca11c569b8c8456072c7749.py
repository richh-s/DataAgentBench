code = """import json
import pandas as pd

path = var_call_XenL60chxRktrM7wdEAZYZIx
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

sports_keywords = ['sport', 'game', 'team', 'match', 'tournament', 'league', 'olympic', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'cricket', 'hockey', 'athlete', 'athletic', 'racing', 'race', 'nascar', 'nfl', 'nba', 'mlb', 'nhl']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

is_sports = text.apply(lambda x: any(k in x for k in sports_keywords))

sports_df = df[is_sports].copy()

sports_df['desc_len'] = sports_df['description'].fillna('').str.len()

idxmax = sports_df['desc_len'].idxmax()

result_title = None if pd.isna(idxmax) else sports_df.loc[idxmax, 'title']

out = json.dumps(result_title)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_XenL60chxRktrM7wdEAZYZIx': 'file_storage/call_XenL60chxRktrM7wdEAZYZIx.json'}

exec(code, env_args)
