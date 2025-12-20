code = """import json

file_path = locals()['var_function-call-6639336741831409058']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Classification Logic
tech_keywords = [
    'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'cyber', 
    'web', 'online', 'digital', 'robot', 'space', 'nasa', 'astronomy', 'galaxy', 'mars', 'moon', 
    'universe', 'biology', 'physics', 'chemistry', 'medical', 'medicine', 'health', 'disease', 
    'virus', 'cancer', 'gene', 'dna', 'cell', 'research', 'study', 'lab', 'laboratory', 'scientist', 
    'researcher', 'innovation', 'invention', 'gadget', 'device', 'mobile', 'phone', 'wireless', 
    'network', 'telecom', 'satellite', 'microsoft', 'apple', 'google', 'intel', 'ibm', 'linux', 
    'window', 'browser', 'server', 'chip', 'processor', 'data', 'algorithm', 'engine', 'machine', 
    'power', 'energy', 'electric', 'battery', 'solar', 'nuclear', 'climate', 'warming', 'environment', 
    'video game', 'gameboy', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'gamer', 'gaming', 
    'hacker', 'spam', 'malware', 'security', 'password', 'firefox', 'explorer', 'ipod', 'mp3', 
    'download', 'upload', 'file', 'email', 'blog', 'search engine', 'shuttle', 'probe', 'orbit',
    'broadband', 'wifi', 'bluetooth', 'semiconductor', 'nanotech', 'laser', 'stem cell', 'cloning',
    'automotive', 'hybrid', 'toyota', 'honda', 'ford', 'gm', 'daimler', 'chrysler' # automotive sometimes Tech or Business
]

business_financial_keywords = [
    'revenue', 'profit', 'earnings', 'loss', 'quarterly', 'share', 'stock', 'market', 'trade', 
    'wall street', 'dow', 'nasdaq', 's&p', 'economy', 'economic', 'fed', 'bank', 'finance', 
    'financial', 'investor', 'investment', 'dividend', 'ipo', 'merger', 'acquisition', 'buyout',
    'interest rate', 'inflation', 'sales', 'retail', 'forecast', 'outlook', 'jobless'
]

sports_keywords = [
    'sport', 'football', 'baseball', 'basketball', 'hockey', 'soccer', 'tennis', 'golf', 'cricket', 
    'rugby', 'team', 'club', 'league', 'season', 'game', 'match', 'cup', 'championship', 'tournament', 
    'olympic', 'medal', 'athlete', 'player', 'coach', 'manager', 'referee', 'score', 'goal', 
    'touchdown', 'homerun', 'basket', 'point', 'win', 'lose', 'defeat', 'victory', 'draw', 'tie', 
    'stadium', 'field', 'court', 'race', 'racing', 'driver', 'f1', 'nascar', 'yankees', 'red sox',
    'lakers', 'knicks', 'bulls', 'cowboys', 'broncos', 'packers', 'arsenal', 'manchester', 'liverpool',
    'real madrid', 'barcelona', 'ac milan', 'juventus', 'bayern', 'fifa', 'nfl', 'nba', 'mlb', 'nhl'
]

sci_tech_count = 0
sci_tech_articles_list = []

for art in articles:
    text = (art.get('title', '') + ' ' + art.get('description', '')).lower()
    
    # Logic:
    # 1. Check for Sports (Game, Win, Team) - careful with "Win prize" in tech.
    # 2. Check for Business Financials.
    # 3. Check for Sci/Tech.
    
    is_sports = False
    is_business = False
    is_tech = False
    
    # Heuristic for Sports vs Tech (Video Game)
    if any(k in text for k in sports_keywords):
        # Exclude if video game context
        if not ('video game' in text or 'gameboy' in text or 'nintendo' in text or 'xbox' in text or 'playstation' in text or 'wii' in text or 'gaming' in text):
             # Also check if it's "win prize" in science
            if 'science' in text or 'award' in text or 'competition' in text:
                 if 'team' in text and 'science' in text:
                     pass # Likely Sci/Tech (e.g. Science Competition Team)
                 elif 'win' in text and ('science' in text or 'tech' in text):
                     pass
                 else:
                     is_sports = True
            else:
                is_sports = True
    
    if any(k in text for k in business_financial_keywords):
        is_business = True
        
    if any(k in text for k in tech_keywords):
        is_tech = True
        
    # Decision
    category = 'World'
    
    if is_tech:
        # Tech matches. Check conflicts.
        if is_business:
            # Business + Tech.
            # If explicit financial report -> Business.
            if 'revenue' in text or 'profit' in text or 'earnings' in text or 'stock' in text or 'wall street' in text:
                category = 'Business'
            else:
                category = 'Sci/Tech'
        elif is_sports:
            # Tech + Sports?
            # e.g. "Tech used in Olympics" -> Tech. "Player plays video game" -> Tech/Sports?
            # "GameBoy mini-games" -> Tech.
            category = 'Sci/Tech'
        else:
            category = 'Sci/Tech'
            
    elif is_sports:
        category = 'Sports'
    elif is_business:
        category = 'Business'
    else:
        category = 'World'
        
    # Refinements
    if 'iraq' in text or 'bush' in text or 'kerry' in text or 'war' in text:
        if not is_tech:
            category = 'World'
            
    if category == 'Sci/Tech':
        sci_tech_count += 1
        sci_tech_articles_list.append(art['title'])

total_articles = len(articles)
fraction = sci_tech_count / total_articles if total_articles > 0 else 0

result = {
    "total": total_articles,
    "sci_tech_count": sci_tech_count,
    "fraction": fraction,
    "sci_tech_titles": sci_tech_articles_list
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7787838767695961006': [{'author_id': '218'}], 'var_function-call-15597772466275859145': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-3475040853335516502': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-9043775116014209632': [{'_id': '69449216a52ce83a68651921', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449216a52ce83a686520d2', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449216a52ce83a6865237d', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449216a52ce83a6865240c', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449216a52ce83a686525dc', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-14258200166317874943': {'total': 5, 'sci_tech_count': 3, 'sci_tech_titles': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award'], 'other_sample': [{'title': 'Bailey Tries WR', 'cat': 'World'}, {'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}]}, 'var_function-call-17791798237475886617': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_function-call-2402884922525956365': [], 'var_function-call-18345078144763632810': [{'_id': '69449216a52ce83a68651861', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69449216a52ce83a68651862', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69449216a52ce83a68651863', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69449216a52ce83a68651864', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69449216a52ce83a68651865', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12873679415327795603': [{'_id': '69449216a52ce83a68651921', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449216a52ce83a686527e3', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-1766160709305878725': [], 'var_function-call-8706062354815371496': [{'_id': '69449216a52ce83a686527e3', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-8102550089426652982': [{'_id': '69449216a52ce83a68651921', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449216a52ce83a686520d2', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449216a52ce83a6865237d', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449216a52ce83a6865240c', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449216a52ce83a686525dc', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12835033471191522845': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-6639336741831409058': 'file_storage/function-call-6639336741831409058.json'}

exec(code, env_args)
