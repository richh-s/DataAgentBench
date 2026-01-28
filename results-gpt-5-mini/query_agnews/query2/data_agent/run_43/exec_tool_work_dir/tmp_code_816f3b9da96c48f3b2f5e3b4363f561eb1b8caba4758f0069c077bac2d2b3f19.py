code = """import json
import pandas as pd

# Load the large articles result from the provided file path variable
path = var_call_jUejEN4Cvvv0JKc7fN52U63r
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Also load the list of article_ids from metadata query (already available as var)
author_articles = var_call_pBVqV0xIZnDxs3epCJQSxlBp

# Prepare set of article_ids authored by Amy Jones (as strings to match records)
authored_ids = set([str(r['article_id']) for r in author_articles])

# Define keywords for Science/Technology categorization
scitech_keywords = [
    'science', 'scientist', 'research', 'laboratory', 'laboratories', 'lab', 'nuclear', 'physics',
    'technology', 'tech', 'nasa', 'space', 'shuttle', 'probe', 'capsule', 'satellite', 'intel', 'microsoft',
    'emc', 'server', 'storage', 'mobile phone', 'phone maker', 'phone', 'email', 'e-mail', 'electronic',
    'engineering', 'engineering', 'competition in math, science and technology', 'siemens', 'westinghouse',
    'gyro-gen', 'wave', 'waves', 'e-mail', 'exchange'
]

# Function to classify a single article text as Science/Technology if any keyword is present
def is_scitech(text):
    t = text.lower()
    for kw in scitech_keywords:
        if kw in t:
            return True
    return False

# Iterate through the articles we fetched and count how many authored by Amy Jones are scitech
total = 0
scitech_count = 0
scitech_article_ids = []
for rec in articles:
    aid = str(rec.get('article_id'))
    if aid in authored_ids:
        total += 1
        combined = (rec.get('title','') or '') + ' ' + (rec.get('description','') or '')
        if is_scitech(combined):
            scitech_count += 1
            scitech_article_ids.append(aid)

# Safety: if total is zero, avoid division by zero
fraction = None
if total > 0:
    fraction = scitech_count / total

result = {
    'science_tech_count': scitech_count,
    'total_articles_by_amy_jones': total,
    'fraction': fraction,
    'science_tech_article_ids': scitech_article_ids
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5iJF052KPM8FI4tkCBZD1Qgh': ['authors', 'article_metadata'], 'var_call_u6qfbCL5xjsDIV9WjtGWmmrU': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_call_pBVqV0xIZnDxs3epCJQSxlBp': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_jUejEN4Cvvv0JKc7fN52U63r': 'file_storage/call_jUejEN4Cvvv0JKc7fN52U63r.json'}

exec(code, env_args)
