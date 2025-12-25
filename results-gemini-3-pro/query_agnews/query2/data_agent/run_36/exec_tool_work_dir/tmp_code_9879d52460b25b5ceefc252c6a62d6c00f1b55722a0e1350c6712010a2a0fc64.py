code = """import json
import string

# Load articles
file_path = locals()['var_function-call-15334098416954364373']
with open(file_path, 'r') as f:
    articles = json.load(f)

sci_tech_keywords = [
    "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", 
    "cyber", "digital", "online", "data", "robot", "robotics", "space", "nasa", "astronomy", "mars", 
    "biology", "physics", "chemistry", "genetic", "medical", "research", "lab", "scientist", 
    "discovery", "innovation", "gadget", "device", "mobile", "phone", "smartphone", "wireless", 
    "network", "satellite", "broadband", "app", "browser", "virus", "hacker", "security", 
    "spam", "email", "microsoft", "apple", "google", "intel", "ibm", "linux", "windows", 
    "nintendo", "sony", "xbox", "playstation", "console", "video game", "gameboy", "gaming",
    "semiconductor", "chip", "processor", "shuttle", "mission", "probe", "orbit", "moon", "sun",
    "telescope", "galaxy", "universe", "laser", "nanotech", "biotech", "cloning", "stem cell",
    "dna", "genome", "mutation", "virus", "bacterium", "disease", "drug", "pharmaceutical",
    "treatment", "therapy", "medicine", "hospital", "doctor", "health", "cancer", "aids", "hiv",
    "flu", "vaccine", "epidemic", "pandemic", "microsoft", "bill gates", "steve jobs",
    "search engine", "blog", "social media", "facebook", "twitter", "youtube", "amazon", "ebay",
    "yahoo", "isp", "dsl", "voip", "wifi", "bluetooth", "gps", "pda", "mp3", "dvd", "hdtv",
    "lcd", "plasma", "oled", "camera", "pixel", "sensor", "battery", "solar", "fuel cell",
    "storage", "server"
]

business_keywords = [
    "stock", "stocks", "market", "markets", "dow", "nasdaq", "s&p", "economy", "economic", 
    "jobless", "unemployment", "inflation", "rate", "rates", "fed", "federal reserve", 
    "bank", "banks", "banking", "finance", "financial", "investment", "investor", "profit", 
    "profits", "earnings", "revenue", "sales", "quarter", "share", "shares", "dividend", 
    "trade", "trading", "merger", "acquisition", "deal", "buyout", "bid", "ipo", "ceo", "cfo", 
    "executive", "company", "companies", "corp", "corporation", "inc", "ltd", "business", 
    "industry", "sector", "retail", "retailer", "store", "stores", "shop", "shopping", 
    "consumer", "spending", "price", "prices", "cost", "costs", "budget", "deficit", "tax", 
    "taxes", "oil", "gas", "energy", "crude", "barrel", "opec", "mining", "mine", "miner", 
    "commodity", "commodities", "gold", "silver", "metal", "dollar", "euro", "yen", "currency"
]

def classify_article(title, desc):
    text = (title + " " + desc).lower()
    
    # Custom tokenization
    tokens = []
    for word in text.split():
        # Remove punctuation from ends
        clean_word = word.strip(string.punctuation)
        if clean_word:
            tokens.append(clean_word)
            
    sci_score = 0
    bus_score = 0
    
    for t in tokens:
        if t in sci_tech_keywords:
            sci_score += 1
        if t in business_keywords:
            bus_score += 1
            
    # Phrases check in raw text
    phrases_sci = ["video game", "social media", "artificial intelligence", "stem cell"]
    for p in phrases_sci:
        if p in text:
            sci_score += 2
            
    # Strong overrides
    if "nasa" in text or "space" in text or "astronomy" in text:
        sci_score += 2
    if "science" in text:
        sci_score += 3
        
    if "revenue" in text or "profit" in text or "earnings" in text:
        bus_score += 3
        
    # Heuristic for specific cases
    if "microsoft" in tokens and "settles" in tokens:
        # Legal/Business vs Tech. Usually tech news.
        # Check scores.
        pass
    
    if sci_score > 0 and sci_score >= bus_score:
        return True
        
    # Game logic
    if "game" in tokens or "games" in tokens:
        # Check context
        game_context = ["nintendo", "sony", "xbox", "console", "video", "computer", "mobile", "app", "software", "gameboy", "innovative", "micro-games", "mini-games"]
        if any(g in text for g in game_context):
             if not any(s in text for s in ["football", "baseball", "basketball", "soccer", "team", "coach"]):
                 return True

    return False

sci_tech_count = 0
for a in articles:
    if classify_article(a['title'], a['description']):
        sci_tech_count += 1

fraction = sci_tech_count / len(articles)

print("__RESULT__:")
print(json.dumps({
    "count": sci_tech_count, 
    "total": len(articles), 
    "fraction": fraction
}))"""

env_args = {'var_function-call-5653833913693159420': [{'author_id': '218'}], 'var_function-call-7433888646430808127': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-12992307347348445405': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-9189534630217385187': [{'_id': '6944b05cbdc646d43f30d05e', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b05cbdc646d43f30d80f', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b05cbdc646d43f30daba', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b05cbdc646d43f30db49', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b05cbdc646d43f30dd19', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-11358798697527574637': {'total': 5, 'sci_tech_count': 4, 'sci_tech_titles': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP'], 'other_titles': ['Bailey Tries WR']}, 'var_function-call-15334098416954364373': 'file_storage/function-call-15334098416954364373.json', 'var_function-call-3755384053590396321': {'total': 111, 'sci_tech_count': 6, 'sci_tech_titles': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Ex-Astronaut Casts Doubt on Space Tourism']}, 'var_function-call-6475461343629668623': [{'title': 'GameBoy mini-games win prize', 'tokens': [], 'sci_score': 0, 'sci_matches': [], 'bus_score': 0, 'bus_matches': []}, {'title': 'Microsoft settles with UK phone maker', 'tokens': [], 'sci_score': 0, 'sci_matches': [], 'bus_score': 0, 'bus_matches': []}, {'title': 'EMC Unveils E-mail Storage For Microsoft Exchange', 'tokens': [], 'sci_score': 0, 'sci_matches': [], 'bus_score': 0, 'bus_matches': []}], 'var_function-call-15749050450620439386': [{'title': 'GameBoy mini-games win prize', 'text': 'gameboy mini-games win prize a set of gameboy micro-games is named as the most innovative game of the year at a festival in scotland.', 'split_tokens': ['gameboy', 'mini-games', 'win', 'prize', 'a', 'set', 'of', 'gameboy', 'micro-games', 'is', 'named', 'as', 'the', 'most', 'innovative', 'game', 'of', 'the', 'year', 'at', 'a', 'festival', 'in', 'scotland.']}]}

exec(code, env_args)
