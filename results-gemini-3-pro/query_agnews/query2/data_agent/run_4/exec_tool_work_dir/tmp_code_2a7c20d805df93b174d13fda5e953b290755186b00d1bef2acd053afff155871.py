code = """import json

# Load articles
file_path = locals()['var_function-call-8909086500841670634']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
tech_keywords = [
    "technology", "science", "computer", "software", "hardware", "internet", "web", "online", 
    "digital", "mobile", "wireless", "phone", "game", "gaming", "video game", "console", 
    "nintendo", "sony", "microsoft", "apple", "google", "intel", "ibm", "linux", "windows", 
    "processor", "chip", "robot", "space", "nasa", "astronomy", "physics", "biology", "genetics", 
    "dna", "stem cell", "medical", "disease", "virus", "hacker", "security", "network", "satellite", 
    "telecom", "browser", "server", "data", "electronic", "gadget", "research", "scientist", "study", 
    "discovery", "invention", "machine", "energy", "fuel", "climate", "environment", "app", "code", 
    "programming", "memory", "disk", "drive", "camera", "mp3", "dvd", "hd", "tv", "email", "spam", 
    "malware", "update", "version", "beta", "download", "bandwidth", "virtual", "simulation", 
    "weather", "solar", "nuclear", "laser", "telescope", "nano", "battery", "engine", "gameboy", 
    "bionics", "biotech", "nanotech", "robotics", "database", "laptop", "smartphone", "gps", 
    "broadband", "ipod", "itunes", "firefox", "explorer", "netscape", "java", "oracle", "sap"
]

business_keywords = [
    "business", "economy", "market", "stock", "trade", "investor", "profit", "loss", "revenue", 
    "earnings", "quarter", "bank", "finance", "corporate", "company", "firm", "deal", "merger", 
    "acquisition", "price", "cost", "dollar", "euro", "oil", "gas", "sales", "ceo", "cfo", "executive", 
    "shareholder", "bond", "index", "dow", "nasdaq", "fed", "inflation", "growth", "job", "labor", 
    "wage", "pension", "lawsuit", "settlement", "regulation", "antitrust", "competitor", "industry", 
    "retail", "consumer"
]

sports_keywords = [
    "sport", "team", "player", "coach", "league", "cup", "championship", "olympic", "medal", "gold", 
    "winner", "victory", "defeat", "score", "goal", "touchdown", "basket", "home run", "ball", 
    "stadium", "race", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", 
    "boxing", "swimming", "cycling", "season", "contract", "ranking", "title", "fan"
]

world_keywords = [
    "world", "politics", "government", "president", "minister", "parliament", "official", "diplomat", 
    "treaty", "election", "vote", "party", "war", "battle", "attack", "bomb", "explosion", "killing", 
    "terrorism", "military", "police", "arrest", "court", "trial", "judge", "human rights", "refugee", 
    "disaster", "hurricane", "earthquake", "flood", "peace", "un", "iraq", "iran", "afghanistan", 
    "china", "russia", "usa", "bush", "kerry", "blair", "sharon", "arafat", "putin"
]

scitech_count = 0
scitech_titles = []

for a in articles:
    text = (a.get('title', '') + " " + a.get('description', '')).lower()
    
    # Calculate scores
    s_tech = sum(1 for k in tech_keywords if k in text)
    s_biz = sum(1 for k in business_keywords if k in text)
    s_sport = sum(1 for k in sports_keywords if k in text)
    s_world = sum(1 for k in world_keywords if k in text)
    
    # Heuristic adjustments
    if "game" in text:
        if any(x in text for x in ["video", "console", "nintendo", "xbox", "ps2", "gameboy", "arcade"]):
            s_tech += 3
        if any(x in text for x in ["team", "coach", "season", "league", "score", "win", "loss"]):
            s_sport += 2

    if "win" in text and "science" in text:
        s_tech += 5
    
    if "nasa" in text or "space" in text:
        if "shuttle" in text or "station" in text or "probe" in text:
            s_tech += 3
    
    # Business overrides
    if s_tech > 0 and (s_biz > s_tech):
        # Check if it's tech business
        if "profit" in text or "stock" in text or "revenue" in text:
            # Likely business
            pass
        else:
            # Maybe tech
            pass
            
    # Determine category
    scores = {'Science/Technology': s_tech, 'Business': s_biz, 'Sports': s_sport, 'World': s_world}
    # Priority: if tech is highest or tied highest
    max_score = max(scores.values())
    
    # If all 0, default to something? or skip?
    if max_score == 0:
        cat = "Unknown"
    else:
        # Get all cats with max_score
        candidates = [k for k, v in scores.items() if v == max_score]
        if 'Science/Technology' in candidates:
            # Tie breaking
            if 'Business' in candidates:
                # If financial terms present, Business
                if "revenue" in text or "profit" in text or "stock" in text or "deal" in text:
                    cat = 'Business'
                else:
                    cat = 'Science/Technology'
            elif 'Sports' in candidates:
                if "game" in text and ("team" in text or "player" in text):
                    cat = 'Sports'
                else:
                    cat = 'Science/Technology'
            else:
                cat = 'Science/Technology'
        else:
            cat = candidates[0]
            
    # Manual fixes based on preview
    if "gameboy" in text:
        cat = 'Science/Technology'
    if "bailey tries wr" in text:
        cat = 'Sports'
    
    if cat == 'Science/Technology':
        scitech_count += 1
        scitech_titles.append(a['title'])

print("__RESULT__:")
print(json.dumps({"total": len(articles), "scitech_count": scitech_count, "scitech_titles": scitech_titles}))"""

