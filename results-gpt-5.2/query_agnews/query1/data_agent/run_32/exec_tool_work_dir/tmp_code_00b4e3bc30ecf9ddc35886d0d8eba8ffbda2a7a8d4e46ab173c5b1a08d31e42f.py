code = """import json, pandas as pd

path = var_call_QJsMMQg6JKSHxThiAvM79wCs
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()

sports_keywords = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','olympics',
    'cricket','rugby','fifa','uefa','premier league','champions league','world cup',
    'coach','quarterback','touchdown','home run','pitcher','goal','match','game','season','playoff','final','team','player','championship'
]

def is_sports_text(text):
    t=text.lower()
    return any(k in t for k in sports_keywords)

# heuristic sports filter
mask = df.apply(lambda r: is_sports_text((r['title']+' '+r['description'])), axis=1)
sports_df = df[mask].copy()

if len(sports_df)==0:
    out={"error":"No sports articles detected by heuristic"}
else:
    max_len=int(sports_df['desc_len'].max())
    top=sports_df[sports_df['desc_len']==max_len].copy()
    top['article_id_int']=pd.to_numeric(top['article_id'], errors='coerce')
    top=top.sort_values(['article_id_int','title'])
    out={"title": top.iloc[0]['title'], "article_id": str(top.iloc[0]['article_id']), "desc_len": int(top.iloc[0]['desc_len'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QJsMMQg6JKSHxThiAvM79wCs': 'file_storage/call_QJsMMQg6JKSHxThiAvM79wCs.json', 'var_call_eu4VQHNnXmhLEiWHjzkavKgb': {'error': 'No sports article found among those with max description length', 'max_desc_len': 985, 'num_candidates': 1}}

exec(code, env_args)
