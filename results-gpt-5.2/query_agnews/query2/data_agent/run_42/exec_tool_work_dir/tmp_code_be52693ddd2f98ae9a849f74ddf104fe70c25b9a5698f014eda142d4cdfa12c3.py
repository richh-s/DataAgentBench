code = """import json, pandas as pd

def is_sci_tech(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d
    sci_terms = [
        'science','scientist','research','researchers','study','studies','laboratory','lab',
        'technology','tech','software','computer','computing','internet','online','web',
        'ai','artificial intelligence','machine learning','robot','robotics','chip','semiconductor',
        'nasa','space','satellite','rocket','mars','astronomy','telescope','physics','quantum',
        'biology','biotech','genome','genetic','dna','medical','medicine','drug','vaccine','health',
        'climate','energy','renewable','electricity','battery'
    ]
    sports_terms = ['game','match','league','cup','season','coach','team','quarterback','broncos','nfl','nba','mlb','soccer','football','baseball','basketball','tennis','golf','olympic']
    business_terms = ['profit','profits','shares','stock','market','earnings','revenue','sales','company','companies','merger','acquisition','oil','mining','billion','bank','economy','economic','trade','prices']
    world_terms = ['president','election','iraq','afghanistan','israel','palestinian','ukraine','russia','china','un','united nations','terror','bomb','war','attack','government','minister','parliament']

    sci = sum(1 for w in sci_terms if w in text)
    sports = sum(1 for w in sports_terms if w in text)
    biz = sum(1 for w in business_terms if w in text)
    world = sum(1 for w in world_terms if w in text)

    # pick sci/tech if it has at least 1 strong indicator and is not clearly dominated by sports/business/world
    return sci >= 1 and sci >= max(sports, biz, world)

articles = var_call_ilr53pzpP4hzcfg9N4b6sMyd

total = len(articles)
count_sci = 0
for a in articles:
    if is_sci_tech(a.get('title'), a.get('description')):
        count_sci += 1

fraction = count_sci / total if total else None
out = {"total_articles": total, "sci_tech_articles": count_sci, "fraction": fraction}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WnfVdwpUAtlRfTZNEXYoKrgF': [{'author_id': '218'}], 'var_call_91d2M9V7e8MRTM889eAMeQjU': [{'total': '111'}], 'var_call_wsZotG5GOLqFmhUbWdpgx1Py': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_ilr53pzpP4hzcfg9N4b6sMyd': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
