code = """import json
import pandas as pd

path = var_call_3WO8r7k2x7VR4z3H9CZenvMz
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].astype('string')

def is_sports(title, desc):
    t = f"{title} {desc}".lower()
    sports_kw = [
        'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf',
        'olympic','formula 1','f1','grand prix','cricket','rugby','coach','quarterback','touchdown',
        'home run','world cup','uefa','fifa','premier league','la liga','serie a','bundesliga','atp','wta',
        'slam','wimbledon','roland garros','us open','australian open','pga','lpga','masters',
        'yankees','red sox','lakers','celtics','warriors','knicks','cowboys','patriots','giants','jets',
        'arsenal','chelsea','manchester united','man city','barcelona','real madrid','juventus',
        'medal','tournament','match','league','season','playoff','finals'
    ]
    return any(k in t for k in sports_kw)

mask = df.apply(lambda r: is_sports(r['title'], r['description']), axis=1)
sports_df = df[mask].copy()

sports_df['desc_len'] = sports_df['description'].fillna('').map(lambda x: len(str(x)))
idx = sports_df['desc_len'].idxmax()
res_title = None if pd.isna(idx) else sports_df.loc[idx, 'title']

out = json.dumps({'title': None if res_title is None else str(res_title)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_3WO8r7k2x7VR4z3H9CZenvMz': 'file_storage/call_3WO8r7k2x7VR4z3H9CZenvMz.json'}

exec(code, env_args)
