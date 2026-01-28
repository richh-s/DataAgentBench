code = """import json, pandas as pd

path = var_call_aHdXyXPpBYFaSCvWJft71Znl
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby',
        'olympic','olympics','grand slam','fifa','uefa','champions league','premier league','la liga','serie a',
        'world cup','super bowl','stanley cup','playoffs','tournament','coach','quarterback','touchdown','home run',
        'goal','match','game','season','league','championship','medal','athlete','team','win','loss','draw'
    ]
    return any(t in text for t in sports_terms)

sports_df = df[df.apply(is_sports, axis=1)].copy()
sports_df['desc_len'] = sports_df['description'].str.len()

if len(sports_df)==0:
    result = {'title': None}
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    result = {'title': top['title'], 'article_id': int(top['article_id']) if str(top['article_id']).isdigit() else top['article_id'], 'description_length': int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aHdXyXPpBYFaSCvWJft71Znl': 'file_storage/call_aHdXyXPpBYFaSCvWJft71Znl.json'}

exec(code, env_args)
