code = """import json, pandas as pd
from collections import defaultdict

# Load full results
with open(var_call_wj95Y508fEHv5eW0JFO8sNMf, 'r') as f:
    meta = json.load(f)
with open(var_call_Nt5tgstiuue6ZBKPtuoM0M9s, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Simple keyword-based classifier for categories
world_keywords = ['iraq','war','government','election','president','minister','united nations','u.n.','conflict','palestinian','israeli','terror','bomb','attack','insurgent','troops','nato','diplomat','policy','parliament','rebel','militia','taliban','al-qaeda','sudan','refugee','nuclear','china','japan','europe','africa','asia','middle east','gaza','afghan','russia','kremlin','prime minister','white house']

sports_keywords = ['football','soccer','nba','nfl','mlb','hockey','olympics','tennis','golf','cricket','racing','formula one','motogp','baseball','basketball','coach','season opener','finals','quarterback','midfielder','striker','grand prix']

business_keywords = ['stocks','wall st','wall street','shares','ipo','interest rates','fed ','federal reserve','economy','markets','nasdaq','dow jones','s&p','profit','losses','q2','quarterly','earning','merger','acquisition','bank','bond','oil prices','crude','investment','trading','fund','mutual fund','retail sales','trade deficit','corporate','dollar','euro','yen']

# Anything not in above but clearly science/tech could be classified, but we only care to identify World.

def is_world(text):
    t = text.lower()
    for kw in world_keywords:
        if kw in t:
            return True
    # Heuristic: if it talks about country names and not clearly business/sports
    country_words = ['iraq','iran','afghanistan','israel','palestine','pakistan','india','china','japan','germany','france','britain','uk ','u.k.','russia','ukraine','sudan','korea','north korea','south korea','saudi','arabia','mexico','canada','brazil','argentina','europe','asia','africa','middle east']
    if any(cw in t for cw in country_words):
        # exclude obvious business-only context
        if not any(kw in t for kw in business_keywords) and not any(kw in t for kw in sports_keywords):
            return True
    return False

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna(''))
arts_df['is_world'] = arts_df['text'].apply(is_world)

# Join meta with arts on article_id
merged = meta_df.merge(arts_df[['article_id','is_world']], on='article_id', how='left')

world_2015 = merged[merged['is_world'] == True]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = {
    'region_with_most_world_articles_2015': counts.index[0] if len(counts)>0 else None,
    'counts_by_region': counts.to_dict()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wj95Y508fEHv5eW0JFO8sNMf': 'file_storage/call_wj95Y508fEHv5eW0JFO8sNMf.json', 'var_call_Nt5tgstiuue6ZBKPtuoM0M9s': 'file_storage/call_Nt5tgstiuue6ZBKPtuoM0M9s.json'}

exec(code, env_args)
