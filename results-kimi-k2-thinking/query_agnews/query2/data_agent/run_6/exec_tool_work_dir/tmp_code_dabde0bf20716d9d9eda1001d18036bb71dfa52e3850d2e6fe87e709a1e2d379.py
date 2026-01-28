code = """# Get all stored results
articles_batch1 = locals()['var_functions.query_db:28']
articles_batch2 = locals()['var_functions.query_db:30']
articles_batch3 = locals()['var_functions.query_db:34']

# Combine all articles
all_articles = articles_batch1 + articles_batch2 + articles_batch3

print(f"Total articles retrieved: {len(all_articles)}")
print(f"Article IDs: {[a['article_id'] for a in all_articles]}")

# Categorize articles based on title and description
science_tech_keywords = [
    'game', 'science', 'technology', 'tech', 'research', 'energy', 'electricity', 'innovation',
    'competition', 'laboratory', 'wave', 'gyro', 'gen', 'electric', 'power', 'innovative'
]

sports_keywords = [
    'game', 'pro bowl', 'cornerback', 'wide receiver', 'broncos', 'practice', 'olympic',
    'gold', 'cycling', 'golf', 'par', 'championship', 'football', 'basketball', 'baseball'
]

world_keywords = [
    'gas', 'explosion', 'blast', 'belgian', 'pipeline', 'france', 'anti-semitism',
    'prime minister', 'somalia', 'parliament', 'terror', 'finance leaders', 'global'
]

business_keywords = [
    'china', 'appetite', 'boosts', 'mining', 'profits', 'commodity', 'prices',
    'food retailer', 'sells', 'stake', 'discount', 'oil', 'production', 'pharmaceutical',
    'diabetes', 'treatment', 'delay'
]

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Check for Science/Technology
    if any(keyword in text for keyword in ['science', 'technology', 'tech', 'research', 'laboratory', 'energy', 'electricity', 'wave', 'innovation', 'competition']):
        if 'game' in text and 'mini-games' in text:
            return 'Science/Technology'
        if 'science' in text or 'technology' in text or 'tech' in text or 'research' in text:
            return 'Science/Technology'
    
    # Check for Sports
    if any(keyword in text for keyword in ['pro bowl', 'cornerback', 'wide receiver', 'broncos', 'olympic', 'gold', 'cycling', 'golf', 'par', 'championship']):
        return 'Sports'
    
    # Check for World
    if any(keyword in text for keyword in ['gas explosion', 'blast', 'belgian', 'france', 'anti-semitism', 'prime minister', 'somalia', 'parliament', 'terror', 'global']):
        return 'World'
    
    # Check for Business
    if any(keyword in text for keyword in ['mining', 'profits', 'commodity', 'prices', 'food retailer', 'sells', 'stake', 'oil', 'production', 'pharmaceutical']):
        return 'Business'
    
    return 'Uncategorized'

# Categorize each article
categories = {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0, 'Uncategorized': 0}

for article in all_articles:
    category = categorize_article(article['title'], article['description'])
    categories[category] += 1
    if category == 'Science/Technology':
        print(f"Science/Tech: {article['title']}")

print(f"Categories: {categories}")
print(f"Science/Tech count: {categories['Science/Technology']}")
print(f"Total articles: {len(all_articles)}")

if len(all_articles) > 0:
    fraction = categories['Science/Technology'] / len(all_articles)
    print(f"Fraction: {fraction:.4f}")
else:
    print("No articles found")"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:6': [{'author_id': '218'}], 'var_functions.execute_python:11': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1, '_id': 0}}, 'var_functions.query_db:16': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}], 'var_functions.query_db:18': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}], 'var_functions.query_db:20': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:22': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1, '_id': 0}}, 'var_functions.query_db:24': [], 'var_functions.query_db:28': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:30': [{'article_id': '4447', 'title': 'Even in win, nasty vibes', 'description': 'ATHENS -- As you saw yesterday, they #39;re fighting back now. Not with the world, but with themselves. When you #39;ve been humiliated at your own game, ridiculed and laughed at back home and can #39;t intimidate Australia anymore, someone #39;s bound to mope. '}, {'article_id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'description': 'AFP - A Belgian gas explosion in which 20 people were killed may have resulted from a combination of a halt in the gas circulation in a pipeline and existing damage to the main, Belgian television said.'}, {'article_id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'description': 'French Prime Minister Jean-Pierre Raffarin declared Sunday that  quot;France will be extremely severe against those who perpetrate anti-semitism, quot; after visiting the Jewish social '}, {'article_id': '6869', 'title': 'Somalians sworn in', 'description': 'NAIROBI International mediators swore in members of Somalia #39;s new Parliament on Sunday, a move seen as a crucial step toward establishing the first central government in the country since 1991.'}, {'article_id': '8962', 'title': 'Muenzer races for gold', 'description': 'Athens - Edmonton #39;s Lori-Ann Muenzer moved to within one win of Olympic gold Tuesday, defeating Australian Anna Meares in the semi-final of the sprint cycling.'}], 'var_functions.query_db:34': [{'article_id': '47439', 'title': 'Charging Els moves to the top', 'description': 'Wild weather seems to bring out the best in Ernie Els, who was both steady and spectacular yesterday in a cool rain, warm sunshine, and blustery conditions for an 8-under-par 64 that gave him a two-shot lead in the American Express Championship at Thomastown, Ireland.'}, {'article_id': '48635', 'title': 'Finance Leaders Urge Vigilance on Terror (Reuters)', 'description': 'Reuters - Finance officials from all over the\\globe gathered under heavy guard on Sunday to push for a\\stepped-up fight against terror financing while warning the\\poor must not be forgotten.'}, {'article_id': '48833', 'title': 'German food retailer Spar sells 50-pct stake in Netto discount to ITM (AFP)', 'description': "AFP - Spar, Germany's eighth-biggest food supermarket chain, plans to sell a 50-percent stake in its discount arm Netto to its French parent company ITM Entreprises, Spar's new chairman Stephan Schelo said in a newspaper interview."}, {'article_id': '49035', 'title': 'But hurricanes and more impact in the third quarter', 'description': 'LONDON (CBS.MW) - British oil major BP Monday said third quarter production rose 11 percent on the year-ago quarter to 3.88 million barrels of oil equivalent a day, missing some analyst expectations for a rise of as much as 14 percent.'}, {'article_id': '52459', 'title': 'Diabetes delay adds to AstraZeneca #39;s ills', 'description': 'The UK #39;s second largest pharmaceutical company, AstraZeneca, yesterday admitted another setback in the development of some of its drugs, as it delayed the expected launch of diabetes treatment Galida for a year.'}]}

exec(code, env_args)
