code = """import json
import pandas as pd
# Load the full result JSON from the file path stored in the variable from the previous tool call
path = var_call_8UYfgBVjzQ3cQBb4WGC2Xed3
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# Ensure title and description exist and are strings
if 'description' not in df.columns:
    df['description'] = ''
if 'title' not in df.columns:
    df['title'] = ''

df['description'] = df['description'].astype(str)
df['title'] = df['title'].astype(str)
df['desc_len'] = df['description'].str.len()

# Heuristic keyword-based sports classifier
sports_keywords = [
    'football','soccer','basketball','baseball','cricket','tennis','golf','match','goal','score',
    'tournament','league','season','coach','olympic','cup','win','wins','defeat','racing','race',
    'innings','pitch','bat','club','boxer','boxing','athlete','runner','homerun','home run','touchdown',
    'mlb','nba','nfl','nhl','fifa','goalkeeper','striker','midfielder','defender'
]

def is_sports_text(text):
    t = text.lower()
    return any(k in t for k in sports_keywords)

combined = (df['title'] + ' ' + df['description']).fillna('').astype(str)
df['is_sports'] = combined.apply(is_sports_text)

sports_df = df[df['is_sports']]
if not sports_df.empty:
    chosen = sports_df.loc[sports_df['desc_len'].idxmax()]
else:
    # Fallback: if no sports articles detected, choose the article with the longest description overall
    chosen = df.loc[df['desc_len'].idxmax()]

result_title = chosen['title'] if pd.notna(chosen['title']) else ''

print("__RESULT__:")
print(json.dumps(result_title))"""

env_args = {'var_call_8UYfgBVjzQ3cQBb4WGC2Xed3': 'file_storage/call_8UYfgBVjzQ3cQBb4WGC2Xed3.json'}

exec(code, env_args)
