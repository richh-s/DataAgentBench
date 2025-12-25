code = """import json
import pandas as pd

# Load full result from file
path = var_call_YQl1ZAyrxpqPV5AAZGWii5pk
with open(path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Heuristic to identify sports articles: look for sports-related keywords in title or description
sports_keywords = ['sport', 'sports', 'game', 'games', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'tournament', 'match', 'league', 'cup', 'final', 'quarterback', 'coach', 'team', 'athlete', 'athletic']

pattern = '|'.join(sports_keywords)
mask = df['title'].str.lower().str.contains(pattern) | df['description'].str.lower().str.contains(pattern)

sports_df = df[mask].copy()

# Compute description length
sports_df['desc_len'] = sports_df['description'].astype(str).str.len()

# Find the article with max description length
if len(sports_df) == 0:
    result = None
else:
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_YQl1ZAyrxpqPV5AAZGWii5pk': 'file_storage/call_YQl1ZAyrxpqPV5AAZGWii5pk.json'}

exec(code, env_args)
