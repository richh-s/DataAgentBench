code = """import json
import re

# Load articles
with open(locals()['var_function-call-6280066398469303272'], 'r') as f:
    articles = json.load(f)

# Keyword lists
# Sci/Tech
scitech_kw = set([
    'technology', 'science', 'computer', 'internet', 'software', 'hardware', 'web', 'online', 'digital', 'cyber', 
    'wireless', 'mobile', 'robot', 'ai', 'nasa', 'space', 'astronomy', 'biology', 'physics', 'chemistry', 
    'genetics', 'dna', 'medical', 'medicine', 'health', 'disease', 'virus', 'vaccine', 'research', 'scientist', 
    'laboratory', 'gadget', 'device', 'electronics', 'video game', 'console', 'nintendo', 'sony', 'microsoft', 
    'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'mac', 'browser', 'search engine', 'yahoo', 'amazon', 
    'facebook', 'twitter', 'email', 'hacker', 'security', 'chip', 'server', 'database', 'network', 'wifi', 
    'gameboy', 'xbox', 'playstation', 'ipod', 'smartphone', 'laptop', 'desktop', 'screen', 'battery', 'energy', 
    'solar', 'nuclear', 'cell', 'telescope', 'microscope', 'nanotech', 'biotech', 'broadband', 'satellite', 'gps',
    'firefox', 'explorer', 'spam', 'spyware', 'malware', 'blog', 'blogger', 'myspace', 'youtube', 'itunes', 'mp3',
    'dvd', 'hdtv', 'lcd', 'plasma', 'voip', 'skype', 'telecom', 'phone', 'tech', 'supercomputer', 'mainframe', 
    'physics', 'astrophysics', 'cloning', 'stem cell', 'genome', 'mars', 'rover', 'shuttle', 'station',
    'oracle', 'cisco', 'hp', 'dell', 'lenovo', 'motorola', 'nokia', 'samsung', 'lg', 'panasonic', 'toshiba',
    'bionic', 'prosthetic', 'transplant', 'surgery', 'surgeon', 'doctor', 'physician', 'hospital', 'clinic',
    'drug', 'pharmaceutical', 'fda', 'clinical', 'trial', 'cancer', 'hiv', 'aids', 'flu', 'malaria', 'bacteria',
    'infection', 'epidemic', 'pandemic', 'hubble', 'comet', 'asteroid', 'meteor', 'galaxy', 'universe', 'black hole',
    'supernova', 'quantum', 'relativity', 'gravity', 'algorithm', 'code', 'coding', 'programming', 'programmer',
    'developer', 'app', 'application', 'api', 'sdk', 'ide', 'open source', 'linux', 'unix', 'java', 'python',
    'c++', 'perl', 'php', 'html', 'xml', 'css', 'javascript', 'ajax', 'web 2.0', 'social networking', 'cloud computing',
    'virtualization', 'saas', 'paas', 'iaas', 'big data', 'analytics', 'data mining', 'machine learning', 'artificial intelligence'
])

# Business
business_kw = set([
    'stock', 'share', 'market', 'profit', 'revenue', 'quarter', 'earnings', 'invest', 'trade', 'deal', 'merger', 
    'acquisition', 'buyout', 'ipo', 'ceo', 'cfo', 'executive', 'business', 'economy', 'financial', 'bank', 'fund',
    'bond', 'debt', 'loan', 'credit', 'rate', 'interest', 'inflation', 'deflation', 'recession', 'gdp', 'budget',
    'deficit', 'tax', 'corporate', 'corporation', 'company', 'industry', 'sector', 'commerce', 'commercial',
    'sales', 'retail', 'consumer', 'spending', 'dow', 'nasdaq', 's&p', 'wall street', 'investor', 'shareholder',
    'dividend', 'yield', 'currency', 'dollar', 'euro', 'yen', 'exchange', 'forex', 'commodity', 'oil', 'gas',
    'gold', 'silver', 'price', 'cost', 'expense', 'margin', 'valuation', 'capital', 'venture', 'equity', 'asset',
    'liability', 'audit', 'accounting', 'regulator', 'sec', 'fed', 'central bank', 'treasury', 'imf', 'wto',
    'nafta', 'tariff', 'subsidy', 'outsourcing', 'offshoring', 'layoff', 'job', 'unemployment', 'hiring', 'labor',
    'union', 'strike', 'negotiation', 'contract', 'agreement', 'settlement', 'lawsuit', 'antitrust', 'monopoly'
])

# Sports
sports_kw = set([
    'sport', 'game', 'team', 'player', 'coach', 'manager', 'cup', 'league', 'championship', 'tournament',
    'win', 'loss', 'victory', 'defeat', 'score', 'goal', 'point', 'touchdown', 'homerun', 'basket', 'run',
    'medal', 'olympic', 'athlete', 'athletics', 'football', 'soccer', 'basketball', 'baseball', 'tennis',
    'golf', 'cricket', 'rugby', 'hockey', 'boxing', 'wrestling', 'swimming', 'cycling', 'racing', 'formula 1',
    'nascar', 'driver', 'rider', 'match', 'bout', 'fight', 'round', 'final', 'semifinal', 'quarterfinal',
    'playoff', 'season', 'standings', 'rank', 'seed', 'club', 'franchise', 'stadium', 'arena', 'field',
    'court', 'track', 'pool', 'gym', 'training', 'practice', 'injury', 'roster', 'trade', 'draft', 'contract',
    'signing', 'transfer', 'agent', 'referee', 'umpire', 'judge', 'official', 'foul', 'penalty', 'red card',
    'yellow card', 'offside', 'strike', 'ball', 'bat', 'racquet', 'helmet', 'jersey', 'uniform',
    'world cup', 'super bowl', 'world series', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'ncaa'
])

# World
world_kw = set([
    'world', 'international', 'government', 'president', 'minister', 'prime minister', 'leader', 'politician',
    'party', 'election', 'vote', 'campaign', 'candidate', 'poll', 'parliament', 'congress', 'senate', 'legislation',
    'law', 'bill', 'court', 'trial', 'judge', 'jury', 'verdict', 'justice', 'police', 'arrest', 'crime', 'prison',
    'jail', 'war', 'peace', 'military', 'army', 'navy', 'air force', 'soldier', 'troop', 'weapon', 'gun', 'bomb',
    'blast', 'explosion', 'attack', 'terror', 'terrorism', 'terrorist', 'rebel', 'insurgent', 'guerrilla', 'militia',
    'conflict', 'fight', 'battle', 'clash', 'violence', 'kill', 'die', 'dead', 'death', 'injury', 'wound', 'casualty',
    'victim', 'hostage', 'kidnap', 'abduct', 'protest', 'demonstration', 'rally', 'strike', 'riot', 'coup',
    'regime', 'dictator', 'human rights', 'refugee', 'asylum', 'immigrant', 'border', 'security', 'foreign',
    'diplomat', 'embassy', 'treaty', 'agreement', 'sanction', 'united nations', 'un', 'nato', 'eu', 'european union',
    'middle east', 'iraq', 'iran', 'afghanistan', 'pakistan', 'israel', 'palestine', 'syria', 'russia', 'china',
    'japan', 'korea', 'india', 'africa', 'asia', 'europe', 'latin america', 'north korea', 'baghdad', 'kabul',
    'jerusalem', 'gaza', 'west bank', 'beijing', 'moscow', 'london', 'paris', 'washington', 'disaster', 'accident',
    'crash', 'plane', 'train', 'bus', 'ship', 'boat', 'fire', 'flood', 'storm', 'hurricane', 'typhoon', 'tornado',
    'earthquake', 'tsunami', 'volcano', 'famine', 'drought', 'environment', 'climate', 'warming'
])

# Ambiguous cleanup
# "game" in Sports vs "video game" in SciTech. 
# Strategy: Pre-process text to handle "video game" as a single token or prioritize scitech if "video" + "game".
# "oil" in Business vs SciTech (energy)? Usually Business context in news (prices).

scitech_titles = []
for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    # Simple tokenization
    tokens = re.findall(r'\w+', text)
    
    # Scoring
    s_tech = 0
    s_bus = 0
    s_sport = 0
    s_world = 0
    
    for token in tokens:
        if token in scitech_kw: s_tech += 1
        if token in business_kw: s_bus += 1
        if token in sports_kw: s_sport += 1
        if token in world_kw: s_world += 1
        
    # Heuristics for phrases
    if 'video game' in text: s_tech += 2
    if 'computer game' in text: s_tech += 2
    if 'space shuttle' in text: s_tech += 2
    if 'stock market' in text: s_bus += 2
    if 'prime minister' in text: s_world += 2
    if 'human rights' in text: s_world += 2
    
    # Specific adjustment
    if 'oil' in tokens:
        if 'price' in tokens or 'market' in tokens: s_bus += 2
    
    if 'microsoft' in tokens or 'google' in tokens or 'apple' in tokens or 'intel' in tokens:
        # Check context
        if 'profit' in tokens or 'revenue' in tokens or 'stock' in tokens:
            s_bus += 3 # Strong pull to Business
        else:
            s_tech += 3 # Strong pull to Tech
            
    # NASA is strong Tech
    if 'nasa' in tokens: s_tech += 5
    
    # Sports teams/terms
    if 'olympic' in tokens: s_sport += 5
    if 'champion' in tokens: s_sport += 2
    if 'coach' in tokens: s_sport += 2
    
    # Determine category
    scores = {'Sci/Tech': s_tech, 'Business': s_bus, 'Sports': s_sport, 'World': s_world}
    # Priority: if max is 0, maybe look closer?
    
    # Tie breaking:
    # If Tech and Business tie, and it mentions a tech company, usually Business if about money.
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        # Default or unclassified.
        # Check titles?
        # "Raffarin pledges..." -> World.
        pass
    
    # Refined check for "Intel lowers revenue" -> Business
    if 'intel' in tokens and 'revenue' in tokens:
        if s_bus >= s_tech: best_cat = 'Business'
        
    if best_cat == 'Sci/Tech':
        scitech_titles.append(article.get('title'))

print("__RESULT__:")
print(json.dumps({"count": len(scitech_titles), "total": len(articles), "titles": scitech_titles}))"""

env_args = {'var_function-call-272766112025871937': [{'author_id': '218'}], 'var_function-call-1129033257989242514': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-2517229971613781264': {'count': 111, 'ids': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}, 'var_function-call-5205776640490666422': [{'_id': '6944b5055d1fedd5e55e6c80', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b5055d1fedd5e55e7431', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b5055d1fedd5e55e76dc', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b5055d1fedd5e55e776b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b5055d1fedd5e55e793b', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-15430713433211264809': {'count': 4, 'total': 5, 'titles': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award']}, 'var_function-call-13974877051957634948': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966'], 'var_function-call-2361739143471268052': [], 'var_function-call-6280066398469303272': 'file_storage/function-call-6280066398469303272.json'}

exec(code, env_args)
