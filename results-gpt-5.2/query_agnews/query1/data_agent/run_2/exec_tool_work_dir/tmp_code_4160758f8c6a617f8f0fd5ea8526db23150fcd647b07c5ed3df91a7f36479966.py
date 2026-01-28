code = """import json, pandas as pd, re

path = var_call_xWL2CyYINACw2nSYwjRXHYsK
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()

sports_terms = [
    'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics',
    'cricket','rugby','fifa','uefa','premier league','champions league','world cup','super bowl','playoff','playoffs',
    'match','tournament','coach','season','league','cup','grand slam','racetrack','formula','nascar','boxing','ufc','mma'
]
pat = r'(?i)\\b(' + '|'.join([re.escape(t) for t in sports_terms]) + r')\\b'
mask_sports = df['title'].str.contains(pat, regex=True) | df['description'].str.contains(pat, regex=True)

cand = df[mask_sports].copy()
if cand.empty:
    out = {"error":"No sports articles detected by heuristic."}
else:
    idx = cand['desc_len'].idxmax()
    out = {"title": cand.loc[idx,'title']}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xWL2CyYINACw2nSYwjRXHYsK': 'file_storage/call_xWL2CyYINACw2nSYwjRXHYsK.json'}

exec(code, env_args)
