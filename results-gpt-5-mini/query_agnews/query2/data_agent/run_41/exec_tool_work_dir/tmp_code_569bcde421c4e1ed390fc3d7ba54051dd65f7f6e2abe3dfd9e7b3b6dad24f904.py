code = """import json
import re
# Load the articles result from the stored JSON file path
path = var_call_1RN34s8Qdvd9rIep4bf8PUQr
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Defensive: ensure articles is a list of dicts
if not isinstance(articles, list):
    articles = list(articles)

# Classification keyword sets
science_kw = [
    'science','scientist','research','technology','technolog','tech','nasa','space','intel','microsoft',
    'semiconductor','nuclear','shuttle','probe','lab','engineering','siemens','westinghouse','gyro-gen','gyro',
    'e-mail','email','genesis mission','electricity','computer','software','mobile phone','phone maker', 'micro-games', 'gameboy', 'video game', 'e-mail storage', 'storage for microsoft'
]
business_kw = [
    'company','profit','profits','revenue','stock','stocks','market','trade','wto','earnings','settles','settled',
    'acquisition','acquires','business','economic','economy','sales','bank','insurance','financial'
]
sports_kw = [
    'olympic','olympics','quarter-final','semi-final','tournament','match','goal','score','u.s. open','champions league',
    'pro bowl','broncos','tennis','baseball','football','soccer','coach','team','player','cup','win','wins','defeat','defeated'
]
world_kw = [
    'gaza','israel','palestine','parliament','nairobi','nepal','kathmandu','president','prime minister','militants',
    'attack','settlement','west bank','settlements','belgian','france','somalia','iraq','china','geneva','diplomat',
    'curfew','terror','militant','islam','u.s. appeal','diplomats','government','peace','wounded','killed'
]

# Helper to count occurrences of keywords
def score_text(text, kw_list):
    s = 0
    for kw in kw_list:
        if kw in text:
            s += text.count(kw)
    return s

science_count = 0
classified = []
for art in articles:
    title = (art.get('title') or '')
    desc = (art.get('description') or '')
    combined = (title + ' ' + desc).lower()
    # Normalize some punctuation
    combined = combined.replace('\n', ' ')

    # Compute scores
    s_science = score_text(combined, science_kw)
    s_business = score_text(combined, business_kw)
    s_sports = score_text(combined, sports_kw)
    s_world = score_text(combined, world_kw)

    scores = {'Science/Technology': s_science, 'Business': s_business, 'Sports': s_sports, 'World': s_world}
    # Choose category with highest score; tie-break by Science, World, Business, Sports
    max_score = max(scores.values())
    if max_score == 0:
        # fallback heuristic: use presence of domain words
        if any(w in combined for w in ['win','team','match','tournament']):
            category = 'Sports'
        elif any(w in combined for w in ['company','revenue','stock','market','trade','business']):
            category = 'Business'
        elif any(w in combined for w in ['science','research','technology','nasa','space','intel','microsoft','lab']):
            category = 'Science/Technology'
        else:
            category = 'World'
    else:
        # tie-break
        # get categories with max score
        candidates = [k for k,v in scores.items() if v == max_score]
        priority = ['Science/Technology','World','Business','Sports']
        for p in priority:
            if p in candidates:
                category = p
                break
    classified.append({'article_id': art.get('article_id'), 'title': title, 'category': category})
    if category == 'Science/Technology':
        science_count += 1

total_count = len(articles)
percentage = (science_count/total_count*100) if total_count>0 else 0.0
result = {'science_count': science_count, 'total_count': total_count, 'fraction': f"{science_count}/{total_count}", 'percentage': round(percentage,2)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ks9uOTueWnVpPdC7kTXc9Cee': [{'author_id': '218'}], 'var_call_1eiCotUT8RvnNJ7Ih4uzk9jl': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_1RN34s8Qdvd9rIep4bf8PUQr': 'file_storage/call_1RN34s8Qdvd9rIep4bf8PUQr.json'}

exec(code, env_args)
