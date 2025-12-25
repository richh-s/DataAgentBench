code = """import json
import collections

# File paths
metadata_path = locals()['var_function-call-8215058594514075225']
articles_path = locals()['var_function-call-5206460372666196868']

# Load metadata
# Map article_id (int) -> region
with open(metadata_path, 'r') as f:
    meta_list = json.load(f)

meta_dict = {}
for m in meta_list:
    try:
        aid = int(m['article_id'])
        meta_dict[aid] = m['region']
    except:
        pass

print(f"Loaded {len(meta_dict)} metadata entries.")

# Keywords
categories = {
    "World": [
        "world", "international", "peace", "war", "military", "troops", "army", "soldier",
        "government", "president", "minister", "official", "election", "parliament", "senate", "congress",
        "law", "court", "judge", "police", "security", "attack", "bomb", "blast", "explosion", "kill", "dead", "death", "injured",
        "disaster", "storm", "hurricane", "typhoon", "flood", "earthquake", "tsunami", "fire",
        "nuclear", "weapon", "missile", "treaty", "diplomacy", "talks", "meeting", "summit", "leader",
        "country", "nation", "state", "border", "refugee", "migrant", "immigrant", "protest", "demonstration", "strike",
        "crisis", "conflict", "violence", "terror", "terrorism", "al-qaeda", "taliban", "isis",
        "iraq", "iran", "afghanistan", "syria", "israel", "palestine", "gaza", "lebanon", "egypt", "libya", "sudan",
        "russia", "ukraine", "crimea", "putin", "china", "beijing", "japan", "korea", "india", "pakistan",
        "usa", "u.s.", "america", "white house", "pentagon", "britain", "uk", "london", "france", "paris", "germany", "berlin",
        "europe", "eu", "european union", "africa", "asia", "middle east", "latin america", "un", "united nations"
    ],
    "Sports": [
        "sport", "game", "match", "tournament", "championship", "cup", "league", "team", "club", "squad",
        "player", "athlete", "coach", "manager", "score", "win", "won", "winner", "lose", "lost", "loss", "defeat",
        "victory", "record", "medal", "gold", "silver", "bronze", "rank", "standings",
        "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby",
        "racing", "driver", "f1", "formula one", "nascar", "cycling", "boxing", "swimming",
        "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "olympic", "olympics", "athens", "beijing",
        "red sox", "yankees", "lakers", "bulls", "knicks", "patriots", "cowboys"
    ],
    "Business": [
        "business", "economy", "economic", "market", "stock", "share", "equity", "bond", "trade", "trading",
        "profit", "loss", "revenue", "earnings", "quarter", "fiscal", "forecast", "dividend",
        "percent", "rate", "interest", "inflation", "debt", "deficit", "budget",
        "dollar", "euro", "yen", "yuan", "currency", "bank", "banking", "finance", "financial",
        "invest", "investment", "investor", "fund", "wall street", "dow", "nasdaq", "s&p",
        "company", "corporation", "firm", "inc", "ltd", "enterprise", "startup",
        "ceo", "cfo", "executive", "chairman", "management",
        "oil", "gas", "energy", "petroleum", "price", "cost", "consumer", "retail", "sales",
        "deal", "merger", "acquisition", "buyout", "bid", "offer", "ipo", "bankruptcy"
    ],
    "Sci/Tech": [
        "technology", "tech", "science", "scientific", "computer", "computing", "software", "hardware",
        "internet", "web", "website", "online", "cyber", "digital", "data", "network", "server", "cloud",
        "mobile", "phone", "cellphone", "smartphone", "wireless", "broadband", "wifi", "app",
        "chip", "processor", "semiconductor", "memory", "storage",
        "google", "microsoft", "apple", "ibm", "intel", "linux", "windows", "android", "ios", "facebook", "twitter",
        "space", "nasa", "shuttle", "rocket", "orbit", "satellite", "mars", "moon", "solar", "planet", "universe", "astronomy", "galaxy",
        "biology", "physics", "chemistry", "research", "study", "experiment", "lab", "scientist", "researcher",
        "discovery", "invention", "innovate", "innovation", "gadget", "device", "robot", "robotics",
        "virus", "antivirus", "spam", "hacker", "malware", "browser", "search engine"
    ]
}

# Pre-process keywords for faster matching
for cat in categories:
    categories[cat] = set(categories[cat])

region_counts = collections.defaultdict(int)

# Read articles
# We can't load all at once if it's too big, but the range query returned around 127k items max (probably less).
# 127k * ~500 bytes = ~60MB. Python can handle it easily.
with open(articles_path, 'r') as f:
    articles = json.load(f)

print(f"Loaded {len(articles)} articles.")

count = 0
for art in articles:
    try:
        aid = int(art['article_id'])
    except:
        continue

    if aid in meta_dict:
        # Categorize
        text = (art.get('title', '') + ' ' + art.get('description', '')).lower()
        
        scores = {k: 0 for k in categories}
        for cat, keywords in categories.items():
            for kw in keywords:
                if kw in text:
                    scores[cat] += 1
        
        # Determine category
        # If all 0, maybe "World" is default? Or ignore.
        # Let's pick max.
        if max(scores.values()) > 0:
            best_cat = max(scores, key=scores.get)
            if best_cat == "World":
                region_counts[meta_dict[aid]] += 1
                count += 1
        else:
            # If no keywords matched, what to do?
            # Maybe it's "General" or "World"?
            # Let's ignore for now.
            pass

print(f"Classified {count} articles as World.")
print("Region counts:")
print(json.dumps(region_counts))

# Find max
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
    print("__RESULT__:")
    print(json.dumps(max_region))
else:
    print("__RESULT__:")
    print(json.dumps("None"))"""

env_args = {'var_function-call-8215058594514075225': 'file_storage/function-call-8215058594514075225.json', 'var_function-call-15796689833732629801': 'file_storage/function-call-15796689833732629801.json', 'var_function-call-412792057028406590': ['articles'], 'var_function-call-17773611342032374061': [{'_id': '69452455473cd748aceb2ef4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69452455473cd748aceb2ef5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69452455473cd748aceb2ef6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69452455473cd748aceb2ef7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69452455473cd748aceb2ef8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2873862478051868880': {'collection': 'articles', 'filter': {'article_id': {'$gte': 13, '$lte': 127570}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1, '_id': 0}}, 'var_function-call-5206460372666196868': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}]}

exec(code, env_args)
