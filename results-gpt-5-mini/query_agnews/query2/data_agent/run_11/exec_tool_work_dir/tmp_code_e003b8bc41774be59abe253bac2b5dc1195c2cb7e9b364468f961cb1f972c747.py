code = """import json
import pandas as pd
import re

# Load Mongo query results from file path in var_call_qvUYOpQlcGMXSUnAun9NEtUs
json_path = var_call_qvUYOpQlcGMXSUnAun9NEtUs
with open(json_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(docs)
# Ensure title and description strings
df['title'] = df['title'].fillna('').astype(str)
df['description'] = df['description'].fillna('').astype(str)

# Classification keywords
sci_keywords = ['science','scientist','research','technology','technologies','tech','nasa','space','nuclear','laboratory','lab','intel','microsoft','sensor','satellite','probe','shuttle','genesis','engineering','electric','electricity','robot','computer','software','hardware','internet','e-mail','email','digital','semiconductor','chip','processor','wave','physics','siemens','chemistry','biology','genetics','stem','innovation']
business_keywords = ['profit','profits','revenue','earnings','stocks','prices','settles','settled','trade','market','company','corp','corp.','shares','lawsuit','settled','settles','reuters','wto','wheat','settlement','revenue','earnings','financial']
sports_keywords = ['game','match','win','wins','defeat','defeated','goal','olympic','olympics','semi-final','semi final','quarter-final','quarter final','coach','team','season','tournament','umpire','red sox','broncos','sprinter','cycling','defeat','score','quarter-final','pro bowl']
world_keywords = ['president','prime minister','parliament','gaza','israel','nepal','somalia','diplomat','militant','explosion','curfew','international','country','foreign','embassy','minister']

# helper to check presence
def contains_any(text, keywords):
    text = text.lower()
    for kw in keywords:
        if kw in text:
            return True
    return False

# classify each article
categories = []
for _, row in df.iterrows():
    text = (row['title'] + ' ' + row['description']).lower()
    # priority: sports if clear sports terms
    if contains_any(text, sports_keywords):
        cat = 'Sports'
    # business if clear financial/business cues
    elif contains_any(text, business_keywords):
        cat = 'Business'
    # science/tech if tech/science cues
    elif contains_any(text, sci_keywords):
        cat = 'Science/Technology'
    # world if world cues
    elif contains_any(text, world_keywords):
        cat = 'World'
    else:
        # fallback: if mentions names like 'gameboy' treat as Science/Technology
        if 'gameboy' in text or 'gameboy' in row['title'].lower():
            cat = 'Science/Technology'
        else:
            # default to World
            cat = 'World'
    categories.append(cat)

df['category'] = categories

# Count Sci/Tech
total = len(df)
sci_count = int((df['category'] == 'Science/Technology').sum())

result = {
    'sci_tech_count': sci_count,
    'total_articles': total,
    'fraction': f"{sci_count}/{total}",
    'decimal': round(sci_count/total if total>0 else 0, 4)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_epG4MpGM0D6EtE9JgTN8WTe8': [{'author_id': '218'}], 'var_call_7CgkeusnPIxQVUa6ZsgSRI7m': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_qvUYOpQlcGMXSUnAun9NEtUs': 'file_storage/call_qvUYOpQlcGMXSUnAun9NEtUs.json'}

exec(code, env_args)
