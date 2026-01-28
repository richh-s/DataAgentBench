code = """import json, pandas as pd, re

# load articles
path = var_call_ElLjDqWTabANT3zuQ3HJrCFn
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

def classify(title, desc):
    t = f"{title or ''} {desc or ''}".lower()
    sci = [
        'nasa','space','shuttle','probe','mars','satellite','rocket','capsule','astronaut',
        'intel','microsoft','google','apple','iphone','android','software','chip','processor','semiconductor',
        'technology','tech','internet','online','website','cyber','computer','e-mail','email','server',
        'science','scientist','research','laboratory','physics','nuclear','genome','dna','vaccine','medical',
        'climate','global warming','energy','wave','electricity','telescope','robot'
    ]
    sports = ['vs','match','tournament','open','olympic','league','champions league','goal','coach','quarter-final','final','semi-final','broncos','giants','dodgers','red sox','cycling','tennis','cricket','football','soccer','baseball']
    biz = ['stocks','shares','profit','earnings','revenue','wto','trade','gap','oil prices','price','inflation','company','corp','acquisition','investors','mining','gold','market']
    world = ['iraq','gaza','israeli','west bank','sharon','kathmandu','nepal','somalia','parliament','ira','british','government','curfew','settlements','militants','hamas']

    score = {'Science/Technology':0,'Sports':0,'Business':0,'World':0}
    for kw in sci:
        if kw in t: score['Science/Technology'] += 1
    for kw in sports:
        if kw in t: score['Sports'] += 1
    for kw in biz:
        if kw in t: score['Business'] += 1
    for kw in world:
        if kw in t: score['World'] += 1
    # choose max; tie-breaker preference Sci/Tech then Business then Sports then World
    order = ['Science/Technology','Business','Sports','World']
    maxv = max(score.values())
    tops = [k for k,v in score.items() if v==maxv]
    for k in order:
        if k in tops:
            return k

cats = [classify(a.get('title',''), a.get('description','')) for a in articles]
science_count = sum(1 for c in cats if c=='Science/Technology')
total = len(cats)
frac = science_count/total if total else None
out = {'science_tech': science_count, 'total': total, 'fraction': frac}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CGgK6mvIgI0kHzKK8YF3YdZ9': [{'author_id': '218'}], 'var_call_WdSsLMdR6lY9LM50DcNvoLQQ': [{'total': '111'}], 'var_call_Frt15YdiJCnsZ5BtesPnLgGi': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_ElLjDqWTabANT3zuQ3HJrCFn': 'file_storage/call_ElLjDqWTabANT3zuQ3HJrCFn.json'}

exec(code, env_args)
