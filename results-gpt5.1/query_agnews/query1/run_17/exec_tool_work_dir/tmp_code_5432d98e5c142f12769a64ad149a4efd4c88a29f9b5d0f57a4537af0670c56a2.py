code = """import json
import pandas as pd

# Load full result from file
file_path = var_call_I4WsZbz8k8Of9QThUa6R1sEZ
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Identify sports articles by keywords in title/description
sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'tournament', 'league', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'athlete', 'athletic', 'nba', 'nfl', 'nhl', 'mlb']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
mask = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[mask].copy()

# Compute description length and get the article with the max length
sports_df['desc_len'] = sports_df['description'].fillna('').astype(str).str.len()

if len(sports_df) == 0:
    result = None
else:
    max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']

out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_I4WsZbz8k8Of9QThUa6R1sEZ': 'file_storage/call_I4WsZbz8k8Of9QThUa6R1sEZ.json'}

exec(code, env_args)
