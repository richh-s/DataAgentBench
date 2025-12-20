code = """import json, pandas as pd

# Load full results if they are file paths
meta_path = var_call_aBH2FrAmcmuNwfkz8Xn08JkQ
arts_path = var_call_5QUE1U8K4CE9l9phzbFIbD8T

with open(meta_path, 'r') as f:
    meta = json.load(f)
with open(arts_path, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Very naive World-category heuristic: presence of certain keywords in title/description
world_keywords = ['iraq','afghan','afghanistan','war','election','president','government','united nations','u.n.','u.n','european union','eu ', 'eu,', 'europe', 'asia', 'africa', 'latin america', 'israel', 'palestinian', 'russia', 'ukraine', 'china', 'japan', 'korea', 'terror','bomb','conflict','refugee','summit']

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

pattern = '|'.join([k.replace(' ', '\\s+') for k in world_keywords])

arts_df['is_world'] = arts_df['text'].str.contains(pattern, regex=True)

world_ids = set(arts_df.loc[arts_df['is_world'], 'article_id'].tolist())

world_meta = meta_df[meta_df['article_id'].isin(world_ids)]

counts = world_meta.groupby('region').size().sort_values(ascending=False)

result_region = counts.index[0] if not counts.empty else None

out = {'region_with_most_world_articles_2015': result_region}

res_json = json.dumps(out)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_aBH2FrAmcmuNwfkz8Xn08JkQ': 'file_storage/call_aBH2FrAmcmuNwfkz8Xn08JkQ.json', 'var_call_5QUE1U8K4CE9l9phzbFIbD8T': 'file_storage/call_5QUE1U8K4CE9l9phzbFIbD8T.json'}

exec(code, env_args)
