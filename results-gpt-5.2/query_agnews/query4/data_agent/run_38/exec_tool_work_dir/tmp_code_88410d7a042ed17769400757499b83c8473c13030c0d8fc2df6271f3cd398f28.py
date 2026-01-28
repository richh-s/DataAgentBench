code = """import json, pandas as pd

# Load metadata 2015
meta_src = var_call_V9oprOKMf4cVwygJ9T61J2rL
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

art_src = var_call_sKrFEnIbbc1KaHsDG5H4kooR
if isinstance(art_src, str):
    with open(art_src, 'r') as f:
        arts = json.load(f)
else:
    arts = art_src

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id comparable
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palest','gaza','syria','syrian','ukraine','russia','moscow','putin',
    'european union','eu ','nato','united nations','u.n.','un ','diplom','minister','president',
    'election','parliament','rebel','militant','terror','bomb','attack','war','peace','sanction',
    'summit','foreign','refugee','border','embassy','china','beijing','japan','tokyo','korea',
    'afghanistan','pakistan','india','turkey','egypt','saudi','yemen','libya','sudan','congo',
    'britain','uk ','london','france','germany','spain','italy','australia','canada','mexico',
    'brazil','argentina','venezuela','chile','peru','colombia','world','international'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','rugby','baseball','hockey','coach','tournament','match','cup','league']
business_kw = ['stocks','wall st','market','ipo','shares','profit','earnings','oil','economy','inflation','trade deficit','bank','fed','interest rates','fund','invest','company','aerospace','commercial']
science_kw = ['research','scientist','nuclear','technology','tech','computer','software','internet','e-mail','email','space','planet','medicine','drug','experimental']

def classify(text):
    t = (text or '').lower()
    scores = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in business_kw if k in t),
        'Science/Technology': sum(1 for k in science_kw if k in t),
    }
    # choose max; tie-break by priority order
    order = ['World','Business','Sports','Science/Technology']
    mx = max(scores.values())
    best = [c for c,v in scores.items() if v==mx]
    for c in order:
        if c in best:
            return c

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna(''))
arts_df['category'] = arts_df['text'].map(classify)

merged = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='left')
world_2015 = merged[merged['category']=='World']

counts = world_2015.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    result = {'region': None, 'count': 0}
else:
    result = {'region': counts.index[0], 'count': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_V9oprOKMf4cVwygJ9T61J2rL': 'file_storage/call_V9oprOKMf4cVwygJ9T61J2rL.json', 'var_call_sKrFEnIbbc1KaHsDG5H4kooR': 'file_storage/call_sKrFEnIbbc1KaHsDG5H4kooR.json'}

exec(code, env_args)
