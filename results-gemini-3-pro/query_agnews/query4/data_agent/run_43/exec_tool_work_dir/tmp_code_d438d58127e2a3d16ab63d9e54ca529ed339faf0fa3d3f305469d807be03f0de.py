code = """import json
import collections
import re

# Load 2015 metadata
# This key is from Tool 1
with open(locals()['var_function-call-14621584579191841765'], 'r') as f:
    meta_list = json.load(f)

target_ids = set()
id_to_region = {}
for m in meta_list:
    aid = int(m['article_id'])
    target_ids.add(aid)
    id_to_region[aid] = m['region']

# Load articles
# This key is from Tool 5 (the large query result)
with open(locals()['var_function-call-9425048213146947809'], 'r') as f:
    all_articles = json.load(f)

keywords = {
    "World": [
        "iraq", "israel", "iran", "palestin", "afghan", "darfur", "sudan", "nigeria", "korea", "syria", "lebanon", "pakistan", "russia", "china", "japan", "indonesia", "bush", "kerry", "election", "president", "minister", "prime", "official", "leader", "govt", "government", "parliament", "senate", "troop", "soldier", "military", "army", "rebel", "guerrilla", "militant", "terror", "bomb", "blast", "attack", "kill", "dead", "wound", "injured", "peace", "war", "treaty", "talks", "negotiation", "diplomat", "un", "nations", "eu", "european union", "nato", "nuclear", "weapon", "atomic", "strike", "hostage", "kidnap", "politic", "poll", "vote", "voter", "campaign", "candidate", "party", "baghdad", "gaza", "cairo", "moscow", "beijing", "tokyo", "london", "paris", "berlin", "tehran", "jerusalem", "kabul", "baghdad", "fallujah", "najaf", "basra", "arafat", "sharon", "putin", "blair", "chirac", "schroeder", "powell", "rice", "rumsfeld", "annan", "al-qaeda", "qaeda", "terrorism", "terrorist", "security", "insurgent", "province", "border", "country", "international", "foreign", "state", "law", "court", "judge", "justice", "police", "arrest", "jail", "prison", "crime", "criminal", "murder", "rights", "human", "aid", "refugee", "disaster", "storm", "hurricane", "flood", "earthquake", "tsunami", "typhoon", "crash", "accident", "plane", "train", "ship", "ferry"
    ],
    "Business": [
        "oil", "gas", "price", "stock", "market", "share", "wall st", "exchange", "nasdaq", "dow", "index", "dollar", "euro", "yen", "currency", "bank", "economy", "economic", "finance", "financial", "rate", "interest", "fed", "federal reserve", "profit", "earning", "revenue", "loss", "quarter", "fiscal", "corp", "inc", "company", "firm", "business", "industry", "sector", "trade", "deal", "merger", "acquisition", "buyout", "bid", "offer", "sales", "retail", "consumer", "ceo", "cfo", "executive", "manager", "chairman", "job", "labor", "workforce", "unemployment", "forecast", "outlook", "growth", "recession", "boeing", "airbus", "ford", "gm", "microsoft", "google", "yahoo", "intel", "oracle", "earnings", "dividend", "invest", "investment", "investor", "fund", "mutual", "bond", "treasury", "commodity", "gold", "silver", "crude", "barrel", "opec", "energy", "power", "utility", "electric", "telecom", "airline", "auto", "car", "manufacturer", "producer", "retailer", "store", "shop", "mall", "market"
    ],
    "Sports": [
        "sport", "game", "match", "play", "player", "team", "coach", "manager", "cup", "league", "championship", "tournament", "olympic", "medal", "gold", "silver", "bronze", "world cup", "euro 2004", "nfl", "nba", "mlb", "nhl", "football", "baseball", "basketball", "soccer", "hockey", "tennis", "golf", "cricket", "rugby", "racing", "f1", "formula one", "driver", "athlete", "win", "lose", "victory", "defeat", "score", "record", "season", "stadium", "club", "red sox", "yankees", "lakers", "pistons", "arsenal", "manchester", "real madrid", "barcelona", "milan", "juventus", "chelsea", "liverpool", "bayern", "ferrari", "schumacher", "armstrong", "phelps", "williams", "federer", "roddick", "agassi", "woods", "mickelson", "final", "semi", "quarter", "round", "playoff", "super bowl", "series", "open", "tour", "grand slam", "wimbledon", "french open", "us open", "australian open", "masters", "pga"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "space", "nasa", "shuttle", "mission", "orbit", "planet", "mars", "moon", "solar", "astronomy", "computer", "pc", "software", "hardware", "internet", "web", "online", "net", "search engine", "virus", "worm", "security", "hacker", "patch", "microsoft", "windows", "linux", "apple", "ipod", "mac", "google", "yahoo", "intel", "amd", "chip", "processor", "server", "network", "wireless", "wifi", "broadband", "mobile", "phone", "cellphone", "cellular", "telecom", "biotech", "biology", "gene", "genome", "stem cell", "cloning", "research", "study", "discovery", "drug", "pharmaceutical", "medicine", "health", "disease", "cancer", "aids", "hiv", "fda", "gadget", "device", "digital", "electronic", "robot", "laser", "nanotech", "physic", "chemist", "biologist", "scientist", "lab", "laboratory", "experiment", "test", "trial", "launch", "satellite", "telescope", "galaxy", "universe", "star"
    ]
}

regex_patterns = {}
for cat, words in keywords.items():
    # Sort by length desc to prioritize longer matches?
    # words.sort(key=len, reverse=True) # Optional
    # Use word boundaries
    pattern_str = r'\b(' + '|'.join(re.escape(w) for w in words) + r')\b'
    regex_patterns[cat] = re.compile(pattern_str, re.IGNORECASE)

region_counts = collections.defaultdict(int)
world_article_count = 0
debug_samples = []

for art in all_articles:
    try:
        aid = int(art['article_id'])
    except:
        continue
        
    if aid in target_ids:
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        
        scores = {}
        for cat, pattern in regex_patterns.items():
            matches = pattern.findall(text)
            scores[cat] = len(matches)
        
        # Check if World is the max (strict or >=)
        # To avoid confusion, I'll select the category with strictly highest score.
        # If tie, maybe look at priority.
        
        if not scores:
            continue
            
        # Get max score
        max_s = max(scores.values())
        if max_s == 0:
            continue
            
        candidates = [c for c, s in scores.items() if s == max_s]
        
        final_cat = candidates[0]
        # Tie breaker logic: If World is tied with Business, which one?
        # Usually World + Business keywords overlap (oil, economy of a country).
        # Let's say if World is in candidates, categorize as World.
        if "World" in candidates:
            final_cat = "World"
            
        if final_cat == "World":
            reg = id_to_region[aid]
            region_counts[reg] += 1
            world_article_count += 1
            if len(debug_samples) < 5:
                debug_samples.append({"id": aid, "title": art.get('title'), "scores": scores})

print("__RESULT__:")
print(json.dumps({"counts": region_counts, "total_world": world_article_count, "debug": debug_samples}))"""

env_args = {'var_function-call-14621584579191841765': 'file_storage/function-call-14621584579191841765.json', 'var_function-call-7803509644995873515': 6696, 'var_function-call-6632200024076563961': 'file_storage/function-call-6632200024076563961.json', 'var_function-call-11326914846194858501': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14573584342887086246': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9425048213146947809': 'file_storage/function-call-9425048213146947809.json'}

exec(code, env_args)
