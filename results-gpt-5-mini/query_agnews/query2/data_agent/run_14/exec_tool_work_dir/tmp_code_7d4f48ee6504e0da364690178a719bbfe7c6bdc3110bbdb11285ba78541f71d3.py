code = """import json

# Load articles result from file path provided in storage
with open(var_call_ot3pWg42P3tm9c1gYo3hnpPU, 'r') as f:
    articles = json.load(f)

# Metadata article ids
metadata_records = var_call_YabSL2qpZ9APCy1AKUEp3kOB
metadata_ids = [int(rec['article_id']) for rec in metadata_records]

# Prepare mapping and counts
retrieved_ids = [int(a['article_id']) for a in articles]
article_map = {int(a['article_id']): a for a in articles}

# Keywords indicative of Science/Technology
keywords = [
    'science', 'scientist', 'research', 'technology', 'technolog', 'tech', 'nasa', 'space', 'satellite', 'probe', 'shuttle',
    'nuclear', 'physics', 'laboratory', 'lab', 'computer', 'software', 'hardware', 'chip', 'semiconductor', 'electronic',
    'emc', 'microsoft', 'intel', 'energy', 'electricity', 'wave', 'waves', 'e-mail', 'email', 'genome', 'biotech',
    'biology', 'chemistry', 'engineering', 'science competition', 'science award'
]

sci_ids = []
for aid in retrieved_ids:
    rec = article_map[aid]
    title = rec.get('title', '') or ''
    desc = rec.get('description', '') or ''
    text = (title + ' ' + desc).lower()
    matched = False
    for kw in keywords:
        if kw in text:
            matched = True
            break
    if matched:
        sci_ids.append(aid)

sci_count = len(sci_ids)
total_metadata = len(metadata_ids)
retrieved_count = len(retrieved_ids)

fraction_by_metadata = sci_count / total_metadata if total_metadata>0 else None
fraction_by_retrieved = sci_count / retrieved_count if retrieved_count>0 else None

result = {
    'total_articles_in_metadata': total_metadata,
    'articles_retrieved': retrieved_count,
    'science_technology_articles_found': sci_count,
    'science_technology_article_ids': sci_ids,
    'fraction_by_metadata': fraction_by_metadata,
    'fraction_by_retrieved': fraction_by_retrieved
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YabSL2qpZ9APCy1AKUEp3kOB': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_ot3pWg42P3tm9c1gYo3hnpPU': 'file_storage/call_ot3pWg42P3tm9c1gYo3hnpPU.json'}

exec(code, env_args)
