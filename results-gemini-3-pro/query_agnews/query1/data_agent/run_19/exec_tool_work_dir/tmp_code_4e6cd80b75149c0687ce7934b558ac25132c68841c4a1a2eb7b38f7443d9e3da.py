code = """import json

file_path = locals()['var_function-call-2872394427068068909']
with open(file_path, 'r') as f:
    data = json.load(f)

# Keyword lists
categories = {
    "Sports": ["sport", "football", "soccer", "basketball", "baseball", "tennis", "golf", "olympic", "game", "match", "team", "league", "cup", "tournament", "coach", "player", "victory", "defeat", "score", "medal", "athlete", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "racing", "f1", "formula one", "cricket", "rugby", "boxing", "wrestling", "athletics", "swimming", "championship", "stadium", "club", "manager", "driver", "gold", "silver", "bronze", "record", "season", "playoff", "world cup", "super bowl", "grand slam", "open", "tour", "touchdown", "homerun", "basket", "inning", "quarter", "referee", "umpire", "podium", "marathon", "sprint", "relay", "volleyball", "hockey", "skating", "skiing", "snowboard", "cyclist", "rider", "jockey", "derby", "red sox", "yankees", "lakers", "bulls", "knicks", "cowboys", "patriots", "steelers", "arsenal", "manchester", "liverpool", "chelsea", "real madrid", "barcelona", "milan", "juventus", "bayern", "ferrari", "williams", "mclaren", "pga", "atp", "wta", "davis cup", "fed cup"],
    "Business": ["stock", "market", "wall street", "economy", "oil", "price", "company", "corp", "profit", "loss", "share", "trade", "dollar", "euro", "yen", "bank", "finance", "invest", "fund", "money", "deal", "merge", "acquire", "buy", "sell", "retail", "sale", "tax", "job", "employment", "unemployment", "inflation", "rate", "fed", "federal reserve", "central bank", "budget", "deficit", "surplus", "ceo", "cfo", "manager", "executive", "business", "industry", "sector", "growth", "recession", "depression", "crisis", "forecast", "outlook", "earnings", "revenue", "cost", "expense", "production", "output", "demand", "supply", "inventory", "export", "import", "tariff", "subsidy", "wto", "imf", "world bank", "nasdaq", "dow", "s&p", "ftse", "nikkei", "hang seng", "airline", "manufacturer", "telecom", "energy", "utility", "bond", "treasury", "currency", "exchange", "audit", "accounting", "bankrupt", "debt", "loan", "credit", "mortgage", "insurance"],
    "Sci/Tech": ["technology", "science", "computer", "internet", "web", "software", "hardware", "chip", "processor", "server", "network", "wireless", "mobile", "phone", "app", "application", "program", "code", "data", "database", "security", "virus", "hacker", "spam", "email", "search", "engine", "google", "microsoft", "apple", "intel", "ibm", "hp", "dell", "oracle", "cisco", "facebook", "twitter", "amazon", "ebay", "yahoo", "nasa", "space", "shuttle", "station", "mars", "moon", "planet", "star", "galaxy", "universe", "physics", "chemistry", "biology", "genetics", "dna", "cell", "stem", "clone", "drug", "medicine", "health", "disease", "cancer", "aids", "hiv", "virus", "bacteria", "study", "research", "experiment", "lab", "scientist", "discovery", "invention", "innovation", "patent", "digital", "online", "browser", "linux", "windows", "java", "api", "robot", "machine", "device", "screen", "display", "battery", "power", "energy", "vehicle", "auto", "satellite", "launch", "rocket", "astronomy", "telescope", "biotech", "nano", "genomics", "log", "blog", "post", "comment", "forum", "chat", "message", "text", "video", "audio", "image", "photo", "camera", "music", "movie", "film", "console", "nintendo", "sony", "xbox", "playstation", "wii", "sega", "gamer", "gaming", "broadband", "voip", "wifi", "bluetooth", "gps", "navigation"],
    "World": ["world", "war", "peace", "treaty", "united nations", "un", "president", "minister", "prime minister", "chancellor", "king", "queen", "prince", "princess", "dictator", "leader", "official", "government", "parliament", "congress", "senate", "house", "representative", "democrat", "republican", "party", "vote", "election", "campaign", "candidate", "poll", "survey", "policy", "law", "bill", "act", "court", "judge", "justice", "trial", "verdict", "sentence", "prison", "jail", "police", "army", "navy", "air force", "military", "soldier", "troop", "weapon", "bomb", "missile", "nuclear", "terror", "attack", "blast", "explosion", "kill", "death", "injury", "casualty", "victim", "hostage", "kidnap", "disaster", "earthquake", "flood", "hurricane", "storm", "fire", "accident", "crash", "plane", "train", "car", "bus", "truck", "ship", "boat", "ferry", "bridge", "road", "street", "building", "city", "town", "village", "country", "nation", "state", "province", "region", "border", "territory", "island", "continent", "europe", "asia", "africa", "america", "australia", "antarctica", "middle east", "iraq", "iran", "afghanistan", "israel", "palestine", "syria", "lebanon", "egypt", "libya", "china", "russia", "usa", "uk", "france", "germany", "japan", "india", "pakistan", "korea", "baghdad", "kabul", "jerusalem", "gaza", "beijing", "moscow", "washington", "london", "paris", "berlin", "tokyo", "delhi"]
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for k in keywords:
            # Check for whole words to avoid partial matches like 'car' in 'card'
            # Simple approach: check " k " or start/end
            # But simpler: use count()
            scores[cat] += text.count(k)
            
    # Heuristics for ties or specific cases
    # If "oil" or "stocks" -> Business
    # If "iraq" or "president" -> World
    # If "software" or "internet" -> Sci/Tech
    # If "team" or "game" or "cup" -> Sports (careful with 'game')
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

sports_articles = []
for article in data:
    cat = classify(article.get('title', ''), article.get('description', ''))
    if cat == "Sports":
        sports_articles.append(article)

# Sort by description length descending
sports_articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

print("__RESULT__:")
print(json.dumps({
    "count_sports": len(sports_articles),
    "top_5": sports_articles[:5]
}))"""

env_args = {'var_function-call-10984581093047168517': [{'_id': '694471bab67b1ebe4e141d39', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-13809299225851108434': [{'_id': '694471bab67b1ebe4e141d39', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694471bab67b1ebe4e141d3a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694471bab67b1ebe4e141d3b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694471bab67b1ebe4e141d3c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694471bab67b1ebe4e141d3d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16901600362174134541': 'file_storage/function-call-16901600362174134541.json', 'var_function-call-14478176964533671910': {'total_records': 10000, 'sports_count': 2358, 'best_title': 'Pretty Log4J', 'best_desc_len': 708, 'best_desc': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\'}, 'var_function-call-2872394427068068909': 'file_storage/function-call-2872394427068068909.json'}

exec(code, env_args)
