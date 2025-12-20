code = """import json
import pandas as pd

# Load full result from file
file_path = var_call_8mQxMaVJRXRw0Ju4GWEo76r8
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Determine sports articles via simple heuristic on title/description
sports_keywords = ['football', 'soccer', 'nba', 'nfl', 'mlb', 'nhl', 'tennis', 'golf', 'olympic', 'olympics', 'world cup', 'grand prix', 'cricket', 'baseball', 'basketball', 'hockey', 'rugby', 'fifa', 'motogp', 'nascar', 'track and field', 'marathon']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

is_sports = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[is_sports].copy()

# Compute description length
sports_df['desc_len'] = sports_df['description'].fillna('').apply(len)

# Find article with maximum description length
if len(sports_df) == 0:
    result_title = None
else:
    max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]
    result_title = max_row['title']

out = json.dumps(result_title)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_8mQxMaVJRXRw0Ju4GWEo76r8': 'file_storage/call_8mQxMaVJRXRw0Ju4GWEo76r8.json'}

exec(code, env_args)
