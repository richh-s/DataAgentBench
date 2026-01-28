code = """import json
import re

# Load articles JSON from file path stored in var_call_K3gfKfRGcuOUH8hD5FFBdTWx
with open(var_call_K3gfKfRGcuOUH8hD5FFBdTWx, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Ensure articles is a list of dicts
texts = []
for a in articles:
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    combined = (title + ' ' + desc).lower()
    texts.append({'article_id': a.get('article_id'), 'text': combined, 'title': title, 'description': desc})

# Define keyword-based classifier
science_kw = [
    'science', 'scientist', 'technology', 'tech', 'nasa', 'space', 'probe', 'research', 'laboratory', 'lab',
    'computer', 'software', 'chip', 'intel', 'emc', 'email', 'e-mail', 'experiment', 'physics', 'nuclear',
    'genetic', 'biology', 'chemistry', 'robot', 'satellite', 'shuttle', 'spacecraft', 'parachute', 'wave',
    'ocean', 'electricity', 'engineer', 'engineering', 'siemens', 'westinghouse', 'gyro-gen', 'gyrogen',
    'science competition', 'scientific'
]

sports_kw = [
    'olymp', 'olympic', 'team', 'season', 'coach', 'goal', 'score', 'match', 'defeat', 'win', 'won', 'league',
    'champions', 'us open', 'u.s. open', 'tennis', 'baseball', 'soccer', 'football', 'basketball', 'cycling',
    'red sox', 'giants', 'dodgers', 'manchester', 'serena', 'capriati', 'championship', 'quarter-final', 'semi-final',
    'pro bowl', 'striker', 'goalkeeper', 'match', 'umpire'
]

business_kw = [
    'profit', 'profits', 'revenue', 'earnings', 'company', 'corp', 'shares', 'stock', 'market', 'business', 'trade',
    'wto', 'settles', 'settlement', 'producer prices', 'bank', 'microsoft', 'settled', 'settlement', 'economy', 'pricedrop', 'prices', 'reuters'
]

# classify
sci_count = 0
sports_count = 0
business_count = 0
world_count = 0
classifications = []
for item in texts:
    txt = item['text']
    classified = None
    # science first
    for kw in science_kw:
        if kw in txt:
            sci_count += 1
            classified = 'Science/Technology'
            break
    if classified is None:
        for kw in sports_kw:
            if kw in txt:
                sports_count += 1
                classified = 'Sports'
                break
    if classified is None:
        for kw in business_kw:
            if kw in txt:
                business_count += 1
                classified = 'Business'
                break
    if classified is None:
        world_count += 1
        classified = 'World'
    classifications.append({'article_id': item['article_id'], 'classification': classified, 'title': item['title']})

total = len(texts)
# prepare fraction
from fractions import Fraction
frac = Fraction(sci_count, total) if total>0 else Fraction(0,1)
decimal = float(sci_count)/total if total>0 else 0.0

result = {
    'science_count': sci_count,
    'total_count': total,
    'fraction': f"{frac.numerator}/{frac.denominator}",
    'decimal': round(decimal, 6),
    'breakdown': {'Science/Technology': sci_count, 'Sports': sports_count, 'Business': business_count, 'World': world_count}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_knQAcAjJem5dBsmZDZBs6jpl': [{'author_id': '218'}], 'var_call_9yAPIJCG1AJVFsWdOoQlZtLh': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_K3gfKfRGcuOUH8hD5FFBdTWx': 'file_storage/call_K3gfKfRGcuOUH8hD5FFBdTWx.json'}

exec(code, env_args)
