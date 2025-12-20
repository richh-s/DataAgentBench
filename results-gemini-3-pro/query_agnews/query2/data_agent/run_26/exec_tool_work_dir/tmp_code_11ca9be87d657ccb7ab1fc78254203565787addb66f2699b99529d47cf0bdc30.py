code = """import json

# Access the articles data
# The result from query_db might be a list or a string (file path) if large.
# Based on the preview, it looks like a list.
articles_data = locals()['var_function-call-16507795083420937304']

# Keywords definitions
sci_tech_keywords = {
    'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
    'digital', 'mobile', 'phone', 'smartphone', 'cellphone', 'game', 'gaming', 'console', 'video game',
    'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'psp', 'ds', 'gameboy', 'gamer',
    'space', 'nasa', 'astronaut', 'cosmos', 'galaxy', 'universe', 'mars', 'moon', 'rocket', 'shuttle', 'station', 'satellite', 'launch',
    'robot', 'robotics', 'ai', 'artificial intelligence', 'automaton', 'cyber', 'cybernetic',
    'virus', 'hacker', 'hacking', 'security', 'firewall', 'spyware', 'malware', 'antivirus',
    'apple', 'google', 'microsoft', 'intel', 'ibm', 'linux', 'windows', 'mac', 'os', 'ios', 'android',
    'browser', 'firefox', 'explorer', 'chrome', 'safari', 'mozilla', 'opera', 'netscape',
    'search engine', 'yahoo', 'ask', 'baidu',
    'chip', 'processor', 'semiconductor', 'memory', 'ram', 'disk', 'drive', 'usb', 'bluetooth', 'wifi', 'wireless',
    'lab', 'laboratory', 'research', 'researcher', 'study', 'scientist', 'scientific',
    'physics', 'physicist', 'chemistry', 'chemist', 'chemical', 'biology', 'biologist', 'biological',
    'genetics', 'gene', 'genome', 'dna', 'stem cell', 'cloning', 'clone',
    'medicine', 'medical', 'health', 'disease', 'cancer', 'aids', 'hiv', 'virus', 'flu', 'vaccine', 'treatment', 'drug', 'therapy',
    'climate', 'warming', 'environment', 'environmental', 'energy', 'power', 'solar', 'wind', 'nuclear', 'electric', 'battery', 'fuel',
    'innovation', 'invention', 'gadget', 'device', 'gizmo', 'app', 'application',
    'ipod', 'iphone', 'ipad', 'mp3', 'player', 'camera', 'digital camera', 'lens',
    'telescope', 'microscope',
    'nanotechnology', 'biotechnology',
    'broadband', 'dsl', 'cable', 'network', 'networking', 'server', 'data', 'database',
    'code', 'coding', 'program', 'programming', 'developer', 'algorithm',
    'silicon', 'valley', 'startup'
}

# Negative keywords for Sci/Tech (words that might appear but strongly suggest another category)
# e.g. "game" in sports context. But "video game" is Sci/Tech.
# If "game" appears with "team", "coach", "score", "league" -> likely Sports.

sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 
    'cricket', 'rugby', 'racing', 'f1', 'formula 1', 'nascar', 'driver',
    'athlete', 'player', 'team', 'coach', 'manager', 'referee', 'umpire',
    'match', 'tournament', 'cup', 'league', 'championship', 'olympic', 'medal',
    'score', 'goal', 'touchdown', 'run', 'wicket', 'inning', 'quarter', 'half', 'season',
    'stadium', 'arena', 'field', 'court',
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'super bowl', 'world series'
}

business_keywords = {
    'business', 'economy', 'economic', 'market', 'stock', 'stocks', 'share', 'shares', 'trade', 'trading', 
    'finance', 'financial', 'money', 'currency', 'dollar', 'euro', 'yen', 'bank', 'banking', 
    'invest', 'investment', 'investor', 'profit', 'revenue', 'sale', 'sales', 'earnings', 
    'company', 'corporation', 'firm', 'industry', 'sector', 'ceo', 'cfo', 'executive', 'management',
    'deal', 'merger', 'acquisition', 'buyout', 'takeover', 'ipo',
    'wall street', 'dow jones', 'nasdaq', 'ftse', 'nikkei',
    'oil', 'price', 'prices', 'cost', 'budget', 'tax', 'inflation', 'recession', 'growth',
    'retail', 'store', 'product', 'brand', 'marketing', 'ad', 'advertising'
}

world_keywords = {
    'world', 'international', 'country', 'nation', 'government', 'politics', 'political', 'politician',
    'president', 'prime minister', 'minister', 'leader', 'official', 'diplomat', 'embassy',
    'war', 'conflict', 'military', 'army', 'soldier', 'troop', 'troops', 'weapon', 'arms',
    'nuclear', 'attack', 'bomb', 'blast', 'explosion', 'terror', 'terrorist', 'terrorism',
    'iraq', 'afghanistan', 'iran', 'korea', 'china', 'russia', 'us', 'usa', 'united states', 'america',
    'un', 'united nations', 'eu', 'european union',
    'election', 'vote', 'poll', 'protest', 'rally', 'riot', 'police', 'crime', 'court', 'law', 'legal', 'judge', 'trial', 'prison',
    'disaster', 'earthquake', 'tsunami', 'flood', 'storm', 'hurricane', 'typhoon', 'fire', 'crash', 'accident',
    'kill', 'death', 'dead', 'die', 'injure', 'victim', 'hostage', 'kidnap',
    'peace', 'treaty', 'agreement'
}

def classify_article(title, description):
    text = (title + " " + description).lower()
    
    # Tokenize simply
    import re
    tokens = set(re.findall(r'\w+', text))
    
    scores = {
        'Science/Technology': 0,
        'Sports': 0,
        'Business': 0,
        'World': 0
    }
    
    # Simple scoring
    for token in tokens:
        if token in sci_tech_keywords:
            scores['Science/Technology'] += 1
        if token in sports_keywords:
            scores['Sports'] += 1
        if token in business_keywords:
            scores['Business'] += 1
        if token in world_keywords:
            scores['World'] += 1
            
    # Ambiguity handling
    # "game" is in Sci/Tech, but if Sports score is high, it's likely sports.
    # Actually "game" is in sci_tech_keywords above.
    # If "game" is present and (team, player, score) are present, it's Sports.
    # I didn't put "game" in sports_keywords to avoid double counting, or I should.
    
    # Let's check max score
    if sum(scores.values()) == 0:
        return "Unknown"
        
    best_cat = max(scores, key=scores.get)
    
    # Tie breaking or specific heuristics
    # If "apple" or "google" -> usually Sci/Tech or Business.
    # If Business == Sci/Tech, check for "profit", "stock" -> Business. Check for "launch", "device" -> Sci/Tech.
    
    return best_cat

sci_tech_count = 0
total_articles = len(articles_data)
debug_list = []

for article in articles_data:
    cat = classify_article(article.get('title', ''), article.get('description', ''))
    if cat == 'Science/Technology':
        sci_tech_count += 1
        debug_list.append((article.get('title'), cat))
    else:
        # Check if it SHOULD have been Sci/Tech (manual check in thought process)
        debug_list.append((article.get('title'), cat))

fraction = sci_tech_count / total_articles if total_articles > 0 else 0

print("__RESULT__:")
print(json.dumps({"sci_tech_count": sci_tech_count, "total": total_articles, "fraction": fraction, "sample_classifications": debug_list[:20]}))"""

env_args = {'var_function-call-9793929957359986129': [{'author_id': '218'}], 'var_function-call-3246306570365587808': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-7367964593078730553': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-16507795083420937304': [{'_id': '6944a5bccd592d2c0c1b1e2c', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a5bccd592d2c0c1b25dd', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a5bccd592d2c0c1b2888', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a5bccd592d2c0c1b2917', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a5bccd592d2c0c1b2ae7', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
