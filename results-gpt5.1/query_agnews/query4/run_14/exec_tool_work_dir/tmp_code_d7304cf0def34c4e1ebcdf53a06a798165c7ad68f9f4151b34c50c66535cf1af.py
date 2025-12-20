code = """import json, pandas as pd

# Load full metadata
with open(var_call_YHlTKCEN5yrthqQYDHSRRGY5, 'r') as f:
    meta = json.load(f)

# Load full articles
with open(var_call_ddSqWTf9BfhlhOC4W4tzYlow, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter to 2015
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Join with articles
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Simple category heuristic for World vs others based on title+description keywords
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

world_keywords = ['iraq','afghanistan','united nations','u.n.','un ','eu ','european union','palestinian','israel','china','india','russia','taliban','war','conflict','election','president','minister','government','attack','bomb','killed','killing','suicide bomb','embassy','troops','military','terror','u.s.','unrest','crisis','refugee','border','protest','diplomat','summit']

# consider Sports/Business/ScienceTech as non-world by indicative keywords
non_world_keywords = ['stock','stocks','shares','market','economy','economic','bank','interest rate','loan','ipo','google','microsoft','apple','earnings','profit','revenue','sales','fund','mutual fund','nasdaq','dow','sport','football','soccer','nba','nfl','mlb','tennis','golf','olympic','olympics','tournament','match','coach','team','science','scientist','research','study','technology','software','internet','computer','tech ']

def classify(txt):
    t = txt
    # If it clearly matches non-world and not world, skip
    if any(k in t for k in non_world_keywords) and not any(k in t for k in world_keywords):
        return 'Non-World'
    if any(k in t for k in world_keywords):
        return 'World'
    # default non-world
    return 'Non-World'

df['category'] = text.apply(classify)

world_df = df[df['category'] == 'World']

# Count by region
counts = world_df.groupby('region')['article_id'].count().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_YHlTKCEN5yrthqQYDHSRRGY5': 'file_storage/call_YHlTKCEN5yrthqQYDHSRRGY5.json', 'var_call_ddSqWTf9BfhlhOC4W4tzYlow': 'file_storage/call_ddSqWTf9BfhlhOC4W4tzYlow.json'}

exec(code, env_args)
