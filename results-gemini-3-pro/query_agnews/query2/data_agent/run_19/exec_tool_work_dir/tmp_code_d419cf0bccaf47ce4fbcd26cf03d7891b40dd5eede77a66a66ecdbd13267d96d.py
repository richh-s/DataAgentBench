code = """import json

# Get the file path
file_path = locals()['var_function-call-9350456290316558969']

# Read the file
with open(file_path, 'r') as f:
    articles = json.load(f)

def get_category(title, description):
    text = (str(title) + " " + str(description)).lower()
    
    # distinct keywords
    scitech_keywords = ["science", "technology", "tech", "computer", "software", "internet", "web", "online", 
                        "space", "nasa", "robot", "gadget", "phone", "mobile", "chip", "microsoft", "google", 
                        "apple", "linux", "windows", "video game", "console", "research", "study", "scientist", 
                        "physics", "biology", "chemistry", "medical", "health", "disease", "cancer", "virus", 
                        "engine", "battery", "solar", "energy", "browser", "server", "digital", "cyber", "intel", "ibm", 
                        "wireless", "network", "broadband", "satellite", "gps", "telescope", "astronomy", "mars", "moon", 
                        "genetic", "dna", "cell", "stem cell", "clone", "drug", "treatment", "vaccine", "aids", "hiv", 
                        "mp3", "ipod", "dvd", "hdtv", "camera", "lens", "pixel", "bluetooth", "wifi", "spam", "hacker", "spyware", 
                        "phishing", "malware", "firefox", "explorer", "netscape", "opera", "safari", "java", "oracle", "sap",
                        "nanotech", "biotech"]
                        
    sports_keywords = ["sport", "football", "soccer", "basketball", "baseball", "tennis", "golf", "cricket", 
                       "racing", "f1", "olympic", "medal", "team", "coach", "player", "match", "tournament", 
                       "league", "cup", "season", "championship", "score", "win", "loss", "victory", "defeat", 
                       "goal", "stadium", "nfl", "nba", "mlb", "fifa", "uefa", "nhl", "rugby", "boxing", "wrestling", 
                       "athlete", "squad", "club", "referee", "umpire", "playoff", "final", "semi-final", "quarter-final", 
                       "race", "lap", "touchdown", "homerun", "basket", "point", "wickets", "runs", "inning"]
                       
    business_keywords = ["business", "economy", "finance", "market", "stock", "trade", "invest", "bank", "money", 
                         "dollar", "euro", "company", "corp", "inc", "ceo", "profit", "revenue", "sale", "price", 
                         "cost", "inflation", "tax", "deal", "merger", "oil", "gas", "mining", "wall street", "fed", 
                         "interest rate", "budget", "deficit", "debt", "currency", "exchange", "nasdaq", "dow jones", 
                         "share", "shareholder", "dividend", "employment", "job", "unemployment", "retail", "consumer", 
                         "spending", "production", "manufacturing", "industry", "sector", "earning", "loss"]
                         
    world_keywords = ["world", "international", "government", "politics", "president", "minister", "war", "peace", 
                      "military", "army", "troop", "bomb", "attack", "terror", "treaty", "un", "united nations", 
                      "election", "vote", "law", "court", "police", "crime", "disaster", "earthquake", "storm", 
                      "protest", "strike", "iraq", "iran", "china", "russia", "israel", "palestine", "afghanistan", 
                      "baghdad", "kabul", "gaza", "prime minister", "parliament", "congress", "senate", "official", 
                      "diplomat", "ambassador", "negotiation", "agreement", "conflict", "battle", "soldier", "weapon", 
                      "nuclear", "missile", "security", "hurricane", "tsunami", "flood", "fire", "accident", "crash", 
                      "refugee", "immigrant"]

    scores = {
        "Science/Technology": 0,
        "Sports": 0,
        "Business": 0,
        "World": 0
    }
    
    # Tokenize and score
    tokens = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace('"', ' ').replace("'", ' ').split()
    
    for word in tokens:
        if word in scitech_keywords: scores["Science/Technology"] += 1
        if word in sports_keywords: scores["Sports"] += 1
        if word in business_keywords: scores["Business"] += 1
        if word in world_keywords: scores["World"] += 1
        
    # Contextual Scoring
    if "game" in text:
        if any(x in text for x in ["video", "console", "nintendo", "xbox", "sony", "playstation", "computer", "online", "software", "tech", "gadget"]):
             scores["Science/Technology"] += 2
        elif any(x in text for x in ["coach", "season", "league", "cup", "team", "score", "player", "sport", "ball", "field"]):
             scores["Sports"] += 2
             
    # "Oil" usually Business, sometimes World
    if "oil" in text and "price" in text:
        scores["Business"] += 2
        
    # "Space" - check if outer space
    if "space" in tokens:
        if any(x in tokens for x in ["shuttle", "nasa", "station", "orbit", "planet", "launch", "mission"]):
            scores["Science/Technology"] += 2
            
    # "Apple" - fruit or company?
    if "apple" in tokens:
        if any(x in tokens for x in ["computer", "ipod", "itunes", "mac", "job", "share", "stock", "market"]):
             scores["Science/Technology"] += 1
             scores["Business"] += 1
             
    # Tie-breaking priority?
    # Usually Sci/Tech vocabulary is quite specific.
    # World vocabulary is very broad.
    
    # Find max
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        # If no keywords found, try to guess or return Unknown
        # For this problem, we must classify.
        # Maybe default to World?
        return "World"
        
    return max_cat

scitech_count = 0
total_count = 0
results_list = []

for art in articles:
    cat = get_category(art.get("title", ""), art.get("description", ""))
    results_list.append({"title": art.get("title"), "cat": cat})
    if cat == "Science/Technology":
        scitech_count += 1
    total_count += 1

result = {
    "total": total_count,
    "scitech": scitech_count,
    "fraction": scitech_count / total_count if total_count > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16186748220380539107': [{'author_id': '218'}], 'var_function-call-13088547404643654170': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1059695270631431239': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-14350953597946120126': [{'_id': '69449f31e2378cb58d5b205d', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69449f31e2378cb58d5b280e', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69449f31e2378cb58d5b2ab9', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69449f31e2378cb58d5b2b48', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69449f31e2378cb58d5b2d18', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-720645202936693653': {'total': 5, 'scitech': 2, 'fraction': 0.4}, 'var_function-call-12956258251938391400': 5, 'var_function-call-9350456290316558969': 'file_storage/function-call-9350456290316558969.json'}

exec(code, env_args)
