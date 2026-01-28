code = """import json, pandas as pd

# Load 2015 metadata
path_meta = var_call_yi0p5EDeBBZPkZ1cKUKuX0UC
with open(path_meta, 'r') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# Load articles
path_art = var_call_YnVI95updlbrUTFrJGcieipm
with open(path_art, 'r') as f:
    arts = json.load(f)
art_df = pd.DataFrame(arts)
art_df['article_id'] = art_df['article_id'].astype(int)

# Simple keyword-based categorization
world_kw = [
    'war','attack','bomb','terror','killed','kills','military','isis','iran','iraq','syria','afghan','pakistan','india','china','russia','ukraine','gaza','israel','palest','north korea','korea','nato','election','president','prime minister','parliament','u.n.','united nations','refugee','earthquake','tsunami','protest','revolt','coup','diplomat','embassy'
]
sports_kw = ['nfl','nba','mlb','nhl','olympic','olympics','soccer','football','baseball','basketball','tennis','golf','pimlico','stakes','race','wins','coach','league']
business_kw = ['ipo','stocks','stock','shares','deficit','trade','earnings','revenue','market','buy','sell','acquisition','merger','deal','company','corp','inc','profit','economy','oil','imports']
science_kw = ['nasa','space','spacecraft','genesis','planet','titan','climate','global warming','forest','tundra','study','scientists','dna','biology','astrobiology','technology','it ','software','java','fcc','spam','alert system']

def categorize(text):
    t = (text or '').lower()
    # prioritize world if strong world signals
    if any(k in t for k in world_kw):
        return 'World'
    if any(k in t for k in sports_kw):
        return 'Sports'
    if any(k in t for k in business_kw):
        return 'Business'
    if any(k in t for k in science_kw):
        return 'Science/Technology'
    # default fallback
    return 'Business'

art_df['text'] = (art_df['title'].fillna('') + ' ' + art_df['description'].fillna(''))
art_df['category'] = art_df['text'].map(categorize)

world_ids = set(art_df.loc[art_df['category']=='World','article_id'].tolist())
world_meta = meta_df[meta_df['article_id'].isin(world_ids)]

counts = world_meta.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    result = {"region": None, "world_article_count": 0}
else:
    top_region = counts.index[0]
    result = {"region": str(top_region), "world_article_count": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yi0p5EDeBBZPkZ1cKUKuX0UC': 'file_storage/call_yi0p5EDeBBZPkZ1cKUKuX0UC.json', 'var_call_YnVI95updlbrUTFrJGcieipm': 'file_storage/call_YnVI95updlbrUTFrJGcieipm.json'}

exec(code, env_args)
