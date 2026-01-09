code = """import json, pandas as pd
path = var_call_Fqo7NI4i7n4tXGxgLz7qMOYE
with open(path,'r',encoding='utf-8') as f:
    records = json.load(f)
df = pd.DataFrame(records)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)
# crude sports classifier
sports_terms = [
    'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics','fifa','uefa','cricket','rugby','formula','nascar','gp','grand slam','atp','wta','mls',
    'coach','season','playoff','playoffs','tournament','match','game','games','win','loss','team','teams','league','champion','championship','cup','final','finals','quarterback','touchdown','home run','pitcher','goal','goals','innings','points','ranked','ranking'
]
pat = r'(?i)\\b(' + '|'.join([t.replace(' ','\\s+') for t in sports_terms]) + r')\\b'
df['is_sports'] = df['title'].str.contains(pat, regex=True) | df['description'].str.contains(pat, regex=True)
sports_df = df[df['is_sports']].copy()
sports_df['desc_len'] = sports_df['description'].str.len()
idx = sports_df['desc_len'].idxmax()
answer = sports_df.loc[idx,'title'] if pd.notna(idx) else None
print('__RESULT__:')
print(json.dumps({'title': answer, 'max_description_length': int(sports_df.loc[idx,'desc_len']) if pd.notna(idx) else None}))"""

env_args = {'var_call_Fqo7NI4i7n4tXGxgLz7qMOYE': 'file_storage/call_Fqo7NI4i7n4tXGxgLz7qMOYE.json'}

exec(code, env_args)
