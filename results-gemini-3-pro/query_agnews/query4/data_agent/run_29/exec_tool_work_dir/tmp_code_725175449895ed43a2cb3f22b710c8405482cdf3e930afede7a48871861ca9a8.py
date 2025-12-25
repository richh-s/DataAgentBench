code = """import json
import re

# Keyword lists
world_keywords = {
    "ministry", "minister", "president", "parliament", "official", "government", "state", "political", "politics", 
    "election", "vote", "voter", "poll", "leader", "campaign", "party", "candidate", "democrat", "republican", 
    "conservative", "liberal", "socialist", "communist", "dictator", "regime", "coup", "protest", "riot", 
    "demonstration", "march", "war", "conflict", "battle", "fight", "attack", "bomb", "blast", "explosion", 
    "terror", "terrorist", "terrorism", "rebel", "insurgent", "militia", "military", "army", "troop", "soldier", 
    "force", "defense", "navy", "air force", "police", "security", "jail", "prison", "arrest", "kill", "dead", 
    "death", "wound", "injure", "casualty", "victim", "survivor", "rescue", "disaster", "flood", "storm", 
    "hurricane", "typhoon", "earthquake", "quake", "tsunami", "fire", "crash", "accident", "peace", "treaty", 
    "accord", "agreement", "talks", "negotiation", "summit", "conference", "meeting", "diplomat", "ambassador", 
    "embassy", "foreign", "international", "global", "world", "united nations", "un", "eu", "european union", 
    "nato", "asean", "opec", "wto", "imf", "world bank", "iraq", "iran", "syria", "israel", "palestin", "gaza", 
    "lebanon", "egypt", "libya", "sudan", "darfur", "afghanistan", "pakistan", "india", "china", "japan", "korea", 
    "russia", "ukraine", "crimea", "georgia", "chechnya", "balkan", "serbia", "bosnia", "kosovo", "venezuela", 
    "cuba", "colombia", "mexico", "brazil", "argentina", "chile", "peru", "bolivia", "africa", "nigeria", "somalia", 
    "kenya", "zimbabwe", "congo", "rwanda", "uganda", "south africa", "australia", "canada", "usa", "us", "america", 
    "britain", "uk", "france", "germany", "italy", "spain", "greece", "turkey", "saudi", "arabia", "yemen", "oman", 
    "qatar", "kuwait", "emirates", "dubai", "abu dhabi", "bahrain", "jordan", "lebanon", "beirut", "baghdad", 
    "tehran", "damascus", "jerusalem", "tel aviv", "cairo", "tripoli", "khartoum", "kabul", "islamabad", "delhi", 
    "beijing", "tokyo", "seoul", "pyongyang", "moscow", "kiev", "london", "paris", "berlin", "rome", "madrid", 
    "athens", "ankara", "riyadh", "washington", "new york", "havana", "caracas", "bogota", "lima", "brasilia", 
    "buenos aires", "santiago", "pretoria", "cape town", "canberra", "ottawa"
}

business_keywords = {
    "business", "company", "corporation", "corp", "inc", "ltd", "firm", "enterprise", "industry", "sector", 
    "market", "stock", "share", "equity", "bond", "future", "option", "derivative", "exchange", "wall street", 
    "nasdaq", "dow jones", "s&p", "ftse", "nikkei", "hang seng", "index", "price", "value", "cost", "expense", 
    "revenue", "income", "earning", "profit", "loss", "margin", "dividend", "yield", "return", "invest", 
    "investor", "investment", "capital", "fund", "bank", "banking", "finance", "financial", "economy", "economic", 
    "fiscal", "monetary", "inflation", "deflation", "recession", "depression", "growth", "gdp", "trade", "commerce", 
    "import", "export", "tariff", "tax", "budget", "deficit", "surplus", "debt", "loan", "credit", "mortgage", 
    "rate", "interest", "currency", "forex", "dollar", "euro", "yen", "pound", "yuan", "ruble", "oil", "gas", 
    "energy", "petroleum", "barrel", "fuel", "gold", "silver", "metal", "commodity", "merger", "acquisition", 
    "takeover", "deal", "contract", "bid", "offer", "sale", "retail", "consumer", "customer", "product", "service", 
    "brand", "marketing", "advertising", "manager", "management", "executive", "ceo", "cfo", "coo", "chairman", 
    "director", "employee", "worker", "labor", "union", "job", "employment", "unemployment", "wage", "salary", 
    "bonus", "compensation", "pension", "retire", "bankruptcy", "insolvency", "default", "audit", "accounting", 
    "regulator", "sec", "fed", "central bank", "treasury"
}

sports_keywords = {
    "sport", "game", "match", "play", "player", "team", "club", "coach", "manager", "athlete", "competition", 
    "tournament", "championship", "league", "season", "cup", "bowl", "series", "olympic", "olympics", "medal", 
    "gold", "silver", "bronze", "record", "score", "result", "standings", "rank", "winner", "loser", "win", 
    "lose", "draw", "tie", "victory", "defeat", "champion", "title", "trophy", "award", "mvp", "stadium", "arena", 
    "field", "court", "track", "pool", "gym", "football", "soccer", "basketball", "baseball", "hockey", "tennis", 
    "golf", "cricket", "rugby", "volleyball", "handball", "boxing", "wrestling", "mma", "racing", "driver", "car", 
    "auto", "moto", "f1", "nascar", "cycling", "swimming", "athletics", "gymnastics", "skiing", "skating", 
    "snowboarding", "surfing", "sailing", "rowing", "horse", "jockey", "derby", "nfl", "nba", "mlb", "nhl", "mls", 
    "fifa", "uefa", "ncaa", "espn", "goal", "touchdown", "homerun", "basket", "point", "run", "race", "lap"
}

scitech_keywords = {
    "science", "scientist", "research", "researcher", "study", "experiment", "lab", "laboratory", "discovery", 
    "invention", "innovation", "technology", "tech", "engineering", "engineer", "computer", "computing", "software", 
    "hardware", "program", "code", "app", "application", "system", "network", "internet", "web", "online", 
    "digital", "virtual", "data", "database", "server", "cloud", "security", "cyber", "hacker", "virus", "malware", 
    "spyware", "spam", "email", "device", "gadget", "mobile", "phone", "smartphone", "tablet", "laptop", "desktop", 
    "pc", "mac", "windows", "linux", "android", "ios", "google", "apple", "microsoft", "amazon", "facebook", 
    "twitter", "instagram", "youtube", "social media", "search", "browser", "chip", "processor", "memory", 
    "storage", "disk", "drive", "screen", "display", "monitor", "camera", "video", "audio", "robot", "robotics", 
    "ai", "artificial intelligence", "space", "universe", "galaxy", "star", "planet", "moon", "mars", "sun", 
    "solar", "orbit", "satellite", "rocket", "launch", "shuttle", "nasa", "esa", "astronomy", "physics", "chemistry", 
    "biology", "genetics", "gene", "dna", "cell", "medicine", "medical", "health", "disease", "illness", "cancer", 
    "tumor", "drug", "treatment", "therapy", "vaccine", "doctor", "surgeon", "hospital", "clinic", "patient"
}

def classify_article(text):
    text = text.lower()
    words = re.findall(r'\w+', text)
    scores = {
        'World': 0,
        'Business': 0,
        'Sports': 0,
        'Sci/Tech': 0
    }
    
    for word in words:
        if word in world_keywords:
            scores['World'] += 1
        if word in business_keywords:
            scores['Business'] += 1
        if word in sports_keywords:
            scores['Sports'] += 1
        if word in scitech_keywords:
            scores['Sci/Tech'] += 1
            
    # Heuristics for ties or zeros
    if max(scores.values()) == 0:
        return None # Could not classify
    
    return max(scores, key=scores.get)

# Load metadata
with open(locals()['var_function-call-12409222309987750024'], 'r') as f:
    metadata_records = json.load(f)
    
id_to_region = {str(r['article_id']): r['region'] for r in metadata_records}

# Load articles
with open(locals()['var_function-call-1468729284124029393'], 'r') as f:
    articles = json.load(f)

region_world_counts = {}

debug_counts = 0

for art in articles:
    aid = str(art.get('article_id'))
    if aid in id_to_region:
        title = art.get('title', '')
        desc = art.get('description', '')
        text = title + " " + desc
        category = classify_article(text)
        
        if category == 'World':
            region = id_to_region[aid]
            region_world_counts[region] = region_world_counts.get(region, 0) + 1
            
        debug_counts += 1

print(f"Processed {debug_counts} articles matching 2015 IDs.")
print("__RESULT__:")
print(json.dumps(region_world_counts))"""

env_args = {'var_function-call-12409222309987750024': 'file_storage/function-call-12409222309987750024.json', 'var_function-call-12143718976322686060': 'file_storage/function-call-12143718976322686060.json', 'var_function-call-2027631672913679820': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17552449948020731570': 5, 'var_function-call-1468729284124029393': 'file_storage/function-call-1468729284124029393.json'}

exec(code, env_args)
