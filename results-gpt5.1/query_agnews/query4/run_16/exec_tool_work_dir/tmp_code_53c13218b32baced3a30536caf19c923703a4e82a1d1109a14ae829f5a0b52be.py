code = """import json, pandas as pd
from pathlib import Path

# Load full results
meta_path = Path(var_call_fA8rkRGNJRp3a7dBbx2Qimsw)
arts_path = Path(var_call_jSxfa53MzY5GcPjmkiqPxdNt)

metadata = json.loads(meta_path.read_text())
articles = json.loads(arts_path.read_text())

mdf = pd.DataFrame(metadata)
adf = pd.DataFrame(articles)

# Ensure types
mdf['article_id'] = mdf['article_id'].astype(int)
adf['article_id'] = adf['article_id'].astype(int)

# Very naive World-category heuristic: presence of country/region/conflict/politics terms
world_keywords = ['iraq','iran','europe','asia','africa','america','united nations','u.n.','u.n','israel','palestinian','election','president','government','minister','war','conflict','rebels','militia','bomb','attacks','taliban','afghan','russia','china','japan','korea','gaza','sudan','refugee']

text = (adf['title'].fillna('') + ' ' + adf['description'].fillna('')).str.lower()

is_world = text.apply(lambda t: any(k in t for k in world_keywords))

world_ids = adf.loc[is_world, 'article_id']

# Filter metadata for 2015 and world articles
mdf['year'] = mdf['publication_date'].str.slice(0,4).astype(int)

mdf_2015_world = mdf[(mdf['year'] == 2015) & (mdf['article_id'].isin(world_ids))]

counts = mdf_2015_world.groupby('region').size().sort_values(ascending=False)

result = {
    'region_with_max_world_articles_2015': None if counts.empty else counts.index[0],
    'counts_by_region_2015_world': counts.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fA8rkRGNJRp3a7dBbx2Qimsw': 'file_storage/call_fA8rkRGNJRp3a7dBbx2Qimsw.json', 'var_call_jSxfa53MzY5GcPjmkiqPxdNt': 'file_storage/call_jSxfa53MzY5GcPjmkiqPxdNt.json'}

exec(code, env_args)
