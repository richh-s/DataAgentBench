code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

recs = load_records(var_call_riBf5b7zS9d8Krf8zNpxCJOg)

def classify(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d

    sports_kw = ['olympic','open','quarter-final','semifinal','final','league','champions league','match','game','goal','coach','team','player','wins','races','gold','broncos','cycling','cricket','football','soccer','baseball','nba','nfl','nhl','tennis','gerrard','ruud','van nistelrooy']
    business_kw = ['stocks','profit','earnings','revenue','shares','wto','trade','prices','oil','economic','company','corp','merger','acquisition','investor','market','microsoft','intel','emc','kroger','shell','bhp','placer dome','production','gold production','trade gap','producer prices']
    sci_kw = ['nasa','space','shuttle','probe','parachute','capsule','sun','physics','physicist','nuclear','science','technology','tech','gameboy','computer','software','server','research','laboratory','energy','electricity','wave','genesis mission']
    world_kw = ['israel','gaza','west bank','sharon','hamas','iraq','kathmandu','nepal','somalia','parliament','ira','northern ireland','british','french','anti-semitism','settlements','missiles','curfew']

    def has_any(kws):
        return any(kw in text for kw in kws)

    if has_any(sci_kw) and not has_any(sports_kw):
        return 'Science/Technology'
    if has_any(sports_kw):
        return 'Sports'
    if has_any(business_kw):
        return 'Business'
    if has_any(world_kw):
        return 'World'
    if has_any(sci_kw):
        return 'Science/Technology'
    return 'World'

rows=[]
for r in recs:
    cat=classify(r.get('title'), r.get('description'))
    rows.append({'article_id': int(r['article_id']), 'category': cat})

df=pd.DataFrame(rows)

total=len(df)
scitech=(df['category']=='Science/Technology').sum()
frac=scitech/total if total else None
out={'author':'Amy Jones','total_articles':total,'science_technology_articles':int(scitech),'fraction':frac}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oRJeL3uvb3grc7fbTpnrF0oh': [{'author_id': '218'}], 'var_call_lK1QGM95G7GHsnUJU1y3yC3W': ['articles'], 'var_call_UZbpw3RffraqkQNE93jeeoFf': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_riBf5b7zS9d8Krf8zNpxCJOg': 'file_storage/call_riBf5b7zS9d8Krf8zNpxCJOg.json'}

exec(code, env_args)
