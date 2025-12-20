code = """import json
import pandas as pd

# Load Amy Jones article IDs
amy_ids = [int(r['article_id']) for r in var_call_wrNPNBNWzYZaOpj7axQFHF8r]

# Load all articles from file
with open(var_call_fdJHoZC1GcAo5O7Vz80Ty2fV, 'r') as f:
    articles = json.load(f)

art_df = pd.DataFrame(articles)
art_df['article_id'] = art_df['article_id'].astype(int)

amy_articles = art_df[art_df['article_id'].isin(amy_ids)].copy()

# Simple keyword-based classifier for categories
science_words = ['science','scientific','research','researchers','study','studies','physics','chemistry','biology','space','nasa','planet','astronomy','genetic','genome','technology','technological','software','computer','computing','internet','online','web','tech ','robot','engineer','engineering','gadget','device','electronics','chip','chips','nuclear','climate','environment','weather','medical','medicine','health','disease','drug','drugs','cancer']

sports_words = ['sport','sports','game','games','match','matches','tournament','league','cup','olympics','olympic','nfl','nba','mlb','nhl','soccer','football','basketball','baseball','tennis','golf','cricket','hockey','coach','player','team','score','scored','goal','goals']

business_words = ['stock','stocks','market','markets','shares','share','ipo','economy','economic','business','company','companies','corporate','profit','profits','loss','losses','trade','trading','bank','banks','banking','loan','loans','investment','investor','investors','fund','funds','currency','currencies','dollar','euro','yen','oil','price','prices','merger','acquisition']

world_words = ['war','election','elections','government','president','prime minister','parliament','iraq','afghanistan','terror','terrorism','bomb','bombing','attack','attacks','palestinian','israeli','united nations','u.n.','conflict','protest','protests','demonstration','demonstrations']

science_set = set(science_words)
sports_set = set(sports_words)
business_set = set(business_words)
world_set = set(world_words)

import re

def classify(text):
    if not isinstance(text, str):
        return 'World'
    low = text.lower()
    # tokenization by non-letters
    tokens = re.split('[^a-z]+', low)
    tok_set = set(tokens)
    s = len(tok_set & science_set)
    sp = len(tok_set & sports_set)
    b = len(tok_set & business_set)
    w = len(tok_set & world_set)
    scores = {
        'Science/Technology': s,
        'Sports': sp,
        'Business': b,
        'World': w
    }
    # pick max, default to World on ties and zeros
    max_cat = 'World'
    max_score = -1
    for cat, sc in scores.items():
        if sc > max_score:
            max_score = sc
            max_cat = cat
    return max_cat

amy_articles['text'] = amy_articles['title'].fillna('') + ' ' + amy_articles['description'].fillna('')
amy_articles['category'] = amy_articles['text'].apply(classify)

total = len(amy_articles)
science_count = (amy_articles['category'] == 'Science/Technology').sum()
frac = science_count / total if total > 0 else None

result = {
    'total_amy_articles': int(total),
    'science_technology_articles': int(science_count),
    'fraction_science_technology': frac
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wrNPNBNWzYZaOpj7axQFHF8r': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_fdJHoZC1GcAo5O7Vz80Ty2fV': 'file_storage/call_fdJHoZC1GcAo5O7Vz80Ty2fV.json'}

exec(code, env_args)
