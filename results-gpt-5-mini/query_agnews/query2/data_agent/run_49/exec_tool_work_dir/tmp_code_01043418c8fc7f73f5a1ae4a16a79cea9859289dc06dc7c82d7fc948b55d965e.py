code = """import json
import pandas as pd

# Load data from previous tool calls stored in variables
# var_call_EnAwguSw40xJAZA1adePKCd8: metadata article list
# var_call_73j2cIuBllVIBggvKSbRahB8: file path to articles JSON

metadata_list = var_call_EnAwguSw40xJAZA1adePKCd8
articles_file_path = var_call_73j2cIuBllVIBggvKSbRahB8

# Read the large articles JSON file
with open(articles_file_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Create dict of article_id -> combined text
articles_dict = {}
for a in articles:
    aid = str(int(a.get('article_id'))) if a.get('article_id') is not None else None
    title = a.get('title') or ''
    desc = a.get('description') or ''
    text = f"{title} {desc}".lower()
    articles_dict[aid] = text

# Metadata article ids
meta_ids = [str(int(item['article_id'])) for item in metadata_list]

# Define keyword sets
sports_kw = ['win', 'defeat', 'beat', 'olympic', 'olympics', 'game', 'match', 'goal', 'scored', 'quarter-final', 'u.s. open', 'champion', 'champions league', 'league', 'tournament', 'coach', 'scored', 'baseball', 'football', 'soccer', 'tennis', 'olympic', 'semi-final', 'final']
business_kw = ['profit', 'profits', 'revenue', 'revenues', 'stocks', 'stock', 'market', 'trade', 'wto', 'earnings', 'settle', 'settled', 'lawsuit', 'lawsuit', 'company', 'companies', 'corp', 'corporation', 'reuters', 'economy', 'producer prices', 'trade gap', 'settles', 'settlement']
tech_kw = ['science', 'scientist', 'technology', 'tech', 'intel', 'nasa', 'space', 'shuttle', 'laboratory', 'research', 'nuclear', 'gameboy', 'gameboy', 'gyro-gen', 'micro-games', 'microsoft', 'phone', 'mobile', 'e-mail', 'email', 'server', 'exchange', 'emc', 'genesis mission', 'probe', 'parachute', 'space probe', 'experiment', 'engineering', 'computer']

# Classification function
def classify(text):
    if not text:
        return 'World'
    t = text.lower()
    # Sports detection
    for kw in sports_kw:
        if kw in t:
            return 'Sports'
    # Business detection
    for kw in business_kw:
        if kw in t:
            return 'Business'
    # Tech/Science detection
    for kw in tech_kw:
        if kw in t:
            return 'Science/Technology'
    return 'World'

# Classify each metadata article (if present)
science_count = 0
classified_count = 0
missing_ids = []
breakdown = {'Science/Technology': 0, 'Business': 0, 'Sports': 0, 'World': 0}
for aid in meta_ids:
    text = articles_dict.get(aid)
    if text is None:
        missing_ids.append(aid)
        continue
    cat = classify(text)
    breakdown[cat] += 1
    classified_count += 1
    if cat == 'Science/Technology':
        science_count += 1

total_articles = len(meta_ids)

# Prepare result string
if len(missing_ids) == 0:
    frac = science_count / total_articles if total_articles > 0 else 0
    pct = round(frac * 100, 2)
    result_str = f"{science_count}/{total_articles} ({pct}%) of Amy Jones's articles are in the Science/Technology category."
else:
    # If missing, compute fraction over total and also note missing
    frac = science_count / total_articles if total_articles > 0 else 0
    pct = round(frac * 100, 2)
    result_str = (f"{science_count}/{total_articles} ({pct}%) of Amy Jones's articles are in the Science/Technology category. "
                  f"Note: {len(missing_ids)} articles were missing from the articles collection and could not be classified.")

import json
print("__RESULT__:")
print(json.dumps(result_str))"""

env_args = {'var_call_4p2IVhOCJpMJQ5irfgX0q0xO': [{'author_id': '218'}], 'var_call_EnAwguSw40xJAZA1adePKCd8': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_73j2cIuBllVIBggvKSbRahB8': 'file_storage/call_73j2cIuBllVIBggvKSbRahB8.json'}

exec(code, env_args)
