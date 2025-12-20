code = """import json, pandas as pd

with open(var_call_AubQggcSXzxjAVSbDXFcqktI, 'r') as f:
    metadata = json.load(f)
with open(var_call_o7wJuIY8FZpiXkvrcw4zP0I0, 'r') as f:
    articles = json.load(f)

md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

md['article_id'] = md['article_id'].astype(int)
art['article_id'] = art['article_id'].astype(int)

md['year'] = md['publication_date'].str.slice(0,4).astype(int)
md_2015 = md[md['year'] == 2015]

world_keywords = ['iraq','iran','afghanistan','war','election','president','minister','united nations','u.n.','taliban','al-qaeda','gaza','israel','palestinian','terror','bomb','attack','peace talks','summit','diplomat','nuclear','missile','korea','russia','china','european union','eu summit','conference','world leaders','prime minister']

text = (art['title'].fillna('') + ' ' + art['description'].fillna('')).str.lower()

def is_world(t):
    try:
        return any(k in t for k in world_keywords)
    except Exception:
        return False

art['is_world'] = text.apply(is_world).fillna(False).astype(bool)

merged = md_2015.merge(art[['article_id','is_world']], on='article_id', how='left')
merged['is_world'] = merged['is_world'].fillna(False).astype(bool)

world_2015 = merged[merged['is_world']]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = counts.index[0] if len(counts) else None

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AubQggcSXzxjAVSbDXFcqktI': 'file_storage/call_AubQggcSXzxjAVSbDXFcqktI.json', 'var_call_o7wJuIY8FZpiXkvrcw4zP0I0': 'file_storage/call_o7wJuIY8FZpiXkvrcw4zP0I0.json'}

exec(code, env_args)
