code = """import json

# Load articles
with open(locals()['var_function-call-13750603828789518820'], 'r') as f:
    articles = json.load(f)

# Define keywords
tech_keywords = {
    "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", 
    "online", "digital", "phone", "mobile", "wireless", "gadget", "device", "robot", 
    "space", "nasa", "astronomy", "biology", "physics", "chemistry", "research", "study", 
    "laboratory", "lab", "scientist", "researcher", "microsoft", "apple", "google", 
    "intel", "ibm", "gameboy", "nintendo", "sony", "console", "video game", "hacker", 
    "virus", "security", "broadband", "satellite", "engine", "motor", "battery", 
    "energy", "solar", "nuclear", "stem cell", "genetics", "medical", "disease", "health",
    "browser", "server", "linux", "windows", "mac", "ipod", "mp3", "dvd", "chip", 
    "semiconductor", "telecom", "nanotech", "biotech", "innovation", "innovative",
    "math", "mathematics", "telescope", "mars", "moon", "rocket", "astronaut",
    "discovery", "experiment", "patent", "silicon", "valley", "net", "dot-com",
    "cyber", "spam", "phishing", "blog", "download", "upload", "file", "data",
    "network", "program", "code", "developer", "app", "application", "user",
    "interface", "screen", "display", "pixel", "resolution", "camera", "lens",
    "sensor", "gps", "navigation", "map", "search", "yahoo", "amazon",
    "facebook", "myspace", "twitter", "youtube", "skype", "voip", "wifi", "bluetooth",
    "firefox", "explorer", "shuttle", "station", "crew", "orbit", "launch"
}

sports_keywords = {
    "sport", "game", "match", "tournament", "cup", "league", "team", "player", "coach", 
    "win", "lose", "score", "victory", "defeat", "football", "soccer", "basketball", 
    "baseball", "tennis", "golf", "cricket", "rugby", "hockey", "racing", "f1", 
    "olympic", "athlete", "championship", "stadium", "club", "nfl", "nba", "mlb", 
    "nhl", "fifa", "uefa", "quarterback", "touchdown", "goal", "striker", "defender",
    "goalkeeper", "pitcher", "batter", "inning", "lap", "medal", "gold", "silver", "bronze",
    "world cup", "super bowl", "world series", "playoff", "final", "semi-final",
    "referee", "umpire", "foul", "penalty", "red card", "yellow card", "offside",
    "doping", "steroid", "marathon", "sprint", "relay", "swim", "gymnast", "boxer",
    "wrestl", "fighter", "bout", "round", "knockout", "ko", "points", "ranking",
    "standings", "season", "draft", "transfer", "contract", "signing", "roster",
    "sox", "yankees", "reds", "mets", "dodgers", "giants", "eagles", "patriots",
    "steelers", "packers", "cowboys", "49ers", "lakers", "bulls", "celtics", "pistons",
    "spurs", "heat", "suns", "mavs", "rockets", "magic", "knicks", "rangers", "devils",
    "flyers", "bruins", "leafs", "habs", "canadiens", "wings", "avalanche", "stars"
}

business_keywords = {
    "business", "economy", "market", "stock", "share", "trade", "finance", "bank", 
    "money", "dollar", "euro", "yen", "currency", "inflation", "rate", "tax", 
    "profit", "revenue", "loss", "company", "corporation", "firm", "industry", 
    "sector", "ceo", "cfo", "manager", "executive", "deal", "merger", "acquisition", 
    "buyout", "price", "cost", "sales", "oil", "gold", "invest", "wall street",
    "dow jones", "nasdaq", "s&p", "dividend", "yield", "bond", "asset", "liability",
    "equity", "capital", "venture", "startup", "ipo", "shareholder", "stake",
    "monopoly", "antitrust", "regulation", "budget", "deficit", "surplus", "gdp",
    "growth", "recession", "depression", "unemployment", "job", "wage", "salary",
    "labor", "union", "strike", "export", "import", "tariff", "outsourcing",
    "retail", "consumer", "spending", "confidence", "fed", "central bank",
    "interest rate", "loan", "mortgage", "credit", "debt", "bankruptcy", "default",
    "bhp", "billiton", "mining", "commodity", "crude", "barrel", "opec", "airlines",
    "automaker", "gm", "ford", "toyota", "honda", "nissan", "chrysler", "daimler"
}

world_keywords = {
    "world", "international", "country", "nation", "government", "politics", "president", 
    "minister", "prime minister", "parliament", "senate", "congress", "law", "policy", 
    "war", "military", "army", "police", "attack", "bomb", "terror", "conflict", 
    "peace", "treaty", "summit", "un", "united nations", "eu", "european union", 
    "foreign", "diplomat", "crisis", "disaster", "earthquake", "flood", "hurricane", 
    "tsunami", "election", "vote", "voter", "campaign", "candidate", "party", 
    "democrat", "republican", "conservative", "liberal", "socialist", "communist",
    "dictator", "regime", "human rights", "refugee", "immigration", "border",
    "security", "intelligence", "cia", "fbi", "nsa", "nato", "troops", "soldier",
    "casualty", "kill", "death", "injured", "wounded", "survivor", "rescue",
    "aid", "relief", "sanction", "embargo", "nuclear", "weapon", "arms", "missile",
    "protest", "demonstration", "riot", "coup", "rebellion", "insurgent",
    "guerrilla", "militia", "hostage", "kidnap", "assassin", "murder", "crime",
    "trial", "court", "judge", "jury", "verdict", "prison", "jail", "sentence",
    "execution", "death penalty", "iraq", "iran", "afghanistan", "korea", "china",
    "russia", "usa", "uk", "france", "germany", "japan", "israel", "palestine",
    "syria", "lebanon", "egypt", "sudan", "darfur", "africa", "asia", "europe",
    "latin america", "middle east", "baghdad", "kabul", "tehran", "pyongyang",
    "beijing", "moscow", "washington", "london", "paris", "berlin", "tokyo",
    "jerusalem", "gaza", "damascus", "beirut", "cairo", "khartoum"
}

tech_count = 0
total = len(articles)
tech_list = []
results = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    # Simple scoring
    s_tech = sum(1 for k in tech_keywords if k in text)
    s_sports = sum(1 for k in sports_keywords if k in text)
    s_business = sum(1 for k in business_keywords if k in text)
    s_world = sum(1 for k in world_keywords if k in text)
    
    # Adjustments
    if "game" in text:
        if any(k in text for k in ["video", "console", "nintendo", "sony", "xbox", "computer", "software", "tech", "gadget", "boy"]):
            s_tech += 3
        if any(k in text for k in ["football", "basketball", "baseball", "soccer", "team", "coach", "league", "cup", "score", "sport"]):
            s_sports += 2

    if "win" in text and "prize" in text and "game" in text and "mini" in text:
        s_tech += 5 # Special case for GameBoy
        
    scores = {'Science/Technology': s_tech, 'Sports': s_sports, 'Business': s_business, 'World': s_world}
    
    # Find max score
    best_cat = max(scores, key=scores.get)
    max_score = scores[best_cat]
    
    # Handling ties or zero scores
    if max_score == 0:
        best_cat = "Unclassified"
    elif list(scores.values()).count(max_score) > 1:
        # Tie-breaking logic
        if scores['Science/Technology'] == max_score:
            if "science" in text or "technology" in text:
                best_cat = 'Science/Technology'
        # Default priority?
        pass

    if best_cat == 'Science/Technology':
        tech_count += 1
        tech_list.append(art['title'])
        
    results.append({"title": art['title'], "category": best_cat, "scores": scores})

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "tech_count": tech_count,
    "tech_list": tech_list,
    # "sample_results": results[:10]
}))"""

env_args = {'var_function-call-1939965024232050517': [{'author_id': '218'}], 'var_function-call-15785083742190214670': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1096118954770325202': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-13750603828789518820': [{'_id': '6944ab0566db455b35c33c29', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ab0566db455b35c343da', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ab0566db455b35c34685', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ab0566db455b35c34714', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ab0566db455b35c348e4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
