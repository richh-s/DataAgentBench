code = """import json
import pandas as pd

# Load the full result from the MongoDB query stored in the provided file path
path = var_call_YfFk4gJhUL54IHcjB1WxA5Rp
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)

# Ensure description and title are strings
df['title'] = df['title'].astype(str)
df['description'] = df['description'].astype(str)

# Define sports-related keywords
sports_keywords = [
    'game', 'match', 'score', 'scored', 'scores', 'defeat', 'beat', 'win', 'won', 'loss', 'draw',
    'season', 'coach', 'team', 'league', 'cup', 'tournament', 'olympic', 'olympics', 'football', 'soccer',
    'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'nba', 'nfl', 'mlb', 'fifa', 'boxing', 'rugby',
    'cricket', 'stadium', 'pitch', 'goal', 'goals', 'match', 'innings', 'race', 'racers', 'coach', 'player', 'players'
]

# Function to classify as sports if any keyword appears in title or description
def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    for kw in sports_keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_sports'] = df.apply(is_sports, axis=1)

# Compute description lengths
df['desc_len'] = df['description'].apply(lambda x: len(x))

# Filter sports articles
sports_df = df[df['is_sports']]

# If no sports articles found, prepare an informative result
if sports_df.empty:
    result = json.dumps(None)
else:
    # Find the article with the maximum description length
    max_idx = sports_df['desc_len'].idxmax()
    title = str(df.loc[max_idx, 'title'])
    result = json.dumps(title)

# Print result in required format
print("__RESULT__:")
print(result)"""

env_args = {'var_call_YfFk4gJhUL54IHcjB1WxA5Rp': 'file_storage/call_YfFk4gJhUL54IHcjB1WxA5Rp.json'}

exec(code, env_args)
