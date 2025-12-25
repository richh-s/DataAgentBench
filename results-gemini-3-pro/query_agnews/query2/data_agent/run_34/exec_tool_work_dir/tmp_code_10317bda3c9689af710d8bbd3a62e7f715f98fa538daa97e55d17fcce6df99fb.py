code = """import json

file_path = locals()['var_function-call-13421910094674221144']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Stems/Keywords
categories = {
    "Science/Technology": [
        "scien", "technolog", "computer", "internet", "softwar", "hardwar", "web", "online", 
        "cyber", "digital", "robot", "space", "nasa", "astro", "mars", "planet", "galaxy", 
        "universe", "physic", "biolog", "chemist", "medic", "health", "disease", "virus", 
        "cancer", "gene", "genome", "cell", "research", "lab", "discover", "invent", "innovat", 
        "gadget", "device", "mobile", "phone", "smartphone", "wireless", "network", "telecom", 
        "broadband", "server", "app", "browser", "video game", "gaming", "console", "nintendo", 
        "sony", "xbox", "playstation", "microsoft", "google", "apple", "intel", "linux", "windows", 
        "satellite", "rocket", "shuttle", "telescope", "nanotech", "biotech", "nuclear", "solar", 
        "wind", "energy", "battery", "electric", "gameboy", "psp", "wii", "ipod", "itunes", 
        "firefox", "explorer", "semiconduct", "chip", "tech"
    ],
    "Sports": [
        "sport", "football", "baseball", "basketball", "hockey", "soccer", "tennis", "golf", 
        "cricket", "rugby", "racing", "nascar", "olympic", "match", "team", "player", "coach", 
        "league", "cup", "champion", "tournament", "win", "lose", "score", "victory", "defeat", 
        "medal", "athlete", "stadium", "club", "squad", "nfl", "nba", "mlb", "nhl", "fifa", 
        "red sox", "yankees", "broncos", "lakers", "f1"
    ],
    "Business": [
        "business", "econom", "market", "stock", "share", "financ", "bank", "invest", "trade", 
        "trading", "industr", "revenue", "profit", "earn", "sale", "deal", "merger", "acqui", 
        "ceo", "manager", "executive", "price", "cost", "debt", "dollar", "euro", "wall street", 
        "dow jones", "nasdaq", "inflation", "jobless", "unemploy", "retail", "spend", "corp", "inc"
    ],
    "World": [
        "world", "govern", "politic", "president", "minister", "senate", "congress", "parliament", 
        "elect", "vote", "war", "militar", "army", "navy", "attack", "bomb", "blast", "terror", 
        "police", "crime", "court", "judge", "trial", "prison", "treaty", "peace", "foreign", 
        "internation", "country", "nation", "state", "iraq", "iran", "china", "russia", "usa", 
        "uk", "france", "germany", "israel", "palestine", "syria", "disaster", "quake", "flood", 
        "hurricane", "storm", "un", "united nations"
    ]
}

def classify_article(title, description):
    text = (str(title) + " " + str(description)).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                 scores[cat] += 1
                 
    # Tie breaking
    # If Sci/Tech and Business tie, and "tech" or "computer" or "microsoft" is present, Sci/Tech wins?
    # Actually, let's look at scores.
    
    max_score = -1
    best_cat = "None"
    
    # Priority if tie: World > Sports > Business > Sci/Tech? 
    # Or Sci/Tech > Business?
    # In AG News, Sci/Tech is often distinct.
    # Let's use the order of keys in dict to break ties? No, random.
    # Let's enforce specific priority.
    # If Sports score == max, choose Sports.
    # If World score == max, choose World.
    # If Business score == max, choose Business.
    # If Sci/Tech score == max, choose Sci/Tech.
    # This means if Tech ties with Business, Business wins?
    # "Intel lowers revenue" -> Tech(1) Biz(1). Business is correct.
    # "Microsoft settles lawsuit" -> Tech(1) World(0) Biz(0). Tech.
    
    priorities = ["Sports", "World", "Business", "Science/Technology"]
    
    # Calculate max score
    for s in scores.values():
        if s > max_score:
            max_score = s
            
    if max_score == 0:
        return "None" # Or default?
        
    candidates = [cat for cat, s in scores.items() if s == max_score]
    
    # Pick based on priority
    best_cat = candidates[0]
    for p in priorities:
        if p in candidates:
            best_cat = p
            break
            
    return best_cat

sci_tech_count = 0
total_articles = len(articles)
debug_list = []

for article in articles:
    cat = classify_article(article.get('title', ''), article.get('description', ''))
    if cat == "Science/Technology":
        sci_tech_count += 1
    debug_list.append({"id": article.get('article_id'), "title": article.get('title'), "cat": cat})

fraction = sci_tech_count / total_articles if total_articles > 0 else 0

result = {
    "total": total_articles,
    "sci_tech_count": sci_tech_count,
    "fraction": fraction,
    "debug_sample": debug_list[:20]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17457919470351386269': [{'author_id': '218'}], 'var_function-call-5457860116644151220': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-4679791817000002691': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-8014510795813072183': [{'_id': '6944ae280e57057b57043f21', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ae280e57057b570446d2', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ae280e57057b5704497d', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ae280e57057b57044a0c', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ae280e57057b57044bdc', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12075235238852955756': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'limit': 121}, 'var_function-call-4966563746488053328': [], 'var_function-call-5017441786467379529': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 121}, 'var_function-call-13421910094674221144': 'file_storage/function-call-13421910094674221144.json', 'var_function-call-17868392873864378783': {'total': 111, 'sci_tech_count': 23, 'fraction': 0.2072072072072072, 'debug_sample': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'cat': 'Sports'}, {'id': '2161', 'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Science/Technology'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}, {'id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'Business'}, {'id': '4447', 'title': 'Even in win, nasty vibes', 'cat': 'Sports'}, {'id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'World'}, {'id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'id': '6869', 'title': 'Somalians sworn in', 'cat': 'World'}]}}

exec(code, env_args)
