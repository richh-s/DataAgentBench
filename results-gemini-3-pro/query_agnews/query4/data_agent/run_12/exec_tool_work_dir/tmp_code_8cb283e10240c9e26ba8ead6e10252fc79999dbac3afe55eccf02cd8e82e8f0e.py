code = """import json
import re
from collections import Counter

# Load metadata (IDs and regions for 2015)
with open(locals()['var_function-call-13553007703269894173'], 'r') as f:
    metadata_list = json.load(f)

# Create a map of article_id -> region
id_to_region = {str(item['article_id']): item['region'] for item in metadata_list}

# Load articles
with open(locals()['var_function-call-15217295247917284599'], 'r') as f:
    all_articles = json.load(f)

# Keywords (simplified and lowercased)
world_keywords = set([
    "iraq", "iran", "palestin", "israel", "gaza", "afghan", "baghdad", "fallujah", "troops", "militants", "rebels", "killed", "dead", "bomb", "blast", "explosion", "president", "minister", "prime", "official", "government", "parliament", "election", "vote", "poll", "un", "united nations", "eu", "european union", "nato", "treaty", "talks", "peace", "deal", "nuclear", "atomic", "program", "sanctions", "china", "russia", "korea", "darfur", "sudan", "hurricane", "storm", "typhoon", "earthquake", "tsunami", "flood", "hostage", "kidnap", "terror", "qaeda", "bush", "kerry", "putin", "blair", "sharon", "arafat", "military", "war", "army", "soldiers", "police", "security", "attack", "force", "crash", "disaster", "crisis"
])

sports_keywords = set([
    "olympic", "athens", "medal", "gold", "silver", "bronze", "game", "match", "cup", "final", "semi", "quarter", "win", "won", "beat", "lost", "loss", "victory", "defeat", "draw", "score", "team", "player", "coach", "manager", "club", "league", "season", "championship", "tournament", "open", "sox", "yankees", "mets", "cubs", "cardinals", "braves", "dodgers", "giants", "patriots", "eagles", "colts", "packers", "steelers", "lakers", "pistons", "spurs", "heat", "bulls", "knicks", "united", "chelsea", "arsenal", "liverpool", "real madrid", "barcelona", "milan", "juventus", "bayern", "ferrari", "schumacher", "armstrong", "phelps", "williams", "federer", "roddick", "agassi", "woods", "mickelson", "singh", "nhl", "nfl", "nba", "mlb", "fifa", "uefa", "soccer", "football", "baseball", "basketball", "tennis", "golf", "hockey", "boxing", "racing", "cricket", "rugby", "sport", "athlete"
])

business_keywords = set([
    "stock", "market", "wall st", "dow", "nasdaq", "s&p", "share", "price", "trade", "invest", "fund", "equity", "profit", "earn", "revenue", "loss", "quarterly", "bank", "finance", "economy", "economic", "growth", "inflation", "rate", "fed", "federal reserve", "greenspan", "dollar", "euro", "yen", "yuan", "oil", "crude", "gas", "energy", "barrel", "opec", "company", "corp", "inc", "ltd", "firm", "business", "industry", "sector", "ceo", "cfo", "chairman", "executive", "manage", "deal", "merge", "acquire", "buyout", "bid", "offer", "ipo", "sec", "accounting", "audit", "bankrupt", "airline", "boeing", "airbus", "wal-mart", "sales", "retail"
])

tech_keywords = set([
    "technology", "tech", "science", "research", "study", "space", "nasa", "shuttle", "station", "orbit", "mars", "moon", "sun", "star", "planet", "galaxy", "universe", "computer", "software", "hardware", "chip", "processor", "memory", "storage", "server", "network", "internet", "web", "online", "site", "search", "engine", "browser", "email", "spam", "virus", "worm", "hacker", "security", "wireless", "mobile", "phone", "cell", "cellular", "telecom", "broadband", "satellite", "gps", "digital", "camera", "video", "audio", "music", "ipod", "itunes", "mp3", "dvd", "hdtv", "microsoft", "windows", "linux", "unix", "mac", "apple", "google", "yahoo", "amazon", "ebay", "intel", "amd", "ibm", "game", "console", "playstation", "xbox", "nintendo", "biology", "genetics", "genome", "dna", "stem cell", "clone", "medical", "medicine", "drug", "cancer", "disease", "health", "hospital", "doctor"
])

region_counts = Counter()

def classify(text):
    text = text.lower()
    # Simple tokenization
    tokens = re.findall(r'\w+', text)
    
    scores = {
        "World": 0,
        "Sports": 0,
        "Business": 0,
        "Sci/Tech": 0
    }
    
    for token in tokens:
        if token in world_keywords:
            scores["World"] += 1
        if token in sports_keywords:
            scores["Sports"] += 1
        if token in business_keywords:
            scores["Business"] += 1
        if token in tech_keywords:
            scores["Sci/Tech"] += 1
            
    # Find max score
    if sum(scores.values()) == 0:
        return None # Unclassified
    
    return max(scores, key=scores.get)

# Process articles
count = 0
for article in all_articles:
    aid = str(article.get('article_id'))
    if aid in id_to_region:
        text = (article.get('title', '') + " " + article.get('description', ''))
        category = classify(text)
        if category == "World":
            region_counts[id_to_region[aid]] += 1
        count += 1

print(f"Processed {count} articles matching 2015 IDs.")
print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-13553007703269894173': 'file_storage/function-call-13553007703269894173.json', 'var_function-call-10354531083663329512': 'file_storage/function-call-10354531083663329512.json', 'var_function-call-11825340913625069070': 'file_storage/function-call-11825340913625069070.json', 'var_function-call-7208729024314595799': [{'_id': '6944f4d143f535bfcb8ae344', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f4d143f535bfcb8ae345', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f4d143f535bfcb8ae346', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f4d143f535bfcb8ae347', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f4d143f535bfcb8ae348', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15196617614673858566': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15217295247917284599': 'file_storage/function-call-15217295247917284599.json', 'var_function-call-16029694141166895603': ['authors', 'article_metadata'], 'var_function-call-384516781604228114': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-5326455973705564077': [{'author_id': '0', 'name': 'Felicia Miles'}]}

exec(code, env_args)
