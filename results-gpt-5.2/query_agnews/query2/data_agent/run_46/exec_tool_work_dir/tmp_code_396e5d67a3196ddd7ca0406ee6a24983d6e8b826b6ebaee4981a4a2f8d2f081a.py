code = """import json, pandas as pd

records = var_call_15z2sTEo4uLViBeQETiqd6I3

def classify(title, desc):
    text = f"{title} {desc}".lower()
    sci = [
        'science','technology','tech','software','internet','online','computer','computing','ai','artificial',
        'robot','robotics','space','nasa','satellite','astronaut','mars','telescope','physics','chemistry',
        'biology','genome','genetic','dna','medical','medicine','health','virus','vaccine','research',
        'laboratory','lab','innovation','gadget','gameboy','video game','gaming','cyber','data'
    ]
    sports = ['nba','nfl','mlb','nhl','olympic','soccer','football','baseball','basketball','hockey','tennis','golf','broncos','pro bowl','cornerback','wide receiver','reciever','coach','tournament','match','season']
    business = ['profit','shares','stock','market','bank','earnings','revenue','merger','acquisition','oil','mining','company','prices','trade','economy','economic','inflation','interest rate','billion','bhp']
    world = ['iraq','afghanistan','election','government','president','minister','war','un','united nations','china','russia','israel','palestinian','terror','police','court','attack','killed']

    def score(keywords):
        return sum(1 for k in keywords if k in text)

    scores = {
        'Science/Technology': score(sci),
        'Sports': score(sports),
        'Business': score(business),
        'World': score(world)
    }
    # tie-breaker: prefer Science/Technology if it has any signal
    best = max(scores.items(), key=lambda x: (x[1], 1 if x[0]=='Science/Technology' else 0))
    if best[1]==0:
        return 'World'
    return best[0]

cats = [classify(r.get('title',''), r.get('description','')) for r in records]

total = len(records)
sci_n = sum(1 for c in cats if c=='Science/Technology')
fraction = sci_n/total if total else None

out = {
    'total_articles': total,
    'science_technology_articles': sci_n,
    'fraction': fraction
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sN13qugK3azosTZ3H3BpDtjH': [{'author_id': '218'}], 'var_call_S2j4AQR7VKQBMnVLwbUqdzgW': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_15z2sTEo4uLViBeQETiqd6I3': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
