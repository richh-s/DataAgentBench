code = """import json
import re

# Load articles
with open(locals()['var_function-call-16150427591355603199'], 'r') as f:
    articles = json.load(f)

# Define keywords
keywords = {
    "Sports": [
        "sport", "sports", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", 
        "olympic", "olympics", "game", "match", "cup", "league", "team", "player", "coach", "champion", 
        "championship", "medal", "score", "win", "won", "winning", "loss", "lost", "victory", "defeat", 
        "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "atp", "wta", "nascar", "f1", "cricket", "rugby", 
        "boxing", "wrestling", "athletics", "marathon", "race", "racing", "stadium", "athlete", 
        "tournament", "doping", "quarterback", "referee", "umpire", "touchdown", "slam", "inning", 
        "red sox", "yankees", "lakers", "bulls", "united", "real madrid", "barcelona", "chelsea", 
        "arsenal", "liverpool", "manchester", "milan", "juventus", "bayern", "tiger woods", "armstrong", 
        "schumacher", "phelps", "serena", "venus", "federer", "roddick", "agassi", "sampras", "kobe", 
        "shaq", "lebron", "jordan", "gretzky", "beckham", "ronaldo", "zidane", "athens", "gold medal", 
        "silver medal", "bronze medal"
    ],
    "Business": [
        "market", "stock", "price", "company", "corp", "inc", "profit", "loss", "economy", "bank", 
        "trade", "dollar", "euro", "oil", "gold", "invest", "share", "revenue", "business", "deal", 
        "merger", "ceo", "cfo", "wall st", "dow jones", "nasdaq", "fed", "inflation", "rate", "tax", 
        "sales", "retail", "industry", "manufacture", "boeing", "airbus", "ford", "gm", "toyota", 
        "honda", "nissan", "ibm", "intel", "amd", "oracle", "sap", "cisco", "dell", "hp", "motorola", 
        "nokia", "samsung", "sony", "panasonic", "toshiba", "hitachi", "siemens", "ge", "pfizer", 
        "merck", "glaxo", "novartis", "roche", "sanofi", "bayer", "basf", "dupont", "dow", "monsanto", 
        "syngenta", "cargill", "adm", "bunge", "dreyfus", "walmart", "target", "costco", "home depot", 
        "lowes", "best buy", "circuit city", "sears", "kmart", "jcpenney", "macys", "nordstrom", "kroger", 
        "safeway", "albertsons", "walgreens", "cvs", "rite aid", "mcdonalds", "burger king", "wendys", 
        "kfc", "pizza hut", "domino", "starbucks", "dunkin", "cocacola", "pepsi", "nestle", "kraft", 
        "unilever", "procter", "gamble", "colgate", "clorox", "kimberly", "clark", "johnson", "gillette", 
        "nike", "adidas", "reebok", "puma", "gap", "limited", "abercrombie", "hollister", "ae", "levis", 
        "wrangler", "lee", "calvin klein", "ralph lauren", "tommy hilfiger", "nautica", "timberland", 
        "columbia", "north face", "patagonia"
    ],
    "Sci/Tech": [
        "technology", "science", "computer", "software", "hardware", "internet", "web", "phone", "mobile", 
        "space", "nasa", "discovery", "research", "study", "virus", "disease", "health", "google", 
        "microsoft", "apple", "chip", "server", "network", "linux", "windows", "broadband", "satellite", 
        "robot", "ai", "biology", "physics", "chemistry", "genetic", "stem cell", "astronomy", "mars", 
        "moon", "planet", "galaxy", "telescope", "hubble", "shuttle", "iss", "soyuz", "rocket", "launch", 
        "orbit", "satellite", "gps", "wireless", "wifi", "bluetooth", "cell", "cellular", "digital", 
        "analog", "pixel", "resolution", "camera", "video", "audio", "mp3", "ipod", "itunes", "napster", 
        "kazaa", "bittorrent", "p2p", "file", "sharing", "copyright", "patent", "trademark", "intellectual", 
        "property", "piracy", "hacker", "virus", "worm", "trojan", "spyware", "adware", "spam", "phishing", 
        "firewall", "encryption", "security", "privacy", "browser", "search", "engine", "portal", "blog", 
        "wiki", "rss", "xml", "html", "java", "php", "perl", "python", "ruby", "c++", "c#", ".net", "j2ee", 
        "linux", "unix", "bsd", "osx", "xp", "vista", "longhorn"
    ],
    "World": [
        "war", "peace", "president", "minister", "government", "election", "country", "un", "iraq", "iran", 
        "china", "usa", "uk", "eu", "police", "attack", "bomb", "killed", "dead", "protest", "treaty", 
        "military", "army", "soldier", "rebel", "crisis", "hostage", "parliament", "senate", "court", 
        "law", "justice", "crime", "prison", "tornado", "hurricane", "earthquake", "tsunami", "flood", 
        "fire", "storm", "disaster", "aid", "refugee", "rights", "human", "nuke", "nuclear", "weapon", 
        "terror", "terrorist", "qaeda", "bin laden", "bush", "kerry", "blair", "chirac", "schroeder", 
        "putin", "sharon", "arafat", "abbas", "khatami", "kim jong il", "castro", "chavez", "lula", 
        "fox", "arroyo", "megawati", "howard", "clark", "martin", "berlusconi", "zapatero", "erdogan", 
        "karzai", "allawi", "sadr", "sistani", "fallujah", "najaf", "baghdad", "kabul", "gaza", "west bank", 
        "jerusalem", "tel aviv", "tehran", "riyadh", "damascus", "beirut", "cairo", "tripoli", "khartoum", 
        "darfur", "congo", "rwanda", "uganda", "kenya", "nigeria", "somalia", "afghanistan", "pakistan", 
        "india", "kashmir", "sri lanka", "nepal", "bangladesh", "burma", "thailand", "indonesia", 
        "philippines", "malaysia", "singapore", "vietnam", "korea", "japan", "taiwan", "hong kong", 
        "russia", "chechnya", "ukraine", "belarus", "georgia", "armenia", "azerbaijan", "turkey", "cyprus", 
        "greece", "balkans", "serbia", "bosnia", "kosovo", "croatia", "slovenia", "macedonia", "albania", 
        "bulgaria", "romania", "hungary", "poland", "czech", "slovakia", "austria", "germany", "france", 
        "italy", "spain", "portugal", "britain", "ireland", "scotland", "wales", "sweden", "norway", 
        "finland", "denmark", "netherlands", "belgium", "luxembourg", "switzerland", "vatican", "canada", 
        "mexico", "brazil", "argentina", "chile", "colombia", "venezuela", "peru", "bolivia", "ecuador", 
        "panama", "cuba", "haiti", "dominican", "jamaica", "trinidad", "australia", "zealand"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            # Simple substring match might be too aggressive, but let's try token matching
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Heuristic adjustments
    if "oil" in text and "price" in text:
        scores["Business"] += 2
    if "game" in text and "video" in text:
        scores["Sci/Tech"] += 2
    if "iraq" in text and "war" in text:
        scores["World"] += 2
    
    # Get max
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return None # Unclassified
    return best_cat

sports_articles = []
for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).replace("\\", "")
    cat = classify(text)
    if cat == "Sports":
        sports_articles.append(art)

# Find max description length
max_len = -1
best_article = None

for art in sports_articles:
    desc = art.get('description', '')
    if len(desc) > max_len:
        max_len = len(desc)
        best_article = art

print("__RESULT__:")
if best_article:
    print(json.dumps({"title": best_article['title'], "len": max_len, "description": best_article['description']}))
else:
    print(json.dumps({"error": "No sports articles found"}))"""

env_args = {'var_function-call-16506696001246171495': ['articles'], 'var_function-call-16238021228284893753': [{'_id': '6944729e341d2706dd78f649', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-12806958727600017459': ['authors', 'article_metadata'], 'var_function-call-6156227315711757339': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-14223567582029322341': [{'_id': '6944729e341d2706dd78f649', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944729e341d2706dd78f64a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944729e341d2706dd78f64b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944729e341d2706dd78f64c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944729e341d2706dd78f64d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16150427591355603199': 'file_storage/function-call-16150427591355603199.json'}

exec(code, env_args)
