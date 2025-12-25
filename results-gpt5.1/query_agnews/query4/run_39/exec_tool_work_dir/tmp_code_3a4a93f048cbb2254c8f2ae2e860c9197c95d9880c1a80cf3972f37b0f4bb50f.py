code = """import json, pandas as pd
from datetime import datetime

# Load full results if stored in external files
meta_path = var_call_w8fBNpWbWdoAPAEicYhiXlZv
arts_path = var_call_wXNrG4uYYnenUvU3jNZSYBzU

with open(meta_path, 'r') as f:
    meta = json.load(f)
with open(arts_path, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter to 2015
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Merge with article text
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Very naive category classifier for "World" vs others
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Keywords suggesting World news (politics, conflicts, international orgs, countries, elections, disasters, diplomacy)
world_keywords = [
    'iraq','iran','afghanistan','syria','israel','palestinian','gaza','terror','attack','bomb','war','military','troop',
    'president','prime minister','election','parliament','government','protest','rebel','militia','ceasefire',
    'united nations','u.n.','un chief','un council','security council','nato','eu ', 'european union',
    'diplomat','diplomatic','embassy','border','refugee','summit','crisis','conflict','clash','coup','killed','dead','death toll',
    'storm','earthquake','tsunami','hurricane','typhoon','flood','wildfire',
    'north korea','south korea','china','russia','ukraine','pakistan','india','japan','britain','france','germany','spain','italy',
    'saudi','qatar','yemen','libya','sudan','darfur','congo','kenya','nigeria','mexico','brazil','argentina','venezuela'
]

# Sports/business/sci-tech cues to EXCLUDE when dominant
non_world_keywords = [
    'stock','stocks','market','shares','profit','loss','quarter','earnings','ipo','bond','currency','dollar','euro',
    'merger','acquisition','bank','fund','ceo','company','firm','corp','inc.',
    'football','soccer','nba','nfl','mlb','nhl','olympic','world cup','tennis','golf','cricket','baseball','basketball','coach',
    'tournament','league','season','match','game','goal','score',
    'scientist','researchers','study finds','clinical trial','vaccine','space','nasa','astronaut','galaxy','planet',
    'software','computer','internet','online','technology','tech','app','smartphone','social media','google','microsoft','apple'
]

text_list = text.tolist()

world_flags = []
for t in text_list:
    tl = t.lower()
    w_hits = sum(1 for kw in world_keywords if kw in tl)
    n_hits = sum(1 for kw in non_world_keywords if kw in tl)
    world_flags.append(w_hits > 0 and w_hits >= n_hits)

df['is_world'] = world_flags

world_df = df[df['is_world']]

counts = world_df.groupby('region').size().sort_values(ascending=False)

if not counts.empty:
    top_region = counts.index[0]
else:
    top_region = None

result = json.dumps({"top_region_2015_world": top_region})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_w8fBNpWbWdoAPAEicYhiXlZv': 'file_storage/call_w8fBNpWbWdoAPAEicYhiXlZv.json', 'var_call_wXNrG4uYYnenUvU3jNZSYBzU': 'file_storage/call_wXNrG4uYYnenUvU3jNZSYBzU.json'}

exec(code, env_args)
