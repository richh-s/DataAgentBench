code = """import json, pandas as pd

amy_ids = [int(r['article_id']) for r in var_call_PCDcc5FUwpl4ORv1fXo7yh1s]

path = var_call_g8P2fbYAOsYiftBuYzzKOlhd
with open(path, 'r') as f:
    articles = json.load(f)

amy_articles = [a for a in articles if int(a['article_id']) in amy_ids]

from collections import Counter

world_words = {'world','iraq','europe','africa','asia','china','election','war','u.n.','united nations'}
sports_words = {'game','games','olympics','championship','league','cup','tournament','soccer','baseball','football','basketball','tennis','golf'}
business_words = {'stock','stocks','market','shares','wall st.','nasdaq','dow','economy','economic','oil','trade','company','companies','profit','profits','fund','funds','loan','bank','banks','business'}

sci_words = {'space','nasa','science','scientists','scientist','research','study','studies','technology','tech','software','internet','computer','computers','physics','biology','genetics','medical','medicine','drug','drugs','disease','diseases'}


def classify(text):
    t = text.lower()
    scores = {"World":0,"Sports":0,"Business":0,"Science/Technology":0}
    for w in world_words:
        if w in t: scores['World']+=1
    for w in sports_words:
        if w in t: scores['Sports']+=1
    for w in business_words:
        if w in t: scores['Business']+=1
    for w in sci_words:
        if w in t: scores['Science/Technology']+=1
    cat = max(scores, key=scores.get)
    if all(v==0 for v in scores.values()):
        cat = 'World'
    return cat

sci_count = 0
for a in amy_articles:
    text = (a.get('title','') or '') + ' ' + (a.get('description','') or '')
    if classify(text) == 'Science/Technology':
        sci_count += 1

frac = sci_count/len(amy_articles) if amy_articles else None

import math
if frac is not None:
    frac = round(frac,3)

result = {"total_articles": len(amy_articles), "science_tech_articles": sci_count, "fraction": frac}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PCDcc5FUwpl4ORv1fXo7yh1s': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_g8P2fbYAOsYiftBuYzzKOlhd': 'file_storage/call_g8P2fbYAOsYiftBuYzzKOlhd.json'}

exec(code, env_args)
