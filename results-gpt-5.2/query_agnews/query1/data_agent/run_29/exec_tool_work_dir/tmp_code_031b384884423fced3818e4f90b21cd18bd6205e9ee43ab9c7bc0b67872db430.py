code = """import json, pandas as pd
path = var_call_nHclE2gw1zAVGPAsaV9BaNQU
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.DataFrame(data)
# classify sports by keyword heuristics
sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics',
    'cricket','rugby','f1','formula','nascar','grand slam','uefa','fifa','world cup','super bowl','playoffs','tournament',
    'match','game','season','coach','quarterback','goal','scored','league','cup','athlete','team','teams','player','players'
]
pat = '|'.join([rf"\\b{pd.regex.escape(k)}\\b" for k in sports_kw])
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
is_sports = text.str.contains(pat, regex=True)
df_sports = df[is_sports].copy()
df_sports['desc_len'] = df_sports['description'].fillna('').astype(str).str.len()
if len(df_sports)==0:
    result = {'title': None}
else:
    top = df_sports.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    result = {'title': top['title'], 'article_id': top['article_id'], 'desc_len': int(top['desc_len'])}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_nHclE2gw1zAVGPAsaV9BaNQU': 'file_storage/call_nHclE2gw1zAVGPAsaV9BaNQU.json'}

exec(code, env_args)
