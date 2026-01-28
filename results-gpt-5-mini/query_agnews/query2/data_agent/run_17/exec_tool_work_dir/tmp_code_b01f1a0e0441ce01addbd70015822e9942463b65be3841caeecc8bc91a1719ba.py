code = """import json
import pandas as pd

# Load the MongoDB query result (stored in a file path)
with open(var_call_oLKlc0Cvr1RzFRrJ5Bgi36Xt, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Load the list of article IDs from the SQL query result
article_id_records = var_call_jGy4AOUhl9bM7iImsHmK0Gkt
article_ids = [int(r['article_id']) for r in article_id_records]

# Create DataFrame
df = pd.DataFrame(articles)
# Ensure article_id is int
df['article_id'] = df['article_id'].astype(int)

# Keep only the articles for this author (should already be the case)
df = df[df['article_id'].isin(article_ids)].copy()

# Lowercase combined text
df['text'] = (df.get('title','').fillna('') + ' ' + df.get('description','').fillna('')).str.lower()

# Define keyword sets
sci_kw = ['science','scientist','research','laboratory','lab','nasa','shuttle','probe','space','intel','microsoft','technology','tech','e-mail','email','phone','nuclear','physics','experiment','competition','award','genesis','gameboy','e-mail','e mail','storage','server','emc','gyro-gen']

sports_kw = ['olympic','semi-final','semi final','quarter-final','quarter final','u.s. open','us open','goal','match','win','defeat','team','champions league','champions','baseball','football','basketball','tennis','pro bowl','cornerback','wide receiver','coach','league','olympics','capriati','serena','williams','medal','gold','scored','goal','ruud','law','piniella']

business_kw = ['profit','profits','revenue','revenues','stock','stocks','market','company','corp','trade','wto','settle','settled','settlement','earnings','price','prices','financial','debt','charges','settlement','settles','microsoft settles']

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

# Apply classification
df['category'] = df['text'].apply(classify)

sci_count = int((df['category'] == 'Science/Technology').sum())
total = int(len(article_ids))

result = {
    'science_technology_count': sci_count,
    'total_articles': total,
    'fraction': f"{sci_count}/{total}",
    'decimal': sci_count/total if total>0 else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lu46sPx08Luq3XBQGJGoSjFk': [{'author_id': '218'}], 'var_call_jGy4AOUhl9bM7iImsHmK0Gkt': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_oLKlc0Cvr1RzFRrJ5Bgi36Xt': 'file_storage/call_oLKlc0Cvr1RzFRrJ5Bgi36Xt.json'}

exec(code, env_args)
