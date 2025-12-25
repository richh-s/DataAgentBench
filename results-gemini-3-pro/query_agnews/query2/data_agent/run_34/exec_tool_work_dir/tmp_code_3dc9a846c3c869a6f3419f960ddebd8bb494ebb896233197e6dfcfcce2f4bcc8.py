code = """import json

file_path = locals()['var_function-call-13421910094674221144']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Weighted Categories
strong_weight = 5
weak_weight = 1

# Define dictionaries
categories = {
    "Science/Technology": {
        "strong": [
            "science", "technology", "computer", "internet", "space", "nasa", "software", "hardware", 
            "robot", "physics", "biology", "chemistry", "medicine", "genome", "lab", "research", 
            "telescope", "shuttle", "mars", "moon", "video game", "nintendo", "xbox", "playstation", 
            "gameboy", "sony", "microsoft", "google", "apple", "intel", "linux", "biotech", "nanotech",
            "virus", "cancer", "gene", "cell", "stem cell", "astronomy", "mission", "launch", "orbit",
            "semiconductor", "processor", "browser", "firefox", "explorer", "oracle", "sun microsystems", "tech"
        ],
        "weak": [
            "web", "online", "app", "device", "mobile", "phone", "wireless", "network", "battery", 
            "energy", "electric", "innovat", "discover", "study", "gadget", "smartphone", "tablet", 
            "laptop", "chip", "server", "cloud", "telecom", "broadband", "satellite", "nuclear", 
            "solar", "wind", "vehicle", "spam", "hacker", "security", "blog", "ipod", "itunes"
        ]
    },
    "Sports": {
        "strong": [
            "football", "baseball", "basketball", "hockey", "soccer", "tennis", "golf", "cricket", 
            "rugby", "racing", "f1", "nascar", "olympic", "nfl", "nba", "mlb", "nhl", "fifa", 
            "wimbledon", "athlete", "stadium", "championship", "tournament", "red sox", "yankees", 
            "broncos", "lakers", "bulls", "knicks", "rangers", "flyers", "penguins", "bruins", 
            "open", "masters", "bowl", "medal", "gold", "silver", "bronze"
        ],
        "weak": [
            "sport", "game", "match", "team", "win", "lose", "score", "victory", "defeat", 
            "club", "coach", "league", "cup", "squad", "season", "final", "semi-final", "quarter-final"
        ]
    },
    "Business": {
        "strong": [
            "stock", "market", "finance", "invest", "trade", "revenue", "profit", "earnings", 
            "merger", "acquisition", "nasdaq", "dow jones", "wall street", "bank", "economy", 
            "inflation", "dividend", "shareholder", "ipo", "imf", "fed", "federal reserve"
        ],
        "weak": [
            "business", "share", "sale", "deal", "price", "cost", "dollar", "euro", "debt", 
            "manager", "ceo", "cfo", "corp", "inc", "retail", "spend", "jobless", "unemployment", 
            "hiring", "company", "industry", "sector", "quarter", "budget", "oil", "gas"
        ]
    },
    "World": {
        "strong": [
            "president", "minister", "parliament", "senate", "congress", "war", "military", "army", 
            "navy", "terror", "bomb", "blast", "iraq", "iran", "israel", "palestine", "syria", 
            "afghanistan", "un", "united nations", "treaty", "election", "hurricane", "tsunami", 
            "quake", "baghdad", "fallujah", "kabul", "darfur", "sudan", "gaza", "prime minister"
        ],
        "weak": [
            "world", "government", "politics", "police", "court", "judge", "trial", "prison", 
            "peace", "foreign", "country", "state", "usa", "china", "russia", "france", "uk", 
            "germany", "law", "official", "authorities", "curfew", "protest", "strike", "crash", 
            "disaster", "storm", "flood", "international", "nation"
        ]
    }
}

def classify_article(title, description):
    text = (str(title) + " " + str(description)).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, key_dict in categories.items():
        # Strong
        for kw in key_dict['strong']:
            if kw in text:
                scores[cat] += strong_weight
        # Weak
        for kw in key_dict['weak']:
            if kw in text:
                scores[cat] += weak_weight
                
    max_score = -1
    best_cat = "None"
    
    # Priority if tie: Business > World > Sports > Sci/Tech
    # This priority handles overlap (e.g. Business news about Tech).
    priority_order = ["Business", "World", "Sports", "Science/Technology"]
    
    # Find max
    for s in scores.values():
        if s > max_score:
            max_score = s
            
    if max_score == 0:
        return "None"
        
    candidates = [cat for cat, s in scores.items() if s == max_score]
    
    # Pick based on priority
    best_cat = candidates[0]
    for p in priority_order:
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
    "debug_sample": debug_list[:25]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17457919470351386269': [{'author_id': '218'}], 'var_function-call-5457860116644151220': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-4679791817000002691': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-8014510795813072183': [{'_id': '6944ae280e57057b57043f21', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ae280e57057b570446d2', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ae280e57057b5704497d', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ae280e57057b57044a0c', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ae280e57057b57044bdc', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12075235238852955756': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'limit': 121}, 'var_function-call-4966563746488053328': [], 'var_function-call-5017441786467379529': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 121}, 'var_function-call-13421910094674221144': 'file_storage/function-call-13421910094674221144.json', 'var_function-call-17868392873864378783': {'total': 111, 'sci_tech_count': 23, 'fraction': 0.2072072072072072, 'debug_sample': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'cat': 'Sports'}, {'id': '2161', 'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Science/Technology'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}, {'id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'Business'}, {'id': '4447', 'title': 'Even in win, nasty vibes', 'cat': 'Sports'}, {'id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'World'}, {'id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'id': '6869', 'title': 'Somalians sworn in', 'cat': 'World'}]}, 'var_function-call-14579178163937966336': {'total': 111, 'sci_tech_count': 15, 'fraction': 0.13513513513513514, 'debug_sample': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'cat': 'Science/Technology'}, {'id': '2161', 'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'World'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'cat': 'World'}, {'id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'Business'}, {'id': '4447', 'title': 'Even in win, nasty vibes', 'cat': 'World'}, {'id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'World'}, {'id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'id': '6869', 'title': 'Somalians sworn in', 'cat': 'World'}, {'id': '8962', 'title': 'Muenzer races for gold', 'cat': 'Sports'}, {'id': '9677', 'title': 'Israelis to Expand West Bank Settlements', 'cat': 'World'}, {'id': '9858', 'title': 'Stocks End Up as Oil Prices Fall', 'cat': 'Business'}, {'id': '14861', 'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'cat': 'World'}, {'id': '15100', 'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'cat': 'World'}, {'id': '15473', 'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'cat': 'Science/Technology'}, {'id': '17491', 'title': 'UPDATE: Intel lowers Q3 revenue estimates', 'cat': 'Business'}, {'id': '19469', 'title': 'Calm as Kathmandu curfew lifted', 'cat': 'Business'}, {'id': '20362', 'title': 'Israeli Missiles Kill 13 Militants', 'cat': 'World'}, {'id': '21238', 'title': 'Serena Blasts Umpire After Dramatic Defeat', 'cat': 'Sports'}]}}

exec(code, env_args)
