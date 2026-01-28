code = """import json, pandas as pd
path = var_call_K3vXzmLxFe5TckkJNz4rH9kb
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.DataFrame(data)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)
# simple sports classifier by keyword
sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','olympics',
    'coach','quarterback','touchdown','home run','world cup','uefa','fifa','formula','grand prix','nascar','boxing',
    'wimbledon','super bowl','playoffs','final','semifinal','tournament','league','championship','match','cup','wins','victory'
]
pat = '|'.join([k.replace(' ','\\s+') for k in sports_kw])
mask = df['title'].str.contains(pat, case=False, regex=True) | df['description'].str.contains(pat, case=False, regex=True)
sports = df[mask].copy()
sports['desc_len'] = sports['description'].str.len()
# if no sports found, fallback to all
use = sports if len(sports)>0 else df
row = use.loc[use['desc_len'].idxmax()]
result = {'title': row['title'], 'article_id': row.get('article_id', None), 'desc_len': int(row['desc_len']), 'sports_count': int(len(sports))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_K3vXzmLxFe5TckkJNz4rH9kb': 'file_storage/call_K3vXzmLxFe5TckkJNz4rH9kb.json'}

exec(code, env_args)
