code = """import json, pandas as pd

path = var_call_cMidJvjQSwFJtWABub9NtQh6
with open(path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# keyword classifier
def classify(text):
    t = (text or '').lower()
    world_kw = ['president','prime minister','parliament','election','government','minister','diplomat','united nations','u.n.','nato','eu','summit','sanctions','refugee','migrant','border','terror','isis','attack','ceasefire','coup','iran','iraq','syria','israel','gaza','ukraine','russia','china','north korea']
    sports_kw = ['match','game','season','league','tournament','coach','player','goal','nba','nfl','mlb','nhl','fifa','olympic','tennis','cricket','soccer','football','basketball','baseball','hockey','golf']
    business_kw = ['stocks','shares','market','earnings','revenue','profit','merger','acquisition','ipo','bank','fed','inflation','oil','prices','trade','tariff','economy','economic','company','ceo']
    science_kw = ['research','study','scientist','space','nasa','mars','rocket','climate','carbon','genome','dna','robot','technology','tech','software','app','internet','ai','artificial intelligence']
    def score(kws):
        return sum(1 for kw in kws if kw in t)
    scores = {
        'World': score(world_kw),
        'Sports': score(sports_kw),
        'Business': score(business_kw),
        'Science/Technology': score(science_kw)
    }
    best = max(scores, key=scores.get)
    return best if scores[best]>0 else None

print('__RESULT__:')
print(json.dumps({'n_2015_articles': int(len(meta_df)), 'note': 'Need tool calls from assistant to fetch article texts for categorization.'}))"""

env_args = {'var_call_cMidJvjQSwFJtWABub9NtQh6': 'file_storage/call_cMidJvjQSwFJtWABub9NtQh6.json'}

exec(code, env_args)
