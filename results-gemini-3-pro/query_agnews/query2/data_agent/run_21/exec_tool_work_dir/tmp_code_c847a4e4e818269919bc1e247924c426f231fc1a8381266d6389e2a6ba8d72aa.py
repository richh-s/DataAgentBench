code = """import json
import re

file_path = locals()['var_function-call-16036194506055267338']

with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords Lists (Updated)

v_strong_tech = {
    "science", "space", "nasa", "orbit", "mars", "moon", "galaxy", "astronomy", "physics", 
    "biology", "chemistry", "genetics", "dna", "stem cell", "clone", "robot", "artificial intelligence", 
    "ai", "laboratory", "lab", "cancer", "aids", "hiv", "virus", "discovery", "study", "research"
}

strong_tech = {
    "technology", "computer", "software", "internet", "web", "online", "digital", "mobile", 
    "wireless", "satellite", "gadget", "chip", "processor", "intel", "amd", "microsoft", "google", 
    "apple", "ibm", "linux", "windows", "browser", "hacker", "broadband", "wifi", "bluetooth", 
    "console", "nintendo", "sony", "xbox", "playstation", "wii", "ipod", "mp3", "dvd", "laptop", 
    "server", "telecom", "nanotech", "innovation", "patent", "solar", "battery", "hybrid", 
    "vaccine", "medical", "health", "clinical", "fda", "shuttle", "video game", "gameboy"
}

weak_tech = {
    "tech", "phone", "network", "device", "monitor", "screen", "data", "database", "scientist", 
    "engine", "motor", "fuel", "energy", "electric", "vehicle", "drug", "disease", "doctor", 
    "hospital", "treatment", "spam", "spyware", "gaming"
}

v_strong_business = {
    "stock", "dow", "nasdaq", "wall street", "profit", "revenue", "earnings", "merger", "acquisition", 
    "buyout", "inflation", "fed", "greenspan", "dividend", "shareholder"
}

strong_business = {
    "business", "economy", "market", "invest", "finance", "ceo", "cfo", "retail", "oil", "crude", 
    "barrel", "corp", "inc", "ltd", "currency", "deficit", "tax", "unemployment", "bankruptcy", 
    "audit", "sec", "accounting"
}

weak_business = {
    "share", "bank", "trade", "deal", "sales", "price", "cost", "rate", "gas", "company", "firm", 
    "dollar", "euro", "yen", "budget", "jobs", "hiring", "strike", "union"
}

strong_sports = {
    "football", "baseball", "basketball", "soccer", "tennis", "golf", "hockey", "league", "nfl", 
    "nba", "mlb", "nhl", "fifa", "cup", "championship", "tournament", "olympic", "athlete", 
    "stadium", "medal", "gold", "silver", "bronze", "record", "f1", "cricket", "rugby", "boxing", 
    "wrestling", "swimming", "cycling", "marathon", "world cup"
}

weak_sports = {
    "sport", "game", "match", "score", "win", "loss", "defeat", "victory", "team", "player", "coach", 
    "season", "captain", "race", "driver", "prix", "club"
}

strong_world = {
    "politics", "president", "presidential", "minister", "parliament", "congress", "senate", "law", "court", "judge", 
    "police", "crime", "murder", "bomb", "attack", "war", "peace", "treaty", "military", "army", "navy", 
    "troop", "soldier", "iraq", "iran", "afghanistan", "palestine", "israel", "china", "russia", "eu", 
    "un", "nation", "country", "disaster", "hurricane", "earthquake", "tsunami", "flood", "terror", 
    "hostage", "kidnap", "protest", "riot", "kabul", "baghdad", "gaza", "bush", "kerry", "candidate", "campaign"
}

weak_world = {
    "world", "international", "official", "government", "election", "vote", "poll", "party", "democrat", 
    "republican", "kill", "state", "city", "region", "fire", "crash", "explosion", "crisis"
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    
    scores = {"sci_tech": 0, "business": 0, "sports": 0, "world": 0}
    
    for word in words:
        stem = word
        if word.endswith('s') and len(word) > 3:
            stem = word[:-1]
            
        if word in v_strong_tech or stem in v_strong_tech: scores["sci_tech"] += 5
        elif word in strong_tech or stem in strong_tech: scores["sci_tech"] += 3
        elif word in weak_tech or stem in weak_tech: scores["sci_tech"] += 1
        
        if word in v_strong_business or stem in v_strong_business: scores["business"] += 5
        elif word in strong_business or stem in strong_business: scores["business"] += 3
        elif word in weak_business or stem in weak_business: scores["business"] += 1
        
        if word in strong_sports or stem in strong_sports: scores["sports"] += 4
        elif word in weak_sports or stem in weak_sports: scores["sports"] += 1
        
        if word in strong_world or stem in strong_world: scores["world"] += 3
        elif word in weak_world or stem in weak_world: scores["world"] += 1

    # Heuristics
    if "video game" in text: scores["sci_tech"] += 5
    if "gameboy" in text: scores["sci_tech"] += 5
    if "oil" in text and ("price" in text or "barrel" in text):
        scores["business"] += 3
        scores["sci_tech"] -= 2
    if "iraq" in text: scores["world"] += 2
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0: return "unknown"
    return best_cat

sci_tech_count = 0
total = 0
sci_tech_articles = []

for art in articles:
    total += 1
    cat = classify(art.get('title', ''), art.get('description', ''))
    if cat == "sci_tech":
        sci_tech_count += 1
        sci_tech_articles.append(art.get('title', ''))

print("__RESULT__:")
print(json.dumps({"total": total, "sci_tech_count": sci_tech_count, "fraction": sci_tech_count/total if total > 0 else 0, "examples": sci_tech_articles}))"""

