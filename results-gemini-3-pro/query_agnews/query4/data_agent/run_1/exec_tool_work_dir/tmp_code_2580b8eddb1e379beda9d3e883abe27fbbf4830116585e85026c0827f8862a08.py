code = """import json
import re

# Load 2015 metadata
with open(locals()['var_function-call-6414145257666997456'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-490337090254977264'], 'r') as f:
    articles_list = json.load(f)

# Create a map for articles
articles_map = {int(a['article_id']): a for a in articles_list}

# Define keywords
world_keywords = [
    "president", "minister", "prime minister", "official", "government", "parliament", "senate", "congress", 
    "election", "vote", "poll", "war", "troop", "soldier", "army", "military", "attack", "bomb", "blast", 
    "kill", "dead", "injured", "wound", "rebel", "militia", "guerrilla", "terrorist", "hostage", "kidnap", 
    "peace", "talks", "treaty", "agreement", "summit", "meeting", "nuclear", "weapon", "sanction", "storm", 
    "hurricane", "typhoon", "earthquake", "flood", "disaster", "crash", "police", "court", "judge", "trial", 
    "prison", "arrest", "protest", "demonstration", "strike", "union", "law", "bill", "pope", "vatican", 
    "un", "united nations", "eu", "european union", "nato", "palestinian", "israeli", "iraqi", "afghan", 
    "syrian", "russian", "chinese", "ukraine", "korea", "iran", "saudi", "sudan", "darfur", "nepal", 
    "indonesia", "pakistan", "india", "baghdad", "kabul", "jerusalem", "gaza", "cairo", "damascus", "beirut",
    "moscow", "beijing", "washington", "london", "paris", "berlin", "tokyo", "politics", "political", "diplomat", 
    "ambassador", "embassy", "border", "security", "refugee", "crisis", "conflict"
]

business_keywords = [
    "stock", "market", "wall street", "dow", "nasdaq", "share", "profit", "earning", "quarter", "dividend", 
    "revenue", "sale", "deal", "merger", "acquisition", "buyout", "ipo", "investor", "analyst", "rate", 
    "fed", "federal reserve", "bank", "central bank", "economy", "economic", "dollar", "euro", "yen", "yuan", 
    "currency", "oil", "price", "barrel", "gold", "silver", "company", "corp", "corporation", "inc", "ltd", 
    "firm", "business", "industry", "trade", "deficit", "surplus", "budget", "tax", "inflation", "recession", 
    "job", "unemployment", "hire", "layoff", "ceo", "cfo", "executive", "manager", "boeing", "airbus", 
    "wal-mart", "general motors", "ford", "toyota", "microsoft", "google", "apple", "ibm", "intel", "oracle",
    "financial", "finance", "bond", "fund", "equity", "asset", "capital"
]

sports_keywords = [
    "sport", "game", "match", "team", "player", "coach", "manager", "score", "win", "loss", "defeat", 
    "victory", "draw", "tie", "season", "league", "cup", "championship", "tournament", "olympic", "medal", 
    "gold", "silver", "bronze", "record", "world cup", "super bowl", "nba", "nfl", "mlb", "nhl", "fifa", 
    "uefa", "tennis", "golf", "soccer", "football", "baseball", "basketball", "hockey", "cricket", "rugby", 
    "boxing", "racing", "f1", "nascar", "athlete", "stadium", "club", "round", "final", "semi-final"
]

scitech_keywords = [
    "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "net", 
    "cyber", "virus", "worm", "hacker", "security", "space", "nasa", "shuttle", "mission", "launch", "orbit", 
    "planet", "mars", "moon", "astronomy", "telescope", "physics", "chemistry", "biology", "gene", "dna", 
    "stem cell", "clone", "medical", "medicine", "drug", "health", "disease", "cancer", "aids", "hiv", 
    "study", "research", "survey", "report", "device", "gadget", "phone", "mobile", "wireless", "broadband", 
    "satellite", "robot", "engine", "motor", "battery", "chip", "processor", "server", "network", "microsoft", 
    "google", "apple", "intel", "linux", "windows", "browser", "search engine", "digital", "electronic"
]

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {
        "World": 0,
        "Business": 0,
        "Sports": 0,
        "SciTech": 0
    }
    
    # Simple tokenization by splitting on non-alphanumeric
    tokens = set(re.findall(r'\b[a-z]+\b', text))
    
    for word in tokens:
        if word in world_keywords:
            scores["World"] += 1
        if word in business_keywords:
            scores["Business"] += 1
        if word in sports_keywords:
            scores["Sports"] += 1
        if word in scitech_keywords:
            scores["SciTech"] += 1
            
    # Heuristics for ties or specific overlapping terms
    # e.g. "oil" is in Business, but if "iraq" is present, it's World.
    # We already count both. "iraq" adds to World. "oil" adds to Business.
    # If text has "iraq" and "oil", scores might be tied.
    
    # Tie-breaking:
    # If World and Business are tied, and score > 0:
    #   If "oil" in tokens, maybe Business? Or World?
    #   Usually Conflict > Business.
    
    # Find max score
    max_score = -1
    best_cat = None
    
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            # Tie breaking preferences: World > Sports > Business > SciTech (arbitrary, but World is distinct)
            if cat == "World":
                best_cat = "World"
            elif cat == "Sports" and best_cat != "World":
                best_cat = "Sports"
            # etc.
    
    if max_score == 0:
        return "Unknown"
        
    return best_cat

# Count World articles by region
region_counts = {}

for meta in metadata_list:
    aid = int(meta['article_id'])
    region = meta['region']
    
    if aid in articles_map:
        article = articles_map[aid]
        category = classify(article['title'], article['description'])
        
        if category == "World":
            region_counts[region] = region_counts.get(region, 0) + 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-6414145257666997456': 'file_storage/function-call-6414145257666997456.json', 'var_function-call-17387279326264468321': 'file_storage/function-call-17387279326264468321.json', 'var_function-call-10428291813963926827': 6696, 'var_function-call-4939086114809291303': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13401999490339433067': 5, 'var_function-call-2594177708310146329': ['articles'], 'var_function-call-1080993007468921455': [{'_id': '6944e918a831038495320111', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-490337090254977264': 'file_storage/function-call-490337090254977264.json'}

exec(code, env_args)
