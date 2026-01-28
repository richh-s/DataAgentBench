code = """import json
import pandas as pd

path = var_call_c23Q1yh5fgQYYlimuqWfpDNB
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max())
# Heuristic sports detection via keywords
sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olymp',
    'cricket','rugby','fifa','uefa','champions league','premier league','coach','quarterback','touchdown',
    'goal','match','tournament','league','playoff','final','defeat','wins','win','medal','athlete','pitcher'
]
pat = r'(' + '|'.join([pd.regex.escape(k) for k in sports_kw]) + r')'
mask_sports = df['title'].str.lower().str.contains(pat, regex=True) | df['description'].str.lower().str.contains(pat, regex=True)

df_s = df[mask_sports].copy()
if len(df_s)==0:
    out = {"error":"No sports articles detected by heuristic.","max_description_length_overall":max_len}
else:
    idx = df_s['desc_len'].idxmax()
    row = df_s.loc[idx]
    out = {"title": row['title'], "description_length": int(row['desc_len']), "article_id": row.get('article_id')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_c23Q1yh5fgQYYlimuqWfpDNB': 'file_storage/call_c23Q1yh5fgQYYlimuqWfpDNB.json'}

exec(code, env_args)
