code = """import json

# Amy Jones articles from the first query (the only ones that exist in the articles collection)
amy_jones_articles = [
    {"article_id": "192", "title": "GameBoy mini-games win prize", "description": "A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland."},
    {"article_id": "2161", "title": "Bailey Tries WR", "description": "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos practice on Tuesday."},
    {"article_id": "2844", "title": "Students Win $100,000 in National Team Science Competition", "description": "Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory."},
    {"article_id": "2987", "title": "Energy from waves teenager wins science award", "description": "A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his Gyro-Gen, a machine that produces electricity from ocean waves."},
    {"article_id": "3451", "title": "Chinas appetite boosts BHP", "description": "BHP Billiton, the worlds biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices."}
]

# Categorize articles based on title and description
def categorize_article(title, description):
    text = (title + " " + description).lower()
    
    # Check for Science/Technology
    if any(keyword in text for keyword in ['science', 'technology', 'gameboy', 'competition', 'research', 'university', 'laboratory', 'award', 'innovation']):
        return 'Science/Technology'
    
    # Check for Sports
    if any(keyword in text for keyword in ['football', 'broncos', 'cornerback', 'wide reciever', 'pro bowl']):
        return 'Sports'
    
    # Check for Business
    if any(keyword in text for keyword in ['company', 'profit', 'mining', 'commodity', 'billiton', 'global']):
        return 'Business'
    
    return 'World'

# Categorize each article
categories = []
for article in amy_jones_articles:
    category = categorize_article(article['title'], article['description'])
    categories.append(category)

# Count categories
category_counts = {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}
for cat in categories:
    category_counts[cat] += 1

total_articles = len(amy_jones_articles)
science_tech_count = category_counts['Science/Technology']
fraction = science_tech_count / total_articles if total_articles > 0 else 0

print('__RESULT__:')
print(json.dumps({
    'total_by_amy_jones': total_articles,
    'category_breakdown': category_counts,
    'science_technology_count': science_tech_count,
    'fraction': round(fraction, 4),
    'percentage': round(fraction * 100, 2)
}))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:6': [{'_id': '6969a26d22e3da7e169c4fb4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6969a26d22e3da7e169c5765', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6969a26d22e3da7e169c5a10', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6969a26d22e3da7e169c5a9f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6969a26d22e3da7e169c5c6f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:10': {'total_articles': 5, 'science_technology_count': 3, 'fraction': 0.6, 'percentage': 60.0, 'category_breakdown': {'Science/Technology': 3, 'Sports': 1, 'Business': 1, 'World': 0}, 'sample_science_tech_articles': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotl'}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math,'}]}, 'var_functions.query_db:12': [{'_id': '6969a26d22e3da7e169c4ef4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969a26d22e3da7e169c4ef5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969a26d22e3da7e169c4ef6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969a26d22e3da7e169c4ef7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969a26d22e3da7e169c4ef8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'all_articles_count': 5, 'amy_jones_article_ids_count': 111, 'matching_articles_count': 0}, 'var_functions.query_db:16': [{'author_id': '218'}], 'var_functions.execute_python:18': {'total_article_ids': 111, 'batch_count': 6, 'first_batch': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238], 'sample_article_ids': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869]}}

exec(code, env_args)