env_args = {'var_function-call-14326919643838715254': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-11621825207488800491': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-5823093432151287573': [{'_id': '69448e8e657623369b3ab684', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69448e8e657623369b3abe35', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69448e8e657623369b3ac0e0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69448e8e657623369b3ac16f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69448e8e657623369b3ac33f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-8092838716419975412': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP'], 'var_function-call-11370130104739028379': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'limit': 200}, 'var_function-call-18387824864304179033': [], 'var_function-call-17042161371249083688': [{'_id': '69448e8e657623369b3ab5c4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-12935055921755806925': [], 'var_function-call-15247452211065426125': {'collection': 'articles', 'filter': {'article_id': {'$in': [57860, '24495', '57918', 14861, 19469, '57860', 110096, '104996', 107036, '120765', '22354', '26535', 109601, 104996, 104998, '27429', '80578', 35882, 108586, '20362', '6705', 6705, '38608', '70498', '103591', '35408', '57510', 57918, 89666, '103003', '92992', '62754', '5354', 35408, 17491, '111422', '96641', 103003, 124509, 82526, '14861', '52459', 40545, '73025', 64102, 93287, '3451', '119920', 93804, '123747', 119920, 2161, 15473, 29297, 54906, '23914', '93287', 9858, 36483, 112770, '108586', '9677', '104998', 101514, '119651', 69262, 41616, '35882', 91286, '48833', '101514', 57510, 103591, 91822, '192', 37042, '89666', '88553', 104123, 126655, 192, 48833, 80578, '37042', '107036', 39623, 39117, '69262', 38608, 33489, '100613', 6869, 96986, '116698', '126412', '19469', '2844', 5354, 52459, 82668, '2161', '40545', '66827', '99699', 21238, '93804', 15100, '68509', 8962, '68958', 100613, '78200', '124509', 66827, '88911', '46531', '112770', 103695, 69393, '28079', '6869', '33489', '70608', 122137, '94618', 2844, '109601', 62754, '8962', 27429, '103695', '69393', '15473', 111422, 92992, 73025, 120129, '47439', 83273, '36182', 105804, 72525, '62404', 47439, 88911, 22354, 36182, '96986', '49035', 68958, 4447, 70498, 119651, 123747, '104123', '113058', '122137', 25960, '110096', 23914, '17491', '54906', '41616', '112063', '73684', 99699, '64102', 78200, 3451, 96641, 3970, '9858', '25960', '83273', 20362, 49035, '21238', '29297', 94618, '126966', 106908, 68509, 113058, 26535, '80853', 2987, 24495, 28079, '48635', 81851, '2987', 120765, 112063, '4447', 46531, 62404, '36483', '39117', '72525', '126655', '120129', 126412, 9677, 70608, 73684, 80853, '29164', 116698, '15100', '82526', '39623', '106908', '105804', 88553, '3970', 29164, '81851', '82668', '91822', 126966, 48635, '91286']}}, 'limit': 200}, 'var_function-call-8909086500841670634': 'file_storage/function-call-8909086500841670634.json'}

exec(code, env_args)
