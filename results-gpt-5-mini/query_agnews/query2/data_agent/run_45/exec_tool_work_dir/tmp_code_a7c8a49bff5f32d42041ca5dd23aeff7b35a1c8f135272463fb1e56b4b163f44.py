code = """import json
# Load data from previous tool results
path = var_call_2awf22uOcpsFwUybisEdu20b
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# total articles retrieved
total = len(articles)

# Define keyword sets
science_kw = ['science','scientist','research','laboratory','lab','nasa','space probe','space','probe','shuttle','intel','technology','technolog','tech','computer','software','microsoft','emc','email','e-mail','micro','physics','nuclear','robot','electric','electricity','gene','dna','researcher','award','competition','engineering','engineer','electronics','wave','gyro-gen','gyrogen']

sports_kw = ['game','olympic','olympics','quarter-final','quarterfinal','final','match','goal','score','league','champions','u.s. open','us open','tennis','cycling','broncos','pro bowl','athens','defeat','win','victory','season','coach','football','soccer','baseball','basketball','dodgers','giants','sprint','semi-final','semi final']

business_kw = ['company','companies','profit','profits','revenue','earnings','stock','shares','market','acquisition','oil prices','economy','economic','reuters','trade','wto','wheat','settles','settled','settlement','kroger','billion','million','dollars','revenue','sales']

world_kw = ['israel','gaza','iraq','somalia','nepal','president','prime minister','diplomat','diplomats','parliament','government','curfew','politic','politics','country','world','foreign','terror','milit','militant','war','peace','border','refugee','settlement','settlements']

# normalize function
def text_from_article(a):
    t = (a.get('title') or '') + ' ' + (a.get('description') or '')
    return t.lower()

# classify
categories = []
for a in articles:
    txt = text_from_article(a)
    scores = {
        'Science/Technology': sum(1 for kw in science_kw if kw in txt),
        'Sports': sum(1 for kw in sports_kw if kw in txt),
        'Business': sum(1 for kw in business_kw if kw in txt),
        'World': sum(1 for kw in world_kw if kw in txt),
    }
    # choose max score, tie-breaker by highest priority Science > World > Business > Sports
    max_score = max(scores.values())
    if max_score == 0:
        cat = 'World'
    else:
        # get categories with max score
        max_cats = [k for k,v in scores.items() if v==max_score]
        priority = ['Science/Technology','World','Business','Sports']
        cat = None
        for p in priority:
            if p in max_cats:
                cat = p
                break
    categories.append(cat)

# count science/technology
sci_count = sum(1 for c in categories if c=='Science/Technology')

fraction = sci_count / total if total>0 else 0.0

result = {'science_technology_count': sci_count, 'total_articles': total, 'fraction': round(fraction,6)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KegcQBUUub6JSxR7luyelOOK': [{'author_id': '218'}], 'var_call_xhPsRmvAGjByncd1nhx8DtXY': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_2awf22uOcpsFwUybisEdu20b': 'file_storage/call_2awf22uOcpsFwUybisEdu20b.json'}

exec(code, env_args)
