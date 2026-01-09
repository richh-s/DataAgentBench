code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_papN0t6lWUmdhidr8MZO1488)
records = json.loads(path.read_text())
df = pd.DataFrame(records)
# normalize types
for c in ['title','description']:
    df[c] = df[c].fillna('')
df['desc_len'] = df['description'].astype(str).str.len()
# sports heuristic keywords
sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf',
    'olympic','olympics','fifa','uefa','championship','tournament','match','game','season','playoff','coach',
    'team','league','cup','grand slam','race','nascar','formula','motogp','cricket','rugby','boxing','ufc','mma'
]
text = (df['title'].astype(str) + ' ' + df['description'].astype(str)).str.lower()
mask = False
for kw in sports_kw:
    mask = mask | text.str.contains(kw, regex=False)
# pick max description length among sports
sports_df = df[mask].copy()
if sports_df.empty:
    result = None
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    result = {'article_id': top['article_id'], 'title': top['title'], 'description_length': int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_papN0t6lWUmdhidr8MZO1488': 'file_storage/call_papN0t6lWUmdhidr8MZO1488.json'}

exec(code, env_args)
