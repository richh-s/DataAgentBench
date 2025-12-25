code = """import json
import re

# Load articles
result_path = locals()['var_function-call-3532961735505256302']
with open(result_path, 'r') as f:
    articles_data = json.load(f)

# Define Keywords (Same as before, with minor tweaks)
keywords_scitech = {
    "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", "space", "nasa", 
    "biology", "physics", "chemistry", "research", "lab", "robot", "gadget", "phone", "mobile", "app", "video game", "console", 
    "gaming", "nintendo", "sony", "microsoft", "apple", "google", "intel", "linux", "windows", "virus", "hacker", "network", 
    "data", "energy", "invention", "innovation", "scientist", "engineer", "astronomy", "genetics", "medical", "health", "disease", 
    "drug", "treatment", "hospital", "doctor", "patient", "cancer", "study", "university", "cyber", "broadband", 
    "wireless", "satellite", "telecom", "browser", "server", "chip", "processor", "screen", "battery", "engine", "machine", 
    "device", "solar", "nuclear", "climate", "warming", "environment", "nature", "animal", "plant", "species", "evolution", 
    "fossil", "dinosaur", "galaxy", "planet", "star", "moon", "mars", "rocket", "shuttle", "station", "telescope", "microscope", 
    "laboratory", "experiment", "discovery", "theory", "math", "mathematics", "algorithm", "code", "program", "developer", 
    "system", "platform", "database", "cloud", "security", "privacy", "encryption", "password", "user", "interface", "display", 
    "monitor", "keyboard", "mouse", "printer", "scanner", "camera", "video", "audio", "sound", "mp3", "ipod", "iphone", "ipad", 
    "tablet", "laptop", "notebook", "desktop", "supercomputer", "mainframe", "gameboy", "xbox", "playstation", "wii", "email", 
    "spam", "blog", "search engine", "wifi", "bluetooth", "gps", "robotics", "automation", "ai", "artificial intelligence", 
    "virtual", "reality", "nanotech", "biotech", "genomics", "stem cell", "cloning", "lasers", "optics", "probe", "orbit", 
    "launch", "flight", "astronaut", "mission", "shuttle", "firefox", "mozilla", "explorer", "netscape", "opera", "safari"
}

keywords_sports = {
    "sport", "football", "soccer", "basketball", "baseball", "tennis", "golf", "cricket", "rugby", "hockey", "olympics", 
    "game", "team", "player", "coach", "league", "cup", "championship", "tournament", "medal", "score", "goal", "touchdown", 
    "run", "race", "winner", "loser", "match", "stadium", "athlete", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", 
    "us open", "grand slam", "world cup", "super bowl", "quarterback", "receiver", "pitcher", "striker", "midfielder", 
    "defender", "goalkeeper", "referee", "umpire", "f1", "formula 1", "racing", "driver", "lap", "boxing", "fight", "round", 
    "knockout", "mma", "ufc", "wrestling", "wwe", "swimming", "gymnastics", "athletics", "track", "field", "marathon", "sprint", 
    "relay", "jump", "throw", "skiing", "skating", "snowboarding", "surfing", "cycling", "biking", "tour de france", "club", 
    "squad", "roster", "draft", "season", "playoff", "final", "semifinal", "quarterfinal", "ranking", "title", "trophy", 
    "gold", "silver", "bronze", "record", "training", "workout", "fitness", "gym", "exercise", "bowl", "pro bowl", "red sox", 
    "yankees", "dodgers", "giants", "patriots", "cowboys", "broncos", "packers", "steelers", "eagles", "colts", "raiders", 
    "vikings", "bears", "lions", "tigers", "indians", "mets", "phillies", "braves", "marlins", "nationals", "rangers", 
    "astros", "mariners", "angels", "athletics", "royals", "twins", "white sox", "blue jays", "rays", "orioles", "padres", 
    "diamondbacks", "rockies", "pirates", "reds", "cardinals", "brewers", "cubs"
}

keywords_business = {
    "business", "economy", "market", "stock", "share", "trade", "finance", "money", "bank", "company", "corporation", 
    "profit", "loss", "revenue", "sale", "price", "cost", "invest", "deal", "merger", "acquisition", "ceo", "manager", 
    "employee", "job", "work", "industry", "sector", "product", "service", "consumer", "customer", "retail", "dollar", 
    "euro", "currency", "inflation", "tax", "budget", "fed", "federal reserve", "interest", "rate", "loan", "debt", "bond", 
    "equity", "dividend", "yield", "dow", "nasdaq", "s&p", "wall street", "exchange", "commodity", "oil", "gas", "mining", 
    "manufacturing", "factory", "supply", "demand", "import", "export", "tariff", "deficit", "surplus", "gdp", "growth", 
    "recession", "depression", "bankruptcy", "default", "rating", "credit", "mortgage", "housing", "real estate", "property", 
    "insurance", "fund", "hedge", "venture", "capital", "startup", "ipo", "valuation", "earnings", "forecast", "outlook", 
    "trend", "strategy", "plan", "project", "contract", "agreement", "partner", "partnership", "joint", "subsidiary", 
    "parent", "holding", "group", "conglomerate", "multinational", "corporate", "executive", "board", "director", "chairman", 
    "president", "vp", "cfo", "coo", "cto", "cio", "cmo", "marketing", "advertising", "brand", "logo", "trademark", "copyright", 
    "patent", "license", "royalty", "franchise", "chain", "store", "shop", "mall", "supermarket", "grocery", "restaurant", 
    "hotel", "airline", "travel", "tourism", "transport", "logistics", "shipping", "delivery", "freight", "cargo", "port", 
    "airport", "railway", "train", "truck", "bus", "auto", "vehicle", "maker", "manufacturer", "producer", "supplier", 
    "distributor", "wholesaler", "retailer", "merchant", "trader", "broker", "firm", "consultancy", "utility", "power", 
    "jobless", "claims", "hiring", "unemployment", "wage", "salary", "bonus", "pension", "retirement", "strike", "union", 
    "labor", "workforce", "layoff", "downsizing", "outsourcing", "offshoring"
}

keywords_world = {
    "world", "politics", "government", "war", "peace", "country", "nation", "state", "city", "president", "minister", 
    "leader", "election", "vote", "law", "court", "crime", "police", "military", "army", "navy", "air force", "terrorism", 
    "attack", "bomb", "kill", "death", "disaster", "earthquake", "flood", "storm", "weather", "un", "eu", "nato", 
    "diplomacy", "foreign", "international", "global", "congress", "senate", "parliament", "assembly", "council", "committee", 
    "commission", "department", "ministry", "agency", "bureau", "office", "administration", "regime", "authority", "rule", 
    "lawyer", "judge", "jury", "trial", "verdict", "sentence", "prison", "jail", "inmate", "prisoner", "human rights", 
    "refugee", "immigrant", "migration", "border", "defense", "intelligence", "spy", "surveillance", "protest", "demonstration", 
    "rally", "march", "strike", "riot", "clash", "violence", "conflict", "crisis", "emergency", "rescue", "aid", "relief", 
    "charity", "ngo", "organization", "group", "movement", "party", "candidate", "campaign", "poll", "survey", "voter", 
    "ballot", "democracy", "republic", "monarchy", "dictatorship", "coup", "rebellion", "revolution", "battle", "fight", 
    "combat", "soldier", "troop", "weapon", "gun", "missile", "blast", "explosion", "fire", "crash", "accident", "incident", 
    "tragedy", "victim", "survivor", "casualty", "injury", "wound", "epidemic", "pandemic", "outbreak", "spread", "vaccine", 
    "medicine", "pharmaceutical", "iraq", "afghanistan", "iran", "korea", "china", "russia", "usa", "uk", "france", "germany", 
    "palestinians", "palestine", "israel", "gaza", "west bank", "jerusalem", "baghdad", "kabul", "tehran", "pyongyang", 
    "beijing", "moscow", "washington", "london", "paris", "berlin", "rome", "madrid", "athens", "ankara", "damascus", 
    "cairo", "riad", "jeddah", "mecca", "medina", "dubai", "abu dhabi", "doha", "kuwait", "manama", "muscat", "sanaa", 
    "beirut", "amman", "tel aviv", "ramallah", "tripoli", "tunis", "algiers", "rabat", "khartoum", "addis ababa", "nairobi", 
    "mogadishu", "johannesburg", "capetown", "lagos", "abuja", "accra", "dakar", "bamako", "niamey", "ouagadougou", 
    "abidjan", "monrovia", "freetown", "conakry", "bissau", "banjul", "nouakchott", "kinshasa", "brazzaville", "luanda", 
    "lusaka", "harare", "maputo", "antananarivo", "port louis", "victoria", "moroni", "djibouti", "asmara", "kigali", 
    "bujumbura", "kampala", "dar es salaam", "lilongwe", "mbabane", "maseru", "gaborone", "windhoek", "pretoria", 
    "bloemfontein", "blast", "explosion", "killed", "dead", "died"
}

def classify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text) # Replace punct with space
    words = text.split()
    
    scores = {
        "Science/Technology": 0,
        "Sports": 0,
        "Business": 0,
        "World": 0
    }
    
    for word in words:
        if word in keywords_scitech:
            scores["Science/Technology"] += 1
        if word in keywords_sports:
            scores["Sports"] += 1
        if word in keywords_business:
            scores["Business"] += 1
        if word in keywords_world:
            scores["World"] += 1
            
    # Heuristics
    
    # "Game" disambiguation
    if "game" in words:
        if any(w in words for w in ["video", "console", "nintendo", "sony", "microsoft", "computer", "software", "app", "online", "mini", "micro"]):
            scores["Science/Technology"] += 2
        elif any(w in words for w in ["football", "soccer", "basketball", "baseball", "league", "cup", "match", "team", "score", "win", "lose", "sox", "yankees"]):
            scores["Sports"] += 2
            
    # Science award
    if "science" in words and ("award" in words or "prize" in words or "competition" in words):
        scores["Science/Technology"] += 3

    # NASA
    if "nasa" in words:
        scores["Science/Technology"] += 3
        
    # Disaster vs Business (e.g. Gas explosion)
    if "blast" in words or "explosion" in words or "killed" in words or "dead" in words:
        scores["World"] += 3
        
    # Financial results of Tech companies
    # If Tech company + Revenue/Profit -> Business
    tech_companies = ["intel", "microsoft", "apple", "google", "ibm", "cisco", "dell", "hp", "oracle", "yahoo"]
    finance_terms = ["revenue", "profit", "earnings", "quarter", "estimate", "sales"]
    if any(tc in words for tc in tech_companies) and any(ft in words for ft in finance_terms):
        scores["Business"] += 3
        
    return max(scores, key=scores.get)

scitech_count = 0
total_count = 0
details = []

for article in articles_data:
    title = article.get('title', '')
    desc = article.get('description', '')
    text = title + " " + desc
    category = classify(text)
    details.append((title, category))
    
    if category == "Science/Technology":
        scitech_count += 1
    total_count += 1

result = {
    "total": total_count,
    "scitech_count": scitech_count,
    "fraction": scitech_count / total_count if total_count > 0 else 0,
    "details_preview": details[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5076110236557448353': [{'author_id': '218'}], 'var_function-call-13918187589593587279': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-14901224986284523906': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-13145615275713243315': [{'_id': '6944bdf0605c2d7a12d3f580', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bdf0605c2d7a12d3fd31', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bdf0605c2d7a12d3ffdc', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bdf0605c2d7a12d4006b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bdf0605c2d7a12d4023b', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-9591507011003145274': {'total': 5, 'scitech': 4, 'fraction': 0.8, 'details': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Science/Technology'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Science/Technology'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Science/Technology'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Business'}]}, 'var_function-call-11089784368196178869': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966'], 'var_function-call-17063699671402258687': [], 'var_function-call-10528255648792540529': [{'_id': '6944bdf0605c2d7a12d40442', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-3532961735505256302': 'file_storage/function-call-3532961735505256302.json', 'var_function-call-10701263220927585816': {'total': 111, 'scitech_count': 24, 'fraction': 0.21621621621621623, 'details_preview': [['GameBoy mini-games win prize', 'Science/Technology'], ['Bailey Tries WR', 'Sports'], ['Students Win \\$100,000 in National Team Science Competition', 'Science/Technology'], ['Energy from waves  teenager wins science award', 'Science/Technology'], ['China #39;s appetite boosts BHP', 'Business'], ['Leading Indicators, Jobless Claims Dip (AP)', 'Business'], ['Even in win, nasty vibes', 'Sports'], ['Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'Business'], ['Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'World'], ['Somalians sworn in', 'World']]}}

exec(code, env_args)
