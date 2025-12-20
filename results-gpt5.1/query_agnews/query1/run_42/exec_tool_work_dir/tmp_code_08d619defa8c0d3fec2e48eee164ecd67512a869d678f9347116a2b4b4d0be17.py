code = """import json
import pandas as pd

# Load full result from file
file_path = var_call_Tkcutu7c8mspenBegTW1VLdB
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Heuristic to classify sports articles: look for sports-related keywords in title or description
sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'tournament', 'league', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'nascar', 'race', 'racing', 'athlete', 'athletic']

pattern = '|'.join(sports_keywords)
mask = df['title'].str.lower().str.contains(pattern) | df['description'].str.lower().str.contains(pattern)

sports_df = df[mask].copy()

# Compute description length and find max
sports_df['desc_len'] = sports_df['description'].astype(str).str.len()
max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]

result = max_row['title']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Tkcutu7c8mspenBegTW1VLdB': 'file_storage/call_Tkcutu7c8mspenBegTW1VLdB.json'}

exec(code, env_args)
