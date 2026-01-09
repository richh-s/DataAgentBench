code = """import json, pandas as pd

path = var_call_Vfs8ukrDIuhD5wplZQAimswk
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# normalize types
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)
# simple sports classifier
sports_terms = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','olympics','fifa','uefa',
    'world cup','super bowl','playoff','playoffs','championship','league','tournament','match','season','coach','team','player','quarterback',
    'home run','goal','touchdown','run batted','pitcher','referee','medal','race','grand slam','pga','atp','wta','nascar','formula','f1'
]
pat = r'(?i)\\b(' + '|'.join([pd.regex.escape(t) if hasattr(pd, 'regex') else t for t in sports_terms]) + r')\\b'
# pandas doesn't have regex.escape; use python re
import re
pat = r'(?i)(' + '|'.join([re.escape(t) for t in sports_terms]) + r')'
text = (df['title'].str.lower() + ' ' + df['description'].str.lower())
df['is_sports'] = text.str.contains(pat, regex=True)

df_s = df[df['is_sports']].copy()
df_s['desc_len'] = df_s['description'].str.len()
idx = df_s['desc_len'].idxmax()
ans = df_s.loc[idx, 'title'] if len(df_s) else None

print('__RESULT__:')
print(json.dumps({'title': ans, 'desc_len': int(df_s.loc[idx,'desc_len']) if len(df_s) else None}))"""

env_args = {'var_call_Vfs8ukrDIuhD5wplZQAimswk': 'file_storage/call_Vfs8ukrDIuhD5wplZQAimswk.json'}

exec(code, env_args)
