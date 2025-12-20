code = """import json
import collections

# Load the data
with open(locals()['var_function-call-6947491916061976961'], 'r') as f:
    articles = json.load(f)

# Keywords
sports_keywords = {
    "sport", "sports", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "rugby",
    "olympic", "olympics", "athens", "medal", "gold", "silver", "bronze", "game", "games", "match", "tournament",
    "championship", "league", "cup", "world cup", "team", "squad", "club", "coach", "manager", "player", "athlete",
    "win", "won", "winner", "lose", "lost", "loser", "draw", "score", "goal", "touchdown", "homerun", "wickets",
    "inning", "run", "points", "race", "racing", "f1", "formula one", "nascar", "driver", "grand prix", "track",
    "field", "marathon", "sprint", "relay", "swim", "swimming", "gymnastics", "boxing", "wrestling", "doping",
    "drug", "record", "champion", "final", "semifinal", "quarterfinal", "stadium", "arena", "nfl", "nba", "mlb",
    "nhl", "fifa", "uefa", "wta", "atp", "pga", "lpga", "tour", "season", "playoff", "super bowl", "series"
}

business_keywords = {
    "business", "market", "stock", "stocks", "wall street", "dow", "nasdaq", "sp", "economy", "economic", "financial",
    "finance", "bank", "banking", "fed", "federal reserve", "interest rate", "inflation", "deflation", "gdp", "trade",
    "deficit", "surplus", "budget", "tax", "profit", "loss", "revenue", "earnings", "quarter", "share", "shares",
    "investor", "investment", "fund", "mutual fund", "hedge fund", "deal", "merger", "acquisition", "buyout", "ipo",
    "company", "corporation", "corp", "inc", "ceo", "cfo", "chairman", "president", "executive", "job", "unemployment",
    "oil", "gas", "energy", "price", "cost", "dollar", "euro", "yen", "currency", "exchange"
}

scitech_keywords = {
    "science", "technology", "tech", "computer", "computing", "software", "hardware", "internet", "web", "online",
    "website", "site", "net", "cyber", "virus", "hacker", "security", "microsoft", "google", "yahoo", "apple", "intel",
    "ibm", "linux", "windows", "phone", "mobile", "cell", "wireless", "broadband", "network", "satellite", "space",
    "nasa", "shuttle", "rocket", "orbit", "planet", "mars", "moon", "star", "galaxy", "astronomy", "biology", "genetics",
    "genome", "dna", "cell", "stem cell", "cloning", "medical", "medicine", "health", "disease", "drug", "pharmaceutical",
    "research", "study", "experiment", "lab", "laboratory", "scientist", "researcher", "invention", "discovery", "robot",
    "gadget", "device"
}

world_keywords = {
    "world", "international", "politics", "government", "president", "minister", "prime minister", "chancellor",
    "king", "queen", "prince", "leader", "official", "diplomat", "ambassador", "embassy", "un", "united nations",
    "eu", "european union", "nato", "war", "peace", "conflict", "fighting", "battle", "troops", "soldiers", "army",
    "military", "navy", "air force", "attack", "bomb", "blast", "explosion", "kill", "death", "casualty", "victim",
    "terror", "terrorist", "terrorism", "al qaeda", "insurgent", "rebel", "guerrilla", "protest", "demonstration",
    "riot", "election", "vote", "poll", "party", "parliament", "congress", "senate", "law", "court", "trial", "judge",
    "police", "arrest", "jail", "prison", "human rights", "refugee", "aid", "disaster", "earthquake", "flood", "storm",
    "hurricane", "typhoon", "tsunami", "nuclear", "weapon", "iraq", "afghanistan", "palestine", "israel", "iran",
    "korea", "china", "russia"
}

def classify(title, description):
    text = (title + " " + description).lower()
    # clean punctuation
    for char in "-.,;!?()":
        text = text.replace(char, " ")
    words = text.split()
    
    scores = {
        "Sports": 0,
        "Business": 0,
        "Sci/Tech": 0,
        "World": 0
    }
    
    for word in words:
        if word in sports_keywords:
            scores["Sports"] += 1
        if word in business_keywords:
            scores["Business"] += 1
        if word in scitech_keywords:
            scores["Sci/Tech"] += 1
        if word in world_keywords:
            scores["World"] += 1
            
    # Heuristics
    if "olympic" in text or "athens" in text:
        scores["Sports"] += 2
        
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

sports_articles = []
for art in articles:
    cat = classify(art.get("title", ""), art.get("description", ""))
    if cat == "Sports":
        sports_articles.append(art)

# Find max description length
if sports_articles:
    max_art = max(sports_articles, key=lambda x: len(x.get("description", "")))
    result = {"title": max_art["title"], "desc_len": len(max_art["description"])}
else:
    result = {"title": "None", "desc_len": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15580350581523998620': ['articles'], 'var_function-call-15580350581523998523': [{'_id': '69446b549762fc32b4d1b1ae', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15580350581523998426': ['authors', 'article_metadata'], 'var_function-call-15580350581523998329': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2000961058329415325': [{'_id': '69446b549762fc32b4d1b1ae', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446b549762fc32b4d1b1af', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446b549762fc32b4d1b1b0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446b549762fc32b4d1b1b1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446b549762fc32b4d1b1b2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6947491916061976961': 'file_storage/function-call-6947491916061976961.json'}

exec(code, env_args)
