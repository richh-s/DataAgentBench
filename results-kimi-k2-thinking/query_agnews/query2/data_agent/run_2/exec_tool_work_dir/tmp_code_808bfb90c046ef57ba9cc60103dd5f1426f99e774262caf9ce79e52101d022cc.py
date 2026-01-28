code = """import json
import os

# Access the MongoDB query result - it might be a string file path or a dict
db_result = locals()['var_functions.query_db:6']

# If it's a string, assume it's a file path
if isinstance(db_result, str):
    # Read the full results from the file
    with open(db_result, 'r') as f:
        articles = json.load(f)
else:
    # Use the result directly (should be list of dicts)
    articles = db_result

# Get the list of all article IDs for Amy Jones from SQL
sql_result = locals()['var_functions.query_db:5']
if isinstance(sql_result, str):
    with open(sql_result, 'r') as f:
        sql_result = json.load(f)

sql_article_ids = {int(row['article_id']) for row in sql_result}

# Filter MongoDB articles to only those by Amy Jones (should already be filtered)
valid_articles = []
for doc in articles:
    try:
        aid = int(doc['article_id'])
        if aid in sql_article_ids:
            valid_articles.append(doc)
    except Exception as e:
        continue

# Analyze categories
def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    # Keywords for categories
    science_tech = {'science', 'technology', 'tech', 'research', 'laboratory', 'experiment', 'computer', 'software', 'hardware', 'internet', 'digital', 'data', 'physics', 'chemistry', 'biology', 'mathematics', 'engineering', 'innovation', 'discovery', 'scientific', 'technical', 'gameboy', 'competition', 'award', 'energy', 'electricity', 'gyro-gen'}
    sports = {'pro bowl', 'cornerback', 'wide receiver', 'broncos', 'practice', 'game', 'match', 'tournament', 'championship', 'football', 'basketball', 'baseball', 'soccer'}
    business = {'company', 'profits', 'mining', 'commodity', 'prices', 'business', 'market', 'economy', 'bhp', 'billiton', 'stock', 'investment', 'finance'}
    world = {'china', 'world', 'global', 'international', 'country', 'nation', 'government', 'political', 'foreign'}
    # Determine category
    is_science_tech = any(k in text for k in science_tech)
    is_sports = any(k in text for k in sports)
    is_business = any(k in text for k in business)
    is_world = any(k in text for k in world)
    # Priority: if multiple, use first match in order Science/Technology, Sports, Business, World
    if is_science_tech:
        return 'Science/Technology'
    if is_sports:
        return 'Sports'
    if is_business:
        return 'Business'
    if is_world:
        return 'World'
    return 'Other'

# Count categories
category_counts = {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0, 'Other': 0}
categorized = []
for art in valid_articles:
    cat = categorize_article(art.get('title', ''), art.get('description', ''))
    category_counts[cat] += 1
    categorized.append({'article_id': art.get('article_id'), 'title': art.get('title'), 'category': cat})

total = len(valid_articles)
science_tech_total = category_counts['Science/Technology']
fraction = science_tech_total / total if total > 0 else 0

# Produce final answer JSON
result = {
    'total_articles': total,
    'science_tech_count': science_tech_total,
    'fraction': round(fraction, 4),
    'category_breakdown': category_counts
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': [{'author_id': '218'}], 'var_functions.query_db:5': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:6': [{'_id': '6969842046fb0ee65a55a209', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969842046fb0ee65a55a9ba', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969842046fb0ee65a55ac65', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969842046fb0ee65a55acf4', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969842046fb0ee65a55aec4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:8': {'total_articles': 5, 'science_tech_count': 1, 'fraction': 0.2}, 'var_functions.execute_python:10': {'total_sql_articles': 111, 'found_in_mongodb': 5, 'missing_in_mongodb': 106, 'missing_sample': [8962, 57860, 100613, 66827, 14861, 19469, 103695, 110096, 69393, 122137]}, 'var_functions.execute_python:12': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1}}}

exec(code, env_args)
