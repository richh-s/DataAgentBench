code = """import json, pandas as pd

# Load full metadata
with open(var_call_EP54IoHNjbkkQ8Tq8Akaxf8h, 'r') as f:
    metadata = json.load(f)

# Load full articles
with open(var_call_wDCNi2W9HpEO1pEUC5tPnW0d, 'r') as f:
    articles = json.load(f)

md = pd.DataFrame(metadata)
art = pd.DataFrame(articles)

# Ensure correct dtypes
md['article_id'] = md['article_id'].astype(int)
art['article_id'] = art['article_id'].astype(int)

# Filter to 2015
md['year'] = md['publication_date'].str.slice(0,4).astype(int)
md_2015 = md[md['year'] == 2015]

# Very simple keyword-based classifier for World category
# Heuristic: contains words related to countries, conflicts, diplomacy, global orgs, etc.
world_keywords = [
    'iraq','saudi','korea','darfur','refugee','united nations','u.n.','un ',
    'eu ','european union','israel','palestinian','afghan','terror','war ',
    'missile','nuclear','election','president','prime minister','government',
    'parliament','protest','rebel','militia','taliban','security council',
    'gaza','west bank','iran','sudan','syria','pakistan','russia','china',
    'japan','africa','asia','europe','latin america','diplomat','embassy',
    'summit','treaty','border','clash','bomb','suicide','attack','insurgent',
]

def is_world(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    return any(k in t for k in world_keywords)

art['is_world'] = art['title'].apply(is_world) | art['description'].apply(is_world)

# Join with 2015 metadata
merged = md_2015.merge(art[['article_id','is_world']], on='article_id', how='left')

world_2015 = merged[merged['is_world']]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = {
    'region_with_most_world_articles_2015': counts.index[0] if len(counts) > 0 else None,
    'counts_by_region': counts.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EP54IoHNjbkkQ8Tq8Akaxf8h': 'file_storage/call_EP54IoHNjbkkQ8Tq8Akaxf8h.json', 'var_call_wDCNi2W9HpEO1pEUC5tPnW0d': 'file_storage/call_wDCNi2W9HpEO1pEUC5tPnW0d.json'}

exec(code, env_args)
