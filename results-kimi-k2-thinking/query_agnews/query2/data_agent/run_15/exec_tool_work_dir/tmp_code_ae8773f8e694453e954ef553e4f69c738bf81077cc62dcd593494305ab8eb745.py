code = """# Let's analyze the articles we have
articles_data = [
    {"article_id": "192", "title": "GameBoy mini-games win prize", "description": "A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland."},
    {"article_id": "2161", "title": "Bailey Tries WR", "description": "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos practice on Tuesday."},
    {"article_id": "2844", "title": "Students Win $100,000 in National Team Science Competition", "description": "Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory."},
    {"article_id": "2987", "title": "Energy from waves teenager wins science award", "description": "A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his machine that produces electricity from ocean waves."},
    {"article_id": "3451", "title": "Chinas appetite boosts BHP", "description": "BHP Billiton, the worlds biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices."}
]

# Define keywords for Science/Technology category
sci_tech_keywords = [
    'science', 'technology', 'tech', 'research', 'study', 'experiment', 'lab', 'laboratory',
    'innovation', 'innovative', 'invention', 'discovery', 'engineering', 'computer', 'software',
    'hardware', 'internet', 'digital', 'energy', 'electricity', 'machine', 'gen', 'wave', 'waves'
]

sports_keywords = [
    'game', 'games', 'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis',
    'player', 'team', 'coach', 'season', 'league', 'championship', 'tournament', 'pro bowl',
    'cornerback', 'wide reciever', 'practice', 'broncos', 'play', 'playing', 'won', 'win',
    'prize', 'competition', 'award'
]

business_keywords = [
    'business', 'company', 'companies', 'corporation', 'stock', 'market', 'economy', 'economic',
    'profit', 'profits', 'loss', 'revenue', 'sales', 'merger', 'acquisition', 'investment',
    'investing', 'investor', 'bank', 'banking', 'crisis', 'appetite', 'boosts', 'booming',
    'commodity', 'commodities', 'prices', 'mining', 'billiton'
]

world_keywords = [
    'world', 'global', 'international', 'nation', 'national', 'country', 'countries',
    'government', 'political', 'politics', 'president', 'prime minister', 'election', 'war',
    'peace', 'china', 'chinese', 'america', 'american', 'united states', 'u.s.', 'us',
    'europe', 'european', 'asia', 'asian', 'africa', 'african'
]

def categorize_article(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    text_combined = title_lower + ' ' + desc_lower
    
    sci_tech_score = sum(1 for keyword in sci_tech_keywords if keyword in text_combined)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text_combined)
    business_score = sum(1 for keyword in business_keywords if keyword in text_combined)
    world_score = sum(1 for keyword in world_keywords if keyword in text_combined)
    
    scores = {
        'Science/Technology': sci_tech_score,
        'Sports': sports_score,
        'Business': business_score,
        'World': world_score
    }
    
    max_score = max(scores.values())
    if max_score == 0:
        return 'World'
    
    if scores['Science/Technology'] == max_score:
        return 'Science/Technology'
    elif scores['Business'] == max_score:
        return 'Business'
    elif scores['Sports'] == max_score:
        return 'Sports'
    else:
        return 'World'

categories = []
for article in articles_data:
    category = categorize_article(article['title'], article['description'])
    categories.append(category)

print('__RESULT__:')
print(categories)"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:5': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:6': 111}

exec(code, env_args)
