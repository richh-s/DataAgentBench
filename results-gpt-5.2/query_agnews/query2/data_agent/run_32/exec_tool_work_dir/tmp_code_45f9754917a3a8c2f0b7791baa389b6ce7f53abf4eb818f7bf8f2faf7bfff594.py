code = """import json, pandas as pd, re
from pathlib import Path

# Load full mongo result
p = Path(var_call_VXafPtZeGIILnOhG05kkc3Jf)
records = json.loads(p.read_text())

def categorize(title, desc):
    text = (str(title) + " " + str(desc)).lower()
    # science/tech keywords
    sci = [
        'nasa','space','shuttle','probe','mars','satellite','astronaut','rocket',
        'microsoft','intel','google','apple','software','computer','internet','e-mail','email','server','phone','mobile','telecom',
        'science','technology','tech','research','laboratory','physics','nuclear','genesis mission','wto' # wto not sci; ignore
    ]
    # adjust: remove wto
    sci = [k for k in sci if k!='wto']
    sports = ['olympic','open','champions league','league','broncos','cycling','tennis','baseball','giants','dodgers','liverpool','cricket','final','gold']
    business = ['stocks','profit','earnings','revenue','shares','oil prices','economy','trade gap','producer prices','wto','company','acquisitions','investors','mining']
    world = ['ira','israeli','gaza','west bank','kathmandu','nepal','somalia','parliament','china','french','anti-semitism','iraq','bush','kerry']

    scores = {'Science/Technology':0,'Sports':0,'Business':0,'World':0}
    for k in sci:
        if k in text: scores['Science/Technology'] += 1
    for k in sports:
        if k in text: scores['Sports'] += 1
    for k in business:
        if k in text: scores['Business'] += 1
    for k in world:
        if k in text: scores['World'] += 1
    # if explicit tokens
    if 'reuters' in text or 'ap -' in text:
        pass
    # choose max; tie-break by priority Sci/Tech if has 'science'/'tech'/'space' etc
    best = max(scores.items(), key=lambda x: x[1])[0]
    if scores[best]==0:
        # fallback: if mentions market/economy->Business else World
        if any(k in text for k in ['market','stocks','profit','earnings','revenue','company']):
            best='Business'
        elif any(k in text for k in ['game','win','defeat','final','season','coach','goal']):
            best='Sports'
        else:
            best='World'
    return best

cats = [categorize(r.get('title',''), r.get('description','')) for r in records]

total = len(records)
sci_total = sum(1 for c in cats if c=='Science/Technology')

fraction = sci_total/total if total else None

out = {
    'total_articles': total,
    'sci_tech_articles': sci_total,
    'fraction': fraction
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VHMrqSi1VgiLYVi2x7mNxHmT': [{'author_id': '218'}], 'var_call_LnecXm1HLXdfb1ecdXrB31XB': [{'total': '111'}], 'var_call_tJzrZLCR7BLM0lYiaEdmZ0Ba': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_VXafPtZeGIILnOhG05kkc3Jf': 'file_storage/call_VXafPtZeGIILnOhG05kkc3Jf.json'}

exec(code, env_args)
