code = """import json, re
import pandas as pd

# Load articles from file if needed
arts_src = var_call_x2SzoP5MvOzDGQccBGPtJrDZ
if isinstance(arts_src, str):
    with open(arts_src, 'r', encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = arts_src

def categorize(text):
    t = (text or '').lower()
    sci_kw = [
        'nasa','space','shuttle','probe','mars','satellite','rocket','astronaut',
        'intel','microsoft','google','apple','software','hardware','chip','semiconductor','server',
        'internet','cyber','computer','phone','mobile','smartphone','telecom','wi-fi','wireless',
        'science','scientist','research','study','laboratory','physics','nuclear','genome','dna',
        'technology','tech','biotech','medical','health','virus','vaccine','climate','energy'
    ]
    sports_kw = ['olympic','league','champions league','match','season','coach','tournament','final','quarter','semi','goal','score','win','defeat','broncos','giants','dodgers','tennis','cycling','cricket','football','baseball','soccer']
    biz_kw = ['stocks','shares','profit','earnings','oil prices','trade','wto','revenue','company','investor','market','economy','inflation','producer prices','trade gap','acquisition','merger','lawsuit','settles']
    world_kw = ['iraq','israel','gaza','west bank','nepal','kathmandu','somalia','parliament','prime minister','anti-semitism','settlements','missiles','militants','curfew','negotiations','ira']

    scores = {'Science/Technology':0,'Sports':0,'Business':0,'World':0}
    for kw in sci_kw:
        if kw in t: scores['Science/Technology'] += 1
    for kw in sports_kw:
        if kw in t: scores['Sports'] += 1
    for kw in biz_kw:
        if kw in t: scores['Business'] += 1
    for kw in world_kw:
        if kw in t: scores['World'] += 1
    # prefer explicit mentions
    if 'science' in t or 'technology' in t or 'nasa' in t or 'space' in t or 'intel' in t or 'microsoft' in t:
        scores['Science/Technology'] += 2
    # pick max; tie-break order
    order = ['Science/Technology','Business','World','Sports']
    mx = max(scores.values())
    best = [k for k,v in scores.items() if v==mx]
    for k in order:
        if k in best:
            return k

for a in arts:
    text = f"{a.get('title','')} {a.get('description','')}"
    a['category'] = categorize(text)

n_total = len(arts)
n_sci = sum(1 for a in arts if a['category']=='Science/Technology')
frac = n_sci / n_total if n_total else None
out = {
    'total_articles': n_total,
    'science_technology_articles': n_sci,
    'fraction': frac
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DDhEUUusIL8BUTT6sfo455Ge': [{'author_id': '218'}], 'var_call_x7JF9TRVsdB9weYiTCqAthTt': ['articles'], 'var_call_poYRGAQDRG3I3H5k5LjuMleZ': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_x2SzoP5MvOzDGQccBGPtJrDZ': 'file_storage/call_x2SzoP5MvOzDGQccBGPtJrDZ.json'}

exec(code, env_args)
