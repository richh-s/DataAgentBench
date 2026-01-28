code = """import json
# Load articles from the JSON file path stored in var_call_fXrCqFMMNcHC3EyaqEYlyWtu
with open(var_call_fXrCqFMMNcHC3EyaqEYlyWtu, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Get list of article_ids for Amy Jones from var_call_wGIjxRUQLQjNJ5pzXOHLVNE0
amy_article_ids = [str(int(d['article_id'])) for d in var_call_wGIjxRUQLQjNJ5pzXOHLVNE0]

# Build a map from article_id to record for quick lookup
article_map = {str(int(a.get('article_id'))): a for a in articles}

# Define keyword lists
science_kw = [
    'science','scientist','research','laboratory','laboratory','nuclear','intel','chip','technology','tech',
    'nasa','space','probe','shuttle','electron','physics','engineering','engineer','robot','robotics','biology',
    'chemistry','electricity','wave','gyro-gen','siemens','westinghouse','email storage','e-mail storage','emc',
    'microsoft','email','e-mail','storage','missile'  # 'missile' might be military but avoid classifying as science unless other tech words
]

sports_kw = [
    'game','win','wins','won','olymp','u.s. open','u.s. open','open','quarter-final','semi-final','goal',
    'champions league','season','coach','score','match','defeat','beat','loses','run','tackle','home run','cycling',
    'tennis','baseball','football','soccer','basketball','pro bowl','red sox','dodgers','giants','capriati','serena',
    'ruud','van nistelrooy','denis law','olympic'
]

business_kw = [
    'company','profit','profits','revenue','revenues','stock','stocks','market','markets','earnings','economy',
    'economic','trade','wheat','settled','settles','lawsuit','bank','financial','kroger','billion','million','price',
    'prices','producer prices','trade gap','settlement','settled','settles'
]

# Classification function
def classify(title, desc):
    text = (title or '') + ' ' + (desc or '')
    text = text.lower()
    # Science/Technology priority
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    return 'World'

# Iterate over Amy's articles, classify
classified = []
science_ids = []
science_titles = []
for aid in amy_article_ids:
    rec = article_map.get(aid)
    if not rec:
        # If article not found in articles collection, skip
        continue
    title = rec.get('title','')
    desc = rec.get('description','')
    cat = classify(title, desc)
    classified.append({'article_id': aid, 'title': title, 'category': cat})
    if cat == 'Science/Technology':
        science_ids.append(aid)
        science_titles.append(title)

total = len(classified)
science_count = len(science_ids)

# Prepare result
result = {
    'science_count': science_count,
    'total_articles': total,
    'fraction': f"{science_count}/{total}" if total>0 else None,
    'decimal': round(science_count/total, 6) if total>0 else None,
    'science_article_ids': science_ids,
    'science_titles': science_titles
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Jnunf1wvaU7Tlp1cAfCLFKlf': [{'author_id': '218'}], 'var_call_wGIjxRUQLQjNJ5pzXOHLVNE0': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_fXrCqFMMNcHC3EyaqEYlyWtu': 'file_storage/call_fXrCqFMMNcHC3EyaqEYlyWtu.json'}

exec(code, env_args)
