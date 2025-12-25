code = """import json
import re
import collections

# Load Metadata
with open(locals()['var_function-call-8192239243877575471'], 'r') as f:
    metadata_list = json.load(f)

# Load Articles
with open(locals()['var_function-call-9935436869235845526'], 'r') as f:
    articles_list = json.load(f)

# Create map
articles_map = {}
for art in articles_list:
    articles_map[str(art['article_id'])] = art['title'] + " " + art['description']

# Check overlap
meta_ids = set(str(x['article_id']) for x in metadata_list)
found_ids = set(articles_map.keys())
overlap = meta_ids & found_ids

# Keywords
keywords = {
    "World": set([
        "president", "minister", "election", "parliament", "government", "official", "leader", 
        "war", "military", "troops", "army", "soldier", "rebel", "militia", "attack", "kill", "bomb", "blast", "explosion", 
        "terror", "hostage", "kidnap", "peace", "treaty", "nuclear", "weapon", "protest", "riot", "strike", 
        "storm", "hurricane", "flood", "earthquake", "tsunami", "crash", "disaster", "aid", "refugee", 
        "un", "nato", "eu", "iraq", "iran", "syria", "israel", "palestine", "gaza", "afghanistan", "pakistan", 
        "russia", "ukraine", "china", "korea", "sudan", "libya", "egypt", "venezuela", "turkey", "lebanon",
        "baghdad", "kabul", "tehran", "jerusalem", "beijing", "moscow", "pyongyang", "london", "paris", "berlin",
        "prime", "premier", "chancellor", "senate", "congress", "law", "legislation", "court", "judge", "police", 
        "arrest", "jail", "prison", "execution", "human", "rights", "insurgent", "guerrilla", "clash", "violence",
        "nations", "diplomacy", "ambassador", "sanctions", "border", "territory", "sovereignty", "independence",
        "coup", "regime", "dictator", "assassination", "massacre", "genocide", "crimes", "humanitarian",
        "fatah", "hamas", "hezbollah", "qaeda", "taliban", "isis", "isil", "jihad", "islamist", "suicide",
        "car", "bombing", "gunmen", "shoot", "fire", "dead", "injured", "wounded", "casualty", "death", "toll"
    ]),
    "Business": set([
        "market", "stock", "dow", "nasdaq", "invest", "trade", "economy", "dollar", "euro", "bank", "fed", "rate", 
        "inflation", "profit", "loss", "sales", "deal", "merger", "acquisition", "ipo", "share", "oil", "price", 
        "company", "corp", "inc", "business", "ceo", "manager", "google", "microsoft", "yahoo", "apple", "ibm", 
        "boeing", "airbus", "walmart", "retail", "financial", "finance", "sector", "industry", "revenue", "dividend",
        "earnings", "quarterly", "fiscal", "budget", "deficit", "surplus", "debt", "bond", "yield", "currency", 
        "exchange", "wall", "street", "investor", "shareholder", "stake", "buyout", "venture", "capital", "equity",
        "fund", "mutual", "hedge", "commodity", "gold", "silver", "crude", "barrel", "opec", "energy", "gas", 
        "telecom", "airline", "automaker", "manufacturing", "consumer", "spending", "confidence", "job", "unemployment",
        "hiring", "salary", "wage", "labor", "workforce", "recruit", "employment"
    ]),
    "Sports": set([
        "sport", "game", "match", "team", "league", "cup", "olympic", "medal", "score", "win", "lose", "victory", 
        "defeat", "champion", "coach", "player", "football", "soccer", "basketball", "baseball", "hockey", "tennis", 
        "golf", "cricket", "athlete", "f1", "racing", "stadium", "season", "final", "semi", "quarter-final", "round", 
        "tournament", "competition", "gold", "silver", "bronze", "record", "world cup", "super bowl", "nfl", "nba", 
        "mlb", "nhl", "fifa", "uefa", "club", "manager"
    ]),
    "Sci_Tech": set([
        "science", "technology", "computer", "software", "internet", "web", "online", "mobile", "phone", "wireless", 
        "chip", "data", "server", "virus", "hacker", "space", "nasa", "orbit", "planet", "galaxy", "drug", "medicine", 
        "cancer", "disease", "study", "research", "scientist", "laboratory", "microsoft", "google", "apple", "intel", 
        "linux", "windows", "browser", "spam", "mail", "email", "search", "engine", "network", "cyber", "digital",
        "hardware", "processor", "memory", "storage", "cloud", "app", "application", "iphone", "ipad", "android",
        "smartphone", "tablet", "device", "gadget", "innovation", "invention", "patent", "discovery", "astronomy",
        "physics", "chemistry", "biology", "genetics", "dna", "stem", "cell", "medical", "health", "treatment",
        "therapy", "vaccine", "aids", "hiv", "flu", "bacteria", "telescope", "mission", "shuttle", "launch", "mars",
        "moon", "solar", "system", "universe"
    ])
}

def classify(text):
    text = text.lower()
    tokens = re.findall(r'\w+', text)
    scores = {k: 0 for k in keywords}
    for t in tokens:
        for cat, kws in keywords.items():
            if t in kws:
                scores[cat] += 1
    
    # Tie breaking: World > Business > Sci_Tech > Sports
    # But wait, "oil" is business. "iraq oil" -> 1 Biz, 1 World.
    # If tie, default to World if World > 0?
    
    if max(scores.values()) == 0:
        return "Unknown"
    
    # Sort by score desc, then by priority
    # Priority: World (0), Business (1), Sci_Tech (2), Sports (3)
    # Actually, if scores are equal, we need a tie breaker.
    # Let's verify classification distribution.
    
    sorted_cats = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    if sorted_cats[0][1] > sorted_cats[1][1]:
        return sorted_cats[0][0]
    else:
        # Tie
        # Check if one is World
        candidates = [c for c, s in sorted_cats if s == sorted_cats[0][1]]
        if "World" in candidates: return "World"
        if "Business" in candidates: return "Business"
        if "Sci_Tech" in candidates: return "Sci_Tech"
        return "Sports"

world_counts = collections.defaultdict(int)
all_counts = collections.defaultdict(int)

for item in metadata_list:
    aid = str(item['article_id'])
    if aid in articles_map:
        cat = classify(articles_map[aid])
        all_counts[cat] += 1
        if cat == "World":
            world_counts[item['region']] += 1

print("__RESULT__:")
print(json.dumps({
    "overlap_count": len(overlap),
    "total_meta": len(metadata_list),
    "category_counts": all_counts,
    "world_region_counts": world_counts,
    "max_region": max(world_counts, key=world_counts.get) if world_counts else "None"
}))"""

