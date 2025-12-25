code = """import json
import re

# Load the articles
data = locals()['var_function-call-10609120748234142351']
with open(data, 'r') as f:
    articles = json.load(f)

# Define keywords (expanded and improved)
scitech_keywords = {
    "science", "sciences", "technology", "technologies", "tech", "computer", "computers", "computing",
    "internet", "web", "software", "hardware", "digital", "network", "networks", "data", "cyber", "cybersecurity",
    "virus", "viruses", "hacker", "hackers", "security", "robot", "robots", "robotics", "ai", "artificial", "intelligence",
    "space", "nasa", "astronomy", "mars", "moon", "planet", "planets", "galaxy", "galaxies", "universe",
    "physics", "physicist", "chemistry", "chemist", "biology", "biologist", "genetics", "genetic", "dna", "stem", "clone", "cloning",
    "medical", "medicine", "health", "disease", "diseases", "cancer", "aids", "hiv", "flu", "vaccine", "vaccines",
    "drug", "drugs", "therapy", "treatment", "doctor", "doctors", "hospital", "hospitals", "patient", "patients",
    "research", "researcher", "study", "studies", "lab", "laboratory", "experiment", "experiments", "trial", "trials",
    "energy", "power", "solar", "wind", "nuclear", "engine", "engines", "battery", "batteries",
    "phone", "phones", "mobile", "mobiles", "cellphone", "cellphones", "smartphone", "smartphones",
    "app", "apps", "tablet", "tablets", "laptop", "laptops", "gadget", "gadgets", "device", "devices",
    "video", "game", "games", "gaming", "gamer", "gamers", "console", "consoles", "nintendo", "sony", "xbox", "playstation", "wii", "gameboy",
    "microsoft", "google", "apple", "amazon", "facebook", "intel", "ibm", "linux", "windows", "browser", "browsers",
    "search", "engine", "email", "online", "blog", "blogs", "wireless", "broadband", "satellite", "satellites",
    "telecom", "nanotech", "nanotechnology", "innovation", "innovative", "scientist", "scientists",
    "telescope", "microscope", "biotech", "biotechnology",
    "fossil", "fuel", "climate", "warming", "environment", "environmental", "pollution", "emission", "emissions", "carbon",
    "shuttle", "probe", "mission", "launch", "launched", "orbit", "orbital"
}

business_keywords = {
    "business", "businesses", "economy", "economies", "economic", "finance", "financial", "market", "markets",
    "stock", "stocks", "share", "shares", "wall", "street", "dow", "jones", "nasdaq",
    "invest", "invests", "investor", "investors", "investment", "investments",
    "profit", "profits", "loss", "losses", "revenue", "revenues", "earnings", "sales",
    "trade", "trading", "deal", "deals", "merger", "mergers", "acquisition", "acquisitions", "buyout",
    "bank", "banks", "banking", "interest", "rate", "rates", "inflation", "tax", "taxes",
    "budget", "deficit", "currency", "currencies", "dollar", "dollars", "euro", "euros", "yen",
    "oil", "gas", "price", "prices", "cost", "costs", "consumer", "consumers", "retail", "retailer", "retailers",
    "corp", "corporation", "corporations", "company", "companies", "firm", "firms", "industry", "industries", "sector", "sectors",
    "ceo", "cfo", "manager", "managers", "management", "executive", "executives",
    "employment", "job", "jobs", "unemployment", "labor", "workforce", "strike", "strikes", "union", "unions",
    "wto", "imf", "fed", "federal", "reserve", "treasury", "growth", "recession", "bankruptcy", "dividend", "dividends",
    "shareholder", "shareholders", "quarter", "quarterly", "estimate", "estimates", "shop", "shops", "store", "stores"
}

sports_keywords = {
    "sport", "sports", "football", "soccer", "baseball", "basketball", "hockey", "cricket", "rugby",
    "tennis", "golf", "boxing", "racing", "race", "races", "f1", "formula", "nascar", "olympic", "olympics",
    "athlete", "athletes", "player", "players", "team", "teams", "coach", "coaches", "manager", "managers",
    "club", "clubs", "league", "leagues", "tournament", "tournaments", "championship", "championships",
    "cup", "cups", "medal", "medals", "gold", "silver", "bronze",
    "score", "scores", "scored", "scoring", "goal", "goals", "touchdown", "homerun", "basket", "point", "points",
    "win", "wins", "won", "winning", "winner", "winners", "lose", "loses", "lost", "loss", "losses", "defeat", "defeats", "defeated",
    "draw", "draws", "match", "matches", "game", "games", "season", "seasons", "playoff", "playoffs", "final", "finals", "semifinal", "semifinals", "quarterfinal", "quarterfinals",
    "stadium", "arena", "fan", "fans", "supporter", "supporters",
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "premier", "world", "super", "bowl",
    "quarterback", "receiver", "pitcher", "striker", "goalkeeper", "umpire", "referee",
    "wimbledon", "masters", "tour", "broncos", "red", "sox", "yankees", "mets", "lakers", "bulls", "knicks",
    "set", "sets"
}

world_keywords = {
    "world", "international", "global", "nation", "nations", "country", "countries", "state", "states",
    "government", "governments", "politics", "political", "politician", "politicians",
    "president", "presidents", "prime", "minister", "ministers", "senate", "congress", "parliament",
    "election", "elections", "vote", "votes", "voting", "voter", "voters", "campaign", "campaigns",
    "party", "parties", "democrat", "democrats", "republican", "republicans", "conservative", "liberal",
    "socialist", "communist", "dictator", "regime", "leader", "leaders", "official", "officials",
    "diplomat", "diplomats", "ambassador", "treaty", "summit", "conference",
    "war", "wars", "peace", "conflict", "conflicts", "fight", "fighting", "battle", "battles",
    "army", "armies", "military", "soldier", "soldiers", "troop", "troops", "navy", "air", "force",
    "weapon", "weapons", "bomb", "bombs", "bombing", "blast", "blasts", "explosion", "explosions",
    "attack", "attacks", "attacked", "kill", "kills", "killed", "killing", "dead", "death", "deaths",
    "terror", "terrorism", "terrorist", "terrorists", "al", "qaeda",
    "iraq", "iraqi", "iran", "iranian", "afghanistan", "afghan", "israel", "israeli", "israelis", "palestine", "palestinian", "palestinians",
    "syria", "syrian", "russia", "russian", "china", "chinese", "usa", "us", "uk", "british", "france", "french", "germany", "german",
    "un", "united", "nations", "eu", "european", "union", "nato",
    "police", "crime", "criminal", "court", "courts", "law", "laws", "legal", "judge", "judges", "justice", "prison",
    "protest", "protests", "riot", "riots", "demonstration", "demonstrations",
    "disaster", "earthquake", "tsunami", "flood", "floods", "hurricane", "hurricanes", "storm", "storms",
    "famine", "refugee", "refugees", "human", "rights", "foreign", "policy", "korea", "korean",
    "curfew", "capital", "authority", "authorities", "hostage", "hostages", "kidnap"
}

def categorize(title, description):
    text = (title + " " + description).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    
    scores = {
        "Science/Technology": 0,
        "Business": 0,
        "Sports": 0,
        "World": 0
    }
    
    for word in words:
        if word in scitech_keywords: scores["Science/Technology"] += 1
        if word in business_keywords: scores["Business"] += 1
        if word in sports_keywords: scores["Sports"] += 1
        if word in world_keywords: scores["World"] += 1
    
    # Heuristics
    if "game" in words or "games" in words:
        tech_context = any(w in words for w in ["video", "console", "nintendo", "xbox", "ps2", "ps3", "computer", "software", "online", "gameboy", "mini", "micro", "innovation", "innovative"])
        sports_context = any(w in words for w in ["team", "coach", "league", "cup", "score", "win", "season", "football", "baseball", "broncos", "red", "sox", "final", "olympic", "gold"])
        if tech_context:
            scores["Science/Technology"] += 3
        if sports_context and not tech_context:
            scores["Sports"] += 3

    tech_companies = ["microsoft", "google", "apple", "intel", "ibm", "sony", "dell", "cisco", "oracle", "yahoo", "ebay", "amazon"]
    if any(w in words for w in tech_companies):
        if any(w in words for w in ["stock", "market", "share", "profit", "revenue", "quarter", "earnings", "estimate", "estimates"]):
            scores["Business"] += 3
        else:
            scores["Science/Technology"] += 1
            
    if "oil" in words and ("price" in words or "prices" in words):
        scores["Business"] += 3

    # Default to World if scores are low/zero? 
    # Or find Max.
    best_cat = max(scores, key=scores.get)
    
    # Disambiguate ties
    # If SciTech is max (or tied for max), and it has a decent score (e.g. >0), prefer it?
    # Wait, if SciTech=1, World=1. "Quest to Rebuild... Science". Science(1). World(1-Iraq).
    # Ideally SciTech.
    # "Israelis to Expand West Bank Settlements". World=Many. SciTech=0.
    
    # If all 0, return World.
    if all(s == 0 for s in scores.values()):
        return "World"

    return best_cat

count_scitech = 0
unique_articles = []
processed_ids = set()
for a in articles:
    if a['article_id'] not in processed_ids:
        unique_articles.append(a)
        processed_ids.add(a['article_id'])

results = []

for article in unique_articles:
    cat = categorize(article.get('title', ''), article.get('description', ''))
    if cat == "Science/Technology":
        count_scitech += 1
    results.append({"id": article.get("article_id"), "title": article.get("title"), "cat": cat})

total = len(unique_articles)
fraction = count_scitech / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "scitech_count": count_scitech,
    "fraction": fraction,
    "sample_results": results[:20]
}))"""

