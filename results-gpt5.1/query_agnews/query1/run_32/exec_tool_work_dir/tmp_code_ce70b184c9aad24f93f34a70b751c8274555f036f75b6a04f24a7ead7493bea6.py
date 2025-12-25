code = """import json
import pandas as pd

# Load data from storage
file_path = var_call_8ZMruCeK6CNOKn6yrf2kEr00
with open(file_path, 'r') as f:
    articles = json.load(f)

# Create DataFrame
df = pd.DataFrame(articles)

# Heuristic to identify sports articles based on title/description keywords
sports_keywords = ['sport', 'sports', 'game', 'games', 'football', 'soccer', 'nba', 'nfl', 'mlb', 'nhl', 'tennis', 'golf', 'olympic', 'olympics', 'baseball', 'basketball', 'hockey', 'cricket', 'rugby', 'athletic', 'tournament', 'league', 'cup', 'championship', 'final', 'playoff']

pattern = '|'.join(sports_keywords)

# Combine title and description for classification
df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Flag as sports if any sports keyword appears
df['is_sports'] = df['text'].str.contains(pattern, regex=True)

sports_df = df[df['is_sports']].copy()

if sports_df.empty:
    result = None
else:
    sports_df['desc_len'] = sports_df['description'].fillna('').str.len()
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']

out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_8ZMruCeK6CNOKn6yrf2kEr00': 'file_storage/call_8ZMruCeK6CNOKn6yrf2kEr00.json'}

exec(code, env_args)
