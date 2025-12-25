code = """import json, pandas as pd

with open(var_call_1jg0S7tcRseynBmU3zovqy8J, 'r') as f:
    meta = json.load(f)
with open(var_call_DIzPU2nKW4ZyazbsONyCJAQm, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

meta_2015 = meta_df[meta_df['publication_date'].astype(str).str.startswith('2015-')]

world_keywords = ['iraq','war','election','president','prime minister','united nations','u.n.','israel','palestine','afghanistan','troops','rebel','militia','attack','bomb','killed','died','clashes','conflict','terror','protest','government','foreign','diplomat','nuclear','missile','taliban','al-qaeda','syria','ukraine','russia','eu','european union','china','india','pakistan','korea','summit','embassy','parliament','sanction','ceasefire','peace talks','border','refugee','crisis','coup']

text = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

def is_world(t):
    return any(k in t for k in world_keywords)

arts_df['is_world'] = text.apply(is_world)

merged = meta_2015.merge(arts_df[['article_id','is_world']], on='article_id', how='left')

merged['is_world'] = merged['is_world'].fillna(False)
world_2015 = merged[merged['is_world'] == True]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = counts.index[0] if not counts.empty else None

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1jg0S7tcRseynBmU3zovqy8J': 'file_storage/call_1jg0S7tcRseynBmU3zovqy8J.json', 'var_call_DIzPU2nKW4ZyazbsONyCJAQm': 'file_storage/call_DIzPU2nKW4ZyazbsONyCJAQm.json'}

exec(code, env_args)
