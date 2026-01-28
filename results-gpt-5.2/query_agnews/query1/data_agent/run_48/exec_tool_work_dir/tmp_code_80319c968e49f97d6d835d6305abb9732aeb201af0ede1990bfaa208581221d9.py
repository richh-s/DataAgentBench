code = """import json
import pandas as pd
import re

path = var_call_poxO0OutWFtTReCgNMUnB6Y7
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

text = (df['title'] + ' ' + df['description']).str.lower()

sports_keywords = [
    'nba','nfl','mlb','nhl','ncaa','uefa','fifa','world cup','olympic','olympics','tennis','golf','soccer','football','basketball','baseball','hockey','cricket','rugby','formula 1','f1','nascar','grand slam',
    'coach','quarterback','touchdown','home run','pitcher','goal','match','tournament','playoffs','championship','league','cup','medal','athlete','team','season','game'
]
pattern = '|'.join([re.escape(k) for k in sports_keywords])
is_sports = text.str.contains(pattern, regex=True)

sports_df = df[is_sports].copy()
sports_df['desc_len'] = sports_df['description'].str.len()

if len(sports_df)==0:
    best = df.assign(desc_len=df['description'].str.len()).sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {'title': best['title'], 'article_id': best.get('article_id'), 'description_length': int(best['desc_len']), 'note': 'No sports articles matched heuristic; returned overall longest description.'}
else:
    best = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {'title': best['title'], 'article_id': best.get('article_id'), 'description_length': int(best['desc_len'])}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_poxO0OutWFtTReCgNMUnB6Y7': 'file_storage/call_poxO0OutWFtTReCgNMUnB6Y7.json'}

exec(code, env_args)
