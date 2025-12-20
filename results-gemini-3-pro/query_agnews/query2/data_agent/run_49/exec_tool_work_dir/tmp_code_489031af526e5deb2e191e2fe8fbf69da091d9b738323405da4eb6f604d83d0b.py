code = """import json
import string

# Load articles
file_path = locals()['var_function-call-13320926440093840629']
with open(file_path, 'r') as f:
    articles = json.load(f)

sci_tech_keywords = {
    "science", "technology", "tech", "computer", "internet", "web", "software", "hardware", "phone", "mobile", 
    "digital", "gameboy", "nintendo", "sony", "microsoft", "google", "apple", "linux", "windows", "virus", "hacker", 
    "security", "space", "nasa", "astronomy", "physics", "biology", "chemistry", "research", "study", "lab", "robot", 
    "ai", "energy", "fuel", "engine", "electric", "battery", "chip", "processor", "memory", "server", "data", "network", 
    "wireless", "broadband", "satellite", "innovation", "invention", "patent", "medical", "health", "disease", "drug", 
    "treatment", "cancer", "gene", "cell", "organism", "species", "planet", "galaxy", "universe", "telescope", 
    "microscope", "videogame", "console", "gadget", "device", "app", "browser", "search", "social", "facebook", "twitter", 
    "youtube", "online", "cyber", "spam", "scam", "phishing", "malware", "spyware", "trojan", "worm", "botnet", "cloud", 
    "computing", "it", "nanotech", "biotech", "shuttle", "mission", "orbit", "moon", "mars", "stem", "cloning", "genetic", 
    "dna", "genome", "laboratory", "scientist", "researcher", "astronomer", "physicist", "biologist", "chemist", "engineer", 
    "algorithm", "database", "programming", "code", "developer", "supercomputer", "mainframe", "laptop", "tablet", 
    "smartphone", "voip", "wifi", "bluetooth", "gps", "navigation", "display", "screen", "monitor", "lcd", "plasma", 
    "pixel", "resolution", "audio", "video", "camera", "lens", "optical", "laser", "sensor", "detector", "radar", "sonar", 
    "antenna", "transistor", "circuit", "semiconductor", "intel", "amd", "nvidia", "ibm", "oracle", "cisco", "dell", "hp", 
    "lenovo", "samsung", "lg", "motorola", "nokia", "blackberry", "palm", "ps3", "xbox", "wii", "ipod", "iphone", "ipad", 
    "macbook", "kindle", "android", "ios", "unix", "java", "python", "perl", "php", "html", "xml", "ajax", "flash", 
    "adobe", "firefox", "explorer", "safari", "chrome", "opera", "netscape", "mozilla", "beagle", "rover", "cassini", 
    "hubble", "iss", "soyuz", "discovery", "atlantis", "endeavour", "challenger", "columbia", "bionics", "robotics", 
    "automation", "genomics", "proteomics", "pharmacology", "toxicology", "virology", "immunology", "neurology", 
    "cardiology", "oncology", "pathology", "radiology", "surgery", "therapy", "vaccine", "antibiotic", "antiviral", 
    "clinical", "fda", "physics", "mathematician", "mathematics", "math"
}

business_keywords = {
    "business", "company", "firm", "market", "stock", "share", "price", "profit", "loss", "revenue", "income", 
    "economy", "finance", "bank", "invest", "trade", "dollar", "euro", "yen", "pound", "oil", "gold", "industry", 
    "sector", "manufacturing", "retail", "sales", "ceo", "cfo", "executive", "merger", "acquisition", "deal", 
    "contract", "growth", "inflation", "tax", "debt", "loan", "interest", "rate", "treasury", "fed", "reserve", 
    "wall", "street", "nasdaq", "dow", "index", "exchange", "currency", "audit", "accounting", "bankrupt", 
    "liquidation", "creditor", "debtor", "shareholder", "dividend", "yield", "bond", "equity", "capital", "asset", 
    "liability", "expense", "cost", "budget", "forecast", "outlook", "estimate", "earnings", "quarterly", "fiscal", 
    "monetary", "policy", "commerce", "commercial", "consumer", "spending", "confidence", "unemployment", "jobs", 
    "hiring", "layoff", "strike", "union", "labor", "negotiation", "agreement", "settlement", "lawsuit", "court", 
    "ruling", "judge", "regulator", "antitrust", "monopoly", "competition", "strategy", "plan", "expansion", 
    "restructuring", "buyout", "takeover", "bid", "offer", "ipo", "venture", "fund", "insurance", "broker", "trader", "analyst"
}

sports_keywords = {
    "sport", "game", "match", "team", "player", "coach", "manager", "league", "championship", "tournament", "cup", 
    "medal", "olympics", "world", "super", "bowl", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "football", "soccer", 
    "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby", "boxing", "racing", "f1", "nascar", 
    "athlete", "score", "win", "lose", "draw", "goal", "point", "touchdown", "stadium", "arena", "field", "pitch", 
    "track", "lap", "race", "driver", "rider", "cyclist", "swimmer", "gymnast", "sprinter", "runner", "marathon", 
    "triathlon", "relay", "qualifier", "heat", "final", "semifinal", "quarterfinal", "playoff", "series", "season", 
    "standings", "rankings", "record", "title", "trophy", "gold", "silver", "bronze", "olympic", "paralympic", "slam", 
    "open", "masters", "classic", "tour", "pro", "amateur", "varsity", "college", "ncaa", "premier", "serie", "liga", 
    "bundesliga", "mls", "champions", "europa", "copa", "wimbledon", "garros", "pga", "lpga"
}

world_keywords = {
    "world", "international", "un", "nations", "war", "peace", "treaty", "foreign", "country", "president", 
    "minister", "parliament", "election", "politics", "government", "law", "crisis", "disaster", "attack", 
    "military", "army", "police", "crime", "protest", "bomb", "iraq", "iran", "korea", "china", "russia", "usa", 
    "uk", "france", "germany", "japan", "india", "pakistan", "afghanistan", "israel", "palestine", "syria", "egypt", 
    "libya", "sudan", "somalia", "nigeria", "congo", "zimbabwe", "safrica", "brazil", "mexico", "venezuela", "colombia", 
    "cuba", "canada", "australia", "zealand", "eu", "nato", "asean", "apec", "g8", "g20", "wto", "who", "imf", "wb", 
    "ngos", "cross", "amnesty", "greenpeace", "chancellor", "governor", "mayor", "senator", "congressman", "representative", 
    "diplomat", "ambassador", "envoy", "delegate", "official", "spokesman", "leader", "dictator", "tyrant", "monarch", 
    "king", "queen", "prince", "princess", "duke", "duchess", "pope", "bishop", "cleric", "imam", "rabbi", "priest", 
    "monk", "nun", "terrorist", "insurgent", "rebel", "guerrilla", "militant", "activist", "demonstrator", "rioter", 
    "victim", "casualty", "refugee", "migrant", "immigrant", "citizen", "civilian", "voter", "poll", "ballot", "campaign", 
    "candidate", "party", "coalition", "alliance", "opposition", "regime", "administration", "cabinet", "council", 
    "assembly", "committee", "commission", "agency", "department", "ministry", "embassy", "consulate", "base", "camp", 
    "station", "border", "territory", "zone", "region", "province", "state", "city", "town", "village", "capital", 
    "nation", "republic", "federation", "kingdom", "empire", "sovereignty", "independence", "autonomy", "democracy", 
    "dictatorship", "monarchy", "theocracy", "anarchy", "communism", "socialism", "capitalism", "liberalism", 
    "conservatism", "nationalism", "patriotism"
}

def clean_text(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, ' ')
    return text.split()

def classify(article):
    text_str = (article.get('title', '') + ' ' + article.get('description', ''))
    words = clean_text(text_str)
    
    s_score = sum(1 for w in words if w in sci_tech_keywords)
    b_score = sum(1 for w in words if w in business_keywords)
    sp_score = sum(1 for w in words if w in sports_keywords)
    w_score = sum(1 for w in words if w in world_keywords)
    
    # Adjustments
    if "game" in words or "games" in words:
        if any(x in words for x in ["video", "console", "nintendo", "sony", "xbox", "computer", "software", "online", "mobile", "app", "gameboy"]):
            s_score += 5
        if any(x in words for x in ["league", "cup", "match", "team", "player", "coach", "ball", "score", "win", "lose", "sport", "nfl", "nba", "mlb"]):
            sp_score += 5

    # Tech vs Business
    # If tech company + financial terms -> Business
    # But if tech company + product terms -> Sci/Tech
    # Let's verify specific ambiguous cases
    
    scores = {"Science/Technology": s_score, "Business": b_score, "Sports": sp_score, "World": w_score}
    best = max(scores, key=scores.get)
    
    # Tie breaking
    # If 0 scores, default to World?
    if scores[best] == 0:
        return "World" 
        
    return best

sci_tech_titles = []
for a in articles:
    cat = classify(a)
    if cat == "Science/Technology":
        sci_tech_titles.append(a['title'])

result = {
    "count": len(sci_tech_titles),
    "total": len(articles),
    "titles": sci_tech_titles,
    "fraction": len(sci_tech_titles) / len(articles) if len(articles) > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17731222421355545554': [{'author_id': '218'}], 'var_function-call-10772589579831415629': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1499085717710810079': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-2672201808982955812': [{'_id': '6944bfacff70ed2d3ca442b9', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bfacff70ed2d3ca44a6a', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bfacff70ed2d3ca44d15', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bfacff70ed2d3ca44da4', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bfacff70ed2d3ca44f74', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-14450440653002166621': {'total': 5, 'sci_tech_count': 2, 'sci_tech_titles': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award'], 'other_examples': [['GameBoy mini-games win prize', 'Sports'], ['Bailey Tries WR', 'Business'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-13320926440093840629': 'file_storage/function-call-13320926440093840629.json', 'var_function-call-16312177675477890472': {'count': 0, 'total': 111, 'titles': []}, 'var_function-call-3612848950533246018': [{'title': 'GameBoy mini-games win prize', 'text': 'gameboy mini-games win prize a set of gameboy micro-games is named as the most innovative game of the year at a festival in scotland.', 'words': [], 's_score': 0}, {'title': 'Bailey Tries WR', 'text': "bailey tries wr pro bowl cornerback champ bailey practiced with the offense at wide reciever during the denver broncos' practice on tuesday.", 'words': [], 's_score': 0}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'text': 'students win \\$100,000 in national team science competition lucie guo, motivated by the death of her grandfather in china before she was born, spent two summers doing research in a duke university laboratory.', 'words': [], 's_score': 0}, {'title': 'Energy from waves  teenager wins science award', 'text': 'energy from waves  teenager wins science award a teenager from the san diego, california area has won the siemens westinghouse competition in math, science and technology for his  quot;gyro-gen, quot; a machine that produces electricity from ocean waves.', 'words': [], 's_score': 0}, {'title': 'China #39;s appetite boosts BHP', 'text': 'china #39;s appetite boosts bhp bhp billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. ', 'words': [], 's_score': 0}]}

exec(code, env_args)
