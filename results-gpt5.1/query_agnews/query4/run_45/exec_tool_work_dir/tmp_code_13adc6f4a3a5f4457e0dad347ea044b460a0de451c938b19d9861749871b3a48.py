code = """import json, pandas as pd

# Load full results from files
with open(var_call_Qc8i39376K2TClTIfCdZPkfS, 'r') as f:
    meta = json.load(f)
with open(var_call_h8K4gAEiU9gCbTe2dZRFD3JS, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter metadata for 2015
meta_2015 = meta_df[meta_df['publication_date'].str.startswith('2015-')]

# Very naive World-category heuristic: keywords related to politics, countries, wars, diplomacy, global orgs, etc.
world_keywords = [
    'iraq','afghanistan','united nations','u.n.','u.n','un ','conflict','war','wars','troops','terror','election','elections',
    'president','prime minister','parliament','diplomat','diplomacy','summit','nato','european union','eu ',
    'israel','palestinian','gaza','west bank','sudan','darfur','refugee','refugees','china','russia','pakistan','india',
    'korea','iran','syria','lebanon','jerusalem','baghdad','bomb','bombing','attack','attacks','politics','government',
    'foreign policy','embassy','sanction','sanctions','nuclear','missile','missiles','coup','rebel','rebels','u.s. ',
    'us ', 'u.s.-','border','international','global summit','world leaders','terrorist','al-qaeda','taliban'
]

text_df = arts_df[['article_id','title','description']].copy()
text_df['text'] = (text_df['title'].fillna('') + ' ' + text_df['description'].fillna('')).str.lower()

pattern = '|'.join([k.replace(' ','\\s+') for k in world_keywords])

text_df['is_world'] = text_df['text'].str.contains(pattern, regex=True, na=False)

# Join with 2015 metadata
merged = meta_2015.merge(text_df[['article_id','is_world']], on='article_id', how='left')

world_2015 = merged[merged['is_world']]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_Qc8i39376K2TClTIfCdZPkfS': 'file_storage/call_Qc8i39376K2TClTIfCdZPkfS.json', 'var_call_h8K4gAEiU9gCbTe2dZRFD3JS': 'file_storage/call_h8K4gAEiU9gCbTe2dZRFD3JS.json'}

exec(code, env_args)
