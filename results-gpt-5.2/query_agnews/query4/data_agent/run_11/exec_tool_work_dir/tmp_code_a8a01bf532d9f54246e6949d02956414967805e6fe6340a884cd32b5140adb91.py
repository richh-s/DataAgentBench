code = """import json, pandas as pd

# load metadata
meta_path = var_call_k05UVIN3wJ6Aex7ni9JNQuV0
with open(meta_path, 'r') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# load articles
art_path = var_call_AXLsBrPvGNfqUfPDAndjsAza
with open(art_path, 'r') as f:
    arts = json.load(f)
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# simple keyword-based classifier for World
text = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()
world_kw = [
    'war','attack','bomb','killed','kills','dead','death','terror','terrorist','isis','isil','taliban','al qaeda',
    'pakistan','india','china','russia','ukraine','iran','iraq','syria','israel','gaza','palestinian','afghanistan',
    'europe','britain','u.k.','france','germany','italy','spain','greece','turkey','egypt','nigeria','sudan',
    'u.n.','united nations','nato','election','president','parliament','prime minister','coup','rebel','military'
]
world_mask = False
for kw in world_kw:
    world_mask = world_mask | text.str.contains(kw, regex=False)
arts_df['is_world'] = world_mask

merged = meta_df.merge(arts_df[['article_id','is_world']], on='article_id', how='inner')
counts = merged[merged['is_world']].groupby('region').size().sort_values(ascending=False)
if counts.empty:
    result = {'region': None, 'world_articles': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_articles': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TpWaKGuLj6JoLzxZMbUuhqyk': ['authors', 'article_metadata'], 'var_call_k05UVIN3wJ6Aex7ni9JNQuV0': 'file_storage/call_k05UVIN3wJ6Aex7ni9JNQuV0.json', 'var_call_AXLsBrPvGNfqUfPDAndjsAza': 'file_storage/call_AXLsBrPvGNfqUfPDAndjsAza.json'}

exec(code, env_args)
