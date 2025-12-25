code = """import json
import pandas as pd

# Load full result from file path
file_path = var_call_OZf30hGK7l9YlJAz5ItLZ0Ns
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Heuristic: classify sports articles by presence of sports-related keywords in title or description
sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'tournament', 'league', 'team', 'teams', 'cup', 'olympic', 'olympics', 'nba', 'nfl', 'mlb', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'cricket', 'hockey']

pattern = '|'.join(sports_keywords)
mask = df['title'].str.lower().str.contains(pattern) | df['description'].str.lower().str.contains(pattern)

sports_df = df[mask].copy()

# Compute length of description
sports_df['desc_len'] = sports_df['description'].astype(str).str.len()

# Get the article with the maximum description length
if not sports_df.empty:
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']
else:
    result = None

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_OZf30hGK7l9YlJAz5ItLZ0Ns': 'file_storage/call_OZf30hGK7l9YlJAz5ItLZ0Ns.json'}

exec(code, env_args)
