code = """import json, pandas as pd

path = var_call_JRcWrCYtVZp5AXFnoBC0bpgq
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
df['title'] = df.get('title','').fillna('').astype(str)
df['description'] = df.get('description','').fillna('').astype(str)

def is_sports(row):
    t = (row['title'] + ' ' + row['description']).lower()
    kws = ['nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics',
           'cricket','rugby','fifa','uefa','premier league','la liga','serie a','bundesliga','coach','quarterback',
           'touchdown','home run','grand slam','world cup','stanley cup','super bowl','world series',
           'tournament','match','game','team','player','season','playoff','league']
    return any(kw in t for kw in kws)

sports_df = df[df.apply(is_sports, axis=1)].copy()
sports_df['desc_len'] = sports_df['description'].str.len()
max_len = int(sports_df['desc_len'].max()) if len(sports_df) else None
if max_len is None:
    out = {'title': None, 'article_id': None, 'description_length': None, 'note': 'No sports articles detected by heuristic.'}
else:
    chosen = sports_df[sports_df['desc_len']==max_len].iloc[0]
    out = {'title': chosen['title'], 'article_id': str(chosen.get('article_id','')), 'description_length': int(chosen['desc_len'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JRcWrCYtVZp5AXFnoBC0bpgq': 'file_storage/call_JRcWrCYtVZp5AXFnoBC0bpgq.json', 'var_call_fq8QX5R8uZgDlx1xu2fBtbEk': {'title': 'Making RSS Scale', 'article_id': '19776', 'description_length': 985}}

exec(code, env_args)
