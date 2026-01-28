code = """import json
import pandas as pd

# Load the large result file from the previous query_db call
with open(var_call_gzFcpP0v8W00csiDB7D8Gr5k, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)

# Ensure description and title fields exist and are strings
df['title'] = df.get('title', '').fillna('').astype(str)
df['description'] = df.get('description', '').fillna('').astype(str)

# Define keyword lists for simple rule-based classification
sports_kw = [
    'match','beat','defeat','win','wins','won','goal','goals','soccer','football',
    'basketball','nba','mlb','nfl','nhl','tennis','cricket','race','racing','olympic',
    'coach','player','players','season','cup','league','tournament','stadium','pitch',
    'score','scored','innings','try','rugby','golf','fifa','world cup','boxing','ufc',
    'wimbledon','f1','formula 1','motorcycle','boxing','corner','midfielder','striker',
    'goalkeeper','goalie'
]
business_kw = [
    'stock','stocks','market','economy','trade','shares','company','companies','profit',
    'dollar','oil','prices','investment','firm','bank','fund','revenue','earnings'
]
tech_kw = [
    'technology','tech','google','iphone','computer','nuclear','scientist','science',
    'hp','microsoft','intel','software','hardware','internet','web','ipod','iphone'
]

# Lowercase combined text for checking
combined = (df['title'].str.lower() + ' ' + df['description'].str.lower()).fillna('')

def classify_text(s):
    for kw in sports_kw:
        if kw in s:
            return 'Sports'
    for kw in business_kw:
        if kw in s:
            return 'Business'
    for kw in tech_kw:
        if kw in s:
            return 'Science/Technology'
    return 'World'

df['category'] = combined.apply(classify_text)

# Compute description lengths
# Use number of characters
df['desc_len'] = df['description'].apply(lambda x: len(x) if x is not None else 0)

# Filter sports articles
sports_df = df[df['category'] == 'Sports']

# If no sports found, return an empty result
if sports_df.empty:
    result = None
else:
    max_len = sports_df['desc_len'].max()
    top = sports_df[sports_df['desc_len'] == max_len]
    # Extract titles (unique) as list
    titles = top['title'].dropna().astype(str).tolist()
    # If only one title, return that string, else return list
    if len(titles) == 1:
        result = titles[0]
    else:
        result = titles

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gzFcpP0v8W00csiDB7D8Gr5k': 'file_storage/call_gzFcpP0v8W00csiDB7D8Gr5k.json'}

exec(code, env_args)
