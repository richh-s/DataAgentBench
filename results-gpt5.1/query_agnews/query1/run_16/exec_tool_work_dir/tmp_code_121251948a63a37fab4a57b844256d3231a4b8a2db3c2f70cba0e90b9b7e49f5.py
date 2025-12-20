code = """import json
import pandas as pd

# Load full result from file
file_path = var_call_gOCGLXjMQdE9nLxKgOyRdCq2
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Heuristic: identify sports articles via title/description keywords
sports_keywords = ['sport', 'sports', 'game', 'games', 'team', 'teams', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'league', 'cup', 'tournament', 'match', 'coach', 'player', 'athlete']

pattern = '|'.join(sports_keywords)
sports_mask = df['title'].str.lower().str.contains(pattern) | df['description'].str.lower().str.contains(pattern)

sports_df = df[sports_mask].copy()

if sports_df.empty:
    result = None
else:
    sports_df['desc_len'] = sports_df['description'].astype(str).str.len()
    max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_gOCGLXjMQdE9nLxKgOyRdCq2': 'file_storage/call_gOCGLXjMQdE9nLxKgOyRdCq2.json'}

exec(code, env_args)
