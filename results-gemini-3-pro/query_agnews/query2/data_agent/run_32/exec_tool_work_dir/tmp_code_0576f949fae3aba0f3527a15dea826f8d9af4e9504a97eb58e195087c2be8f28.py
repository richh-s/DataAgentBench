code = """import json
import re

# Access the articles list directly
articles = locals()['var_function-call-16787211040643364345']

# Define keywords for each category
keywords = {
    "Sci/Tech": [
        "science", "technology", "computer", "software", "hardware", "internet", "web", "online", "digital",
        "mobile", "phone", "wireless", "satellite", "network", "server", "database", "cyber", "hacker", "virus",
        "security", "firewall", "microsoft", "google", "apple", "intel", "ibm", "linux", "unix", "windows", "mac",
        "ipod", "iphone", "blackberry", "nokia", "sony", "nintendo", "gameboy", "xbox", "playstation", "wii",
        "console", "video game", "videogame", "gaming", "nasa", "space", "astronomy", "universe", "planet",
        "mars", "moon", "rocket", "shuttle", "robot", "bot", "artificial intelligence", "biotech", "biology",
        "genome", "dna", "cell", "physic", "chemist", "research", "lab", "laboratory", "study", "innovat",
        "gadget", "device", "electronic", "broadband", "telecom", "semiconductor", "chip", "browser", "firefox",
        "explorer", "spam", "email", "search engine", "blog", "download", "upload", "mp3", "dvd", "lcd", "plasma",
        "high-tech", "tech", "data", "code", "program", "app", "application", "algorithm", "supercomputer",
        "laser", "nano", "nuclear", "stem cell", "cloning", "telescope", "hubble", "voip", "wifi", "bluetooth",
        "gps", "pda", "smartphone", "laptop", "notebook", "desktop", "monitor", "screen", "keyboard", "mouse",
        "processor", "cpu", "memory", "storage", "disk", "drive", "usb", "flash", "camera", "pixel", "resolution",
        "format", "media", "audio", "video", "streaming", "podcast", "rss", "xml", "html", "java", "script",
        "oracle", "sap", "cisco", "dell", "hp", "lenovo", "motorola", "samsung", "lg", "panasonic", "toshiba",
        "sharp", "philips", "siemens", "ge", "general electric", "at&t", "verizon", "sprint", "t-mobile",
        "vodafone", "orange", "bt", "british telecom", "ntt", "skype", "ebay", "amazon", "yahoo", "facebook",
        "myspace", "twitter", "youtube", "flickr", "wikipedia", "encyclopedia", "book", "kindle", "reader"
    ],
    "Sports": [
        "sport", "football", "soccer", "basketball", "baseball", "tennis", "cricket", "rugby", "hockey", "golf",
        "olympic", "athlete", "player", "team", "coach", "match", "tournament", "cup", "league", "champion",
        "medal", "score", "win", "lost", "game", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "nascar", "f1",
        "racing", "stadium", "club", "squad", "quarterback", "touchdown", "goal", "striker", "defender",
        "goalkeeper", "pitcher", "batter", "inning", "playoff", "super bowl", "world series", "wimbledon",
        "open", "grand slam", "title", "cup", "race", "driver", "lap", "finish", "start", "points", "standing",
        "rank", "seed", "draw", "round", "final", "semi-final", "quarter-final", "heat", "event", "competition",
        "contest", "meet", "games", "athletics", "gymnastics", "swimming", "cycling", "boxing", "wrestling",
        "martial arts", "judo", "karate", "taekwondo", "skiing", "skating", "snowboarding", "surfing", "sailing",
        "rowing", "canoeing", "kayaking", "equestrian", "horse racing", "jockey", "trainer", "owner", "betting",
        "odds", "favorite", "underdog", "upset", "victory", "defeat", "loss", "draw", "tie", "penalty", "foul",
        "red card", "yellow card", "referee", "umpire", "official", "commissioner", "manager", "agent", "draft",
        "trade", "contract", "salary", "cap", "free agent", "roster", "lineup", "injury", "season", "preseason",
        "postseason", "regular season"
    ],
    "Business": [
        "business", "company", "corp", "inc", "market", "stock", "share", "trade", "economy", "finance", "money",
        "dollar", "euro", "yen", "bank", "invest", "profit", "revenue", "sale", "ceo", "cfo", "manager", "merger",
        "acquisition", "oil", "price", "industry", "dow jones", "nasdaq", "wall street", "inflation", "rate",
        "fed", "federal reserve", "tax", "budget", "deficit", "employment", "job", "imf", "wto", "deal", "bid",
        "offer", "bankruptcy", "earnings", "quarter", "fiscal", "report", "statement", "forecast", "outlook",
        "growth", "decline", "recession", "depression", "recovery", "expansion", "boom", "bust", "bubble",
        "crash", "crisis", "bailout", "stimulus", "cut", "hike", "interest", "loan", "mortgage", "credit",
        "debt", "bond", "yield", "currency", "exchange", "forex", "commodity", "gold", "silver", "platinum",
        "copper", "steel", "aluminum", "energy", "power", "gas", "utility", "retail", "consumer", "spending",
        "confidence", "index", "average", "future", "option", "derivative", "hedge", "fund", "equity", "asset",
        "liability", "balance", "sheet", "cash", "flow", "dividend", "yield", "payout", "return", "roi", "roe",
        "roa", "margin", "operating", "net", "gross", "ebitda", "valuation", "cap", "capital", "market cap"
    ],
    "World": [
        "world", "international", "country", "government", "president", "minister", "prime minister", "politics",
        "war", "peace", "military", "army", "navy", "air force", "police", "attack", "bomb", "blast", "kill",
        "suicide", "terror", "election", "vote", "poll", "crisis", "disaster", "aid", "united nations", "un",
        "eu", "europe", "asia", "africa", "middle east", "mideast", "iraq", "iran", "afghanistan", "israel",
        "palestine", "syria", "russia", "china", "korea", "nuclear", "weapon", "treaty", "diplomat", "official",
        "parliament", "congress", "senate", "law", "court", "judge", "trial", "prison", "hurricane", "earthquake",
        "tsunami", "flood", "fire", "storm", "typhoon", "cyclone", "tornado", "volcano", "eruption", "famine",
        "drought", "disease", "epidemic", "pandemic", "flu", "virus", "aids", "hiv", "malaria", "tb", "polio",
        "vaccine", "health", "hospital", "doctor", "nurse", "patient", "drug", "medicine", "pharmaceutical",
        "school", "education", "student", "teacher", "university", "college", "protest", "demonstration", "strike",
        "riot", "clash", "violence", "crime", "murder", "homicide", "robbery", "theft", "kidnap", "hostage",
        "ransom", "arrest", "suspect", "convict", "sentence", "jail", "execution", "death penalty", "human rights",
        "freedom", "democracy", "dictator", "regime", "coup", "rebel", "insurgent", "guerrilla", "militia",
        "paramilitary", "troops", "soldiers", "forces", "bases", "occupation", "withdrawal", "peacekeeping",
        "mission", "envoy", "ambassador", "embassy", "consulate", "visa", "passport", "immigration", "migration",
        "refugee", "asylum", "border", "customs", "smuggling", "trafficking"
    ]
}

def classify_article(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in keywords}
    
    for cat, words in keywords.items():
        for word in words:
            # Using regex for word boundaries
            if re.search(r'\b' + re.escape(word) + r'\b', text):
                scores[cat] += 1
                
    # Boosts / Penalties
    if "video game" in text or "nintendo" in text or "sony" in text or "xbox" in text or "gameboy" in text:
        scores["Sci/Tech"] += 5
    
    if "oil" in text or "price" in text or "profit" in text:
        scores["Business"] += 2
        
    if "team" in text or "coach" in text or "player" in text:
        scores["Sports"] += 2

    # If "game" is matched, it might have added to Sports. 
    # If "video game" is present, we want Sci/Tech.
    # The boost above handles it.
    
    # Tie breaking:
    # If tie between Sci/Tech and Business (e.g. tech company earning), favor Business if "profit/stock" words exist?
    # Actually, usually news about tech companies' earnings is "Business". News about new products is "Sci/Tech".
    # My keywords setup should handle this naturally by count.
    
    if max(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

sci_tech_count = 0
total_count = len(articles)
results = []

for article in articles:
    cat = classify_article(article.get('title', ''), article.get('description', ''))
    results.append({'id': article['article_id'], 'title': article['title'], 'category': cat})
    if cat == "Sci/Tech":
        sci_tech_count += 1

print("__RESULT__:")
print(json.dumps({"sci_tech_count": sci_tech_count, "total_count": total_count, "fraction": sci_tech_count/total_count if total_count > 0 else 0, "sample_classifications": results[:20]}))"""

env_args = {'var_function-call-13530167711218597416': [{'author_id': '218'}], 'var_function-call-2039518021578433563': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-2120325614100718992': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-16787211040643364345': [{'_id': '6944ac495017b3003ef4bff8', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ac495017b3003ef4c7a9', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ac495017b3003ef4ca54', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ac495017b3003ef4cae3', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ac495017b3003ef4ccb3', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
