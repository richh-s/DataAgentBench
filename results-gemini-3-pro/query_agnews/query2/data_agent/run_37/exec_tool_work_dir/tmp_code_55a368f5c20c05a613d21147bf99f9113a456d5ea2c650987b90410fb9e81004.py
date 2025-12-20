code = """import json
import re

# Load data
file_path = locals()['var_function-call-1952057739142738482']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Categories and Keywords (Refined)
categories = {
    'Science/Technology': [
        'technology', 'science', 'computer', 'software', 'internet', 'web', 'online', 'digital', 'robot', 
        'space', 'nasa', 'galaxy', 'mars', 'moon', 'solar', 'astronomy', 'biology', 'physics', 'chemistry', 
        'genetic', 'genome', 'dna', 'cell', 'virus', 'disease', 'medical', 'health', 'cancer', 'aids', 'hiv', 
        'research', 'study', 'lab', 'scientist', 'engineer', 'innovation', 'gadget', 'device', 'mobile', 
        'phone', 'smartphone', 'tablet', 'app', 'application', 'data', 'network', 'server', 'cloud', 'cyber', 
        'security', 'hacker', 'microsoft', 'apple', 'google', 'ibm', 'intel', 'facebook', 'twitter', 'amazon', 
        'youtube', 'netflix', 'videogame', 'game', 'gaming', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 
        'ipod', 'iphone', 'ipad', 'mac', 'windows', 'linux', 'unix', 'java', 'programming', 'code', 'algorithm', 
        'processor', 'chip', 'semiconductor', 'broadband', 'wireless', 'wifi', 'bluetooth', 'satellite', 'rocket', 
        'launch', 'orbit', 'tech', 'nanotech', 'biotech', 'browser', 'search engine', 'email', 'spam', 'virus',
        'update', 'upgrade', 'version', 'release', 'beta', 'download', 'file', 'format', 'mp3', 'dvd', 'lcd', 
        'plasma', 'screen', 'monitor', 'keyboard', 'mouse', 'drive', 'memory', 'storage', 'usb', 'flash', 'ram',
        'cpu', 'gpu', 'motherboard', 'laptop', 'notebook', 'desktop', 'pc', 'server', 'mainframe', 'supercomputer',
        'calculator', 'camera', 'pixel', 'resolution', 'image', 'video', 'audio', 'sound', 'multimedia', 'animation',
        'graphics', 'interface', 'user', 'password', 'login', 'account', 'profile', 'blog', 'forum', 'chat', 'message',
        'text', 'sms', 'mms', 'voip', 'skype', 'zoom', 'teams', 'slack', 'discord', 'whatsapp', 'telegram', 'signal',
        'viber', 'line', 'wechat', 'snapchat', 'tiktok', 'instagram', 'pinterest', 'linkedin', 'tumblr', 'reddit',
        'biometric', 'encryption', 'firewall', 'malware', 'spyware', 'phishing', 'domain', 'hosting', 'bandwidth',
        'ethernet', 'modem', 'router', 'switch', 'protocol', 'http', 'html', 'css', 'xml', 'json', 'sql', 'database',
        'oracle', 'sap', 'salesforce', 'adobe', 'photoshop', 'illustrator', 'premiere', 'flash', 'shockwave',
        'plugin', 'extension', 'addon', 'widget', 'toolbar', 'menu', 'icon', 'cursor', 'click', 'scroll', 'drag',
        'drop', 'copy', 'paste', 'cut', 'undo', 'redo', 'save', 'open', 'close', 'print', 'scan', 'fax', 'email'
    ],
    'Business': [
        'market', 'stock', 'wall street', 'dow', 'nasdaq', 'investor', 'investment', 'profit', 'revenue', 'loss', 
        'earnings', 'quarter', 'percent', 'sales', 'trade', 'economy', 'economic', 'bank', 'federal', 'fed', 
        'rate', 'inflation', 'currency', 'dollar', 'euro', 'yen', 'oil', 'gas', 'price', 'cost', 'company', 
        'corp', 'inc', 'ltd', 'share', 'merger', 'acquisition', 'deal', 'buyout', 'ceo', 'cfo', 'executive', 
        'manager', 'business', 'industry', 'commercial', 'retail', 'store', 'consumer', 'spending', 'budget', 
        'debt', 'loan', 'credit', 'finance', 'financial', 'tax', 'employment', 'job', 'hiring', 'salary', 'wage',
        'union', 'strike', 'negotiation', 'contract', 'agreement', 'partner', 'partnership', 'client', 'customer',
        'supplier', 'vendor', 'distributor', 'logistics', 'transport', 'shipping', 'cargo', 'freight', 'airline',
        'automotive', 'manufacturing', 'factory', 'plant', 'production', 'output', 'supply', 'demand', 'trend',
        'forecast', 'analyst', 'report', 'audit', 'accounting', 'regulation', 'policy', 'lawsuit', 'litigation',
        'court', 'settlement', 'fine', 'penalty', 'bankruptcy', 'insolvency', 'liquidation', 'restructuring'
    ],
    'Sports': [
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'rugby', 'cricket', 
        'team', 'club', 'league', 'match', 'game', 'tournament', 'championship', 'cup', 'win', 'loss', 'score', 
        'player', 'athlete', 'coach', 'manager', 'olympic', 'medal', 'record', 'season', 'playoff', 'final', 
        'stadium', 'field', 'court', 'race', 'driver', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 
        'open', 'bowl', 'super bowl', 'world cup', 'euro', 'copa', 'gold medal', 'silver medal', 'bronze medal',
        'qualifier', 'qualifying', 'round', 'heat', 'lap', 'goal', 'point', 'run', 'touchdown', 'basket', 'homerun',
        'inning', 'quarter', 'half', 'period', 'overtime', 'penalty', 'foul', 'referee', 'umpire', 'judge', 
        'standings', 'ranking', 'seed', 'draw', 'fixture', 'schedule', 'roster', 'squad', 'lineup', 'substitution',
        'transfer', 'draft', 'contract', 'salary', 'agent', 'fan', 'spectator', 'audience', 'broadcast', 'telecast'
    ],
    'World': [
        'world', 'international', 'country', 'nation', 'government', 'president', 'minister', 'premier', 'official', 
        'politics', 'election', 'vote', 'campaign', 'war', 'conflict', 'army', 'military', 'soldier', 'troop', 
        'attack', 'bomb', 'blast', 'explosion', 'terror', 'police', 'crime', 'court', 'judge', 'law', 'legal', 
        'treaty', 'agreement', 'nuclear', 'weapon', 'peace', 'summit', 'meeting', 'talks', 'crisis', 'disaster', 
        'storm', 'hurricane', 'flood', 'earthquake', 'tsunami', 'fire', 'crash', 'accident', 'death', 'kill', 
        'injure', 'die', 'dead', 'victim', 'human rights', 'protest', 'strike', 'union', 'labour', 'europe', 'asia', 
        'africa', 'america', 'middle east', 'iraq', 'iran', 'afghanistan', 'china', 'russia', 'usa', 'uk', 'france', 
        'germany', 'palestine', 'israel', 'syria', 'lebanon', 'jordan', 'egypt', 'libya', 'sudan', 'yemen', 'saudi', 
        'turkey', 'greece', 'spain', 'italy', 'poland', 'ukraine', 'belarus', 'romania', 'bulgaria', 'serbia', 
        'croatia', 'bosnia', 'montenegro', 'kosovo', 'albania', 'macedonia', 'greece', 'cyprus', 'malta', 'portugal', 
        'ireland', 'scotland', 'wales', 'sweden', 'norway', 'finland', 'denmark', 'iceland', 'switzerland', 'austria', 
        'hungary', 'czech', 'slovakia', 'slovenia', 'estonia', 'latvia', 'lithuania', 'moldova', 'georgia', 'armenia', 
        'azerbaijan', 'kazakhstan', 'uzbekistan', 'turkmenistan', 'kyrgyzstan', 'tajikistan', 'pakistan', 'india', 
        'bangladesh', 'sri lanka', 'nepal', 'bhutan', 'maldives', 'myanmar', 'thailand', 'laos', 'cambodia', 'vietnam', 
        'malaysia', 'singapore', 'indonesia', 'philippines', 'brunei', 'timor', 'papua', 'australia', 'new zealand', 
        'fiji', 'samoa', 'tonga', 'kiribati', 'tuvalu', 'nauru', 'vanuatu', 'solomon', 'marshall', 'micronesia', 'palau', 
        'japan', 'korea', 'mongolia', 'canada', 'mexico', 'brazil', 'argentina', 'chile', 'colombia', 'peru', 'venezuela', 
        'ecuador', 'bolivia', 'paraguay', 'uruguay', 'guyana', 'suriname', 'panama', 'costa rica', 'nicaragua', 'honduras', 
        'salvador', 'guatemala', 'belize', 'cuba', 'haiti', 'dominican', 'jamaica', 'bahamas', 'barbados', 'trinidad'
    ]
}

def classify(title, desc):
    # Weight title more
    text_title = title.lower()
    text_desc = desc.lower()
    full_text = text_title + " " + text_desc
    
    scores = {cat: 0 for cat in categories}
    
    # Specific disambiguation for context
    # If "win" or "game", check context
    
    # Scoring
    for cat, keywords in categories.items():
        for word in keywords:
            # Check title (weight 2)
            if len(word) < 4:
                 if re.search(r'\b' + re.escape(word) + r'\b', text_title):
                     scores[cat] += 2
            else:
                if word in text_title:
                    scores[cat] += 2
            
            # Check desc (weight 1)
            if len(word) < 4:
                 if re.search(r'\b' + re.escape(word) + r'\b', text_desc):
                     scores[cat] += 1
            else:
                if word in text_desc:
                    scores[cat] += 1
    
    # Boost Sci/Tech if specific strong keywords are present
    if 'science' in full_text or 'technology' in full_text or 'nasa' in full_text or 'space' in full_text or 'computer' in full_text or 'internet' in full_text:
        scores['Science/Technology'] += 3
        
    # Boost Sports if strong keywords
    if 'sport' in full_text or 'olympic' in full_text or 'nfl' in full_text or 'nba' in full_text or 'championship' in full_text:
        scores['Sports'] += 3

    # Boost Business
    if 'market' in full_text or 'stock' in full_text or 'economy' in full_text or 'company' in full_text:
        scores['Business'] += 3
        
    # Get max score
    best_cat = max(scores, key=scores.get)
    max_score = scores[best_cat]
    
    # Tie breaking
    # If tie between Sci/Tech and others, prefer Sci/Tech if 'science'/'tech' words were matched.
    # Actually, the boost handles this.
    
    return best_cat

sci_tech_count = 0
total_count = 0

# debug_list = []

for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    cat = classify(title, description)
    if cat == 'Science/Technology':
        sci_tech_count += 1
    total_count += 1
    
    # debug_list.append({
    #     'id': article.get('article_id'),
    #     'title': title,
    #     'cat': cat
    # })

result = {
    'total': total_count,
    'sci_tech': sci_tech_count,
    'fraction': sci_tech_count / total_count if total_count > 0 else 0,
    # 'debug': debug_list # Remove debug to keep output clean
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7732121751950235257': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-7700996152353519431': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-3197390966498998112': [{'_id': '6944b119c6f6625ec5ac2730', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b119c6f6625ec5ac2ee1', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b119c6f6625ec5ac318c', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b119c6f6625ec5ac321b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b119c6f6625ec5ac33eb', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-5521936711292883543': {'total': 5, 'sci_tech': 2, 'fraction': 0.4, 'debug': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'cat': 'Science/Technology'}, {'id': '2161', 'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'World'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}]}, 'var_function-call-1952057739142738482': 'file_storage/function-call-1952057739142738482.json'}

exec(code, env_args)
