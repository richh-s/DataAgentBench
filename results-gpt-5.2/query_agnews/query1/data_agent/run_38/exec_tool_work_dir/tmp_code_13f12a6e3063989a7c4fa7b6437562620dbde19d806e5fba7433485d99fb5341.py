code = """import json, pandas as pd

path = var_call_R0G7zD91xjLcaGH7sO41eHQ1
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# normalize types
for c in ['title','description']:
    df[c] = df[c].fillna('')

df['desc_len'] = df['description'].astype(str).str.len()

# simple sports classifier by keywords in title/description
sports_kw = [
    'sport','sports','game','match','tournament','league','cup','nba','nfl','mlb','nhl','ncaa',
    'soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby','olympic','fifa',
    'coach','season','playoff','championship','goal','touchdown','quarterback','pitcher','home run',
    'wimbledon','us open','masters','grand slam','boxing','ufc','formula','nascar','motogp'
]
pat = r'(?i)\\b(' + '|'.join([pd.re.escape(k) for k in sports_kw]) + r')\\b'
mask = df['title'].astype(str).str.contains(pat, regex=True, na=False) | df['description'].astype(str).str.contains(pat, regex=True, na=False)

dfs = df[mask].copy()
if dfs.empty:
    out = {'error':'No sports articles detected with keyword heuristic.'}
else:
    top = dfs.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {'title': str(top['title']), 'article_id': str(top.get('article_id','')), 'description_length': int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_R0G7zD91xjLcaGH7sO41eHQ1': 'file_storage/call_R0G7zD91xjLcaGH7sO41eHQ1.json'}

exec(code, env_args)
