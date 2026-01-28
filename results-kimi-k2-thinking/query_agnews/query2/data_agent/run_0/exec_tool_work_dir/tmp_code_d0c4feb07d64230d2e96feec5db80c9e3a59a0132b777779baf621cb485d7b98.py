code = """import json

# Access the articles data
articles = locals()['var_functions.query_db:14']

# Debug info
print(f"Number of articles: {len(articles)}")
print(f"First article: {articles[0]}")

# Classify articles by category
science_tech_keywords = [
    'science', 'technology', 'research', 'computer', 'digital', 'internet', 'software', 'hardware',
    'physics', 'chemistry', 'biology', 'engineering', 'data', 'algorithm', 'innovation', 'game',
    'energy', 'electricity', 'laboratory', 'experiment', 'scientific', 'tech', 'gen', 'wave'
]

sports_keywords = [
    'sports', 'game', 'team', 'player', 'league', 'tournament', 'championship', 'football',
    'basketball', 'baseball', 'soccer', 'olympic', 'coach', 'season', 'practice', 'bronco'
]

business_keywords = [
    'business', 'company', 'market', 'stock', 'economy', 'profit', 'revenue', 'trade',
    'finance', 'investment', 'corp', 'industry', 'sales', 'growth', 'mining', 'billiton'
]

world_keywords = [
    'politics', 'government', 'international', 'country', 'nation', 'war', 'peace',
    'president', 'minister', 'election', 'china', 'america', 'africa', 'europe', 'asia'
]

def classify_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Check for Science/Technology
    if any(keyword in text for keyword in science_tech_keywords):
        return 'Science/Technology'
    
    # Check for Sports
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    
    # Check for Business
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    
    # Check for World
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Default to World if unclear
    return 'World'

# Classify all articles
categories = []
for article in articles:
    category = classify_article(article['title'], article['description'])
    categories.append(category)

# Count categories
from collections import Counter
category_counts = Counter(categories)

# Calculate fraction of Science/Technology
total = len(articles)
science_tech_count = category_counts.get('Science/Technology', 0)
fraction = science_tech_count / total

result = {
    'total_articles': total,
    'science_tech_count': science_tech_count,
    'fraction': fraction,
    'category_breakdown': dict(category_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_articles': 111, 'article_ids': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}, 'var_functions.query_db:8': [{'_id': '696983336749e1518fa19a0a', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696983336749e1518fa1a1bb', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696983336749e1518fa1a466', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696983336749e1518fa1a4f5', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696983336749e1518fa1a6c5', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:14': [{'_id': '696983336749e1518fa19a0a', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696983336749e1518fa1a1bb', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696983336749e1518fa1a466', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696983336749e1518fa1a4f5', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696983336749e1518fa1a6c5', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
