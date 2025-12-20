code = """import json

# Load articles directly from the variable
articles = locals()['var_function-call-12359104834319763328']

print(f"Total articles retrieved: {len(articles)}")

# Keywords
sci_tech_keywords = [
    'science', 'technology', 'tech', 'computer', 'internet', 'web', 'software', 'hardware', 
    'chip', 'processor', 'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'windows', 
    'browser', 'server', 'network', 'wireless', 'mobile', 'phone', 'cellphone', 'telecom', 
    'satellite', 'space', 'nasa', 'astronaut', 'mars', 'orbit', 'astronomy', 'physics', 
    'chemistry', 'biology', 'genetics', 'genome', 'medical', 'research', 'study', 'lab', 
    'scientist', 'researcher', 'robot', 'gadget', 'device', 'electronic', 'digital', 'online', 
    'virtual', 'cyber', 'hacker', 'virus', 'spam', 'security', 'encryption', 'game', 'gaming', 
    'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'console', 'video game', 'ipod', 'mp3', 
    'dvd', 'camera', 'pixel', 'blog', 'search engine', 'yahoo', 'amazon', 'facebook', 
    'myspace', 'youtube', 'email', 'mail', 'firefox', 'explorer', 'opera', 'netscape', 'voip',
    'skype', 'broadband', 'wifi', 'bluetooth', 'gps', 'nanotech', 'stem cell', 'cloning',
    'solar', 'energy', 'battery', 'fuel cell', 'lcd', 'plasma', 'hdtv', 'definition', 'screen',
    'monitor', 'laptop', 'notebook', 'desktop', 'pda', 'palm', 'blackberry', 'symbian', 'java',
    'flash', 'adobe', 'photoshop', 'oracle', 'sap', 'cisco', 'juniper', 'router', 'switch',
    'ethernet', 'cable', 'dsl', 'modem', 'isp', 'domain', 'hosting', 'server', 'mainframe',
    'supercomputer', 'algorithm', 'code', 'program', 'developer', 'engineer', 'technique',
    'innovative', 'innovation', 'invention', 'patent', 'copyright', 'piracy', 'p2p', 'file sharing',
    'torrent', 'napster', 'kazaa', 'bittorrent', 'itunes', 'store', 'retail', 'consumer', 'electronics'
]
# Note: 'store', 'retail' are business. 'consumer' is generic. 'electronics' is tech.

sports_keywords = [
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 
    'team', 'player', 'coach', 'match', 'cup', 'league', 'tournament', 'olympic', 'medal', 
    'champion', 'win', 'loss', 'score', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wta', 
    'atp', 'nascar', 'f1', 'formula 1', 'racing', 'athlete', 'stadium', 'club', 'game' 
    # 'game' is in both. We need logic.
]

business_keywords = [
    'business', 'company', 'corp', 'inc', 'stock', 'market', 'price', 'profit', 'loss', 
    'revenue', 'bank', 'economy', 'trade', 'deal', 'merger', 'acquisition', 'oil', 'gas', 
    'dollar', 'euro', 'yen', 'finance', 'invest', 'industry', 'ceo', 'cfo', 'shares', 
    'nasdaq', 'dow', 'wall street', 'fed', 'rates', 'inflation', 'jobs', 'unemployment',
    'sales', 'marketing', 'retail', 'consumer'
]

def classify(title, desc):
    text = (title + " " + desc).lower()
    
    st_score = 0
    sp_score = 0
    bu_score = 0
    
    # Simple counting
    for kw in sci_tech_keywords:
        if kw in text:
            st_score += 1
            
    for kw in sports_keywords:
        if kw in text:
            sp_score += 1
            
    for kw in business_keywords:
        if kw in text:
            bu_score += 1
            
    # Adjustments
    if 'game' in text:
        # If 'video game', 'computer game', 'nintendo', 'xbox', etc. are present, it's Tech.
        if any(x in text for x in ['video', 'computer', 'console', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'tech', 'software']):
            st_score += 5
        # If 'football', 'basketball', 'league', 'cup' are present, it's Sports.
        if any(x in text for x in ['football', 'basketball', 'baseball', 'hockey', 'league', 'cup', 'nfl', 'nba']):
            sp_score += 5
            
    scores = {'Science/Technology': st_score, 'Sports': sp_score, 'Business': bu_score}
    best = max(scores, key=scores.get)
    
    # Default to World if all 0?
    if scores[best] == 0:
        return 'World' # or Other
        
    return best

sci_tech_count = 0
results = []

for art in articles:
    cat = classify(art['title'], art['description'])
    if cat == 'Science/Technology':
        sci_tech_count += 1
        results.append((art['title'], 'ST'))
    else:
        results.append((art['title'], cat))

final_res = {
    "total": len(articles),
    "st_count": sci_tech_count,
    "sample": results
}

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-7921738261678552472': [{'author_id': '218'}], 'var_function-call-15988986839234050151': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-3807883415123841385': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-12359104834319763328': [{'_id': '694495f9bcd2c7e4a7fdf919', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '694495f9bcd2c7e4a7fe00ca', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '694495f9bcd2c7e4a7fe0375', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '694495f9bcd2c7e4a7fe0404', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '694495f9bcd2c7e4a7fe05d4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
