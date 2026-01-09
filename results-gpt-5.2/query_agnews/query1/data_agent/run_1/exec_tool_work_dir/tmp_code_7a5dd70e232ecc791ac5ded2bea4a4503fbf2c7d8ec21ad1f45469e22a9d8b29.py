code = """import json
import pandas as pd

path = var_call_St3C2pOl7ksP4MW9tpgsIlSf
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

def is_sports(text: str) -> bool:
    t = text.lower()
    keywords = [
        'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','cricket','rugby',
        'olympic','olympics','fifa','uefa','premier league','la liga','serie a','bundesliga','champions league',
        'coach','quarterback','touchdown','home run','grand slam','tournament','match','season','playoffs','final','championship',
        'athlete','athletics','race','grand prix','formula one','f1','nascar','motogp','boxing','ufc','mma','wrestling'
    ]
    return any(k in t for k in keywords)

sport_mask = df.apply(lambda r: is_sports(r['title'] + ' ' + r['description']), axis=1)
sp = df[sport_mask].copy()
sp['desc_len'] = sp['description'].map(len)
if sp.empty:
    result = {'title': None}
else:
    # greatest number of characters; tie-break by first occurrence
    top = sp.sort_values(['desc_len'], ascending=False).iloc[0]
    result = {'title': top['title']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_St3C2pOl7ksP4MW9tpgsIlSf': 'file_storage/call_St3C2pOl7ksP4MW9tpgsIlSf.json'}

exec(code, env_args)
