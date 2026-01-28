code = """import json
import re

# Load data from storage-provided variables
# var_call_YXqvDviRTU2sZlkmMuAPozD6 is a file path to the full MongoDB query result
with open(var_call_YXqvDviRTU2sZlkmMuAPozD6, 'r') as f:
    articles = json.load(f)

# List of article_id dicts from metadata query
article_id_dicts = var_call_tyzxTfJYHfie5zkCEWqetRQN

# Total number of articles authored by Amy Jones
total = len(article_id_dicts)

# Prepare keyword sets
science_kw = [
    'science', 'scientist', 'research', 'laboratory', 'laboratories', 'lab', 'technology', 'technolog', 'tech',
    'nuclear', 'physics', 'chemistry', 'biology', 'biotech', 'space', 'nasa', 'probe', 'shuttle', 'satellite',
    'electric', 'electricity', 'engineer', 'engineering', 'robot', 'ai', 'artificial intelligence', 'computer',
    'software', 'hardware', 'chip', 'processor', 'semiconductor', 'intel', 'microsoft', 'emc', 'e-mail', 'email',
    'storage', 'robotics', 'researcher', 'gen', 'gyro-gen'
]

sports_kw = [
    'olymp', 'win', 'wins', 'defeat', 'defeated', 'match', 'goal', 'score', 'quarter', 'semifinal', 'championship',
    'champions', 'u s open', 'us open', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'coach', 'team',
    'league', 'cup', 'pro bowl', 'sprint', 'gold', 'silver', 'bronze'
]

business_kw = [
    'profit', 'profits', 'revenue', 'revenues', 'earnings', 'stocks', 'shares', 'company', 'companies', 'trade', 'wto',
    'settle', 'settled', 'lawsuit', 'market', 'bank', 'economic', 'economy', 'investor', 'investment', 'acquisition',
    'merger', 'quarter', 'price', 'prices', 'commodity'
]

# Normalize keywords to lowercase
science_kw = [k.lower() for k in science_kw]
sports_kw = [k.lower() for k in sports_kw]
business_kw = [k.lower() for k in business_kw]

# Helper function to check presence of any keyword
def contains_any(text, keywords):
    for kw in keywords:
        if kw in text:
            return True
    return False

# Count science/technology articles
sci_count = 0

# Build a map of article_id to article content for quick lookup
articles_map = {str(a.get('article_id')): a for a in articles}

# Iterate over the list of article IDs from metadata to ensure we consider all of Amy Jones's articles
for aid_dict in article_id_dicts:
    aid = str(aid_dict.get('article_id'))
    art = articles_map.get(aid)
    if not art:
        # If the article document wasn't retrieved for some reason, skip it
        continue
    title = (art.get('title') or '')
    desc = (art.get('description') or '')
    text = (title + ' ' + desc).lower()

    # Priority: Science/Technology > Sports > Business > World
    if contains_any(text, science_kw):
        sci_count += 1
    elif contains_any(text, sports_kw):
        pass
    elif contains_any(text, business_kw):
        pass
    else:
        pass

# Prepare result
fraction_decimal = (sci_count / total) if total > 0 else None
result = {
    'science_count': sci_count,
    'total_articles': total,
    'fraction': f"{sci_count}/{total}",
    'fraction_decimal': round(fraction_decimal, 4) if fraction_decimal is not None else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fkeNRrJPyCWpht9vAmA531RL': [{'author_id': '218'}], 'var_call_tyzxTfJYHfie5zkCEWqetRQN': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_YXqvDviRTU2sZlkmMuAPozD6': 'file_storage/call_YXqvDviRTU2sZlkmMuAPozD6.json'}

exec(code, env_args)
