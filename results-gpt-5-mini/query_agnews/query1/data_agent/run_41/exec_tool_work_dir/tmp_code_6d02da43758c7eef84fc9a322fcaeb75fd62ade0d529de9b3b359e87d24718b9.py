code = """import json
import pandas as pd

# Load the JSON result from the previous query_db call
with open(var_call_wjijicMPNedUw4ONyAHg4xMA, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# Ensure expected columns
if 'description' not in df.columns:
    df['description'] = ''
if 'title' not in df.columns:
    df['title'] = ''

# Compute description length
df['description'] = df['description'].fillna('').astype(str)
df['desc_len'] = df['description'].apply(len)

# Prepare text for keyword matching
df['combined'] = (df['title'].fillna('') + ' ' + df['description']).str.lower()

# Sports keywords (broad)
keywords = ['game','match','season','goal','score','scored','defeat','defeats','beat','beats','won','win','loss','lose',
            'quarterback','basketball','football','soccer','tennis','baseball','golf','olympic','olympics','coach','team',
            'league','cup','inning','innings','bat','run','home run','tackle','try','tries','manager','pitch','goalkeeper',
            'foul','referee','boxing','mma','wrestling','cricket','nba','mlb','nhl','mls','vs','v ']

# Function to detect sports
import re
pattern = re.compile(r"\b(" + "|".join([re.escape(k) for k in keywords]) + r")\b")

def is_sports(text):
    return bool(pattern.search(text))

# Apply detection
df['is_sports'] = df['combined'].apply(is_sports)

# Filter sports articles
sports_df = df[df['is_sports']].copy()

if sports_df.empty:
    result = None
else:
    # Find row(s) with maximum description length
    max_len = sports_df['desc_len'].max()
    top = sports_df[sports_df['desc_len'] == max_len]
    # If multiple, pick the first by original order
    title = top.iloc[0]['title']
    result = title

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wjijicMPNedUw4ONyAHg4xMA': 'file_storage/call_wjijicMPNedUw4ONyAHg4xMA.json'}

exec(code, env_args)
