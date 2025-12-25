code = """import json
import pandas as pd

# Load full data from file path in var_call_nv7NddEHgnpVGjpeeOLGZqGc
file_path = var_call_nv7NddEHgnpVGjpeeOLGZqGc
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Simple categorization based on keywords in title/description
sports_keywords = ['sport', 'sports', 'game', 'games', 'match', 'soccer', 'football', 'basketball', 'tennis', 'golf', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'tournament', 'league', 'cup', 'race', 'racing', 'athlete', 'athletic', 'baseball', 'cricket', 'hockey']

sports_mask = (
    df['title'].str.lower().str.contains('|'.join(sports_keywords), na=False) |
    df['description'].str.lower().str.contains('|'.join(sports_keywords), na=False)
)

sports_df = df[sports_mask].copy()

# Compute description length
sports_df['desc_len'] = sports_df['description'].fillna('').astype(str).str.len()

# Find the row with maximum description length
if len(sports_df) == 0:
    result = None
else:
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_nv7NddEHgnpVGjpeeOLGZqGc': 'file_storage/call_nv7NddEHgnpVGjpeeOLGZqGc.json'}

exec(code, env_args)
