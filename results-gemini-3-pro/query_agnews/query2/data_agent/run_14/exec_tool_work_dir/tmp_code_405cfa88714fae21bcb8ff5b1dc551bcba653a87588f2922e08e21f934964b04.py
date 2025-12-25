code = """import json

# Load the file path
file_path = locals()['var_function-call-6562556386407846297']

with open(file_path, 'r') as f:
    articles = json.load(f)

categories = {
    'Sci/Tech': [
        'science', 'technology', 'tech', 'computer', 'internet', 'web', 'online', 'software', 
        'hardware', 'digital', 'mobile', 'phone', 'wireless', 'network', 'satellite', 'space', 
        'nasa', 'robot', 'gadget', 'device', 'app', 'google', 'microsoft', 'apple', 'linux', 
        'windows', 'intel', 'ibm', 'chip', 'processor', 'virus', 'hacker', 'security', 'cyber', 
        'broadband', 'telecom', 'biotech', 'biology', 'physics', 'chemistry', 'astronomy', 
        'genetic', 'research', 'lab', 'scientist', 'engineer', 'innovation', 'video game', 
        'gameboy', 'nintendo', 'sony', 'console', 'gaming', 'engine', 'machine', 'solar', 
        'energy', 'battery', 'pixel', 'browser', 'email', 'spam', 'server', 'database', 'code', 
        'programming', 'algorithm', 'data', 'gps', 'dvd', 'mp3', 'ipod', 'camera', 'emc', 'storage',
        'physicist', 'nuclear', 'astronomer', 'biologist', 'chemist', 'mathematics', 'math'
    ],
    'Sports': [
        'sport', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf', 'cricket', 
        'rugby', 'hockey', 'f1', 'nascar', 'racing', 'olympic', 'medal', 'athlete', 'champion', 
        'championship', 'tournament', 'league', 'cup', 'match', 'game', 'team', 'club', 'coach', 
        'player', 'manager', 'referee', 'stadium', 'score', 'win', 'loss', 'defeat', 'victory', 
        'season', 'playoff', 'super bowl', 'world cup', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 
        'uefa', 'quarterback', 'striker', 'goalkeeper', 'red sox', 'yankees', 'lakers', 'broncos', 'reciever', 'cornerback'
    ],
    'Business': [
        'business', 'economy', 'market', 'stock', 'share', 'trade', 'finance', 'invest', 
        'bank', 'profit', 'revenue', 'loss', 'earnings', 'corporate', 'company', 'firm', 
        'deal', 'merger', 'acquisition', 'buyout', 'bid', 'sale', 'price', 'cost', 'oil', 
        'gas', 'gold', 'currency', 'dollar', 'euro', 'yen', 'inflation', 'tax', 'budget', 
        'ceo', 'cfo', 'executive', 'manager', 'industry', 'sector', 'retail', 'sales', 
        'dow jones', 'nasdaq', 'wall street', 'fed', 'federal reserve', 'rates', 'wto', 'imf', 
        'mining', 'bhp', 'shell', 'kroger', 'store', 'consumer'
    ],
    'World': [
        'world', 'international', 'nation', 'country', 'politics', 'government', 'president', 
        'minister', 'official', 'election', 'vote', 'parliament', 'congress', 'senate', 
        'law', 'court', 'legal', 'judge', 'police', 'military', 'army', 'war', 'peace', 
        'conflict', 'attack', 'bomb', 'blast', 'explosion', 'terror', 'crisis', 'disaster', 
        'storm', 'hurricane', 'earthquake', 'tsunami', 'flood', 'kill', 'death', 'die', 
        'un', 'united nations', 'eu', 'nato', 'iraq', 'iran', 'afghanistan', 'palestine', 
        'israel', 'china', 'russia', 'usa', 'uk', 'france', 'germany', 'protest', 'strike', 'settlement', 'anti-semitism'
    ]
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # Weights for Title vs Description? Title is more important.
    # Check title specifically for strong indicators
    title_lower = title.lower()
    if 'science' in title_lower or 'technology' in title_lower:
        scores['Sci/Tech'] += 3
        
    # Adjustments
    if 'game' in text:
        if any(x in text for x in ['video', 'console', 'nintendo', 'sony', 'xbox', 'gameboy', 'computer', 'software', 'mini-game', 'micro-game']):
            scores['Sci/Tech'] += 5
        elif any(x in text for x in ['league', 'cup', 'ball', 'coach', 'player', 'season', 'nfl', 'nba', 'mlb', 'nhl', 'team', 'sport']):
            scores['Sports'] += 2
            
    if 'oil' in text or 'gas' in text:
        if any(x in text for x in ['price', 'market', 'company', 'profit', 'supply', 'stock']):
            scores['Business'] += 2
        elif any(x in text for x in ['blast', 'explosion', 'deadly', 'kill']):
            scores['World'] += 2
            
    if 'space' in text and 'shuttle' in text:
        scores['Sci/Tech'] += 5
        
    best_cat = max(scores, key=scores.get)
    
    # Priority handling
    # If Sci/Tech has a decent score, prefer it over others if close?
    # Or just strict max.
    
    # Tie breaking: Sci/Tech > Business > Sports > World?
    # If scores are equal, we want a consistent order.
    # Let's sort categories by score desc, then by priority.
    # Priority: Sci/Tech, Sports, Business, World
    priority = {'Sci/Tech': 4, 'Sports': 3, 'Business': 2, 'World': 1}
    
    sorted_cats = sorted(scores.keys(), key=lambda c: (scores[c], priority[c]), reverse=True)
    best_cat = sorted_cats[0]
    
    return best_cat

sci_tech_count = 0
total = len(articles)

for art in articles:
    cat = classify(art.get('title', ''), art.get('description', ''))
    if cat == 'Sci/Tech':
        sci_tech_count += 1

fraction = sci_tech_count / total if total > 0 else 0

print('__RESULT__:')
print(json.dumps({'total': total, 'sci_tech_count': sci_tech_count, 'fraction': fraction}))"""

env_args = {'var_function-call-4543763625448909526': [{'author_id': '218'}], 'var_function-call-18345443234622362206': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-2908010073206243140': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-8805528309593782801': [{'_id': '69449a12167fb3092dac2098', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449a12167fb3092dac2849', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449a12167fb3092dac2af4', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449a12167fb3092dac2b83', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449a12167fb3092dac2d53', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-8980571335187390356': {'total': 5, 'sci_tech_count': 2, 'fraction': 0.4}, 'var_function-call-16059281399130894669': [{'_id': '69449a12167fb3092dac1fd8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-5137302673197555686': [], 'var_function-call-16381582803236136243': [{'_id': '69449a12167fb3092dac2098', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}], 'var_function-call-16306135841593885497': [], 'var_function-call-9729880910181895876': [], 'var_function-call-1443691345671367213': [{'_id': '69449a12167fb3092dac2098', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}], 'var_function-call-13335704238129162362': [{'_id': '69449a12167fb3092dac2849', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}], 'var_function-call-13084081676049590344': 5, 'var_function-call-16758180423608854463': [{'_id': '69449a12167fb3092dac2af4', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}], 'var_function-call-14196190956062322418': [{'_id': '69449a12167fb3092dac2b83', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}], 'var_function-call-3627293955929679158': [{'_id': '69449a12167fb3092dac2d53', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-2437059294244847465': [{'_id': '69449a12167fb3092dac2f5a', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-6562556386407846297': 'file_storage/function-call-6562556386407846297.json', 'var_function-call-6880634589228552652': {'total': 111, 'sci_tech_count': 16, 'fraction': 0.14414414414414414}}

exec(code, env_args)