env_args = {'var_function-call-8913720872656963662': [{'author_id': '218'}], 'var_function-call-11893012323498731901': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-14955974731588177278': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-6100868222952334146': [{'_id': '6944a134e13b7ef48d50ea20', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a134e13b7ef48d50f1d1', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a134e13b7ef48d50f47c', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a134e13b7ef48d50f50b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a134e13b7ef48d50f6db', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-723980121988753707': {'total': 5, 'sci_tech_count': 2, 'fraction': 0.4, 'examples': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award']}, 'var_function-call-16303600765718085335': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-16036194506055267338': 'file_storage/function-call-16036194506055267338.json', 'var_function-call-14908525211183673538': {'total': 111, 'sci_tech_count': 21, 'fraction': 0.1891891891891892, 'examples': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker']}, 'var_function-call-1412172594589923084': 111, 'var_function-call-8970742504592012222': {'total': 111, 'sci_tech_count': 22, 'fraction': 0.1981981981981982, 'examples': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Even in win, nasty vibes', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'Not all sweet for Lou', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Swedes fire into top two spots']}, 'var_function-call-9187406630116217182': {'total': 111, 'sci_tech_count': 21, 'fraction': 0.1891891891891892, 'examples': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'FCC Approves Merger, Wireless Giant Created', 'Satellite write-downs widen DirecTV #39;s loss', 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'Revealed: why the fear factor runs with the pack', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', "EBay Adds 'Want It Now' Feature (Reuters)", 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}, 'var_function-call-3145445534784094112': {'total': 111, 'sci_tech_count': 20, 'fraction': 0.18018018018018017, 'examples': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'FCC Approves Merger, Wireless Giant Created', 'Satellite write-downs widen DirecTV #39;s loss', 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'Revealed: why the fear factor runs with the pack', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', "EBay Adds 'Want It Now' Feature (Reuters)", 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}, 'var_function-call-15340943995583323575': [{'title': 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'description': 'Some Web logs were swift to provide dark theories about the presidential election, but others were just as quick to debunk them.'}, {'title': 'Revealed: why the fear factor runs with the pack', 'description': 'THE rapid spread of fear that can cause crush injuries and serious accidents in crowds could be provoked by an innate reaction to body language, a provocative new study has found.'}]}

exec(code, env_args)
