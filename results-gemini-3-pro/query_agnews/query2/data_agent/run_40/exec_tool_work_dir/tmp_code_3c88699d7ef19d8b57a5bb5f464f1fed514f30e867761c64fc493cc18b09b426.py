code = """import json
import re

# Load the articles
with open(locals()['var_function-call-9867695846899870663'], 'r') as f:
    articles = json.load(f)

# Define keywords
categories = {
    "Science/Technology": [
        "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", 
        "cyber", "digital", "wireless", "mobile", "phone", "gadget", "robot", "space", "nasa", "mars", 
        "astronomy", "physics", "biology", "chemistry", "genome", "research", "lab", "scientist", 
        "innovation", "innovative", "silicon", "google", "microsoft", "apple", "intel", "ibm", "linux", 
        "windows", "virus", "spam", "hacker", "browser", "broadband", "network", "telecom", 
        "video game", "gaming", "nintendo", "sony", "xbox", "playstation", "console", "ipod", "mp3", 
        "dvd", "gps", "satellite", "engine", "machine", "device", "app", "blog", "search engine",
        "gameboy", "micro-game", "gyro-gen", "electricity", "ocean waves", "biotech", "spam", "net",
        "firefox", "explorer", "server", "chip", "semiconductor", "laser", "nanotech", "cloning", "stem cell",
        "probe", "capsule", "sun", "samples"
    ],
    "Sports": [
        "sport", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", 
        "rugby", "athlete", "player", "coach", "team", "stadium", "league", "tournament", "championship", 
        "olympic", "medal", "race", "racing", "f1", "nascar", "driver", "score", "goal", "touchdown", 
        "run", "wicket", "inning", "quarter", "match", "win", "loss", "victory", "defeat", "cup", 
        "season", "club", "nfl", "nba", "mlb", "nhl", "pro bowl", "cornerback", "receiver", "broncos",
        "red sox", "yankees", "lakers", "bulls", "united", "city", "real madrid", "barcelona", "chelsea",
        "arsenal", "liverpool", "juventus", "milan", "inter", "bayern", "dortmund", "psg", "ajax",
        "davis cup", "wimbledon", "open", "masters", "world cup", "super bowl", "world series", "stanley cup",
        "boxing", "fighter", "round", "knockout", "marathon", "sprint", "cycling", "cyclist", "gold", "silver", "bronze"
    ],
    "Business": [
        "business", "economy", "economic", "market", "stock", "share", "trade", "finance", "financial", 
        "bank", "banking", "invest", "investment", "investor", "money", "dollar", "euro", "currency", 
        "profit", "revenue", "earning", "loss", "debt", "bankrupt", "merger", "acquisition", "deal", 
        "contract", "ceo", "cfo", "executive", "company", "corporation", "firm", "industry", "sector", 
        "price", "cost", "rate", "inflation", "tax", "budget", "wall street", "dow jones", "nasdaq", 
        "oil", "gas", "energy", "retail", "sales", "mining", "commodity", "bhp", "billiton", "yukos", 
        "gazprom", "airline", "airbus", "boeing", "ford", "gm", "toyota", "honda", "nissan", "vw",
        "oracle", "people soft", "bid", "hostile", "takeover", "shareholder", "product sales", "quarter", "q1", "q2", "q3", "q4"
    ],
    "World": [
        "world", "international", "nation", "country", "government", "politics", "political", "president", 
        "minister", "leader", "official", "diplomat", "war", "peace", "conflict", "military", "army", 
        "soldier", "troop", "police", "attack", "bomb", "blast", "kill", "death", "died", "victim", 
        "disaster", "earthquake", "flood", "storm", "hurricane", "tsunami", "election", "vote", "poll", 
        "campaign", "party", "democrat", "republican", "parliament", "congress", "senate", "law", 
        "court", "judge", "trial", "prison", "right", "un", "united nations", "eu", "nato", "iraq", 
        "iran", "afghanistan", "israel", "palestine", "syria", "russia", "china", "korea", "nuclear", 
        "weapon", "terror", "terrorism", "al qaeda", "bin laden", "bush", "putin", "blair", "chirac",
        "arafat", "sharon", "kofi annan", "powell", "rice", "rumsfeld", "baghdad", "fallujah", "gaza",
        "settlement", "occupied", "territory", "sworn in", "mediator", "parliament", "prime minister"
    ]
}

def classify(title, desc):
    # Preprocessing
    text = (str(title) + " " + str(desc)).lower()
    text = re.sub(r'[^a-z0-9]', ' ', text)
    
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for kw in keywords:
            # Word boundary check
            # Handle multi-word keywords
            if " " in kw:
                if kw in text:
                    scores[cat] += 1
            else:
                if kw in text.split(): # Exact word match
                    scores[cat] += 1
    
    # Specific Boosts
    # Boost Business for financial terms
    if any(w in text.split() for w in ["profit", "revenue", "earning", "stock", "share", "market", "economy", "investment", "investor"]):
        scores["Business"] += 2

    # Boost Sports for league/match terms
    if any(w in text.split() for w in ["nfl", "nba", "mlb", "nhl", "football", "soccer", "tennis", "olympic", "championship", "tournament", "medal", "gold"]):
        scores["Sports"] += 2
        
    # Boost World for conflict/political terms
    if any(w in text.split() for w in ["war", "president", "minister", "election", "bomb", "attack", "killed", "dead", "peace", "iraq", "gaza"]):
        scores["World"] += 2

    # Boost Tech for strong tech terms
    if any(w in text.split() for w in ["science", "software", "internet", "browser", "nasa", "space", "robot", "linux", "microsoft", "google"]):
        scores["Science/Technology"] += 2

    # Disambiguation
    # "Win": common in Sports and Tech (awards).
    # "Game": "Video game" (Tech) vs "Game" (Sports).
    if "game" in text:
        if any(w in text for w in ["video", "console", "nintendo", "sony", "xbox", "boy", "micro"]):
            scores["Science/Technology"] += 3
        elif any(w in text for w in ["match", "league", "cup", "season", "score", "coach"]):
            scores["Sports"] += 3

    # Tie-breaking logic:
    # If Business and Tech have high scores, check if it's financial news about tech (Business) or product news (Tech).
    # If "revenue", "profit", "stock" present -> likely Business.
    if scores["Business"] >= 1 and scores["Science/Technology"] >= 1:
        if any(w in text for w in ["revenue", "profit", "stock", "share", "market", "estimate", "drop", "rise"]):
             scores["Business"] += 2 # Push towards Business
        elif any(w in text for w in ["unveil", "launch", "release", "new", "feature"]):
             scores["Science/Technology"] += 1

    # Return category with max score
    if sum(scores.values()) == 0:
        return "Unclassified"
    
    return max(scores, key=scores.get)

results = []
for art in articles:
    cat = classify(art.get('title', ''), art.get('description', ''))
    results.append({"title": art.get('title'), "category": cat})

# Count
total = len(results)
scitech_count = sum(1 for r in results if r['category'] == "Science/Technology")

print("__RESULT__:")
print(json.dumps({"total": total, "scitech_count": scitech_count, "fraction": scitech_count/total if total else 0, "details": results}))"""

env_args = {'var_function-call-14802185822981372221': [{'author_id': '218'}], 'var_function-call-14553611907080601669': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15828535751467272093': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'title': 1, 'description': 1, 'article_id': 1, '_id': 0}}, 'var_function-call-8677478758674628797': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-6582939166409369247': {'total': 5, 'scitech_count': 1, 'fraction': 0.2, 'details': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Unclassified'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Unclassified'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Unclassified'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Unclassified'}]}, 'var_function-call-9867695846899870663': 'file_storage/function-call-9867695846899870663.json'}

exec(code, env_args)
