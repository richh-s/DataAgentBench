code = """import json, pandas as pd
from pathlib import Path

# Load full results
articles_path = Path(var_call_Fs40nC1d0WeEoziYm3jyVdmY)
with open(articles_path, 'r') as f:
    articles = json.load(f)

meta_path = Path(var_call_0I4THkLhKfMZ2dsOOGtbFZEW)
with open(meta_path, 'r') as f:
    meta = json.load(f)

# Build dataframes
articles_df = pd.DataFrame(articles)[['article_id','title','description']]
articles_df['article_id'] = articles_df['article_id'].astype(int)

meta_df = pd.DataFrame(meta)[['article_id','region','publication_date']]
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Simple heuristic to classify World vs other categories based on keywords
world_keywords = ['iraq','europe','africa','asia','china','russia','election','war','united nations','u.n.','eu ', 'european union','taliban','israel','palestinian','bomb','attack','military','middle east','rebel','pakistan','india','afghan','global','world']

def is_world(text):
    if not isinstance(text,str):
        return False
    t = text.lower()
    return any(k in t for k in world_keywords)

articles_df['is_world'] = articles_df['title'].apply(is_world) | articles_df['description'].apply(is_world)

# Join and filter for 2015 World articles
merged = meta_df.merge(articles_df, on='article_id', how='inner')
world_2015 = merged[(merged['year'] == 2015) & (merged['is_world'])]

# Count by region
counts = world_2015.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = {'region': None, 'count': 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    result = {'region': top_region, 'count': top_count}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Fs40nC1d0WeEoziYm3jyVdmY': 'file_storage/call_Fs40nC1d0WeEoziYm3jyVdmY.json', 'var_call_0I4THkLhKfMZ2dsOOGtbFZEW': 'file_storage/call_0I4THkLhKfMZ2dsOOGtbFZEW.json'}

exec(code, env_args)
