code = """import json

# Load articles
file_path = locals()['var_function-call-14645694745949228888']
with open(file_path, 'r') as f:
    articles = json.load(f)

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
    'solar', 'energy', 'battery', 'fuel cell', 'shuttle', 'telescope', 'hubble', 'supercomputer',
    'ibm', 'dell', 'hp', 'compaq', 'palm', 'pda', 'blackberry', 'algorithm', 'program', 'code'
]

sports_keywords = [
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 
    'team', 'player', 'coach', 'match', 'cup', 'league', 'tournament', 'olympic', 'medal', 
    'champion', 'win', 'loss', 'score', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wta', 
    'atp', 'nascar', 'f1', 'formula 1', 'racing', 'athlete', 'stadium', 'club', 'game', 
    'quarterback', 'receiver', 'cornerback', 'touchdown', 'offense', 'defense', 'practice', 
    'bowl', 'rookie', 'squad', 'ranking', 'title', 'championship', 'red sox', 'yankees', 
    'dodgers', 'giants', 'mets', 'bulls', 'lakers', 'celtics', 'knicks', 'rangers', 'flyers', 
    'eagles', 'patriots', 'cowboys', '49ers', 'packers', 'steelers', 'raiders', 'broncos',
    'mariners', 'athletics', 'cardinals', 'astros', 'braves', 'marlins', 'phillies', 'nationals',
    'wizards', 'pistons', 'heat', 'spurs', 'suns', 'mavericks', 'rockets', 'clippers', 'warriors',
    'kings', 'ducks', 'sharks', 'stars', 'wild', 'blues', 'predators', 'hurricanes', 'lightning',
    'panthers', 'jaguars', 'colts', 'titans', 'texans', 'bills', 'dolphins', 'jets', 'ravens',
    'bengals', 'browns', 'chiefs', 'chargers', 'rams', 'seahawks', 'buccaneers', 'saints',
    'falcons', 'vikings', 'lions', 'bears', 'arsenal', 'chelsea', 'liverpool', 'manchester',
    'real madrid', 'barcelona', 'ac milan', 'juventus', 'inter milan', 'bayern munich',
    'world cup', 'super bowl', 'world series', 'ncaa'
]

business_keywords = [
    'business', 'company', 'corp', 'inc', 'stock', 'market', 'price', 'profit', 'loss', 
    'revenue', 'bank', 'economy', 'trade', 'deal', 'merger', 'acquisition', 'oil', 'gas', 
    'dollar', 'euro', 'yen', 'finance', 'invest', 'industry', 'ceo', 'cfo', 'shares', 
    'nasdaq', 'dow', 'wall street', 'fed', 'rates', 'inflation', 'jobs', 'unemployment',
    'sales', 'marketing', 'retail', 'consumer', 'earnings', 'forecast', 'estimate'
]

world_keywords = [
    'world', 'government', 'president', 'minister', 'war', 'peace', 'election', 'country', 
    'state', 'police', 'military', 'attack', 'bomb', 'kill', 'official', 'united nations', 
    'un', 'eu', 'treaty', 'iraq', 'iran', 'china', 'russia', 'usa', 'uk', 'france', 'germany',
    'israel', 'palestine', 'gaza', 'baghdad', 'kabul', 'afghanistan', 'terrorism', 'terrorist',
    'qaeda', 'bush', 'kerry', 'blair', 'putin', 'sharon', 'arafat', 'hussein', 'congress',
    'senate', 'parliament', 'law', 'court', 'judge', 'trial', 'prison', 'jail', 'crime',
    'murder', 'kidnap', 'hostage', 'explosion', 'blast', 'crash', 'disaster', 'hurricane',
    'storm', 'flood', 'earthquake', 'tsunami', 'politic', 'democrat', 'republican'
]

def classify(title, desc):
    text = (title + " " + desc).lower()
    
    st_score = 0
    sp_score = 0
    bu_score = 0
    wo_score = 0
    
    # Simple counting
    for kw in sci_tech_keywords:
        if kw in text:
            # Avoid matching substring like "at" in "cat" - actually just basic check for now
            # But python "in" matches substrings. We should split? 
            # Splitting is safer.
            words = set(re.findall(r'\w+', text))
            if kw in words or kw in text: # keep 'in text' for multi-word keywords
                if kw == 'game': continue # Handle separately
                if kw == 'win': continue
                if kw == 'loss': continue
                st_score += 1
            
    for kw in sports_keywords:
        if kw in text:
            if kw == 'game': continue
            sp_score += 1
            
    for kw in business_keywords:
        if kw in text:
            bu_score += 1
            
    for kw in world_keywords:
        if kw in text:
            wo_score += 1
            
    # Adjustments for 'game'
    if 'game' in text or 'games' in text:
        # Check context
        tech_context = any(x in text for x in ['video', 'console', 'software', 'computer', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'electronic', 'device', 'gadget', 'online', 'mobile', 'boy', 'prize', 'award', 'festival']) 
        # 'prize', 'award' might be science too. 'GameBoy' -> 'boy'
        
        sport_context = any(x in text for x in ['football', 'baseball', 'basketball', 'hockey', 'soccer', 'team', 'player', 'coach', 'match', 'league', 'cup', 'olympic', 'medal', 'stadium', 'score', 'win', 'loss', 'season', 'playoff', 'final', 'red sox', 'yankees'])
        
        if tech_context and not sport_context:
            st_score += 3
        elif sport_context:
            sp_score += 3
        else:
            # Ambiguous "game". 
            # "GameBoy mini-games win prize" -> tech_context ('boy', 'prize')
            pass

    scores = {'Science/Technology': st_score, 'Sports': sp_score, 'Business': bu_score, 'World': wo_score}
    
    # Tie breaking
    # If Science and Business tie (common in tech companies), prefer Sci/Tech if tech keywords are strong?
    # Actually, AG News usually puts "Microsoft releases new Windows" in Sci/Tech. "Microsoft profit up" in Business.
    # If 'profit', 'revenue', 'stock', 'shares' -> Business
    if bu_score > 0 and (st_score > 0 or sp_score > 0 or wo_score > 0):
        if any(x in text for x in ['profit', 'revenue', 'earnings', 'stock', 'share', 'market', 'price', 'invest', 'deal', 'billion', 'million']):
             # Strong business indicator
             bu_score += 2
    
    # If Sci/Tech and World tie (e.g. Space), prefer Sci/Tech for Space/NASA.
    if 'nasa' in text or 'space' in text or 'shuttle' in text:
        st_score += 2

    # If Sports and World tie (e.g. Olympics in Athens), prefer Sports.
    if 'olympic' in text or 'athens' in text and sp_score > 0:
        sp_score += 2

    best = max(scores, key=scores.get)
    
    # If all 0
    if scores[best] == 0:
        return 'World' # Default fallback
        
    return best

import re

results = []
st_titles = []
for art in articles:
    cat = classify(art['title'], art['description'])
    results.append(cat)
    if cat == 'Science/Technology':
        st_titles.append(art['title'])

count_st = results.count('Science/Technology')
total = len(results)

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "st_count": count_st,
    "st_fraction": count_st/total if total > 0 else 0,
    "st_titles_sample": st_titles,
    "all_cats": results
}))"""

env_args = {'var_function-call-7921738261678552472': [{'author_id': '218'}], 'var_function-call-15988986839234050151': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-3807883415123841385': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-12359104834319763328': [{'_id': '694495f9bcd2c7e4a7fdf919', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '694495f9bcd2c7e4a7fe00ca', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '694495f9bcd2c7e4a7fe0375', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '694495f9bcd2c7e4a7fe0404', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '694495f9bcd2c7e4a7fe05d4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-13061389522128022440': {'total': 5, 'st_count': 3, 'sample': [['GameBoy mini-games win prize', 'ST'], ['Bailey Tries WR', 'World'], ['Students Win \\$100,000 in National Team Science Competition', 'ST'], ['Energy from waves  teenager wins science award', 'ST'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-14645694745949228888': 'file_storage/function-call-14645694745949228888.json'}

exec(code, env_args)
