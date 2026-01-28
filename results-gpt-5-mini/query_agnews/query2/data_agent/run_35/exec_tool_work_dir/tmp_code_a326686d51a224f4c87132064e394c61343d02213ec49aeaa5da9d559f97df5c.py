code = """import json, re

# Load the articles result from the provided file path variable
with open(var_call_3CQsLC5wrdtdHZRdo88OIL1W, 'r') as f:
    articles = json.load(f)

# Prepare keyword lists for simple rule-based classification
science_kw = [
    'science','scientist','research','laboratory','lab','nuclear','physics','chemistry','biology',
    'biotech','technology','tech','intel','microsoft','emc','software','computer','e-mail','email',
    'space','nasa','shuttle','probe','parachute','satellite','solar','gyro-gen','wave','electricity',
    'electric','engineering','engineer','server','exchange','storage'
]

business_kw = [
    'profit','profits','revenue','revenues','stock','stocks','trade','wheat','company','companies',
    'settle','settled','settles','lawsuit','earnings','price','prices','market','financial','cost',
    'sales','microsoft settles','settled a lawsuit','corp.','company'
]

sports_kw = [
    'win','wins','defeat','defeated','match','quarter-final','quarterfinal','olympic','olympics',
    'u.s. open','us open','tennis','goal','scored','league','champions league','game','team',
    'coach','beat','defense','defended','semi-final','semi final','sprint','cycling','broncos',
    'red sox','dodgers','giants','capriati','serena','umpire'
]

world_kw = [
    'israel','gaza','west bank','palestine','nepal','kathmandu','somalia','belgian','france',
    'geneva','iraq','diplomat','president','government','parliament','militant','international',
    'bush','kerry','congress','terror','military','border','refugee'
]

# Function to count keyword matches
def count_matches(text, keywords):
    text = text.lower()
    count = 0
    for kw in keywords:
        # use simple substring match for multi-word keywords and word boundary for single words
        if ' ' in kw or '.' in kw or '-' in kw:
            if kw in text:
                count += 1
        else:
            # word boundary
            if re.search(r'\b' + re.escape(kw) + r"\b", text):
                count += 1
    return count

# Classify articles
results = []
for art in articles:
    aid = int(art.get('article_id'))
    title = art.get('title','') or ''
    desc = art.get('description','') or ''
    text = (title + ' ' + desc).lower()
    s = count_matches(text, science_kw)
    b = count_matches(text, business_kw)
    sp = count_matches(text, sports_kw)
    w = count_matches(text, world_kw)
    scores = {'Science/Technology': s, 'Business': b, 'Sports': sp, 'World': w}
    # Choose the category with highest score; tie-breaker order: Science/Technology, Sports, Business, World
    best_cat = max(scores, key=lambda k: (scores[k], 1 if k=='Science/Technology' else 0, 0))
    # If all zero, fallback to World
    if sum(scores.values()) == 0:
        best_cat = 'World'
    results.append({'article_id': aid, 'title': title, 'assigned_category': best_cat, 'scores': scores})

# Compute totals
total = len(results)
science_count = sum(1 for r in results if r['assigned_category']=='Science/Technology')

# Prepare output
out = {
    'total_articles': total,
    'science_technology_articles': science_count,
    'fraction': f"{science_count}/{total}",
    'decimal': 0.0 if total==0 else science_count/total,
    'percentage': "0%" if total==0 else f"{science_count/total:.2%}"
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_s3yyX2IRXOxTypVgaU4OX0ho': [{'author_id': '218'}], 'var_call_WCRwMYvUasMtCvEBeCVqcxQn': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_3CQsLC5wrdtdHZRdo88OIL1W': 'file_storage/call_3CQsLC5wrdtdHZRdo88OIL1W.json'}

exec(code, env_args)
