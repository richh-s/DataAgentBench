code = """import json
from fractions import Fraction

# Load data from storage variables
# var_call_kEhl9Fexor2dnoPQSHdUCV6G contains article_id list
# var_call_JUvc19aT9Yic978kiBR4Wgg3 contains path to JSON file with article documents

article_ids = [int(d['article_id']) for d in var_call_kEhl9Fexor2dnoPQSHdUCV6G]

# Load full articles JSON from file path
with open(var_call_JUvc19aT9Yic978kiBR4Wgg3, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Build a map article_id -> combined text
records = []
for a in articles:
    aid = int(a.get('article_id'))
    title = a.get('title') or ''
    desc = a.get('description') or ''
    text = (title + ' ' + desc).lower()
    records.append({'article_id': aid, 'text': text, 'title': title, 'description': desc})

# Define keyword lists
sci_kw = ['science','scientist','technology','tech','nasa','space','intel','research','laboratory','lab','physics','chemical','chemistry','biology','genetic','genetics','engineering','engineer','computer','software','hardware','electronics','e-mail','email','storage','chip','processor','semiconductor','genesis','shuttle','probe','nuclear','scientific','siemens','westinghouse']

sports_kw = ['game','win','wins','won','defeat','defeated','olympic','u.s. open','u.s. open','champions league','quarter-final','semi-final','goal','match','coach','team','tournament','umpire','cycling','score','reds','red sox','giants','dodgers','pro bowl','wide receiver','quarterfinal','semifinal']

business_kw = ['company','profits','profit','revenue','revenues','stock','stocks','market','trade','wto','settlement','settles','acquisition','earnings','financial','economic','commodity','oil prices','producer prices','settled','settles','bank','corporate']

# Classification function
def classify(text):
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    return 'World'

# Classify each record for the provided article_ids (ensure we consider only those authored by Amy)
selected_records = [r for r in records if r['article_id'] in article_ids]

# It's possible some article_ids were missing from articles collection; count total as length of article_ids, but classification only for found records.
# We'll classify only found records and assume missing ones are non-Science/Technology for conservative estimate? Better: treat only found records as basis.
# For this task, we'll compute fraction based on found articles (articles we retrieved).

classified = []
for r in selected_records:
    cat = classify(r['text'])
    classified.append({'article_id': r['article_id'], 'category': cat, 'title': r['title']})

total = len(selected_records)
science_count = sum(1 for c in classified if c['category']=='Science/Technology')

# Simplify fraction
if total == 0:
    frac = None
    frac_simplified = None
    frac_decimal = None
else:
    frac = f"{science_count}/{total}"
    frac_simplified = str(Fraction(science_count, total))
    frac_decimal = science_count/total

result = {
    'science_count': science_count,
    'total_found_articles': total,
    'fraction': frac,
    'fraction_simplified': frac_simplified,
    'fraction_decimal': round(frac_decimal, 4) if frac_decimal is not None else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3WZLQegbTzKUvDacPV5viHau': [{'author_id': '218'}], 'var_call_kEhl9Fexor2dnoPQSHdUCV6G': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_JUvc19aT9Yic978kiBR4Wgg3': 'file_storage/call_JUvc19aT9Yic978kiBR4Wgg3.json'}

exec(code, env_args)
