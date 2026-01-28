code = """import json, pandas as pd

path = var_call_2jhZSBRbairIg5bnELWgXNft
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def is_sports(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    txt = t + ' ' + d
    sports_kw = [
        'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby',
        'olympic','olympics','grand slam','fifa','uefa','premier league','la liga','serie a','bundesliga','champions league',
        'world cup','super bowl','touchdown','quarterback','pitcher','home run','goal','goals','coach','coaching','tournament',
        'match','matches','seed','playoff','playoffs','final','finals','semi-final','semifinal','ring','medal','medals',
        'athlete','athletes','sport','sports','race','racing','formula 1','f1','nascar','indy', 'boxing','ufc','mma','wrestling'
    ]
    # require at least one sports keyword and avoid obvious business/scitech/world-only contexts
    if not any(k in txt for k in sports_kw):
        return False
    # exclude stock-market "rally" etc.
    non_sports = ['stocks','wall st','nasdaq','dow','shares','earnings','oil prices','ipo','trade deficit','economy']
    if any(k in txt for k in non_sports) and not any(k in txt for k in ['team','season','game','match','tournament','coach','player','players','goal','touchdown','home run']):
        return False
    return True

sports_df = df[df.apply(lambda r: is_sports(r.get('title'), r.get('description')), axis=1)].copy()
if sports_df.empty:
    ans = ''
else:
    sports_df['desc_len'] = sports_df['description'].fillna('').map(len)
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    ans = top['title']

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_2jhZSBRbairIg5bnELWgXNft': 'file_storage/call_2jhZSBRbairIg5bnELWgXNft.json'}

exec(code, env_args)
