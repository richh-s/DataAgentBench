code = """import json
import pandas as pd

# Load full result from file
path = var_call_hIpUdCY8NtsPlTGjAMLXavVi
with open(path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Heuristic classifier for Sports based on title+description
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

sports_keywords = [' sport', 'sports', ' game', 'games', 'tournament', 'league', 'cup', 'olympic', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'cricket', 'hockey', 'racing', 'nascar', 'fifa', 'uefa', 'world cup']

is_sports = pd.Series(False, index=df.index)
for kw in sports_keywords:
    is_sports |= text.str.contains(kw)

sports_df = df[is_sports].copy()

if sports_df.empty:
    result = None
else:
    sports_df['desc_len'] = sports_df['description'].fillna('').str.len()
    max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']

out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_hIpUdCY8NtsPlTGjAMLXavVi': 'file_storage/call_hIpUdCY8NtsPlTGjAMLXavVi.json'}

exec(code, env_args)
