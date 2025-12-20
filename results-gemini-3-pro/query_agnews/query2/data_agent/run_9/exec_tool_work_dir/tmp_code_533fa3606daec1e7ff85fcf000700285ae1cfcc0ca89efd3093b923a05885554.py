code = """import json
import re

# Load articles
articles = locals()['var_function-call-9476915159118176490']

# Define keywords
categories = {
    "Science/Technology": [
        "science", "technology", "tech", "computer", "computing", "software", "hardware", 
        "internet", "web", "online", "cyber", "digital", "mobile", "wireless", "network", 
        "telecom", "satellite", "space", "nasa", "astronomy", "universe", "galaxy", "planet", 
        "mars", "moon", "robot", "robotics", "artificial intelligence", "ai", "machine learning", 
        "gadget", "device", "electronic", "silicon", "chip", "semiconductor", "processor", 
        "intel", "amd", "microsoft", "apple", "google", "ibm", "linux", "windows", "mac", 
        "os", "browser", "search engine", "virus", "malware", "hacker", "security", "encryption", 
        "biotech", "biology", "genome", "dna", "gene", "clone", "stem cell", "physics", 
        "chemistry", "research", "lab", "laboratory", "scientist", "innovation", "invention", 
        "patent", "gaming", "gameboy", "nintendo", "sony", "xbox", "playstation", "wii", 
        "ipod", "iphone", "smartphone", "app", "blog", "social media", "facebook", "twitter", 
        "youtube", "video game", "data", "server", "broadband", "firefox", "explorer", "netscape",
        "spam", "spyware", "phishing", "trojan", "worm", "botnet", "firewall", "antivirus",
        "router", "modem", "wifi", "bluetooth", "gps", "lcd", "plasma", "hdtv", "dvd", "mp3",
        "nanotech", "supercomputer", "pixel", "resolution", "download", "upload", "streaming",
        "voip", "skype", "podcast", "wiki", "wikipedia"
    ],
    "Sports": [
        "sport", "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", 
        "hockey", "rugby", "racing", "f1", "nascar", "olympic", "athlete", "player", "team", 
        "coach", "manager", "stadium", "match", "tournament", "championship", "league", "cup", 
        "medal", "score", "win", "loss", "victory", "defeat", "nfl", "nba", "mlb", "nhl", 
        "fifa", "uefa", "club", "squad", "roster", "referee", "umpire", "quarterback", 
        "touchdown", "goal", "striker", "midfielder", "defender", "goalkeeper", "pitcher", 
        "batter", "inning", "homerun", "slam", "dunk", "basket", "race", "driver", "lap", 
        "circuit", "track", "field", "court", "gymnast", "swimmer", "medal", "gold", "silver", 
        "bronze", "record", "world cup", "super bowl", "series", "playoff", "final", "semi-final"
    ],
    "Business": [
        "business", "company", "corporation", "inc", "ltd", "market", "stock", "share", "trade", 
        "exchange", "economy", "economic", "finance", "financial", "bank", "invest", "investment", 
        "investor", "money", "dollar", "euro", "yen", "currency", "profit", "loss", "revenue", 
        "earnings", "dividend", "sale", "sales", "merger", "acquisition", "deal", "contract", 
        "ceo", "cfo", "executive", "manager", "chairman", "industry", "sector", "production", 
        "manufacture", "retail", "consumer", "customer", "price", "cost", "inflation", "tax", 
        "oil", "gas", "energy", "mining", "airline", "auto", "car", "automaker", "boeing", 
        "airbus", "wal-mart", "exxon", "gm", "ford", "toyota", "dow", "nasdaq", "wall street", 
        "fed", "federal reserve", "interest rate", "loan", "debt", "mortgage", "bankruptcy", 
        "ipo", "commodity", "crude", "barrel", "futures", "options", "mutual fund", "hedge fund"
    ],
    "World": [
        "world", "international", "nation", "country", "state", "government", "politics", 
        "political", "politician", "president", "minister", "prime minister", "chancellor", 
        "senate", "congress", "parliament", "legislature", "election", "vote", "voter", 
        "poll", "campaign", "party", "democrat", "republican", "conservative", "liberal", 
        "war", "peace", "conflict", "military", "army", "navy", "air force", "marine", 
        "troop", "soldier", "weapon", "bomb", "blast", "explosion", "attack", "terrorism", 
        "terrorist", "suicide", "insurgent", "rebel", "guerrilla", "al-qaeda", "iraq", 
        "afghanistan", "iran", "syria", "israel", "palestine", "gaza", "lebanon", "korea", 
        "china", "russia", "usa", "uk", "britain", "france", "germany", "europe", "asia", 
        "africa", "latin america", "un", "united nations", "eu", "european union", "nato", 
        "treaty", "diplomacy", "foreign", "policy", "sanction", "crisis", "disaster", 
        "earthquake", "tsunami", "flood", "hurricane", "typhoon", "cyclone", "storm", 
        "volcano", "police", "crime", "criminal", "court", "law", "judge", "justice", 
        "prison", "jail", "arrest", "kidnap", "hostage", "protest", "demonstration", "strike"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for keyword in keywords:
            # Check for whole word matches to avoid partial matches like 'os' in 'cost'
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                scores[cat] += 1
                
    # Tie breaking and special cases
    # If "game" is present, it counts for Sports and Tech (via video game). 
    # But my list has "video game" separately. 
    # If scores are all 0, default to World? Or Unknown.
    
    # Return category with max score
    if sum(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

# Calculate
total_articles = len(articles)
scitech_count = 0

matched_articles = []

for article in articles:
    # Combine title and description
    content = article.get('title', '') + " " + article.get('description', '')
    category = classify(content)
    if category == "Science/Technology":
        scitech_count += 1
        matched_articles.append(article['title'])

fraction = scitech_count / total_articles if total_articles > 0 else 0

result = {
    "total_articles": total_articles,
    "scitech_count": scitech_count,
    "fraction": fraction,
    "matched_titles": matched_articles
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11433653939230441729': [{'author_id': '218'}], 'var_function-call-2165630416878048107': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-5222953381905483758': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-9476915159118176490': [{'_id': '6944950dcee3e8d7112f6e4f', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944950dcee3e8d7112f7600', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944950dcee3e8d7112f78ab', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944950dcee3e8d7112f793a', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944950dcee3e8d7112f7b0a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
