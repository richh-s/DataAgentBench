code = """import json
from pathlib import Path
# Load the full MongoDB query result from the file path provided by the previous tool call
data_path = Path(var_call_oDixqT8OoxOJv23fSgDWPsgA)
with data_path.open('r', encoding='utf-8') as f:
    articles = json.load(f)

# Helper for classification
import re

def categorize_article(title, description):
    text = ((title or '') + ' ' + (description or '')).lower()
    # keyword lists
    business_kw = ['profit','profits','revenue','revenues','earnings','stock','stocks','market','markets','investor','investors','settle','settled','settles','lawsuit','lawsuits','wto','trade','trading','reuters','q1','q2','q3','quarter','deal','settlement','company','companies']
    sports_kw = ['olympic','olympics','pro bowl','pro-bowl','quarter-final','quarterfinal','semi-final','semifinal','u.s. open','u.s. open','open','match','goal','score','scores','defeat','defeated','win','wins','won','season','coach','red sox','dodgers','giants','champions league','tennis','football','soccer','basketball','cycling','umpire','goalkeeper','strike','match']
    world_kw = ['israel','gaza','somalia','nepal','kathmandu','prime minister','parliament','diplomat','diplomats','militant','militants','government','president','bush','iraq','kerry','west bank','palestinian','palestinians','belgian','belgium','france']
    science_kw = ['science','scientist','research','laboratory','laboratories','nuclear','physics','chemistry','space','shuttle','nasa','probe','genesis','technology','tech','emc','micro-games','gameboy','gameboy','e-mail','email','microsoft exchange','emc unveils','gyro-gen','siemens','westinghouse','researcher','laboratory']

    # Business check first (to avoid misclassifying company-related tech business as science)
    for kw in business_kw:
        if kw in text:
            return 'Business'
    # Sports
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    # Science/Technology
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    # World
    for kw in world_kw:
        if kw in text:
            return 'World'
    # Default fallback: World
    return 'World'

# Classify all articles
classified = []
for art in articles:
    title = art.get('title','')
    desc = art.get('description','')
    cat = categorize_article(title, desc)
    classified.append({'article_id': int(art.get('article_id')), 'title': title, 'category': cat})

# Compute counts for Amy Jones' articles
total = len(classified)
science_count = sum(1 for a in classified if a['category'] == 'Science/Technology')

# Prepare result
fraction = None
fraction_decimal = None
if total > 0:
    from fractions import Fraction
    frac = Fraction(science_count, total)
    fraction = f"{science_count}/{total}"
    fraction_decimal = float(science_count) / float(total)

result = {
    'science_tech_count': science_count,
    'total_articles': total,
    'fraction': fraction,
    'fraction_decimal': round(fraction_decimal, 6)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wXgxv3R7JERwgGZjqoAkIgUq': [{'author_id': '218'}], 'var_call_r4SJdPbBdvhvtjYkxnyD5ZY1': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_oDixqT8OoxOJv23fSgDWPsgA': 'file_storage/call_oDixqT8OoxOJv23fSgDWPsgA.json'}

exec(code, env_args)