env_args = {'var_function-call-4900156496155206436': [{'author_id': '218'}], 'var_function-call-12198714421739599460': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15666126011967161689': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-16647193750153873959': [{'_id': '6944b9dddb8150d8433ea0cf', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b9dddb8150d8433ea880', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b9dddb8150d8433eab2b', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b9dddb8150d8433eabba', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b9dddb8150d8433ead8a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-6642870725842964935': {'total': 5, 'scitech_count': 2, 'fraction': 0.4, 'sample_results': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'cat': 'Sports'}, {'id': '2161', 'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Science/Technology'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'cat': 'World'}]}, 'var_function-call-7914346055210354139': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966'], 'var_function-call-8233641910163502347': [], 'var_function-call-12077939091008176646': [{'_id': '6944b9dddb8150d8433ea00f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944b9dddb8150d8433ea010', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944b9dddb8150d8433ea011', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944b9dddb8150d8433ea012', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944b9dddb8150d8433ea013', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6944b9dddb8150d8433ea014', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6944b9dddb8150d8433ea015', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6944b9dddb8150d8433ea016', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6944b9dddb8150d8433ea017', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6944b9dddb8150d8433ea018', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-14588557736139879700': [{'_id': '6944b9dddb8150d8433ea880', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}], 'var_function-call-10609120748234142351': 'file_storage/function-call-10609120748234142351.json', 'var_function-call-15969782137158893164': {'total': 111, 'scitech_count': 29, 'fraction': 0.26126126126126126, 'sample_results': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'cat': 'Science/Technology'}, {'id': '2161', 'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Science/Technology'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'cat': 'World'}, {'id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'Business'}, {'id': '4447', 'title': 'Even in win, nasty vibes', 'cat': 'Sports'}, {'id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'Business'}, {'id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'id': '6869', 'title': 'Somalians sworn in', 'cat': 'World'}, {'id': '8962', 'title': 'Muenzer races for gold', 'cat': 'Sports'}, {'id': '9677', 'title': 'Israelis to Expand West Bank Settlements', 'cat': 'World'}, {'id': '9858', 'title': 'Stocks End Up as Oil Prices Fall', 'cat': 'Business'}, {'id': '14861', 'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'cat': 'Business'}, {'id': '15100', 'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'cat': 'World'}, {'id': '15473', 'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'cat': 'Science/Technology'}, {'id': '17491', 'title': 'UPDATE: Intel lowers Q3 revenue estimates', 'cat': 'Business'}, {'id': '19469', 'title': 'Calm as Kathmandu curfew lifted', 'cat': 'Science/Technology'}, {'id': '20362', 'title': 'Israeli Missiles Kill 13 Militants', 'cat': 'Science/Technology'}, {'id': '21238', 'title': 'Serena Blasts Umpire After Dramatic Defeat', 'cat': 'Sports'}]}}

exec(code, env_args)
