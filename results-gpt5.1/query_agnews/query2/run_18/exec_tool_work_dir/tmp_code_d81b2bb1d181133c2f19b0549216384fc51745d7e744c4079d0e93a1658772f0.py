code = """import json, pandas as pd
from math import isfinite

amy_articles = pd.DataFrame(var_call_512F4NgjRSMBIwz7fLyaK303)

# Load full articles data
path = var_call_qBwFvb7NkSG5x4fZKekvqHH4
with open(path, 'r') as f:
    articles = json.load(f)
articles_df = pd.DataFrame(articles)

# Ensure types align
amy_ids = set(amy_articles['article_id'].astype(str))

# Filter Amy's articles
amy_articles_df = articles_df[articles_df['article_id'].astype(str).isin(amy_ids)].copy()

# Simple keyword-based categorization into 4 classes
world_kw = ['iraq','europe','africa','asia','election','government','minister','united nations','u.n.','taliban','palestinian','israel','war','conflict','refugee','policy','parliament','president','prime minister']
sports_kw = ['soccer','football','nba','nfl','mlb','olympic','tennis','golf','cricket','baseball','basketball','hockey','tournament','grand slam','world cup','coach','player','team','league']
business_kw = ['stock','stocks','wall st','nasdaq','dow','business','market','economy','economic','trade','shares','ipo','merger','acquisition','company','profit','losses','earnings','revenue','sales','loan','fund','currency','oil','price','prices','growth','bank','interest rate','bond']


def categorize(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for w in world_kw:
        if w in text: scores['World'] += 1
    for w in sports_kw:
        if w in text: scores['Sports'] += 1
    for w in business_kw:
        if w in text: scores['Business'] += 1
    # If none of above strongly match, assume Science/Technology
    if max(scores.values()) == 0:
        scores['Science/Technology'] = 1
    # Choose max category; tie-breaker prefers non-Science if matched
    max_cat = max(scores, key=scores.get)
    # handle ties
    max_score = scores[max_cat]
    tied = [k for k,v in scores.items() if v==max_score]
    if len(tied)>1 and 'Science/Technology' in tied and max_score>0:
        tied.remove('Science/Technology')
    return tied[0] if tied else 'Science/Technology'

amy_articles_df['category'] = amy_articles_df.apply(categorize, axis=1)

total = len(amy_articles_df)
if total == 0:
    frac = None
else:
    sci = (amy_articles_df['category']=='Science/Technology').sum()
    frac = sci/total

result = json.dumps({'total_articles': int(total), 'science_tech_count': int((amy_articles_df['category']=='Science/Technology').sum()), 'fraction_science_tech': frac})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_512F4NgjRSMBIwz7fLyaK303': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_qBwFvb7NkSG5x4fZKekvqHH4': 'file_storage/call_qBwFvb7NkSG5x4fZKekvqHH4.json'}

exec(code, env_args)
