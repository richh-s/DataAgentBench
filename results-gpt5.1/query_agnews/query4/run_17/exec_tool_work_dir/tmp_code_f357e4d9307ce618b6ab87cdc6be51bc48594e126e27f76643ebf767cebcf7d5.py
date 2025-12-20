code = """import json, pandas as pd
from collections import Counter

# Load full results from JSON files
with open(var_call_1Ns3F4HEW5M5mgithNqdQ1FB, 'r') as f:
    meta = json.load(f)
with open(var_call_TeIGS3i4Dc8OaozIp4cOtrB1, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# ensure article_id comparable
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# very simple World-category heuristic: presence of certain world/geo/politics terms
world_keywords = ['iraq','war','president','election','palestinian','israel','government','minister','military','troops','terror','conflict','united nations','u.n.','UN ','UN.', 'global','world','international','diplomat','afghanistan','nuclear','gaza','taliban','al-qaeda','al qaeda']

def is_world(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(k in text for k in world_keywords)

arts_df['is_world'] = arts_df.apply(is_world, axis=1)

world_ids = set(arts_df[arts_df['is_world']]['article_id'].tolist())

world_meta_2015 = meta_df[meta_df['article_id'].isin(world_ids)]

counts = world_meta_2015['region'].value_counts().to_dict()

if counts:
    top_region = max(counts.items(), key=lambda x: x[1])[0]
else:
    top_region = None

result = json.dumps({'top_region_2015_world': top_region, 'counts': counts})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_1Ns3F4HEW5M5mgithNqdQ1FB': 'file_storage/call_1Ns3F4HEW5M5mgithNqdQ1FB.json', 'var_call_TeIGS3i4Dc8OaozIp4cOtrB1': 'file_storage/call_TeIGS3i4Dc8OaozIp4cOtrB1.json'}

exec(code, env_args)
