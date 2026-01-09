code = """import json, pandas as pd

path = var_call_61ux5pVb5J6uCswyW8RDxfCZ
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].astype('string')

# crude sports classifier via keywords in title/description
sports_kw = [
    'sport','sports','game','match','tournament','league','cup','olympic','nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby','f1','formula','nascar','grand prix',
    'coach','season','playoff','final','semifinal','quarterfinal','touchdown','home run','goal','pts','ranked','medal','athlete','players','team','championship','world series','stanley cup','super bowl'
]
pattern = '|'.join([pd.regex.escape(k) if hasattr(pd, 'regex') else k for k in sports_kw])
# pandas doesn't have pd.regex.escape; use re
import re
pattern = '|'.join([re.escape(k) for k in sports_kw])
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
is_sports = text.str.contains(pattern, regex=True)

df_s = df[is_sports].copy()
df_s['desc_len'] = df_s['description'].fillna('').str.len()
row = df_s.sort_values(['desc_len','article_id'], ascending=[False, True]).head(1)
ans = row['title'].iloc[0] if len(row) else None
print('__RESULT__:')
print(json.dumps({'title': ans}))"""

env_args = {'var_call_61ux5pVb5J6uCswyW8RDxfCZ': 'file_storage/call_61ux5pVb5J6uCswyW8RDxfCZ.json'}

exec(code, env_args)
