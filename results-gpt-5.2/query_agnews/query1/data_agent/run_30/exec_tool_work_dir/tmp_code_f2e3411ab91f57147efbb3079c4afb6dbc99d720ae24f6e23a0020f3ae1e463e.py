code = """import json, pandas as pd

# load full articles list
p = var_call_7HtwF0TiTZJXLEF11sR0F0lO
with open(p, 'r', encoding='utf-8') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)
# normalize types
for col in ['title','description']:
    df[col] = df[col].fillna('')

# classify sports by simple keyword rules on title+description
text = (df['title'].astype(str) + ' ' + df['description'].astype(str)).str.lower()
kw = [
    'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','golf','tennis','cricket','rugby',
    'olympic','olympics','formula 1','f1','nascar','grand prix','uefa','fifa','world cup','super bowl','playoff','playoffs',
    'coach','quarterback','touchdown','home run','pitcher','goalkeeper','tournament','championship','league','match','game',
    'yankees','lakers','celtics','arsenal','chelsea','manchester','barcelona','real madrid'
]
pattern = '|'.join([pd.regex.escape(k) for k in kw])
# pandas doesn't have regex.escape; use re
import re
pattern = '|'.join([re.escape(k) for k in kw])

sports_mask = text.str.contains(pattern, regex=True)

dfs = df[sports_mask].copy()
dfs['desc_len'] = dfs['description'].astype(str).str.len()

if len(dfs)==0:
    out = {'title': None, 'article_id': None, 'description_length': None}
else:
    row = dfs.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {'title': row['title'], 'article_id': row.get('article_id'), 'description_length': int(row['desc_len'])}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_7HtwF0TiTZJXLEF11sR0F0lO': 'file_storage/call_7HtwF0TiTZJXLEF11sR0F0lO.json'}

exec(code, env_args)