env_args = {'var_function-call-8192239243877575471': 'file_storage/function-call-8192239243877575471.json', 'var_function-call-4285467361081759445': 6696, 'var_function-call-13346176432867388839': [{'_id': '69450821ec4d8e6298d328d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450821ec4d8e6298d328d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450821ec4d8e6298d328d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450821ec4d8e6298d328da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450821ec4d8e6298d328db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-152803809967091269': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13229976580628931333': 'file_storage/function-call-13229976580628931333.json', 'var_function-call-14357045956631284067': {'region': 'Africa', 'count': 27, 'all_counts': {'South America': 23, 'Europe': 21, 'Asia': 22, 'North America': 20, 'Africa': 27}}, 'var_function-call-2003783828452005932': 6696, 'var_function-call-5861112987740130627': {'counts': {'Business': 143, 'Sci_Tech': 57, 'Unknown': 66, 'Sports': 96, 'World': 132}, 'samples': [['Google IPO Auction Off to Rocky Start  WASHINGTON/', 'Business'], ['US trade deficit swells in June The US trade defic', 'Business'], ['Google auction begins on Friday An auction of shar', 'Sci_Tech'], ["Delightful Dell The company's results show that it", 'Business'], ["Chrysler's Bling King After a tough year, Detroit'", 'Unknown'], ['IT Myth 5: Most IT projects fail Do most IT projec', 'Business'], ["U.K.'s NHS taps Gartner to help plan \\$9B IT overh", 'Business'], ['HP to Buy Synstar Hewlett-Packard will pay \\$297 m', 'Business'], ['Oracle Sales Data Seen Being Released (Reuters) Re', 'Business'], ["What's in a Name? Well, Matt Is Sexier Than Paul (", 'Unknown'], ["NASA's Genesis Spacecraft Adjusts Course (AP) AP -", 'Sci_Tech'], ['Earth is Rare, New Study Suggests (SPACE.com) SPAC', 'Sci_Tech'], ['Indictments Using DNA on Rise Nationally (AP) AP -', 'Unknown'], ["Insecurity: (Or Why Americans Aren't Feeling The R", 'Business'], ["Reverse Psychology \\\\I really hope SUN doesn't Ope", 'Business'], ["'Madden,' 'ESPN' Football Score in Different Ways ", 'Sports'], ["News: Climate Change Could Doom Alaska's Tundra In", 'Business'], ['News: Warmer Weather, Human Disturbances Interact ', 'World'], ['Building Dedicated to Space Shuttle Columbia Astro', 'World'], ["Saturn's Moon Titan: Prebiotic Laboratory by Harry", 'Sports']]}, 'var_function-call-18187326317049292616': 'file_storage/function-call-18187326317049292616.json', 'var_function-call-9935436869235845526': 'file_storage/function-call-9935436869235845526.json'}

exec(code, env_args)
