code = """import json, pandas as pd

path = var_call_pZDDscv8pWwtc22y9G1uNcHX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','ncaa','soccer','football','basketball','baseball','hockey','tennis','golf',
        'olympic','olympics','world cup','uefa','fifa','cricket','rugby','formula 1','f1','grand prix','nascar',
        'coach','quarterback','touchdown','home run','goal','match','tournament','playoffs','league','championship'
    ]
    return any(t in text for t in sports_terms)

sports_df = df[df.apply(is_sports, axis=1)].copy()
sports_df['desc_len'] = sports_df['description'].map(len)

if sports_df.empty:
    result = {'title': None, 'max_description_characters': None}
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    result = {'title': top['title'], 'max_description_characters': int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_pZDDscv8pWwtc22y9G1uNcHX': 'file_storage/call_pZDDscv8pWwtc22y9G1uNcHX.json'}

exec(code, env_args)
