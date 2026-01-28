code = """import json, pandas as pd

# Load Amy Jones article_ids
amy_ids = [int(r['article_id']) for r in var_call_UiI2al9SH3zgZjnDaB3TqVaC]
amy_set = set(amy_ids)

# Load all articles from file
path = var_call_s214nDdho5ZfUikSztH57zM3
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Build dict for Amy articles text
amy_articles = []
for a in articles:
    aid = int(a.get('article_id'))
    if aid in amy_set:
        title = (a.get('title') or '')
        desc = (a.get('description') or '')
        amy_articles.append({'article_id': aid, 'text': (title + ' ' + desc).lower()})

# Keyword-based categorization
sci_terms = [
    'science','scientist','research','researchers','study','studies','nasa','space','planet','mars','moon','telescope','astronom',
    'technology','tech','software','hardware','internet','web','online','cyber','computer','ai','artificial intelligence','robot',
    'biotech','genome','genetic','dna','virus','bacteria','vaccine','medical','medicine','health','climate','global warming',
    'physics','chemistry','quantum','nanotech','semiconductor','chip','smartphone','phone','mobile','satellite','launch'
]

sports_terms = ['game','games','season','team','teams','coach','tournament','match','league','nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','olympic','golf','tennis','cricket','race','racing']
biz_terms = ['stocks','stock','market','shares','earnings','profit','loss','revenue','quarter','ipo','merger','acquisition','bank','banks','fed','interest rate','inflation','economy','economic','oil','crude','dollar','euro','trade','deficit','imf','opec']
world_terms = ['iraq','iran','israel','palestin','afghan','russia','ukraine','china','japan','korea','un','united nations','election','president','minister','rebels','militia','war','attack','bomb','police','killed','court','government','parliament']


def score(text, terms):
    s = 0
    for t in terms:
        if t in text:
            s += 1
    return s

classified = []
for rec in amy_articles:
    text = rec['text']
    sc = score(text, sci_terms)
    sp = score(text, sports_terms)
    bz = score(text, biz_terms)
    wd = score(text, world_terms)
    # choose max; tie-breaker: sci > biz > world > sports
    scores = {'Science/Technology': sc, 'Business': bz, 'World': wd, 'Sports': sp}
    maxv = max(scores.values())
    top = [k for k,v in scores.items() if v==maxv]
    order = ['Science/Technology','Business','World','Sports']
    cat = sorted(top, key=lambda k: order.index(k))[0]
    classified.append({'article_id': rec['article_id'], 'category': cat, 'scores': scores})

# If any all-zero, default to World (most general)
for c in classified:
    if max(c['scores'].values()) == 0:
        c['category'] = 'World'

n_total = len(classified)
n_sci = sum(1 for c in classified if c['category']=='Science/Technology')
frac = n_sci / n_total if n_total else None

out = {'total_articles_by_amy_jones': n_total, 'science_technology_articles': n_sci, 'fraction': frac}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UiF99JCQi6avs151vVlXjSwd': [{'author_id': '218'}], 'var_call_UiI2al9SH3zgZjnDaB3TqVaC': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_s214nDdho5ZfUikSztH57zM3': 'file_storage/call_s214nDdho5ZfUikSztH57zM3.json'}

exec(code, env_args)
