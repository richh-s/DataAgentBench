code = """import json, os
from collections import Counter

# Load metadata for Amy Jones
metadata_result = locals()['var_functions.query_db:16']
if isinstance(metadata_result, str) and os.path.exists(metadata_result):
    with open(metadata_result, 'r') as f:
        amy_jones_articles = json.load(f)
else:
    amy_jones_articles = metadata_result

# Load articles from MongoDB
mongo_result = locals()['var_functions.query_db:14']
if isinstance(mongo_result, str) and os.path.exists(mongo_result):
    with open(mongo_result, 'r') as f:
        retrieved_articles = json.load(f)
else:
    retrieved_articles = mongo_result

article_ids = [art['article_id'] for art in amy_jones_articles]
retrieved_ids = [art['article_id'] for art in retrieved_articles]

print('Total articles by Amy Jones:', len(article_ids))
print('Articles retrieved:', len(retrieved_ids))

# Categorize articles
science_tech_keywords = [
    'technology', 'science', 'research', 'scientist', 'computer', 'software', 
    'algorithm', 'physics', 'chemistry', 'biology', 'engineering', 'data',
    'digital', 'innovation', 'device', 'energy', 'electric', 'wireless',
    'satellite', 'telescope', 'experiment', 'laboratory', 'study', 'discovery',
    'genetic', 'dna', 'medical', 'clinical', 'vaccine', 'brain', 'cancer',
    'disease', 'drug', 'molecule', 'quantum', 'laser', 'nanotechnology',
    'biotechnology', 'gameboy', 'micro-games', 'internet', 'ai', 'robot', 
    'solar', 'battery', 'chip', 'semiconductor', 'tech', 'competition', 
    'award', 'math', 'physics', 'gyro-gen', 'electricity', 'ocean waves', 
    'duke university', 'laboratory', 'samsung'
]

sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'olympic', 'sport', 'pro bowl', 'cornerback', 'wide receiver', 'broncos',
    'team', 'player', 'championship', 'race', 'medal', 'coach', 'season',
    'league', 'practice', 'game', 'play', 'competition', 'athlete', 'player',
    'olympics', 'record', 'olympic games', 'competitor'
]

business_keywords = [
    'economy', 'stocks', 'market', 'finance', 'bank', 'investment',
    'company', 'business', 'quarterly', 'profit', 'sales', 'deal',
    'revenue', 'earnings', 'industry', 'executive', 'mining', 'bhp',
    'billiton', 'commodity', 'prices', 'market', 'appetite', 'boosts',
    'china', 'economy', 'economic', 'trade', 'global', 'growth', 'stock',
    'index', 'fund', 'money', 'financial', 'corporation'
]

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    if any(kw in text for kw in science_tech_keywords):
        return 'Science/Technology'
    if any(kw in text for kw in business_keywords):
        return 'Business'
    if any(kw in text for kw in sports_keywords):
        return 'Sports'
    return 'World'

categories = []
for art in retrieved_articles:
    cat = categorize_article(art['title'], art['description'])
    categories.append(cat)
    print(f"Article {art['article_id']}: {cat} - {art['title'][:50]}")

# Count categories
counts = Counter(categories)
science_tech_count = counts.get('Science/Technology', 0)
total_categorized = len(categories)
fraction = science_tech_count / total_categorized if total_categorized > 0 else 0

print('\nCategory counts:', dict(counts))
print(f'Fraction: {science_tech_count}/{total_categorized} = {fraction:.3f}')

result = {
    'total_articles': len(article_ids),
    'categorized_articles': len(retrieved_articles),
    'science_technology_count': science_tech_count,
    'fraction': fraction
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:5': [{'_id': '6969a8b2e6173d823feeeae3', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969a8b2e6173d823feef294', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969a8b2e6173d823feef53f', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969a8b2e6173d823feef5ce', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969a8b2e6173d823feef79e', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:6': {'total_articles': 5, 'science_technology_count': 3, 'fraction': 0.6}, 'var_functions.execute_python:8': {'error': 'Truncated result'}, 'var_functions.execute_python:10': {'total_articles': 5, 'science_technology_count': 4, 'fraction': 0.8, 'all_categories': {'Science/Technology': 4, 'Business': 1}}, 'var_functions.execute_python:12': {'total_articles_by_amy_jones': 111, 'articles_retrieved': 5, 'science_technology_count': 4, 'fraction': 0.8, 'categories': ['Science/Technology', 'Science/Technology', 'Science/Technology', 'Science/Technology', 'Business']}, 'var_functions.query_db:14': [{'_id': '6969a8b2e6173d823feeeae3', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969a8b2e6173d823feef294', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969a8b2e6173d823feef53f', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969a8b2e6173d823feef5ce', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969a8b2e6173d823feef79e', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:16': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.execute_python:18': {'total_articles': 111, 'articles_retrieved': 5, 'science_tech_count': 4, 'fraction_of_retrieved': 0.8, 'warning': 'Only retrieved 5 out of 111 articles due to query limitations'}, 'var_functions.execute_python:20': {'total_article_ids': 111, 'returned_articles': 5, 'sample_ids': ['93287', '38608', '2844', '62754', '124509', '54906', '36483', '9677', '62404', '80578'], 'returned_ids': ['192', '2161', '2844', '2987', '3451']}}

exec(code, env_args)
