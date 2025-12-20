code = """import json
import pandas as pd

# Load full result from file
path = var_call_cLKdn3YkVyBSCWtvnp573P8N
with open(path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Heuristic: classify sports articles by presence of sports-related keywords in title or description
sports_keywords = ['football', 'soccer', 'nba', 'nfl', 'mlb', 'hockey', 'tennis', 'golf', 'olympic', 'olympics', 'world cup', 'grand prix', 'cricket', 'baseball', 'basketball', 'rugby', 'fifa', 'uefa', 'nascar', 'motogp', 'athletics', 'marathon', 'swimming', 'track and field', 'formula one', 'f1', 'tour de france']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
pattern = '|'.join([k.replace(' ', '\\s+') for k in sports_keywords])
mask_sports = text.str.contains(pattern, regex=True)

sports_df = df[mask_sports].copy()

# Compute description length
sports_df['desc_len'] = sports_df['description'].fillna('').astype(str).str.len()

# Get row with max description length
if sports_df.empty:
    result = None
else:
    max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cLKdn3YkVyBSCWtvnp573P8N': 'file_storage/call_cLKdn3YkVyBSCWtvnp573P8N.json'}

exec(code, env_args)
