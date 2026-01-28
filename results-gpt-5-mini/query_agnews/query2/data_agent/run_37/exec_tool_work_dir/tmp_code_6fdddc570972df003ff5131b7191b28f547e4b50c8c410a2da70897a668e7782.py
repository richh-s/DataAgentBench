code = """import json
import os
# Load the SQL result stored in var_call_8kQhMZ08vWp9JGXGfxYQD7H8 (list of dicts)
sql_records = var_call_8kQhMZ08vWp9JGXGfxYQD7H8
# Load the MongoDB result from var_call_wmT77742AyjSyd7UpETEneYP which is a filepath string
mongo_path = var_call_wmT77742AyjSyd7UpETEneYP
with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)

# Build a map from article_id to combined text
articles = {}
for rec in mongo_records:
    aid = str(rec.get('article_id'))
    title = rec.get('title') or ''
    desc = rec.get('description') or ''
    text = (title + ' ' + desc).lower()
    articles[aid] = text

# List of article_ids from SQL (authors join)
article_ids = [str(r['article_id']) for r in sql_records]

# Define keyword sets
tech_keywords = ['science','scientist','research','nasa','intel','microsoft','technology','tech','lab','laboratory','space probe','space','probe','shuttle','nuclear','semiconductor','email','e-mail','ocean','wave','waves','genesis','siemens','westinghouse','gyro-gen','electricity','e-mail storage','storage for microsoft','storage product']

sports_keywords = ['game','win','wins','season','coach','cup','olympic','olympics','final','semi-final','quarter-final','goal','score','tournament','pro bowl','broncos','red sox','champions league','match','umpire','cycling','tennis','basketball','soccer','football']

business_keywords = ['company','companies','stock','stocks','revenue','profit','profits','earnings','market','wto','trade','settlement','settles','settled','wheat','board','kroger','microsoft settles','settlement','lawsuit','debt','bank','corporation','corp']

# Function to classify
def classify(text):
    for kw in tech_keywords:
        if kw in text:
            return 'Science/Technology'
    for kw in sports_keywords:
        if kw in text:
            return 'Sports'
    for kw in business_keywords:
        if kw in text:
            return 'Business'
    return 'World'

# Classify all articles authored by Amy Jones
class_counts = {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}
missing = []
for aid in article_ids:
    text = articles.get(aid)
    if text is None:
        missing.append(aid)
        continue
    cat = classify(text)
    class_counts[cat] += 1

total = len(article_ids) - len(missing)
science_count = class_counts['Science/Technology']

# Prepare result
percentage = (science_count / total * 100) if total>0 else 0
result = {
    'science_count': science_count,
    'total_articles': total,
    'fraction': f"{science_count}/{total}",
    'percentage': round(percentage,2),
    'missing_article_ids': missing
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8kQhMZ08vWp9JGXGfxYQD7H8': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_wmT77742AyjSyd7UpETEneYP': 'file_storage/call_wmT77742AyjSyd7UpETEneYP.json'}

exec(code, env_args)
