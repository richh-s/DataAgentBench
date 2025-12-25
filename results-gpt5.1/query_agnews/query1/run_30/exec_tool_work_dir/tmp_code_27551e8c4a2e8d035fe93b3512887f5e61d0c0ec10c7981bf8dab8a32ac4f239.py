code = """import json
import pandas as pd

# Load full Mongo query result
path = var_call_5qEYhRWacdcP20oxOE8U7h2i
with open(path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Heuristic: classify sports articles by presence of sports-related keywords in title or description
sports_keywords = ['football', 'soccer', 'nba', 'nfl', 'mlb', 'nhl', 'tennis', 'golf', 'olympic', 'olympics', 'world cup', 'grand prix', 'motogp', 'formula one', 'f1', 'cricket', 'rugby', 'baseball', 'basketball', 'hockey', 'nascar', 'motorsport', 'motorsports', 'championship', 'tournament']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
mask_sports = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[mask_sports].copy()

# Compute description length in characters
sports_df['desc_len'] = sports_df['description'].fillna('').astype(str).str.len()

# Find article with maximum description length
if len(sports_df) == 0:
    result = None
else:
    idx = sports_df['desc_len'].idxmax()
    title = sports_df.loc[idx, 'title']
    result = title

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5qEYhRWacdcP20oxOE8U7h2i': 'file_storage/call_5qEYhRWacdcP20oxOE8U7h2i.json'}

exec(code, env_args)
