code = """import json

# Load the articles
articles_data = locals()['var_function-call-2672201808982955812']
if isinstance(articles_data, str):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_data

sci_tech_keywords = [
    "science", "technology", "tech", "computer", "internet", "web", "software", "hardware", "phone", "mobile", 
    "digital", "gameboy", "nintendo", "sony", "microsoft", "google", "apple", "linux", "windows", "virus", "hacker", 
    "security", "space", "nasa", "astronomy", "physics", "biology", "chemistry", "research", "study", "lab", "robot", 
    "ai", "energy", "fuel", "engine", "electric", "battery", "chip", "processor", "memory", "server", "data", "network", 
    "wireless", "broadband", "satellite", "innovation", "invention", "patent", "medical", "health", "disease", "drug", 
    "treatment", "cancer", "gene", "cell", "organism", "species", "planet", "galaxy", "universe", "telescope", 
    "microscope", "video game", "console", "gadget", "device", "app", "browser", "search engine", "social network", 
    "facebook", "twitter", "youtube", "online", "cyber", "spam", "scam", "phishing", "malware", "spyware", "trojan", 
    "worm", "botnet", "cloud", "computing", "it", "information technology", "nanotech", "biotech", "ibm", "intel", 
    "amd", "nvidia", "oracle", "cisco", "dell", "hp", "lenovo", "samsung", "lg", "panasonic", "toshiba", "hitachi", 
    "fujitsu", "nec", "siemens", "ge", "philips", "medtronic", "pfizer", "merck", "novartis", "roche", "glaxosmithkline", 
    "sanofi", "astrazeneca", "bayer", "monsanto", "dupont", "dow", "basf", "3m", "honeywell", "utc", "boeing", "airbus", 
    "lockheed", "northrop", "raytheon", "gd", "bae", "thales", "finmeccanica", "safran", "rolls-royce", "pratt", 
    "whitney", "ge aviation", "cfm", "iae", "engine alliance", "powerjet", "kuznetsov", "aviadvigatel", "ivchenko", 
    "motor", "sich", "npo", "saturn", "uec", "tumansky", "klimov", "izotov", "soloviev", "lotarev", "d-18t", "ps-90", 
    "sam146", "saam", "kaveri", "gtk", "gtre", "hal", "drdo", "isro", "esa", "jaxa", "cnsa", "roscosmos", "spacex", 
    "blue origin", "virgin galactic", "orbital atk", "ula", "ariane", "soyuz", "proton", "falcon", "delta", "atlas", 
    "sls", "orion", "dragon", "cygnus", "dream chaser", "starliner", "new shepard", "new glenn", "vulcan", "ariane 6", 
    "h3", "long march", "angara", "soyuz-5", "irtysh", "yenisei", "don", "amur", "orel", "federation", "kliper", "parom"
]

business_keywords = [
    "business", "company", "firm", "market", "stock", "share", "price", "profit", "loss", "revenue", "income", 
    "economy", "finance", "bank", "invest", "trade", "dollar", "euro", "yen", "pound", "oil", "gold", "industry", 
    "sector", "manufacturing", "retail", "sales", "ceo", "merger", "deal", "contract", "growth", "inflation", 
    "tax", "debt", "loan", "interest", "rate", "corp", "inc", "ltd", "plc", "llc", "gmbh", "sa", "nv", "bv", "kk", 
    "ag", "se", "spa", "srl", "sl", "sarl", "sas", "ab", "oy", "as", "asa", "pty", "proprietary", "limited", 
    "incorporated", "corporation", "company", "co", "partners", "group", "holdings", "capital", "management", 
    "associates", "enterprises", "solutions", "systems", "technologies", "resources", "energy", "power", "motors", 
    "auto", "automotive", "financial", "insurance", "investment", "properties", "real estate", "development", 
    "construction", "engineering", "consulting", "services", "media", "entertainment", "communications", "telecom", 
    "transport", "logistics", "shipping", "airline", "airways", "railway", "railroad", "train", "bus", "truck", 
    "shipping", "marine", "maritime"
]

sports_keywords = [
    "sport", "game", "match", "team", "player", "coach", "manager", "league", "championship", "tournament", "cup", 
    "medal", "olympics", "world cup", "super bowl", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "football", "soccer", 
    "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby", "boxing", "racing", "f1", "nascar", 
    "athlete", "score", "win", "lose", "draw", "goal", "point", "touchdown", "stadium"
]

world_keywords = [
    "world", "international", "un", "united nations", "war", "peace", "treaty", "foreign", "country", "president", 
    "minister", "parliament", "election", "politics", "government", "law", "court", "crisis", "disaster", "attack", 
    "military", "army", "police", "crime", "protest", "bomb", "iraq", "iran", "korea", "china", "russia", "usa", 
    "uk", "france", "germany", "japan", "india", "pakistan", "afghanistan", "israel", "palestine", "syria", "egypt", 
    "libya", "sudan", "somalia", "nigeria", "congo", "zimbabwe", "safrica", "brazil", "mexico", "venezuela", "colombia", 
    "cuba", "canada", "australia", "zealand", "eu", "nato", "asean", "apec", "g8", "g20", "wto", "who", "imf", "wb", 
    "ngos", "red cross", "doctors without borders", "amnesty", "hrw", "greenpeace", "wwf", "peta"
]

def classify_article(article):
    text = (article.get('title', '') + ' ' + article.get('description', '')).lower()
    
    scores = {
        "Science/Technology": 0,
        "Business": 0,
        "Sports": 0,
        "World": 0
    }
    
    for word in sci_tech_keywords:
        if word in text:
            scores["Science/Technology"] += 1
            
    for word in business_keywords:
        if word in text:
            scores["Business"] += 1
            
    for word in sports_keywords:
        if word in text:
            scores["Sports"] += 1
            
    for word in world_keywords:
        if word in text:
            scores["World"] += 1
            
    # Heuristics adjustments
    # "Game" is tricky.
    if "game" in text:
        # Check context
        tech_context = any(w in text for w in ["video", "console", "nintendo", "sony", "xbox", "computer", "software", "online", "mobile"])
        sport_context = any(w in text for w in ["league", "cup", "match", "team", "player", "coach", "ball", "score", "win", "lose"])
        if tech_context and not sport_context:
            scores["Science/Technology"] += 5
        elif sport_context and not tech_context:
            scores["Sports"] += 5
            
    # "Company" is business, but "Software Company" is Sci/Tech? Usually Business category covers the financial aspect, Sci/Tech covers the product.
    # The prompt implies articles belong to ONE category.
    # Let's look at the "China's appetite boosts BHP" example. It has "mining company", "profits". Classified as Business.
    # "GameBoy mini-games win prize" -> Sci/Tech.
    
    # Priority: If it's about profits/stocks of a tech company, it might be Business.
    # But often news datasets classify "Tech" business news under "Technology".
    # Let's see the examples again.
    # "Students Win $100,000 in National Team Science Competition" -> Sci/Tech.
    # "Energy from waves teenager wins science award" -> Sci/Tech.
    
    # Let's pick the max score.
    # If tie, prioritize Sci/Tech if specific keywords are present?
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown" # Or default to World?
        
    return best_cat

sci_tech_count = 0
sci_tech_articles = []
other_articles = []

for article in articles:
    cat = classify_article(article)
    if cat == "Science/Technology":
        sci_tech_count += 1
        sci_tech_articles.append(article['title'])
    else:
        other_articles.append((article['title'], cat))

result = {
    "total": len(articles),
    "sci_tech_count": sci_tech_count,
    "sci_tech_titles": sci_tech_articles,
    "other_examples": other_articles[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17731222421355545554': [{'author_id': '218'}], 'var_function-call-10772589579831415629': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1499085717710810079': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-2672201808982955812': [{'_id': '6944bfacff70ed2d3ca442b9', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bfacff70ed2d3ca44a6a', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bfacff70ed2d3ca44d15', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bfacff70ed2d3ca44da4', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bfacff70ed2d3ca44f74', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
