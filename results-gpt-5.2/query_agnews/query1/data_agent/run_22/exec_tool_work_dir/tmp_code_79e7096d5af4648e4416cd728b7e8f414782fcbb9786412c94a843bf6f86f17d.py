code = """import json, pandas as pd

path = var_call_8a6frjBw3KHXlOub7YFAjyGf
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# coerce to strings safely
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].map(len)
max_len = int(df['desc_len'].max()) if len(df) else 0
candidates = df[df['desc_len'] == max_len]
# need sports article among those; classify by keyword heuristics from title/description
text = (candidates['title'] + ' ' + candidates['description']).str.lower()
# sports keywords
kw = ['sport','nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olymp','fifa','uefa','cricket','rugby','formula','grand prix','nascar','wimbledon','world cup','coach','quarterback','touchdown','goal','match','tournament','league','championship','playoff','yankees','lakers','celtics','arsenal','chelsea','manchester','madrid','barcelona']
mask = False
for k in kw:
    mask = mask | text.str.contains(k, regex=False)

sports_candidates = candidates[mask]
# If none among max-len tied, find overall sports max
if len(sports_candidates)==0:
    df_text = (df['title'] + ' ' + df['description']).str.lower()
    mask_all = False
    for k in kw:
        mask_all = mask_all | df_text.str.contains(k, regex=False)
    sdf = df[mask_all].copy()
    if len(sdf)==0:
        out = {"error":"No sports articles detected"}
    else:
        sdf['desc_len']=sdf['description'].map(len)
        row = sdf.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
        out = {"title": row['title'], "description_length": int(row['desc_len']), "article_id": row.get('article_id')}
else:
    row = sports_candidates.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {"title": row['title'], "description_length": int(row['desc_len']), "article_id": row.get('article_id')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8a6frjBw3KHXlOub7YFAjyGf': 'file_storage/call_8a6frjBw3KHXlOub7YFAjyGf.json'}

exec(code, env_args)
