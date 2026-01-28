code = """import json
import pandas as pd
import re

# Load the MongoDB query result from the provided storage path
path = var_call_lss22wSI4c3Vs0tfi0hIyNnK
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Ensure expected columns
if 'description' not in df.columns:
    df['description'] = ''
if 'title' not in df.columns:
    df['title'] = ''

# Normalize to strings
df['description'] = df['description'].fillna('').astype(str)
df['title'] = df['title'].fillna('').astype(str)

# Simple rule-based classifier for Sports category using keywords
sports_keywords = [
    'football','soccer','nba','mlb','nfl','cricket','golf','tennis','match','tournament',
    'season','coach','manager','inning','pitch','goal','scored','score','defeat','beat',
    'race','olympic','rugby','hockey','basketball','baseball','fired','won','loss','draw',
    'series','cup','championship','athlete','athletes','midfielder','striker','goalkeeper'
]
pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in sports_keywords) + r')\b', re.IGNORECASE)

# Determine if article is sports by checking title and description
def is_sports(row):
    text = (row['title'] + ' ' + row['description'])
    return bool(pattern.search(text))

df['is_sports'] = df.apply(is_sports, axis=1)

# Compute description lengths
df['desc_len'] = df['description'].str.len()

# Filter sports articles
sports_df = df[df['is_sports']]

# If no sports articles found, try a broader heuristic: look for 'sport' word
if sports_df.empty:
    broader = df[(df['title'].str.contains('sport', case=False, na=False)) | (df['description'].str.contains('sport', case=False, na=False))]
    sports_df = broader

if sports_df.empty:
    result = None
else:
    # Get article with max description length
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = max_row['title']

# Print result in required format as JSON string
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lss22wSI4c3Vs0tfi0hIyNnK': 'file_storage/call_lss22wSI4c3Vs0tfi0hIyNnK.json'}

exec(code, env_args)
