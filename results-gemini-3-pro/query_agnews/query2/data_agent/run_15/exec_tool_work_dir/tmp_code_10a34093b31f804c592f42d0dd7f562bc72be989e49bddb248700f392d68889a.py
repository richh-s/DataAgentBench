code = """import json

# Load data
filename = locals()['var_function-call-11611652781333538792']
with open(filename, 'r') as f:
    articles = json.load(f)

# Keywords (simplified list for debugging/running)
keywords = {
    "Science/Technology": [
        "science", "technology", "tech", "computer", "internet", "web", "software", "hardware", 
        "digital", "online", "net", "google", "microsoft", "apple", "intel", "ibm", "linux", "unix", 
        "virus", "worm", "security", "hacker", "cyber", "space", "nasa", "astronomer", "mars", "moon", 
        "robot", "gadget", "phone", "mobile", "wireless", "broadband", "satellite", "biology", "physics", 
        "chemistry", "genetic", "dna", "stem cell", "research", "lab", "laboratory", "discovery", "study", 
        "innovation", "patent", "engine", "machine", "power", "energy", "battery", "electric", "fuel", 
        "video game", "nintendo", "sony", "xbox", "playstation", "wii", "gameboy", "gamer", "gaming", 
        "console", "browser", "search engine", "email", "spam", "blog", "ipod", "itunes", "mp3", "dvd", 
        "blu-ray", "hd", "pixel", "camera", "chip", "semiconductor", "processor", "server", "network", 
        "data", "database", "program", "code", "developer", "app", "application", "windows", "mac", "os", 
        "firefox", "explorer", "safari", "chrome", "facebook", "twitter", "myspace", "youtube", "amazon", 
        "ebay", "yahoo", "aol", "isp", "voip", "wifi", "bluetooth", "gps", "nanotech", "biotech",
        "physicist", "scientist", "telescope", "shuttle", "mission", "launch", "orbit", "asteroid", "comet"
    ],
    "Sports": [
        "sport", "football", "soccer", "baseball", "basketball", "cricket", "tennis", "golf", "rugby", 
        "hockey", "olympic", "athlete", "player", "coach", "team", "match", "game", "cup", "league", 
        "tournament", "championship", "win", "lose", "score", "goal", "touchdown", "run", "wicket", 
        "medal", "stadium", "club", "manager", "fifa", "nfl", "nba", "mlb", "nhl", "race", "driver", 
        "f1", "nascar", "boxing", "boxer", "round", "wrestling", "swimming", "cycling", "marathon", "sprint"
    ],
    "Business": [
        "business", "company", "corp", "inc", "market", "stock", "share", "trade", "economy", "economic", 
        "finance", "financial", "bank", "invest", "profit", "loss", "revenue", "sale", "deal", "merger", 
        "acquisition", "ceo", "cfo", "manager", "industry", "factory", "production", "price", "oil", 
        "gold", "dollar", "euro", "yen", "currency", "inflation", "tax", "budget", "fed", "rate", 
        "wall street", "nasdaq", "dow", "index", "recession", "growth", "forecast", "analyst", "earnings", 
        "quarter", "dividend", "bond", "debt", "loan", "mortgage", "credit", "retail", "store", "sales", 
        "consumer", "spending", "jobs", "unemployment", "hiring", "salary", "wage", "strike", "union", 
        "bankruptcy", "audit", "fraud"
    ],
    "World": [
        "world", "international", "government", "president", "minister", "prime minister", "senator", 
        "congress", "parliament", "election", "vote", "poll", "politics", "political", "war", "peace", 
        "military", "army", "navy", "air force", "soldier", "troop", "police", "attack", "bomb", "blast", 
        "kill", "dead", "death", "wound", "injure", "casualty", "victim", "disaster", "earthquake", "flood", 
        "storm", "hurricane", "typhoon", "tsunami", "fire", "crash", "accident", "terror", "terrorist", 
        "terrorism", "qaeda", "taliban", "isis", "hamas", "rebel", "insurgent", "protest", "riot", "hostage", 
        "kidnap", "nuclear", "weapon", "arms", "treaty", "agreement", "sanction", "diplomat", "ambassador", 
        "embassy", "un", "nato", "eu", "refugee", "immigrant", "border", "security", "court", "judge", "trial", 
        "prison", "jail", "rights", "human rights", "freedom", "democracy", "dictator", "regime", "coup", 
        "iraq", "iran", "afghanistan", "palestine", "israel", "china", "russia", "korea", "baghdad", "kabul"
    ]
}

def classify(title, description):
    text = (str(title) + " " + str(description)).lower()
    scores = {c: 0 for c in keywords}
    
    for cat, words in keywords.items():
        for w in words:
            if w in text:
                scores[cat] += 1
                
    # Heuristic adjustments
    if "game" in text:
        # Context check
        if any(x in text for x in ["video", "console", "xbox", "sony", "nintendo", "boy", "software"]):
            scores["Science/Technology"] += 2
        elif any(x in text for x in ["coach", "team", "league", "cup", "stadium"]):
            scores["Sports"] += 2
        else:
             # Ambiguous "game"
             pass
             
    if "nasa" in text:
         scores["Science/Technology"] += 2

    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "Unknown"
    return best

tech_count = 0
total = 0
for a in articles:
    cat = classify(a['title'], a['description'])
    if cat == "Science/Technology":
        tech_count += 1
    total += 1
    
fraction = tech_count / total if total else 0

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "tech": tech_count,
    "fraction": fraction
}))"""

env_args = {'var_function-call-8926378661725277850': [{'author_id': '218'}], 'var_function-call-3818012289303590375': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1204740519098011335': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-2622913981393963558': [{'_id': '69449b098747628b1c393460', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449b0a8747628b1c393c11', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449b0a8747628b1c393ebc', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449b0a8747628b1c393f4b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449b0a8747628b1c39411b', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-4483397608760778638': {'total_articles': 5, 'tech_articles': 0, 'fraction': 0.0, 'details': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'category': 'Unknown'}, {'id': '2161', 'title': 'Bailey Tries WR', 'category': 'Unknown'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Unknown'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'category': 'Unknown'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'category': 'Unknown'}]}, 'var_function-call-4924300181866773930': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966, '192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_function-call-9848690821629723026': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_function-call-11947402460081273967': [], 'var_function-call-5455535494256034943': [{'_id': '69449b0a8747628b1c394322', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-14391902516029988447': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-11611652781333538792': 'file_storage/function-call-11611652781333538792.json', 'var_function-call-3422265911834970105': 'file_storage/function-call-3422265911834970105.json', 'var_function-call-15084909493789153720': {'total': 111, 'tech': 3, 'fraction': 0.02702702702702703, 'samples': [{'title': 'GameBoy mini-games win prize', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Bailey Tries WR', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Energy from waves  teenager wins science award', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'China #39;s appetite boosts BHP', 'cat': 'Business', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 1, 'World': 0}}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Even in win, nasty vibes', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}, {'title': 'Somalians sworn in', 'cat': 'Unknown', 'scores': {'Science/Technology': 0, 'Sports': 0, 'Business': 0, 'World': 0}}]}}

exec(code, env_args)
