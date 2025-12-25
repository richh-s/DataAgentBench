code = """import json

with open(locals()['var_function-call-5617771522699572231'], 'r') as f:
    articles = json.load(f)

def classify_debug(title, description):
    text = (title + " " + (description or "")).lower()
    
    scores = {'Sci/Tech': 0, 'Business': 0, 'Sports': 0, 'World': 0}
    
    # Keyword Lists
    
    sci_tech = {
        'science', 'technology', 'tech', 'computer', 'internet', 'web', 'software', 'hardware', 
        'digital', 'mobile', 'phone', 'smartphone', 'wireless', 'network', 'satellite', 'space', 'nasa', 
        'astronomy', 'physics', 'biology', 'genetics', 'robot', 'gadget', 'device', 'video game', 
        'nintendo', 'sony', 'microsoft', 'google', 'apple', 'intel', 'linux', 'windows', 'browser', 
        'virus', 'hacker', 'cyber', 'online', 'data', 'innovation', 'research', 'lab', 'scientist', 
        'engineer', 'shuttle', 'mars', 'moon', 'galaxy', 'telescope', 'solar', 'energy', 'battery', 
        'fuel cell', 'autonomous', 'drone', 'ai', 'artificial intelligence', 'virtual reality', 
        'gameboy', 'spam', 'spyware', 'worm', 'encryption', 'algorithm', 'database', 'code', 'coding', 
        'silicon', 'semiconductor', 'chip', 'processor', 'server', 'broadband', 'wifi', 'bluetooth',
        'supercomputer', 'cloning', 'stem cell', 'genome', 'dna', 'nanotech', 'biotech', 'console',
        'xbox', 'playstation', 'wii', 'ipod', 'itunes', 'firefox', 'mozilla', 'explorer', 'java',
        'fcc', 'telecom', 'lcd', 'plasma', 'mp3', 'dvd', 'usb', 'gps', 'blog', 'voip', 'skype',
        'ebay', 'yahoo', 'amazon', 'facebook', 'myspace', 'youtube', 'wikipedia', 'ibm', 'hp', 'dell',
        'lenovo', 'motorola', 'nokia', 'samsung', 'siemens', 'oracle', 'cisco', 'sap', 'adobe'
    }

    business = {
        'business', 'economy', 'market', 'stock', 'trade', 'finance', 'bank', 'company', 'corp', 'inc', 
        'profit', 'loss', 'revenue', 'earn', 'invest', 'deal', 'merge', 'acquire', 'acquisition', 'ceo', 
        'executive', 'industry', 'price', 'rate', 'dollar', 'euro', 'oil', 'gold', 'wall street', 
        'dow', 'nasdaq', 'sales', 'retail', 'consumer', 'spending', 'inflation', 'fed', 'treasury', 
        'bond', 'deficit', 'budget', 'tax', 'job', 'hiring', 'layoff', 'bankruptcy', 'debt', 'loan', 
        'mortgage', 'interest', 'currency', 'exchange', 'export', 'import', 'tariff', 'bid', 'offer',
        'share', 'stake', 'equity', 'capital', 'fund', 'audit', 'accounting', 'regulator', 'sec', 
        'quarter', 'forecast', 'outlook', 'estimate', 'growth', 'recession', 'depression', 'rally',
        'slump', 'plunge', 'surge', 'record', 'high', 'low', 'index', 'sector', 'airline', 'auto',
        'automaker', 'manufacturer', 'producer', 'retailer', 'store', 'shop', 'brand', 'marketing'
    }

    sports = {
        'sport', 'football', 'baseball', 'basketball', 'soccer', 'hockey', 'tennis', 'golf', 'cricket', 
        'rugby', 'team', 'game', 'match', 'player', 'coach', 'score', 'win', 'lose', 'tie', 'champion', 
        'cup', 'league', 'season', 'olympic', 'medal', 'athlete', 'stadium', 'club', 'nba', 'nfl', 
        'mlb', 'nhl', 'fifa', 'uefa', 'nascar', 'f1', 'formula', 'racing', 'race', 'tournament', 
        'playoff', 'final', 'round', 'touchdown', 'homerun', 'goal', 'basket', 'wicket', 'inning', 
        'penalty', 'foul', 'referee', 'umpire', 'manager', 'squad', 'roster', 'ranking', 'seed', 
        'qualify', 'record', 'title', 'broncos', 'yankees', 'red sox', 'lakers', 'bulls', 'cowboys', 
        'packers', 'eagles', 'patriots', 'giants', 'jets', 'mets', 'knicks', 'rangers', 'united', 
        'city', 'real', 'barcelona', 'madrid', 'liverpool', 'arsenal', 'chelsea', 'milan', 'juventus',
        'bayern', 'ferrari', 'williams', 'schumacher', 'woods', 'armstrong', 'phelps', 'williams',
        'cornerback', 'quarterback', 'receiver', 'pitcher', 'batter', 'striker', 'midfielder', 'defender',
        'goalie', 'goalkeeper'
    }

    world = {
        'world', 'news', 'politics', 'government', 'president', 'minister', 'country', 'nation', 
        'international', 'war', 'peace', 'conflict', 'army', 'military', 'police', 'court', 'law', 
        'crime', 'disaster', 'storm', 'flood', 'quake', 'election', 'vote', 'party', 'parliament', 
        'congress', 'senate', 'diplomat', 'ambassador', 'treaty', 'agreement', 'negotiation', 'sanction',
        'nuclear', 'weapon', 'terror', 'bomb', 'attack', 'kill', 'wound', 'casualty', 'death', 'dead',
        'refugee', 'immigrant', 'border', 'security', 'un', 'eu', 'nato', 'iraq', 'afghanistan', 
        'iran', 'korea', 'china', 'russia', 'usa', 'uk', 'france', 'germany', 'japan', 'israel', 
        'palestine', 'middle east', 'africa', 'asia', 'europe', 'america', 'baghdad', 'kabul', 
        'tehran', 'pyongyang', 'beijing', 'moscow', 'washington', 'london', 'paris', 'berlin', 
        'tokyo', 'jerusalem', 'gaza', 'west bank', 'cairo', 'damascus', 'beirut', 'khartoum', 'darfur',
        'balkans', 'serbia', 'kosovo', 'ukraine', 'georgia', 'venezuela', 'colombia', 'brazil', 
        'mexico', 'canada', 'australia', 'india', 'pakistan', 'kashmir', 'srilanka', 'nepal', 
        'indonesia', 'philippines', 'thailand', 'vietnam', 'burma', 'myanmar', 'sudan', 'somalia',
        'nigeria', 'zimbabwe', 'south africa', 'kenya', 'egypt', 'libya', 'syria', 'jordan', 'saudi',
        'yemen', 'oman', 'kuwait', 'qatar', 'uae', 'turkey', 'greece', 'cyprus', 'spain', 'italy',
        'vatican', 'pope', 'catholic', 'muslim', 'islam', 'jewish', 'christian', 'religious', 'religion',
        'human rights', 'red cross', 'aid', 'relief', 'rescue', 'hostage', 'kidnap', 'assassinate',
        'murder', 'suicide', 'explosion', 'blast', 'crash', 'accident', 'fire', 'burn', 'hurricane',
        'typhoon', 'cyclone', 'tsunami', 'landslide', 'mudslide', 'drought', 'famine', 'starvation',
        'disease', 'epidemic', 'virus', 'flu', 'aids', 'hiv', 'malaria', 'polio', 'vaccine', 'health',
        'hospital', 'doctor', 'nurse', 'patient', 'supreme court', 'judge', 'jury', 'verdict', 'trial',
        'prison', 'jail', 'inmate', 'guard', 'officer', 'sheriff', 'deputy', 'cop', 'detective', 
        'investigation', 'protest', 'demonstration', 'rally', 'strike', 'union', 'labor', 'activist'
    }

    # Count hits
    for w in sci_tech:
        if w in text: scores['Sci/Tech'] += 1
    for w in business:
        if w in text: scores['Business'] += 1
    for w in sports:
        if w in text: scores['Sports'] += 1
    for w in world:
        if w in text: scores['World'] += 1

    # Overrides / Weights
    if "oil" in text and "prices" in text: scores['Business'] += 5
    if "stocks" in text or "wall street" in text: scores['Business'] += 5
    if "iraq" in text or "war" in text: scores['World'] += 5
    if "olympic" in text: scores['Sports'] += 5
    if "video game" in text or "nintendo" in text or "xbox" in text: scores['Sci/Tech'] += 5

    # Contextual disambiguation
    # "Game"
    if "game" in text:
        if scores['Sci/Tech'] > scores['Sports']:
            # Likely video game
            pass
        else:
            scores['Sports'] += 2
    
    # "Chip" (could be potato chip? Unlikely in news) -> Tech
    
    # "Virus" (health vs computer)
    if "virus" in text:
        if any(x in text for x in ['computer', 'software', 'internet', 'pc', 'microsoft', 'worm']):
            scores['Sci/Tech'] += 3
        if any(x in text for x in ['flu', 'bird', 'avian', 'health', 'hospital', 'outbreak', 'human']):
            scores['World'] += 3 # Or Sci/Tech (Health)?
            # Usually Health is categorized as World or Sci/Tech depending on the source. 
            # In AG News (common dataset), Health is often Sci/Tech or World.
            # Let's assume generic news categorization: Health often Sci/Tech.
            # But "Bird Flu" often World.
            # Let's look at the dataset hint: "World, Sports, Business, or Science/Technology".
            # Usually Health is under Sci/Tech or World.
            # Let's stick to standard keywords.
            pass

    # Pick winner
    # If tie?
    # Priority: Sci/Tech > Business > Sports > World (arbitrary)
    # But usually World is default for general news.
    
    # Check if all zero
    if sum(scores.values()) == 0:
        return "Unclassified", scores
        
    best_cat = max(scores, key=scores.get)
    return best_cat, scores

sci_tech_count = 0
results = []
for article in articles:
    cat, scores = classify_debug(article['title'], article['description'])
    if cat == 'Sci/Tech':
        sci_tech_count += 1
        results.append((article['title'], scores))
    # Debug specific cases
    if "Bailey" in article['title']:
        print(f"DEBUG: {article['title']} -> {cat} {scores}")
    if "Liverpool" in article['title']:
        print(f"DEBUG: {article['title']} -> {cat} {scores}")
    if "Burma" in article['title']:
        print(f"DEBUG: {article['title']} -> {cat} {scores}")

print("__RESULT__:")
print(json.dumps({
    "sci_tech_count": sci_tech_count,
    "total": len(articles),
    "sci_tech_examples": [r[0] for r in results]
}))"""

env_args = {'var_function-call-15528725958592451348': [{'author_id': '218'}], 'var_function-call-1578166081036399350': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-16030178928395895073': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-10746133605277861360': [{'_id': '6944a74a0741a8bd2860bc34', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a74a0741a8bd2860c3e5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a74a0741a8bd2860c690', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a74a0741a8bd2860c71f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a74b0741a8bd2860c8ef', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-2352657671891290551': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP'], 'var_function-call-4959353213615004144': 5, 'var_function-call-5617771522699572231': 'file_storage/function-call-5617771522699572231.json', 'var_function-call-14598211073292394500': {'total': 111, 'sci_tech_count': 17, 'sci_tech_titles': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Liverpool prepares for life without Gerrard', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'Burma army intelligence  #39;purged #39;', 'Satellite write-downs widen DirecTV #39;s loss', 'HP to launch  #39;virus-throttling #39; software', 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}}

exec(code, env_args)
