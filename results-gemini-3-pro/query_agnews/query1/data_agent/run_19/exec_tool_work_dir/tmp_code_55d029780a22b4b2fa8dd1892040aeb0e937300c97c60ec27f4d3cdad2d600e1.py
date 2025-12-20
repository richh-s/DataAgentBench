code = """import json

file_path = locals()['var_function-call-16901600362174134541']
with open(file_path, 'r') as f:
    data = json.load(f)

count = len(data)
print(f"Loaded {count} records.")

# Simple Keyword based classification check
categories = {
    "Sports": ["sport", "football", "soccer", "basketball", "baseball", "tennis", "golf", "olympic", "game", "match", "team", "league", "cup", "tournament", "coach", "player", "victory", "defeat", "score", "medal", "athlete", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "racing", "f1", "formula one", "cricket", "rugby", "boxing", "wrestling", "athletics", "swimming", "championship", "stadium", "club", "manager", "driver", "gold", "silver", "bronze", "record", "season", "playoff", "final", "semi-final", "quarter-final", "world cup", "super bowl", "grand slam", "open", "tour", "won", "lost", "beat", "leads", "trails", "points", "goals", "runs", "yards", "touchdown", "homerun", "basket", "inning", "quarter", "half", "period", "lap", "race", "finish", "start", "time", "clock", "referee", "umpire", "judge", "medal", "podium"],
    "Business": ["stock", "market", "wall street", "economy", "oil", "price", "company", "corp", "profit", "loss", "share", "trade", "dollar", "euro", "yen", "bank", "finance", "invest", "fund", "money", "deal", "merge", "acquire", "buy", "sell", "retail", "sale", "tax", "job", "employment", "unemployment", "inflation", "rate", "fed", "federal reserve", "central bank", "budget", "deficit", "surplus", "ceo", "cfo", "manager", "executive", "business", "industry", "sector", "growth", "recession", "depression", "crisis", "forecast", "outlook", "earnings", "revenue", "cost", "expense", "production", "output", "demand", "supply", "inventory", "export", "import", "tariff", "subsidy", "wto", "imf", "world bank", "nasdaq", "dow", "s&p", "ftse", "nikkei", "hang seng"],
    "Sci/Tech": ["technology", "science", "computer", "internet", "web", "software", "hardware", "chip", "processor", "server", "network", "wireless", "mobile", "phone", "app", "application", "program", "code", "data", "database", "security", "virus", "hacker", "spam", "email", "search", "engine", "google", "microsoft", "apple", "intel", "ibm", "hp", "dell", "oracle", "cisco", "facebook", "twitter", "amazon", "ebay", "yahoo", "nasa", "space", "shuttle", "station", "mars", "moon", "planet", "star", "galaxy", "universe", "physics", "chemistry", "biology", "genetics", "dna", "cell", "stem", "clone", "drug", "medicine", "health", "disease", "cancer", "aids", "hiv", "virus", "bacteria", "study", "research", "experiment", "lab", "scientist", "discovery", "invention", "innovation", "patent"],
    "World": ["world", "war", "peace", "treaty", "united nations", "un", "president", "minister", "prime minister", "chancellor", "king", "queen", "prince", "princess", "dictator", "leader", "official", "government", "parliament", "congress", "senate", "house", "representative", "democrat", "republican", "party", "vote", "election", "campaign", "candidate", "poll", "survey", "policy", "law", "bill", "act", "court", "judge", "justice", "trial", "verdict", "sentence", "prison", "jail", "police", "army", "navy", "air force", "military", "soldier", "troop", "weapon", "bomb", "missile", "nuclear", "terror", "attack", "blast", "explosion", "kill", "death", "injury", "casualty", "victim", "hostage", "kidnap", "disaster", "earthquake", "flood", "hurricane", "storm", "fire", "accident", "crash", "plane", "train", "car", "bus", "truck", "ship", "boat", "ferry", "bridge", "road", "street", "building", "city", "town", "village", "country", "nation", "state", "province", "region", "border", "territory", "island", "continent", "europe", "asia", "africa", "america", "australia", "antarctica", "middle east", "iraq", "iran", "afghanistan", "israel", "palestine", "syria", "lebanon", "egypt", "libya", "china", "russia", "usa", "uk", "france", "germany", "japan", "india", "pakistan"]
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for k in keywords:
            if k in text:
                scores[cat] += 1
    
    # Return category with max score
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return None # Unclassified
    return best_cat

sports_articles = []
for article in data:
    cat = classify(article.get('title', ''), article.get('description', ''))
    if cat == "Sports":
        sports_articles.append(article)

print(f"Found {len(sports_articles)} Sports articles.")
if len(sports_articles) > 0:
    # Find longest description
    best_article = max(sports_articles, key=lambda x: len(x.get('description', '')))
    print("__RESULT__:")
    print(json.dumps({
        "total_records": count,
        "sports_count": len(sports_articles),
        "best_title": best_article['title'],
        "best_desc_len": len(best_article['description']),
        "best_desc": best_article['description']
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"total_records": count, "sports_count": 0}))"""

env_args = {'var_function-call-10984581093047168517': [{'_id': '694471bab67b1ebe4e141d39', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-13809299225851108434': [{'_id': '694471bab67b1ebe4e141d39', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694471bab67b1ebe4e141d3a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694471bab67b1ebe4e141d3b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694471bab67b1ebe4e141d3c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694471bab67b1ebe4e141d3d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16901600362174134541': 'file_storage/function-call-16901600362174134541.json'}

exec(code, env_args)
