code = """import json
import pandas as pd

path = var_call_Gyz2GwR1rB8nT5Cirkp1960t
with open(path, 'r') as f:
    data = json.load(f)

# Simple sports keyword-based classifier
sports_keywords = ['game','games','match','matches','tournament','league','cup','olympic','olympics','football','soccer','nba','nfl','mlb','nhl','tennis','golf','cricket','baseball','basketball','hockey','race','racing','grand prix','fifa','uefa','coach','coaches','team','teams','athlete','athletes','medal','medals','final','semifinal','quarterfinal']

rows = []
for doc in data:
    title = doc.get('title') or ''
    desc = doc.get('description') or ''
    text = (title + ' ' + desc).lower()
    is_sports = any(k in text for k in sports_keywords)
    if is_sports:
        rows.append({'title': title, 'description': desc})

if not rows:
    result = None
else:
    df = pd.DataFrame(rows)
    df['desc_len'] = df['description'].astype(str).str.len()
    max_row = df.sort_values('desc_len', ascending=False).iloc[0]
    result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Gyz2GwR1rB8nT5Cirkp1960t': 'file_storage/call_Gyz2GwR1rB8nT5Cirkp1960t.json'}

exec(code, env_args)
