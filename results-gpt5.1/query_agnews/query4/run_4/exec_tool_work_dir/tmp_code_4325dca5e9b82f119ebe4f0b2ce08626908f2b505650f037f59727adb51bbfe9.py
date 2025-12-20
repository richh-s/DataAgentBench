code = """import json, pandas as pd

# Load full metadata and articles from their JSON files
with open(var_call_gXv7Q4KciQ3Dr34BBaWLH45X, 'r') as f:
    meta = json.load(f)
with open(var_call_uJTpg3MrCmwUJQx4soUe0qra, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter to 2015
meta_2015 = meta_df[meta_df['publication_date'].str.startswith('2015-')]

# Join with articles to get title & description
merged = meta_2015.merge(arts_df, on='article_id', how='inner')

# Very simple keyword-based classifier for 'World' category
# We'll treat as World if it mentions countries, wars, international orgs, diplomacy etc.
world_keywords = [
    'iraq','iran','afghanistan','sudan','darfur','israel','palestine','gaza','europe','asia','africa','latin america','united nations','u.n.','u.n','un ',
    'eu ','european union','refugee','refugees','war','conflict','military','troops','terror','al-qaeda','taliban','bomb','attacks','border','diplomat','diplomacy',
    'korea','china','japan','russia','ukraine','syria','pakistan','india','saudi','arabia','yemen','global','world ','foreign','embassy','nato','allies','alliance'
]

text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

def is_world(t):
    return any(k in t for k in world_keywords)

merged['is_world'] = text.apply(is_world)

world_2015 = merged[merged['is_world']]

# Count by region
counts = world_2015.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = None
else:
    top_region = counts.idxmax()
    result = top_region

res_json = json.dumps(result)

print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_gXv7Q4KciQ3Dr34BBaWLH45X': 'file_storage/call_gXv7Q4KciQ3Dr34BBaWLH45X.json', 'var_call_uJTpg3MrCmwUJQx4soUe0qra': 'file_storage/call_uJTpg3MrCmwUJQx4soUe0qra.json'}

exec(code, env_args)
