code = """import json, pandas as pd
path = var_call_g8uobpeqBg0BZyaqyr98oSLM
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# normalize
if 'description' not in df.columns:
    df['description'] = None
if 'title' not in df.columns:
    df['title'] = None

df['description'] = df['description'].fillna('').astype(str)
df['title'] = df['title'].fillna('').astype(str)
df['desc_len'] = df['description'].map(len)

# sports heuristic keywords
sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','cricket',
    'olympic','olympics','fifa','uefa','world cup','super bowl','playoffs','playoff','final','tournament',
    'coach','quarterback','touchdown','home run','goal','match','game','season','league','championship',
    'celtics','lakers','yankees','red sox','manchester','arsenal','chelsea','barcelona','real madrid'
]

def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    return any(kw in text for kw in sports_kw)

df['is_sports'] = df.apply(is_sports, axis=1)
sports_df = df[df['is_sports']].copy()
if sports_df.empty:
    result = {"title": None}
else:
    max_row = sports_df.loc[sports_df['desc_len'].idxmax()]
    result = {"title": max_row['title'], "article_id": str(max_row.get('article_id', '')), "description_length": int(max_row['desc_len'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_g8uobpeqBg0BZyaqyr98oSLM': 'file_storage/call_g8uobpeqBg0BZyaqyr98oSLM.json'}

exec(code, env_args)
