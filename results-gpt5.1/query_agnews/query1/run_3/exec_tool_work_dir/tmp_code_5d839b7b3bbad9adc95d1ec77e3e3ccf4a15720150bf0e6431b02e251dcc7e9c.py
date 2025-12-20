code = """import json
import pandas as pd

# Load data from storage
file_path = var_call_0KArV0bo56ovZDj15fOU7R8V
with open(file_path, 'r') as f:
    articles = json.load(f)

# Create DataFrame
df = pd.DataFrame(articles)

# Drop rows without description
df = df.dropna(subset=['description'])

# Compute description length
df['desc_len'] = df['description'].astype(str).str.len()

# For this task, we need only sports articles. We'll classify based on keywords in title/description.
# A simple heuristic: if either field contains common sports-related terms, mark as Sports.

sports_keywords = ['sport', 'sports', 'game', 'games', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'nhl', 'mlb', 'league', 'tournament', 'cup', 'match', 'coach', 'player', 'athlete']

pattern = '|'.join(sports_keywords)
mask_sports = df['title'].str.lower().str.contains(pattern) | df['description'].str.lower().str.contains(pattern)

sports_df = df[mask_sports]

if sports_df.empty:
    result = None
else:
    max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_0KArV0bo56ovZDj15fOU7R8V': 'file_storage/call_0KArV0bo56ovZDj15fOU7R8V.json'}

exec(code, env_args)
