code = """import json

# Load articles
data = locals()['var_function-call-14040634808463423946']
if isinstance(data, str) and not data.startswith("["):
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    articles = data

# Define keywords
# I will use a scoring system.
# Some keywords are strong indicators.

categories = {
    'Science/Technology': {
        'keywords': [
            'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 
            'mobile', 'phone', 'wireless', 'network', 'broadband', 'telecom', 'satellite', 'space', 'nasa', 'astronomy', 
            'physics', 'biology', 'chemistry', 'research', 'lab', 'laboratory', 'study', 'medical', 'health', 'disease', 
            'virus', 'cancer', 'drug', 'pharma', 'biotech', 'robot', 'gadget', 'device', 'electronic', 'game', 'gaming', 
            'video game', 'console', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'apple', 'google', 'microsoft', 'intel', 
            'ibm', 'linux', 'windows', 'browser', 'server', 'chip', 'processor', 'battery', 'solar', 'energy', 'innovation', 
            'patent', 'scientist', 'researcher', 'engineer', 'data', 'cyber', 'security', 'hacker', 'spam', 'spyware',
            'ipod', 'mp3', 'dvd', 'gps', 'blog', 'email', 'search engine', 'yahoo', 'amazon', 'ebay', 'facebook', 'myspace',
            'firefox', 'explorer', 'java', 'flash', 'algorithm', 'pixel', 'monitor', 'screen', 'keyboard', 'mouse', 'laptop', 'notebook',
            'shuttle', 'mars', 'moon', 'astronaut', 'orbit', 'galaxy', 'universe', 'telescope', 'stem cell', 'cloning', 'genetics'
        ],
        'weight': 1.0
    },
    'Sports': {
        'keywords': [
            'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympic', 'league', 
            'team', 'player', 'athlete', 'coach', 'stadium', 'match', 'tournament', 'win', 'loss', 'score', 'champion', 
            'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'club', 'cup', 'medal', 'race', 'racing', 'driver', 'f1', 'formula one',
            'cricket', 'rugby', 'boxing', 'wrestling', 'swimming', 'run', 'marathon', 'sprint', 'cycling', 'game',
            'quarterback', 'touchdown', 'goal', 'basket', 'homerun', 'strike', 'pitcher', 'batter', 'inning', 'set', 'match',
            'wimbledon', 'us open', 'french open', 'australian open', 'world cup', 'super bowl', 'world series', 'stanley cup',
            'broncos', 'reciever', 'cornerback', 'pro bowl'
        ],
        'weight': 1.0
    },
    'Business': {
        'keywords': [
            'business', 'economy', 'market', 'stock', 'trade', 'finance', 'money', 'price', 'cost', 'profit', 'revenue', 
            'sale', 'company', 'corp', 'corporation', 'inc', 'bank', 'invest', 'dollar', 'euro', 'yen', 'currency', 
            'oil', 'gas', 'mining', 'deal', 'merger', 'acquisition', 'ceo', 'cfo', 'manager', 'executive', 'share', 
            'nasdaq', 'dow', 'wall street', 'fed', 'federal reserve', 'rate', 'tax', 'inflation', 'job', 'unemployment',
            'retail', 'sales', 'consumer', 'growth', 'quarter', 'earnings', 'dividend', 'wto', 'imf', 'world bank'
        ],
        'weight': 1.0
    },
    'World': {
        'keywords': [
            'world', 'war', 'peace', 'politic', 'government', 'president', 'minister', 'election', 'vote', 'country', 
            'nation', 'state', 'military', 'army', 'navy', 'air force', 'police', 'attack', 'bomb', 'kill', 'iraq', 
            'iran', 'china', 'usa', 'uk', 'europe', 'asia', 'africa', 'un', 'united nations', 'law', 'court', 'trial', 
            'judge', 'legal', 'crime', 'prison', 'jail', 'terror', 'security', 'treaty', 'diplomat', 'foreign', 'international',
            'israel', 'palestine', 'gaza', 'syria', 'russia', 'korea', 'nuclear', 'weapon', 'blast', 'explosion', 'crash', 
            'disaster', 'storm', 'hurricane', 'typhoon', 'earthquake', 'tsunami', 'parliament', 'senate', 'congress', 'prime minister'
        ],
        'weight': 1.0
    }
}

sci_tech_count = 0
total_count = 0
classified_articles = []

# Special handling for "game" which is in both Sports and Sci/Tech
# "game" in title "GameBoy mini-games" -> Sci/Tech
# "game" in "win the game" -> Sports
# I will put "game" in both, but context matters.
# For now, let's assume if it has "video", "console", "computer", "nintendo" etc. it is Sci/Tech.

for article in articles:
    total_count += 1
    title = article.get('title', '')
    desc = article.get('description', '')
    text = (title + " " + desc).lower()
    
    scores = {cat: 0 for cat in categories}
    
    for cat, data in categories.items():
        keywords = data['keywords']
        for kw in keywords:
            if " " in kw: # Multi-word keyword
                if kw in text:
                    scores[cat] += 1
            else:
                # Basic check
                if kw in text: # Substring match can be risky e.g. "os" in "cost"
                    # Let's do token based for single words
                    # But Python split might be too simple.
                    # Let's rely on substring but check boundaries if needed?
                    # "win" in "windows" -> bad.
                    # "run" in "trunk" -> bad.
                    # "us" in "virus" -> bad.
                    
                    # Simple boundary check:
                    import re
                    if re.search(r'\b' + re.escape(kw) + r'\b', text):
                        scores[cat] += 1

    # Heuristics adjustments
    # If "game" matched both, check for tech related words.
    # If "oil" matched Business, but also "prices", it is Business.
    # "Nuclear" -> World (weapons) or Sci/Tech (power)? Usually World if "Iran", "Weapon".
    
    # Check for specific strong indicators
    if "science" in text or "technology" in text:
        scores['Science/Technology'] += 2
        
    if "nasa" in text or "space" in text:
        scores['Science/Technology'] += 1
        
    if "olympic" in text:
        scores['Sports'] += 2
        
    if "stocks" in text or "wall street" in text:
        scores['Business'] += 2
        
    if "iraq" in text or "president" in text:
        scores['World'] += 1

    best_cat = max(scores, key=scores.get)
    max_score = scores[best_cat]
    
    # Tie breaking
    # If tie between World and Business (common), Business usually specific to companies/money.
    # If tie between Sci/Tech and Business (tech companies), usually Sci/Tech if product focus, Business if stock focus.
    
    # Let's inspect some ties if necessary.
    # For now, max score wins.
    
    if best_cat == 'Science/Technology' and max_score > 0:
        sci_tech_count += 1
        classified_articles.append((title, 'Science/Technology'))
    else:
        # If score is 0, default to World? Or check manually?
        if max_score == 0:
            # Fallback or mark unknown
            classified_articles.append((title, 'Unknown'))
        else:
            classified_articles.append((title, best_cat))

result = {
    "total": total_count,
    "sci_tech_count": sci_tech_count,
    "fraction": sci_tech_count / total_count if total_count > 0 else 0,
    "details": classified_articles[:20] # Show first 20 for verification
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14328801216293120792': [{'author_id': '218'}], 'var_function-call-17750634695583173816': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-14897546693670721389': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'projection': {'_id': 0, 'article_id': 1, 'title': 1, 'description': 1}}, 'var_function-call-15351057347351575481': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'_id': 0, 'article_id': 1, 'title': 1, 'description': 1}}, 'var_function-call-13712062339796133904': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-13503341959501974273': {'total': 5, 'sci_tech_count': 3, 'fraction': 0.6, 'details': [['GameBoy mini-games win prize', 'Science/Technology'], ['Bailey Tries WR', 'Science/Technology'], ['Students Win \\$100,000 in National Team Science Competition', 'Science/Technology'], ['Energy from waves  teenager wins science award', 'Science/Technology'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-4690738625233810077': {'collection': 'articles', 'filter': {'article_id': {'$in': ['39623', '25960', 57860, '126966', 14861, 19469, 110096, '92992', '6705', '52459', '100613', 107036, '104123', 109601, '29164', 104996, 104998, 35882, 108586, 6705, '91822', '57860', 57918, '103003', 89666, '37042', '94618', '110096', 35408, 17491, '69393', '104998', '68958', '119920', 103003, '192', 124509, 82526, '69262', '99699', 40545, '62404', '101514', 64102, 93287, '124509', 93804, '35408', 119920, 2161, 15473, 29297, '93287', '21238', '122137', '123747', 54906, '93804', '105804', '96986', 9858, 36483, 112770, '20362', 101514, 69262, '120129', 41616, '82668', 91286, '78200', '2844', '5354', 57510, 103591, '80578', '89666', 91822, '108586', 37042, '116698', '23914', '119651', '48833', '82526', 104123, '72525', 126655, 192, 48833, 80578, '8962', '3451', '9858', '112770', 39623, '28079', '73025', '54906', 39117, '2987', '19469', 38608, 33489, 6869, 96986, '41616', '88911', '91286', '2161', '33489', '38608', 5354, 52459, 82668, '70498', '26535', '22354', '3970', '14861', 21238, 15100, '126655', 8962, 100613, 66827, 103695, 69393, '64102', '9677', 122137, '88553', 2844, '29297', 62754, 27429, '48635', '83273', '27429', '57510', '35882', 111422, 92992, 73025, 120129, '36483', '104996', '126412', '106908', 83273, 105804, 72525, 47439, 88911, '40545', 22354, 36182, '24495', 68958, 4447, '15100', '62754', 70498, 119651, 123747, '109601', 25960, 23914, '49035', 99699, '70608', 78200, 3451, '68509', 96641, 3970, '107036', '80853', 20362, 49035, '73684', '96641', 94618, '81851', 106908, 68509, '4447', 113058, '66827', '15473', 26535, '111422', '113058', 2987, 24495, 28079, '103591', '112063', '120765', 81851, 120765, 112063, '57918', 46531, 62404, '39117', 126412, 9677, 70608, 73684, 80853, '103695', 116698, '6869', '36182', '47439', 88553, 29164, '17491', 126966, 48635, '46531']}}, 'projection': {'_id': 0, 'article_id': 1, 'title': 1, 'description': 1}, 'limit': 1000}, 'var_function-call-14040634808463423946': 'file_storage/function-call-14040634808463423946.json'}

exec(code, env_args)
