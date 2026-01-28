code = """import json
# Load data from storage variables provided by previous tool calls
# var_call_B0K4HL8FOi0DkRd8rl1RuJRp is the filepath to the JSON file with articles
articles_path = var_call_B0K4HL8FOi0DkRd8rl1RuJRp
with open(articles_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# var_call_Enql6oQ0R2wQxt2lwJlRou3h is the list of article_id dicts for Amy Jones
amy_article_records = var_call_Enql6oQ0R2wQxt2lwJlRou3h
amy_article_ids = set(int(r['article_id']) for r in amy_article_records)

# Build a mapping from article_id to combined text
id_to_text = {}
for doc in articles:
    try:
        aid = int(doc.get('article_id'))
    except:
        continue
    title = doc.get('title') or ''
    desc = doc.get('description') or ''
    text = (title + ' ' + desc).lower()
    id_to_text[aid] = text

# Define keyword sets for categories
science_keywords = {'science', 'scientist', 'research', 'laboratory', 'lab', 'technology', 'tech', 'nasa', 'shuttle', 'probe', 'space', 'physics', 'chemistry', 'engineer', 'engineering', 'intel', 'microsoft', 'emc', 'email storage', 'e-mail', 'email', 'silicon', 'chip', 'virus', 'software', 'electronic', 'robot', 'rocket', 'gen', 'gyrogen', 'gyro-gen', 'siemens', 'westinghouse'}
sports_keywords = {'win', 'defeat', 'olympic', 'match', 'coach', 'goal', 'score', 'tournament', 'quarter-final', 'semi-final', 'league', 'cup', 'season', 'home run', 'inning', 'draft', 'pro bowl', 'wr', 'wide receiver', 'runner', 'cycling', 'tennis', 'u.s. open', 'capriati', 'serena', 'baseball', 'football', 'soccer'}
business_keywords = {'profit', 'revenue', 'company', 'business', 'shares', 'stock', 'oil prices', 'investor', 'earnings', 'reuters', 'market', 'wto', 'trade', 'deal', 'microsoft', 'settles', 'settled', 'bank', 'kroger'}
world_keywords = {'minister', 'country', 'gaza', 'israel', 'palestine', 'iraq', 'china', 'france', 'nepal', 'kenya', 'nairobi', 'geneva', 'world', 'militant', 'militants', 'settlements', 'parliament', 'curfew'}

# Classify each of Amy's articles
total = len(amy_article_ids)
science_count = 0
unmatched_ids = []
for aid in sorted(amy_article_ids):
    text = id_to_text.get(aid, '').lower()
    if not text:
        # If article text not found, count as unmatched and skip
        unmatched_ids.append(aid)
        continue
    classified = None
    # Check science/technology first
    for kw in science_keywords:
        if kw in text:
            classified = 'Science/Technology'
            break
    if classified is None:
        for kw in sports_keywords:
            if kw in text:
                classified = 'Sports'
                break
    if classified is None:
        for kw in business_keywords:
            if kw in text:
                classified = 'Business'
                break
    if classified is None:
        for kw in world_keywords:
            if kw in text:
                classified = 'World'
                break
    if classified is None:
        # default to World if nothing matched
        classified = 'World'
    if classified == 'Science/Technology':
        science_count += 1

# Compute fraction and percentage
if total > 0:
    fraction_str = f"{science_count}/{total}"
    percentage = (science_count/total)*100
    result_str = f"{fraction_str} ({percentage:.2f}%)"
else:
    result_str = "0/0 (0.00%)"

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result_str))"""

env_args = {'var_call_DUM8w9Y5lCnOHUWY01Rdr6cb': [{'author_id': '218'}], 'var_call_Enql6oQ0R2wQxt2lwJlRou3h': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_B0K4HL8FOi0DkRd8rl1RuJRp': 'file_storage/call_B0K4HL8FOi0DkRd8rl1RuJRp.json'}

exec(code, env_args)
