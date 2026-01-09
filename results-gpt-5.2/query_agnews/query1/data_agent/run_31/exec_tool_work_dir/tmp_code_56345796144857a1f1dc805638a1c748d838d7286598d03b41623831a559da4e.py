code = """import json, pandas as pd

path = var_call_5caL0VgwEP7iHzZ8QZH0pTrI
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    sports_terms = [
        'nba','nfl','nhl','mlb','uefa','fifa','world cup','olympic','olympics','tennis','golf','soccer','football','baseball','basketball','hockey',
        'cricket','rugby','formula one','f1','nascar','grand slam','championship','coach','quarterback','touchdown','goal','match','tournament','playoff',
        'league','cup','innings','home run','pitcher','striker'
    ]
    return any(t in text for t in sports_terms)

sports_df = df[df.apply(is_sports, axis=1)].copy()
sports_df['desc_len'] = sports_df['description'].str.len()
if len(sports_df)==0:
    result = {'title': None, 'article_id': None, 'description_length': None}
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    result = {'title': top['title'], 'article_id': top['article_id'], 'description_length': int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_5caL0VgwEP7iHzZ8QZH0pTrI': 'file_storage/call_5caL0VgwEP7iHzZ8QZH0pTrI.json'}

exec(code, env_args)
