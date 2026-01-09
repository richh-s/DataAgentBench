code = """import json, pandas as pd

path = var_call_hKVtOc29TORP25yMgYhZaq9l
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)
# Ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max())
# candidates
cand = df[df['desc_len'] == max_len].copy()

# sports keyword heuristic on title+description
text = (cand['title'] + ' ' + cand['description']).str.lower()
keywords = [
    'sport','sports','game','team','season','match','tournament','league','cup','championship','coach','player','quarterback','touchdown','goal','nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','fifa','uefa','cricket','rugby','nascar','formula','grand prix','boxing','mma','ufc','wwe'
]
mask = False
for k in keywords:
    mask = mask | text.str.contains(k, regex=False)

sports_cand = cand[mask]
result = {
    'max_description_length': max_len,
    'num_articles_with_max_length': int(len(cand)),
    'num_sports_articles_with_max_length': int(len(sports_cand)),
    'titles': sports_cand['title'].tolist() if len(sports_cand)>0 else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hKVtOc29TORP25yMgYhZaq9l': 'file_storage/call_hKVtOc29TORP25yMgYhZaq9l.json'}

exec(code, env_args)
