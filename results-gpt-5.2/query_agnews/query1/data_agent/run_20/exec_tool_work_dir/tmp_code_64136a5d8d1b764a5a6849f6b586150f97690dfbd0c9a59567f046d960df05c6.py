code = """import json
import pandas as pd
import re

path = var_call_c23Q1yh5fgQYYlimuqWfpDNB
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()

sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olymp',
    'cricket','rugby','fifa','uefa','champions league','premier league','coach','quarterback','touchdown',
    'goal','match','tournament','league','playoff','final','defeat','wins','win','medal','athlete','pitcher'
]
pat = re.compile(r'(' + '|'.join([re.escape(k) for k in sports_kw]) + r')', re.IGNORECASE)
mask_sports = df['title'].str.contains(pat) | df['description'].str.contains(pat)

df_s = df[mask_sports].copy()

if len(df_s)==0:
    out = {"error":"No sports articles detected by heuristic."}
else:
    row = df_s.loc[df_s['desc_len'].idxmax()]
    out = {"title": row['title'], "description_length": int(row['desc_len']), "article_id": row.get('article_id')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_c23Q1yh5fgQYYlimuqWfpDNB': 'file_storage/call_c23Q1yh5fgQYYlimuqWfpDNB.json'}

exec(code, env_args)
