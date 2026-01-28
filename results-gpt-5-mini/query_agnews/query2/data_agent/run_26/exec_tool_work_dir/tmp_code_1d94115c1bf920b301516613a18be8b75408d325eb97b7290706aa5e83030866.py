code = """import json
import pandas as pd

# Load the articles result from the provided JSON file path
file_path = var_call_EcIctk0sDWonNjEaZANGfPFS
with open(file_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Create DataFrame
df = pd.DataFrame(articles)

# Ensure article_id and text fields
df['title'] = df.get('title', '').fillna('')
df['description'] = df.get('description', '').fillna('')

def classify_article(title, description):
    text = (str(title) + ' ' + str(description)).lower()
    # Science/Technology keywords
    science_kw = [
        'science','scientist','laboratory','research','nasa','shuttle','space','probe',
        'technology','tech','computer','email','e-mail','microsoft','intel','semiconductor',
        'genetic','physics','nuclear','experiment','scientific','engineer','engineering',
        'dna','robot','robotics','biotech','biology','chemistry','innovation','gadget',
        'mobile phone','phone','gameboy','game boy','video game','micro-games','gyro-gen',
        'ocean waves','wave','waves','e-mail','email storage','e-mail storage','lab','researcher'
    ]
    sports_kw = [
        'olympic','olympics','quarter-final','quarterfinal','game','team','season','score','goal',
        'football','soccer','tennis','u.s. open','us open','champions league','broncos','dodgers',
        'giants','cycling','cyclist','semi-final','semifinal','win','defeat','coach','match','cup','league',
        'olympic','medal','gold','silver','bronze','pro bowl','quarterfinal','quarter-final'
    ]
    business_kw = [
        'company','profit','profits','revenue','market','stocks','stock','shares','trade','wto',
        'business','settlement','lawsuit','earnings','economy','oil price','oil prices','producer prices',
        'settled','settles','settlement','revenue expectations','settled'
    ]

    # Check science first
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    # Then sports
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    # Then business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    # Else World
    return 'World'

# Apply classification
df['category'] = df.apply(lambda r: classify_article(r['title'], r['description']), axis=1)

# Compute counts
total = len(df)
science_count = int((df['category'] == 'Science/Technology').sum())

result = {
    'science_count': science_count,
    'total_count': total,
    'fraction': None,
    'fraction_str': f"{science_count}/{total}",
    'percentage': None
}
if total > 0:
    frac = science_count / total
    result['fraction'] = round(frac, 6)
    result['percentage'] = round(frac * 100, 4)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_t43IzfZbpOUVoqEaG20yB7Aw': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_EcIctk0sDWonNjEaZANGfPFS': 'file_storage/call_EcIctk0sDWonNjEaZANGfPFS.json'}

exec(code, env_args)
