code = """import json

file_path = locals()['var_function-call-12578962602218889819']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
scitech_keywords = {
    'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'cyber',
    'space', 'nasa', 'microsoft', 'intel', 'ibm', 'apple', 'google', 'linux', 'virus', 'antivirus',
    'hacker', 'robot', 'biotech', 'physics', 'astronomy', 'mars', 'moon', 'galaxy', 'orbit', 
    'telecom', 'wireless', 'phone', 'mobile', 'cell', 'digital', 'electronic', 'device', 
    'gadget', 'gameboy', 'nintendo', 'sony', 'xbox', 'ps2', 'gamer', 'videogame', 'video game',
    'online', 'network', 'satellite', 'engine', 'fuel', 'battery', 'chip', 'processor', 
    'server', 'browser', 'spam', 'email', 'security', 'genetic', 'clone', 'dna', 'stem cell', 
    'research', 'lab', 'scientist', 'discovery', 'innovation', 'launch', 'shuttle', 'station',
    'telescope', 'asteroid', 'comet', 'planet', 'supernova', 'biometric', 'nanotech', 'broadband',
    'wifi', 'bluetooth', 'gps', 'lcd', 'plasma', 'mp3', 'ipod', 'itunes', 'firefox', 'explorer',
    'windows', 'oracle', 'cisco', 'dell', 'hp', 'lenovo', 'motorola', 'nokia', 'samsung',
    'search engine', 'blog', 'voip', 'phishing', 'spyware', 'malware', 'upgrade', 'beta', 'download'
}

business_keywords = {
    'business', 'company', 'market', 'stock', 'share', 'price', 'profit', 'loss', 'revenue', 
    'earnings', 'quarter', 'fiscal', 'deal', 'merge', 'acquisition', 'buy', 'sell', 'trade', 
    'invest', 'bank', 'finance', 'economy', 'inflation', 'rate', 'fed', 'wto', 'imf', 'ceo', 
    'cfo', 'manager', 'executive', 'job', 'employment', 'oil', 'gas', 'energy', 'crude', 
    'barrel', 'dollar', 'euro', 'yen', 'wall street', 'dow', 'nasdaq', 's&p', 'index', 
    'sector', 'corp', 'inc', 'ltd', 'retail', 'sale', 'consumer', 'spending', 'deficit', 
    'budget', 'tax', 'audit', 'accounting', 'bankruptcy', 'debt', 'loan', 'credit', 'mortgage',
    'airline', 'automaker', 'boeing', 'airbus', 'wal-mart', 'exxon', 'gm', 'ford', 'toyota',
    'lawsuit', 'settle', 'legal', 'court', 'regulatory', 'regulator', 'antitrust', 'monopoly',
    'dividend', 'outlook', 'forecast', 'estimate', 'bid', 'offer', 'ipo', 'venture', 'capital',
    'write-down', 'charge', 'restructure', 'layoff', 'cut', 'hiring', 'strike'
}

sports_keywords = {
    'sport', 'game', 'match', 'cup', 'league', 'team', 'coach', 'player', 'score', 'win', 
    'lose', 'victory', 'defeat', 'olympic', 'medal', 'gold', 'silver', 'bronze', 'football', 
    'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 
    'racing', 'f1', 'driver', 'athlete', 'champion', 'stadium', 'tournament', 'round', 
    'final', 'quarter', 'semi', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 
    'open', 'bowl', 'sox', 'yankee', 'mets', 'bulls', 'lakers', 'united', 'city', 'real', 
    'barcelona', 'chelsea', 'arsenal', 'liverpool', 'manchester', 'reds', 'eagles', 'patriots',
    'giants', 'jets', 'knicks', 'rangers', 'islanders', 'devils', 'nets', 'heat', 'magic',
    'dolphins', 'braves', 'phillies', 'nationals', 'orioles', 'ravens', 'redskins', 'wizards',
    'capitals', 'flyers', 'penguins', 'steelers', 'pirates', 'buccaneers', 'rays', 'lightning',
    'marlins', 'panthers', 'jaguars', 'colts', 'pacers', 'titans', 'predators', 'grizzlies',
    'blues', 'cardinals', 'rams', 'chiefs', 'royals', 'twins', 'vikings', 'timberwolves', 'wild',
    'bears', 'cubs', 'white sox', 'blackhawks', 'tigers', 'lions', 'pistons', 'red wings',
    'browns', 'indians', 'cavaliers', 'bengals', 'packers', 'brewers', 'bucks', 'cowboys',
    'mavericks', 'stars', 'texans', 'astros', 'rockets', 'spurs', 'suns', 'diamondbacks', 'coyotes',
    '49ers', 'warriors', 'sharks', 'raiders', 'athletics', 'chargers', 'padres', 'kings',
    'clippers', 'ducks', 'angels', 'dodgers', 'mariners', 'seahawks', 'sonics', 'blazers', 'jazz',
    'nuggets', 'rockies', 'avalanche', 'olympics', 'marathon', 'sprint', 'relay'
}

world_keywords = {
    'world', 'international', 'government', 'president', 'minister', 'prime', 'official', 
    'state', 'country', 'nation', 'war', 'peace', 'treaty', 'talk', 'negotiation', 'attack', 
    'bomb', 'blast', 'explosion', 'kill', 'dead', 'injure', 'soldier', 'troop', 'army', 
    'military', 'police', 'arrest', 'prison', 'law', 'court', 'judge', 'trial', 'election', 
    'vote', 'poll', 'campaign', 'candidate', 'party', 'leader', 'un', 'united nations', 
    'security council', 'iraq', 'iran', 'palestine', 'israel', 'afghanistan', 'china', 
    'russia', 'north korea', 'baghdad', 'kabul', 'gaza', 'west bank', 'jerusalem', 'darfur', 
    'sudan', 'hurricane', 'storm', 'earthquake', 'flood', 'disaster', 'tsunami', 'typhoon',
    'cyclone', 'tornado', 'fire', 'crash', 'accident', 'hostage', 'kidnap', 'rebel', 'insurgent',
    'terror', 'qaeda', 'taliban', 'hamas', 'hezbollah', 'jihad', 'nuclear', 'weapon', 'atomic',
    'diplomat', 'ambassador', 'embassy', 'parliament', 'senate', 'congress', 'legislation',
    'bill', 'act', 'ban', 'sanction', 'border', 'immigrant', 'refugee', 'asylum', 'protest',
    'demonstration', 'strike', 'riot', 'coup', 'human rights', 'aid', 'relief', 'red cross'
}

scitech_count = 0
total_count = len(articles)
scitech_articles = []

for article in articles:
    text = (article['title'] + " " + article['description']).lower()
    
    # Tokenize simply
    words = set(text.replace('.', '').replace(',', '').replace('"', '').replace("'", '').split())

    # Scoring
    score_scitech = len(words.intersection(scitech_keywords))
    score_business = len(words.intersection(business_keywords))
    score_sports = len(words.intersection(sports_keywords))
    score_world = len(words.intersection(world_keywords))
    
    # Adjustments
    if 'video game' in text or 'gameboy' in text:
        score_scitech += 3
    if 'olympic' in text:
        score_sports += 3
    
    scores = {'Science/Technology': score_scitech, 'Business': score_business, 
              'Sports': score_sports, 'World': score_world}
    
    # Resolve conflicts
    if score_scitech > 0 and score_business > 0:
        # If financial terms are strong, prefer Business
        if any(w in words for w in ['stock', 'share', 'profit', 'loss', 'revenue', 'market', 'earnings', 'quarter', 'result']):
            scores['Business'] += 2
        # If merger/acquisition
        if any(w in words for w in ['merger', 'acquisition', 'deal', 'buy', 'sell']):
            scores['Business'] += 2
    
    # Handle zeros
    if max(scores.values()) == 0:
        # Default to World if ambiguous? Or Business?
        # Let's inspect "Cherkasky" and "Call Service" cases.
        # "Call Service with a Sneer" -> "Sneer" is emotion. "Service" is generic.
        # Maybe I should just ignore "Call Service" for now.
        pass

    best_category = max(scores, key=scores.get)
    if scores[best_category] == 0:
        # If all 0, default to 'World' as it's often general news, or check if 'Business' fits better?
        # Let's just assign 'World' as a fallback.
        best_category = 'World'
    
    if best_category == 'Science/Technology':
        scitech_count += 1
        scitech_articles.append(article['title'])

print("__RESULT__:")
print(json.dumps({"total": total_count, "scitech_count": scitech_count, "scitech_titles": scitech_articles}))"""

env_args = {'var_function-call-8261879849909471108': [{'author_id': '218'}], 'var_function-call-16924440477281949050': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-5657054443732360127': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-5893484946564982131': [{'_id': '69449fe8ebf551b1a9d3f69e', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449fe8ebf551b1a9d3fe4f', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449fe8ebf551b1a9d400fa', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449fe8ebf551b1a9d40189', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449fe8ebf551b1a9d40359', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-10504055220596960736': 5, 'var_function-call-3208385939353031017': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966'], 'var_function-call-18178766340529439150': [], 'var_function-call-7154421778765295367': [{'_id': '69449fe8ebf551b1a9d40560', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-12578962602218889819': 'file_storage/function-call-12578962602218889819.json', 'var_function-call-4408787667420472293': {'total': 111, 'scitech_count': 18, 'scitech_titles': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Satellite write-downs widen DirecTV #39;s loss', "Cherkasky says Marsh may settle Spitzer's lawsuit within a month", 'Call Service with a Sneer (Reuters)', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}}

exec(code, env_args)
