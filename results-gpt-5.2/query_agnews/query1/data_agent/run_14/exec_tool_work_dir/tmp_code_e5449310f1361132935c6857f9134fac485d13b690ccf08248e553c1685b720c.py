code = """import json, pandas as pd

path = var_call_42w1U5VQuGQ3PMnvclmvZuhX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['description'] = df['description'].fillna('')
df['title'] = df['title'].fillna('')
# classify sports by keyword heuristics
sports_terms = [
    'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','olympics',
    'championship','tournament','coach','quarterback','touchdown','home run','goal','match','game','season','playoff','final',
    'f1','formula','grand prix','nascar','boxing','ufc','mma','cricket','rugby','world cup','cup','league'
]
pat = r'(?i)\\b(' + '|'.join([pd.regex.escape(t) for t in sports_terms]) + r')\\b'
# pandas doesn't have regex.escape; use re
import re
pat = r'(?i)\\b(' + '|'.join([re.escape(t) for t in sports_terms]) + r')\\b'
mask = df['title'].str.contains(pat, regex=True, na=False) | df['description'].str.contains(pat, regex=True, na=False)
# also include common team/athlete indicators
more_pat = r'(?i)\\b(player|team|scored|win|won|lost|beat|defeat|ranked|seeded|pitcher|striker|midfielder|goalkeeper)\\b'
mask = mask | df['title'].str.contains(more_pat, regex=True, na=False) | df['description'].str.contains(more_pat, regex=True, na=False)

dfs = df[mask].copy()
dfs['desc_len'] = dfs['description'].astype(str).map(len)
if len(dfs)==0:
    out = {"title": None, "article_id": None, "description_length": None}
else:
    row = dfs.sort_values('desc_len', ascending=False).iloc[0]
    out = {"title": row['title'], "article_id": row.get('article_id'), "description_length": int(row['desc_len'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_42w1U5VQuGQ3PMnvclmvZuhX': 'file_storage/call_42w1U5VQuGQ3PMnvclmvZuhX.json'}

exec(code, env_args)
