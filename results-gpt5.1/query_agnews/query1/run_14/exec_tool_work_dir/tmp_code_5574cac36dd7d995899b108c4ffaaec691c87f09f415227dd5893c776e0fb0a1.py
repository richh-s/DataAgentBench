code = """import json
import pandas as pd

file_path = var_call_vFYNXkJ9dU4rzQwTFGf2olYP
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Drop rows with null descriptions just in case
df = df.dropna(subset=['description'])

# Compute length of descriptions
df['desc_len'] = df['description'].astype(str).str.len()

# We need sports articles only; simple keyword-based classification on title+description
text = (df['title'].astype(str) + ' ' + df['description'].astype(str)).str.lower()

sports_keywords = ['game', 'games', 'team', 'teams', 'match', 'matches', 'season', 'league', 'tournament', 'cup', 'olympic', 'olympics', 'championship', 'score', 'scored', 'scoring', 'goal', 'goals', 'basketball', 'baseball', 'football', 'soccer', 'tennis', 'golf', 'hockey', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'cricket', 'rugby', 'athletics', 'swimming', 'track and field']

is_sports = text.apply(lambda x: any(kw in x for kw in sports_keywords))

sports_df = df[is_sports]

if sports_df.empty:
    result = None
else:
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_vFYNXkJ9dU4rzQwTFGf2olYP': 'file_storage/call_vFYNXkJ9dU4rzQwTFGf2olYP.json'}

exec(code, env_args)
