code = """import json
import re

# Load the articles
file_path = locals()['var_function-call-5424179638557031609']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Re-use keywords and logic
keywords = {
    "Sports": {
        "strong": [
            "olympics", "olympic", "paralympic", "athlete", "stadium", "medal", "gold medal", 
            "silver medal", "bronze medal", "football", "soccer", "basketball", "baseball", 
            "tennis", "golf", "hockey", "cricket", "rugby", "volleyball", "badminton", 
            "swimming", "gymnastics", "marathon", "triathlon", "wrestling", "boxing", 
            "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "wta", "atp", "pga", "lpga", "nascar", 
            "f1", "formula 1", "formula one", "grand prix", "tour de france", "wimbledon", 
            "us open", "french open", "australian open", "davis cup", "ryder cup", "super bowl", 
            "world series", "stanley cup", "world cup", "euro 2004", "athens 2004", "games 2004",
            "red sox", "yankees", "lakers", "pistons", "spurs", "heat", "knicks", "celtics", 
            "cowboys", "patriots", "eagles", "packers", "giants", "jets", "raiders", "49ers", 
            "real madrid", "barcelona", "manchester united", "arsenal", "liverpool", "chelsea", 
            "ac milan", "inter milan", "juventus", "bayern munich", "referee", "umpire", 
            "quarterback", "touchdown", "homerun", "inning", "pitcher", "goalkeeper", "striker", 
            "midfielder", "defender", "doping", "drug test", "dream team"
        ],
        "weak": [
            "sport", "sports", "game", "games", "match", "tournament", "championship", "champion", 
            "league", "cup", "team", "coach", "manager", "player", "score", "victory", "defeat", 
            "win", "winner", "loser", "playoff", "final", "semi-final", "quarter-final", "race", 
            "racing", "sprint", "relay", "basket", "goal", "field"
        ]
    },
    "Business": {
        "strong": [
            "stock", "stocks", "market", "markets", "economy", "economic", "business", "corporate", 
            "corporation", "company", "companies", "inc", "ltd", "plc", "profit", "profits", 
            "earnings", "revenue", "loss", "losses", "share", "shares", "shareholder", "investor", 
            "investment", "bank", "banking", "finance", "financial", "wall street", "dow jones", 
            "nasdaq", "s&p", "ftse", "nikkei", "dollar", "euro", "yen", "currency", "inflation", 
            "rate", "rates", "fed", "federal reserve", "greenspan", "treasury", "bond", "oil", 
            "crude", "barrel", "opec", "gas", "energy", "prices", "price", "ceo", "cfo", "merger", 
            "acquisition", "deal", "takeover", "bid", "ipo", "bankruptcy", "audit", "accounting", 
            "retail", "sales", "consumer", "spending", "wal-mart", "mcdonald's", "coca-cola", 
            "general motors", "ford", "toyota", "boeing", "airbus", "delta", "airline", "trade", 
            "deficit", "surplus", "tariff", "wto", "imf", "world bank", "job", "jobs", "unemployment"
        ],
        "weak": [
            "money", "cash", "cost", "pay", "plan", "strategy", "growth", "cut", "rise", "fall", 
            "drop", "high", "low", "record", "report", "firm", "industry", "sector"
        ]
    },
    "Sci/Tech": {
        "strong": [
            "technology", "tech", "science", "scientific", "computer", "computers", "software", 
            "hardware", "internet", "web", "website", "online", "digital", "network", "server", 
            "data", "database", "cyber", "virus", "hacker", "security", "microsoft", "windows", 
            "linux", "unix", "apple", "mac", "macintosh", "google", "search engine", "yahoo", 
            "amazon", "ebay", "intel", "amd", "ibm", "hp", "dell", "cisco", "oracle", "java", 
            "broadband", "wireless", "wifi", "mobile", "phone", "cellphone", "smartphone", "nokia", 
            "motorola", "samsung", "sony", "nintendo", "xbox", "playstation", "video game", "gaming", 
            "space", "nasa", "astronomy", "planet", "mars", "moon", "orbit", "satellite", "rocket", 
            "robot", "robotics", "ai", "artificial intelligence", "biotech", "biology", "genome", 
            "dna", "gene", "research", "study", "laboratory", "scientist", "researcher", "discovery", 
            "invention", "innovation", "patent", "browser", "explorer", "firefox", "mozilla", "spam"
        ],
        "weak": [
            "system", "program", "code", "app", "application", "device", "tool", "user", "monitor", 
            "screen", "chip", "memory", "disk", "drive", "file", "link", "click", "download", 
            "upload", "update", "version", "beta", "launch"
        ]
    },
    "World": {
        "strong": [
            "world", "international", "politics", "political", "government", "president", "bush", 
            "kerry", "clinton", "putin", "chirac", "schroeder", "blair", "prime minister", "minister", 
            "parliament", "congress", "senate", "election", "vote", "voter", "campaign", "candidate", 
            "party", "democrat", "republican", "labour", "conservative", "war", "peace", "treaty", 
            "ceasefire", "military", "army", "navy", "air force", "troops", "soldiers", "guerrilla", 
            "rebel", "insurgent", "terror", "terrorism", "terrorist", "al qaeda", "bin laden", "iraq", 
            "baghdad", "afghanistan", "kabul", "iran", "tehran", "israel", "palestine", "gaza", 
            "jerusalem", "syria", "lebanon", "egypt", "sudan", "darfur", "africa", "asia", "europe", 
            "russia", "china", "japan", "korea", "india", "pakistan", "nuclear", "weapon", "bomb", 
            "blast", "explosion", "attack", "suicide bomber", "hostage", "kidnap", "united nations", 
            "un", "security council", "diplomat", "ambassador", "embassy", "foreign", "policy"
        ],
        "weak": [
            "country", "nation", "state", "city", "region", "border", "law", "court", "judge", 
            "police", "arrest", "kill", "dead", "death", "wound", "injure", "crash", "disaster", 
            "storm", "hurricane", "flood", "earthquake"
        ]
    }
}

def score_text(text, cat_keywords):
    score = 0
    text_tokens = set(re.split(r'[^a-z0-9]+', text.lower()))
    
    for kw in cat_keywords["strong"]:
        if " " in kw:
            if kw in text.lower():
                score += 3
        else:
            if kw in text_tokens:
                score += 3
    for kw in cat_keywords["weak"]:
        if " " in kw:
            if kw in text.lower():
                score += 1
        else:
            if kw in text_tokens:
                score += 1
    return score

candidates = []
for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    full_text = title + " " + desc
    
    scores = {}
    for cat in keywords:
        scores[cat] = score_text(full_text, keywords[cat])
    
    max_s = max(scores.values())
    if max_s > 0:
        best_cats = [cat for cat, s in scores.items() if s == max_s]
        if len(best_cats) == 1 and best_cats[0] == "Sports":
            candidates.append(art)

# Sort by description length
candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

top_candidates = candidates[:5]
# Create a serializable result
result_list = []
for c in top_candidates:
    result_list.append({
        "title": c['title'],
        "description": c['description'],
        "length": len(c['description'])
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-4105202590194221422': ['articles'], 'var_function-call-4105202590194223563': ['authors', 'article_metadata'], 'var_function-call-17850915415032394466': [{'_id': '69447340826b7850ce02734f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-17850915415032395251': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-4116783351500848285': [{'_id': '69447340826b7850ce02734f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447340826b7850ce027350', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447340826b7850ce027351', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447340826b7850ce027352', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447340826b7850ce027353', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12552155713391860353': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_function-call-11673459665629763925': [{'_id': '69447340826b7850ce02734f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447340826b7850ce027350', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447340826b7850ce027351', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447340826b7850ce027352', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447340826b7850ce027353', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17308268192770250264': 'file_storage/function-call-17308268192770250264.json', 'var_function-call-5424179638557031609': 'file_storage/function-call-5424179638557031609.json', 'var_function-call-3377846123651307841': {'title': 'Microsoft, IE and Bloat', 'description_length': 708, 'description': '\\\\Zawodny  threads off of Scoble  on the IE issue:\\\\"I have to say, when I first read that I nearly fell off my chair laughing. I was\\thinking "how stupid ARE these IE guys?!?!?!" But we all know that Microsoft is\\full of smart people who care about what they\'re doing. So something really\\doesn\'t compute here."\\\\"Last time I checked, IE wasn\'t even close to feature parity with Mozilla\'s\\browsers. No popup blocking, no tabbed browsing, etc."\\\\"Does the IE team really not know what their product is missing?"\\\\Perhaps.  It\'s highly likely that they just don\'t know.\\\\The bigger issue here is that Microsoft products can\'t fail and they can\'t\\succeed.  Microsoft has 40-50 billion in the bank.  There ...\\\\'}, 'var_function-call-15052254020291569735': {'title': 'THECHAT', 'description_length': 631}}

exec(code, env_args)
