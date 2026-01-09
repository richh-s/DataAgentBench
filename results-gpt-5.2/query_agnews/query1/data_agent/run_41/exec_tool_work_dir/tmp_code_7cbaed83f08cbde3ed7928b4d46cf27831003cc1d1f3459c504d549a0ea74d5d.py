code = """import json, pandas as pd
path = var_call_CDmRh54PrMYGpMC4P9kiTs2W
with open(path,'r',encoding='utf-8') as f:
    records = json.load(f)
df = pd.DataFrame(records)
# classify sports via keyword heuristics
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
keywords = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','golf','tennis','cricket','rugby','olympic',
    'championship','tournament','league','season','coach','player','team','match','game','wins','win','loss','score','scored',
    'fielder','pitcher','quarterback','touchdown','home run','grand slam','stanley cup','world cup','fifa','uefa','atp','wta',
    'nascar','formula one','f1','grand prix','boxing','ufc','mma','wrestling','track and field','marathon'
]
pat = r'(' + '|'.join([k.replace(' ','\\s+') for k in keywords]) + r')'
is_sports = text.str.contains(pat, regex=True)
sports_df = df[is_sports].copy()
# compute description length
sports_df['desc_len'] = sports_df['description'].fillna('').map(len)
max_len = sports_df['desc_len'].max() if len(sports_df) else None
best = sports_df[sports_df['desc_len']==max_len].sort_values(['article_id','title']).head(1)
answer = best['title'].iloc[0] if len(best) else None
print('__RESULT__:')
print(json.dumps({'title': answer, 'max_description_length': int(max_len) if max_len is not None else None}))"""

env_args = {'var_call_CDmRh54PrMYGpMC4P9kiTs2W': 'file_storage/call_CDmRh54PrMYGpMC4P9kiTs2W.json'}

exec(code, env_args)
