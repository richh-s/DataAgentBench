code = """import json
import os

# Load all articles from the file
query_result = locals()['var_functions.query_db:44']
if isinstance(query_result, str) and query_result.endswith('.json') and os.path.exists(query_result):
    with open(query_result, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = query_result if isinstance(query_result, list) else []

# Get Amy Jones' article IDs from metadata
metadata_result = locals()['var_functions.query_db:2']
amy_jones_article_ids = [int(article['article_id']) for article in metadata_result]

# Filter Amy Jones' articles from the full collection
amy_jones_articles = [article for article in all_articles if int(article['article_id']) in amy_jones_article_ids]

# Categorize each article
def categorize_article(title, description):
    text_combined = (title + ' ' + description).lower()
    
    # Science/Technology keywords
    science_tech_keywords = [
        'science', 'technology', 'research', 'laboratory', 'laboratories', 'lab', 'experiment', 
        'energy', 'electricity', 'machine', 'innovation', 'innovative', 'game', 'games', 'gaming',
        'computer', 'software', 'hardware', 'internet', 'digital', 'robot', 'robotics', 'award',
        'competition', 'discovery', 'discover', 'invent', 'invention', 'scientist', 'researcher',
        'genetics', 'genetic', 'dna', 'physics', 'chemistry', 'biology', 'mathematics', 'math'
    ]
    
    # Sports keywords (to differentiate 'game' in sports context)
    sports_keywords = [
        'football', 'basketball', 'soccer', 'baseball', 'hockey', 'tennis', 'golf',
        'broncos', 'pro bowl', 'cornerback', 'wide receiver', 'quarterback', 'running back',
        'coach', 'player', 'team', 'league', 'season', 'game'  # 'game' is ambiguous but we'll handle it
    ]
    
    # Business keywords
    business_keywords = [
        'wall st', 'stocks', 'stock', 'economy', 'economics', 'profits', 'profit',
        'mining', 'company', 'companies', 'corporation', 'corporate', 'market', 'markets',
        'trade', 'trading', 'investment', 'investing', 'finance', 'financial', 'bank',
        'banking', 'business', 'commercial', 'industry', 'industries', 'oil', 'gas',
        'commodity', 'commodities', 'price', 'prices', 'revenue', 'sales'
    ]
    
    # Check if it's clearly sports (to avoid misclassifying sports articles)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text_combined)
    science_score = sum(1 for keyword in science_tech_keywords if keyword in text_combined)
    business_score = sum(1 for keyword in business_keywords if keyword in text_combined)
    
    # Priority: If sports indicators are strong, classify as sports
    if sports_score > 2:  # Multiple sports keywords found
        return 'Sports'
    
    # Check for Science/Technology
    for keyword in science_tech_keywords:
        if keyword in text_combined:
            # Special handling for 'game' - check if it's in a tech context
            if keyword == 'game' and ('consoles' in text_combined or 'gaming' in text_combined):
                return 'Science/Technology'
            elif keyword == 'game' and sports_score > 0:
                continue  # Skip 'game' if sports context is detected
            else:
                return 'Science/Technology'
    
    # Check for Business
    for keyword in business_keywords:
        if keyword in text_combined:
            return 'Business'
    
    # Check for Sports (if not caught by the initial check)
    for keyword in sports_keywords:
        if keyword in text_combined:
            return 'Sports'
    
    # Default to World if nothing matches
    return 'World'

# Categorize all Amy Jones' articles
categories = []
if amy_jones_articles:
    for article in amy_jones_articles:
        category = categorize_article(article['title'], article['description'])
        categories.append(category)
    
    # Count by category
    total_articles = len(categories)
    science_tech_count = categories.count('Science/Technology')
    sports_count = categories.count('Sports')
    business_count = categories.count('Business')
    world_count = categories.count('World')
    
    # Calculate fraction
    fraction = science_tech_count / total_articles if total_articles > 0 else 0
    
    result = {
        'total_articles': total_articles,
        'science_tech_count': science_tech_count,
        'sports_count': sports_count,
        'business_count': business_count,
        'world_count': world_count,
        'fraction': round(fraction, 3),
        'percentage': round(fraction * 100, 1)
    }
else:
    result = {'error': 'No articles found for Amy Jones'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:4': [{'_id': '696989275f546b04529bcf84', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989275f546b04529bd735', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989275f546b04529bd9e0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989275f546b04529bda6f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989275f546b04529bdc3f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:6': [{'_id': '696989275f546b04529bcf84', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989275f546b04529bd735', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989275f546b04529bd9e0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989275f546b04529bda6f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989275f546b04529bdc3f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:10': 'Total articles by Amy Jones: 5', 'var_functions.query_db:12': [{'_id': '696989275f546b04529bcf84', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989275f546b04529bd735', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989275f546b04529bd9e0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989275f546b04529bda6f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989275f546b04529bdc3f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:14': [{'_id': '696989275f546b04529bcec4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696989275f546b04529bcec5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696989275f546b04529bcec6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696989275f546b04529bcec7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696989275f546b04529bcec8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:16': {'total_article_ids': 111, 'first_few_int': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869], 'first_few_str': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869']}, 'var_functions.execute_python:20': "Amy Jones has 5 articles. Source: direct. Result type: <class 'list'>", 'var_functions.execute_python:22': {'total_article_ids': 111, 'first_20': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238], 'last_20': [106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}, 'var_functions.execute_python:24': {'type': "<class 'list'>", 'is_string': False, 'is_list': True, 'repr': "[{'_id': '696989275f546b04529bcf84', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a fe", 'json_files_in_dir': []}, 'var_functions.execute_python:26': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_functions.query_db:28': [], 'var_functions.execute_python:30': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238]}}}, 'var_functions.query_db:32': [{'_id': '696989275f546b04529bcf84', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989275f546b04529bd735', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989275f546b04529bd9e0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989275f546b04529bda6f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989275f546b04529bdc3f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:34': [{'_id': '696989275f546b04529bcec4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696989275f546b04529bcec5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696989275f546b04529bcec6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696989275f546b04529bcec7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696989275f546b04529bcec8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:36': {'total_articles_sampled': 5, 'science_tech_count': 3, 'fraction': 0.6, 'percentage': 60.0}, 'var_functions.execute_python:38': {'total_article_ids': 111, 'batch_sizes': [20, 40, 60, 80, 100, 111]}, 'var_functions.query_db:40': [{'_id': '696989275f546b04529bcf84', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989275f546b04529bd735', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989275f546b04529bd9e0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989275f546b04529bda6f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989275f546b04529bdc3f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:42': {'num_articles_retrieved': 5, 'result_type': "<class 'list'>", 'is_file_path': False}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_articles_in_db': 10000, 'source': 'file', 'first_few': [{'_id': '696989275f546b04529bcec4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696989275f546b04529bcec5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696989275f546b04529bcec6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.execute_python:48': {'total_metadata_article_ids': 111, 'total_existing_in_articles_db': 10000, 'amy_jones_existing_article_count': 13, 'amy_jones_articles_retrieved': 13}}

exec(code, env_args)
