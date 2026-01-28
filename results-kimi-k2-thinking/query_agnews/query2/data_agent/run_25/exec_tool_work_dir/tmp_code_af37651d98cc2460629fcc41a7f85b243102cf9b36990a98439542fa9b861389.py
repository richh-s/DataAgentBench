code = """import json
import re

# Access results
author_data = var_functions.query_db:0
metadata_articles = var_functions.query_db:2
article_details = var_functions.query_db:4

# Debug: check what we have
print('Author data:', author_data)
print('Number of articles in metadata:', len(metadata_articles))
print('Number of articles retrieved:', len(article_details))
print('First few retrieved:', [a['article_id'] for a in article_details[:3]])

# Function to classify article category
def classify_category(title, description):
    text = (title + ' ' + description).lower()
    
    # Science/Technology indicators
    sci_tech_keywords = [
        'science', 'technology', 'tech', 'research', 'laboratory', 'university', 
        'student', 'award', 'competition', 'energy', 'electricity', 'game', 'gameboy',
        'innovation', 'innovative', 'experiment', 'study', 'data', 'computer',
        'internet', 'software', 'hardware', 'robot', 'battery', 'medical', 'genetic',
        'physics', 'chemistry', 'biology', 'mathematics', 'math', 'discovery',
        'scientist', 'engineer', 'engineering', 'nasa', 'space', 'satellite',
        'solar', 'renewable', 'climate', 'environmental', 'digital'
    ]
    
    # Sports indicators  
    sports_keywords = [
        'game', 'team', 'player', 'coach', 'season', 'league', 'tournament',
        'championship', 'football', 'soccer', 'basketball', 'baseball', 'hockey',
        'tennis', 'golf', 'olympics', 'medal', 'win', 'score', 'goal', 'quarterback',
        'running back', 'wide receiver', 'broncos', 'practice', 'training',
        'athlete', 'competition', 'match', 'playoff', 'final'
    ]
    
    # Business indicators
    business_keywords = [
        'business', 'company', 'corporation', 'profit', 'loss', 'revenue', 'earnings',
        'stock', 'market', 'economy', 'economic', 'trade', 'industry', 'mining',
        'oil', 'gas', 'price', 'investment', 'investor', 'bank', 'financial',
        'quarter', 'annual', 'sales', 'growth', 'decline', 'market', 'shares'
    ]
    
    # World indicators (general news, politics, etc.)
    world_keywords = [
        'government', 'political', 'election', 'president', 'prime minister',
        'congress', 'senate', 'war', 'conflict', 'peace', 'treaty', 'diplomatic',
        'international', 'country', 'nation', 'china', 'us', 'uk', 'france',
        'germany', 'russia', 'japan', 'korea', 'india', 'afghanistan', 'iraq',
        'iran', 'israel', 'palestine', 'united nations', 'un', 'eu', 'union'
    ]
    
    # Check for Science/Technology first (it has many specific terms)
    if any(keyword in text for keyword in sci_tech_keywords):
        if not any(sport in text for sport in ['football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf', 'olympics']):
            return 'Science/Technology'
    
    # Check for Sports
    if any(keyword in text for keyword in sports_keywords):
        # Distinguish between game (sports) and game (video game)
        if 'gameboy' in text or 'video game' in text or 'digital' in text or 'software' in text:
            return 'Science/Technology'
        sport_count = sum(1 for keyword in sports_keywords if keyword in text)
        if sport_count >= 2:  # Multiple sports terms = likely sports
            return 'Sports'
    
    # Check for Business
    if any(keyword in text for keyword in business_keywords):
        business_count = sum(1 for keyword in business_keywords if keyword in text)
        if business_count >= 2:
            return 'Business'
    
    # Check for World news
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Default based on common patterns
    return 'World'  # Most general category

# Classify the few articles we have
sci_tech_count = 0
total_classified = len(article_details)

print('\nClassifying retrieved articles:')
for article in article_details:
    category = classify_category(article['title'], article['description'])
    print(f"  {article['article_id']}: {category} - {article['title'][:50]}...")
    if category == 'Science/Technology':
        sci_tech_count += 1

fraction = sci_tech_count / total_classified if total_classified > 0 else 0
print(f'\nScience/Technology: {sci_tech_count}/{total_classified} = {fraction:.3f}')

# Output result
result_data = {
    'author': 'Amy Jones',
    'total_known_articles': len(metadata_articles),
    'classified_articles': total_classified,
    'sci_tech_count': sci_tech_count,
    'fraction': fraction,
    'note': 'Only partial data retrieved from articles collection'
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:4': [{'_id': '696997e60f9b1ae348c0a69b', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696997e60f9b1ae348c0ae4c', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696997e60f9b1ae348c0b0f7', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696997e60f9b1ae348c0b186', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696997e60f9b1ae348c0b356', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
