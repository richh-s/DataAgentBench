code = """import json, pandas as pd

path = var_call_fXtJBH4zIupOZ2FCHymb3EYF
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

def is_sports(title, desc):
    t = (title + ' ' + desc).lower()
    # exclude clear non-sports topics
    non = ['stock','stocks','oil','opec','ipo','dollar','trade deficit','economy','sales','mutual fund','aerospace','google','nuclear','telecom','interest rates','imf','refugee','inflation']
    if any(k in t for k in non):
        return False
    sports_kw = [
        'nba','nfl','mlb','nhl','ncaa','uefa','fifa','world cup','olympic','olympics','tennis','golf','soccer','football','baseball','basketball','hockey','cricket','rugby','formula one','f1','grand prix','nascar','cycling','tour de france','boxing','wrestling',
        'coach','quarterback','touchdown','home run','goal','goals','match','tournament','season','playoffs','championship','final','finals','league','cup','medal','race','win','wins','victory','defeat','draw',
        'yankees','red sox','lakers','celtics','patriots','cowboys','manchester','arsenal','chelsea','barcelona','real madrid'
    ]
    return any(k in t for k in sports_kw)

sports_mask = df.apply(lambda r: is_sports(r['title'], r['description']), axis=1)
sports_df = df[sports_mask].copy()

sports_df['desc_len'] = sports_df['description'].str.len()
if len(sports_df)==0:
    out = {"error":"No sports articles detected with heuristic keywords."}
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {"title": top['title'], "article_id": str(top['article_id']), "description_length": int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fXtJBH4zIupOZ2FCHymb3EYF': 'file_storage/call_fXtJBH4zIupOZ2FCHymb3EYF.json'}

exec(code, env_args)
