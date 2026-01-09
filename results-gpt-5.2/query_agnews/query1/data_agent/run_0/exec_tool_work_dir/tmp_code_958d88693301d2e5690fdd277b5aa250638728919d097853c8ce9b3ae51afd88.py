code = """import json, pandas as pd

path = var_call_FcAxad2B7ai2RQ0gEDKZDzW6
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max()) if len(df) else 0
cand = df[df['desc_len']==max_len].copy()
# sports heuristic keyword match in title+description
text = (cand['title'] + ' ' + cand['description']).str.lower()
kw = [
    'vs', 'match', 'tournament', 'league', 'season', 'coach', 'quarterback', 'touchdown',
    'goal', 'goals', 'nba', 'nfl', 'mlb', 'nhl', 'uefa', 'fifa', 'olympic', 'olympics',
    'tennis', 'soccer', 'football', 'basketball', 'baseball', 'hockey', 'cricket', 'golf',
    'race', 'grand prix', 'boxing', 'ufc', 'wimbledon', 'super bowl', 'world cup'
]
mask_sports = False
for k in kw:
    mask_sports = mask_sports | text.str.contains(k)

sports_cand = cand[mask_sports]
# If none among max_len candidates, search globally among sports articles for longest desc
if len(sports_cand)==0:
    text_all = (df['title'] + ' ' + df['description']).str.lower()
    mask_all = False
    for k in kw:
        mask_all = mask_all | text_all.str.contains(k)
    sdf = df[mask_all].copy()
    sdf['desc_len'] = sdf['description'].str.len()
    max_len = int(sdf['desc_len'].max()) if len(sdf) else 0
    sports_cand = sdf[sdf['desc_len']==max_len]

# deterministically pick smallest article_id if ties
if len(sports_cand):
    # article_id may be str
    def to_int(x):
        try:
            return int(x)
        except:
            return None
    sports_cand['article_id_int'] = sports_cand['article_id'].apply(to_int)
    sports_cand = sports_cand.sort_values(['article_id_int','article_id','title'])
    title = sports_cand.iloc[0]['title']
else:
    title = None

print('__RESULT__:')
print(json.dumps({'title': title}, ensure_ascii=False))"""

env_args = {'var_call_FcAxad2B7ai2RQ0gEDKZDzW6': 'file_storage/call_FcAxad2B7ai2RQ0gEDKZDzW6.json'}

exec(code, env_args)
