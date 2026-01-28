code = """import json
import pandas as pd

# Load the large query result from the provided storage key path
with open(var_call_lgxb6TZjxdpNhqMYHh1qGD0s, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure description and title are strings
df['title'] = df.get('title', '').fillna('').astype(str)
df['description'] = df.get('description', '').fillna('').astype(str)

# Define sports-related keywords (broad but focused)
keywords = [
    'sport','sports','match','game','team','score','scores','scored','beat','beats','defeat','defeated',
    'win','wins','won','goal','goals','penalty','season','coach','manager','football','soccer',
    'basketball','baseball','cricket','tennis','golf','hockey','nhl','mlb','nba','fifa','olympic',
    'olympics','racing','race','runner','boxer','boxing','stadium','league','cup','tackle','tries',
    'innings','quarterback','touchdown'
]

kw_set = set(keywords)

# function to detect if text contains any keyword as a word
import re
word_pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in kw_set) + r")\b", flags=re.IGNORECASE)

def is_sports_text(text):
    return bool(word_pattern.search(text))

# Apply detection on title or description
is_sports = df['title'].apply(is_sports_text) | df['description'].apply(is_sports_text)

sports_df = df[is_sports].copy()
# Compute description length
sports_df['desc_len'] = sports_df['description'].astype(str).apply(len)

result_title = None
if not sports_df.empty:
    # pick the article with the greatest description length
    idx = sports_df['desc_len'].idxmax()
    result_title = sports_df.at[idx, 'title']
else:
    # fallback: if no sports found, return an empty string
    result_title = ""

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result_title))"""

env_args = {'var_call_lgxb6TZjxdpNhqMYHh1qGD0s': 'file_storage/call_lgxb6TZjxdpNhqMYHh1qGD0s.json'}

exec(code, env_args)
