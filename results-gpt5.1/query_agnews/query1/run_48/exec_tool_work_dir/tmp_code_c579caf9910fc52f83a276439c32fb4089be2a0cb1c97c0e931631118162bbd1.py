code = """import json, pandas as pd
from pathlib import Path

# Load full articles data
path = Path(var_call_Kfhe51MRV1YLQq8XjXhl6dZe)
with path.open() as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Define a simple classifier for Sports based on title/description keywords
sports_keywords = ['sport', 'sports', 'game', 'games', 'tournament', 'match', 'league', 'cup', 'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 'race', 'racing', 'grand prix']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

is_sports = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[is_sports].copy()

# Compute description length (characters)
sports_df['desc_len'] = sports_df['description'].fillna('').astype(str).str.len()

# Find row with max description length
if len(sports_df) == 0:
    result = None
else:
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Kfhe51MRV1YLQq8XjXhl6dZe': 'file_storage/call_Kfhe51MRV1YLQq8XjXhl6dZe.json'}

exec(code, env_args)
