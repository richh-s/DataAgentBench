code = """import json
from pathlib import Path

def classify_text(text):
    t = text.lower()
    # keyword sets
    sports = ['game','win','wins','defeat','defeated','quarter-final','quarterfinal','semi-final','semifinal','goal','match','league','season','olympic','u.s. open','u.s. open','open','tournament','coach','score','scored','innings','dodgers','giants','tennis','serena','capriati','red sox','baseball','football','basketball','soccer','olympics','championship','cup','coach','goalkeeper','striker']
    business = ['company','companies','profit','profits','revenue','revenues','stock','stocks','shares','market','markets','economy','economic','trade','wto','trade','lawsuit','settled','settles','settlement','bank','earnings','prices','inflation','reuters','dow','nasdaq','billion','million']
    scitech = ['science','scientist','research','technology','technolog','nasa','space','probe','shuttle','lab','laboratory','engineering','engineer','tech','nuclear','scientific','competition in math, science and technology','siemens westinghouse','e-mail','email','microsoft','intel','emc','storage','phone maker','gyro-gen','gyrogen']
    world = ['president','prime minister','parliament','parliament','militants','militant','gaza','west bank','nepal','somalia','israel','iraq','british','diplomat','diplomats','geneva','nairobi','curfew','peace','attack','killed','military','settlements','west bank']

    def score(keywords):
        s = 0
        for kw in keywords:
            if kw in t:
                s += t.count(kw)
        return s

    s_scores = score(sports)
    b_scores = score(business)
    st_scores = score(scitech)
    w_scores = score(world)

    scores = {'Sports': s_scores, 'Business': b_scores, 'Science/Technology': st_scores, 'World': w_scores}
    # choose category with highest score; tie-breaker order Science/Technology, Sports, Business, World
    best = max(scores, key=lambda k: (scores[k], 1 if k=='Science/Technology' else 0, 1 if k=='Sports' else 0, 1 if k=='Business' else 0))
    # if all zero, default to World
    if all(v==0 for v in scores.values()):
        best = 'World'
    return best, scores

# load the query result file path from storage variable
file_path = var_call_09pJF61JJSFIhckzHyP3PvYw
# open and load
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for r in records:
    aid = int(r.get('article_id'))
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    text = title + ' ' + desc
    cat, scores = classify_text(text)
    results.append({'article_id': aid, 'title': title, 'category': cat, 'scores': scores})

total = len(results)
scitech_count = sum(1 for r in results if r['category']=='Science/Technology')

out = {'total_articles': total, 'science_technology_count': scitech_count, 'fraction': f"{scitech_count}/{total}", 'percentage': round(scitech_count/total*100,2)}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_4aNGbvuWnDZsi4bDC0Jb6YSy': [{'author_id': '218'}], 'var_call_KJg6ZBnPuHuoWu3WLSeQecjn': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_09pJF61JJSFIhckzHyP3PvYw': 'file_storage/call_09pJF61JJSFIhckzHyP3PvYw.json'}

exec(code, env_args)
