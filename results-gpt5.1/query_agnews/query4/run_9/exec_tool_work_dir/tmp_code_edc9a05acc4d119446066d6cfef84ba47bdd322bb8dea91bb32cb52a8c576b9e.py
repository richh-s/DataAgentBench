code = """import json, pandas as pd
from datetime import datetime

with open(var_call_n6CYRWFWmeRWokEUezNkxI37, 'r') as f:
    meta = json.load(f)
with open(var_call_IcGTlwuxaBvPRJVOooQvAd84, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

meta_df['year'] = pd.to_datetime(meta_df['publication_date']).dt.year
meta_2015 = meta_df[meta_df['year'] == 2015]

text = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

world_keywords = [
    'iraq','election','elections','president','prime minister','government','united nations','u.n.',
    'conflict','war','troops','terror','taliban','israel','palestinian','gaza','afghanistan','nuclear',
    'diplomat','diplomats','summit','parliament','protest','protests','rally','rallies','demonstration',
    'eu ', 'european union','u.s.','united states','china','russia','korea','iran','syria','ukraine',
    'bomb','suicide attack','military','missile','border','refugee','refugees','killed','dead','quake',
    'earthquake','hurricane','floods','tsunami','attack','violence','clashes','ceasefire','peace talks'
]

world_mask = text.apply(lambda t: any(k in t for k in world_keywords)).fillna(False)
arts_df['is_world'] = world_mask.astype(bool)

merged = meta_2015.merge(arts_df[['article_id','is_world']], on='article_id', how='left')
merged['is_world'] = merged['is_world'].fillna(False)
world_2015 = merged[merged['is_world'] == True]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = counts.index[0] if len(counts) > 0 else None

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_n6CYRWFWmeRWokEUezNkxI37': 'file_storage/call_n6CYRWFWmeRWokEUezNkxI37.json', 'var_call_IcGTlwuxaBvPRJVOooQvAd84': 'file_storage/call_IcGTlwuxaBvPRJVOooQvAd84.json'}

exec(code, env_args)
