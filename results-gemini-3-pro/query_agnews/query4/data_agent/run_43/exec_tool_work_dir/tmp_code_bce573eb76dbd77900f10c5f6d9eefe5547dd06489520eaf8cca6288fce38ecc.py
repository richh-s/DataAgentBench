code = """import json
import collections
import re

# Load 2015 metadata
with open(locals()['var_function-call-14621584579191841765'], 'r') as f:
    meta_list = json.load(f)

target_ids = set()
id_to_region = {}
for m in meta_list:
    aid = int(m['article_id'])
    target_ids.add(aid)
    id_to_region[aid] = m['region']

# Load articles
with open(locals()['var_function-call-14573584342887086246'], 'r') as f:
    all_articles = json.load(f)

# Keywords
keywords = {
    "World": [
        "iraq", "israel", "iran", "palestin", "afghan", "darfur", "sudan", "nigeria", "korea", "syria", "lebanon", "pakistan", "russia", "china", "japan", "indonesia", "bush", "kerry", "election", "president", "minister", "prime", "official", "leader", "govt", "government", "parliament", "senate", "troop", "soldier", "military", "army", "rebel", "guerrilla", "militant", "terror", "bomb", "blast", "attack", "kill", "dead", "wound", "injured", "peace", "war", "treaty", "talks", "negotiation", "diplomat", "un", "nations", "eu", "european union", "nato", "nuclear", "weapon", "atomic", "strike", "hostage", "kidnap", "politic", "poll", "vote", "voter", "campaign", "candidate", "party", "baghdad", "gaza", "cairo", "moscow", "beijing", "tokyo", "london", "paris", "berlin", "tehran", "jerusalem", "kabul", "baghdad", "fallujah", "najaf", "basra", "arafat", "sharon", "putin", "blair", "chirac", "schroeder", "powell", "rice", "rumsfeld", "annan"
    ],
    "Business": [
        "oil", "gas", "price", "stock", "market", "share", "wall st", "exchange", "nasdaq", "dow", "index", "dollar", "euro", "yen", "currency", "bank", "economy", "economic", "finance", "financial", "rate", "interest", "fed", "federal reserve", "profit", "earning", "revenue", "loss", "quarter", "fiscal", "corp", "inc", "company", "firm", "business", "industry", "sector", "trade", "deal", "merger", "acquisition", "buyout", "bid", "offer", "sales", "retail", "consumer", "ceo", "cfo", "executive", "manager", "chairman", "job", "labor", "workforce", "unemployment", "forecast", "outlook", "growth", "recession", "boeing", "airbus", "ford", "gm", "microsoft", "google", "yahoo", "intel", "oracle", "earnings"
    ],
    "Sports": [
        "sport", "game", "match", "play", "player", "team", "coach", "manager", "cup", "league", "championship", "tournament", "olympic", "medal", "gold", "silver", "bronze", "world cup", "euro 2004", "nfl", "nba", "mlb", "nhl", "football", "baseball", "basketball", "soccer", "hockey", "tennis", "golf", "cricket", "rugby", "racing", "f1", "formula one", "driver", "athlete", "win", "lose", "victory", "defeat", "score", "record", "season", "stadium", "club", "red sox", "yankees", "lakers", "pistons", "arsenal", "manchester", "real madrid", "barcelona", "milan", "juventus", "chelsea", "liverpool", "bayern", "ferrari", "schumacher", "armstrong", "phelps", "williams", "federer", "roddick", "agassi", "woods", "mickelson"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "space", "nasa", "shuttle", "mission", "orbit", "planet", "mars", "moon", "solar", "astronomy", "computer", "pc", "software", "hardware", "internet", "web", "online", "net", "search engine", "virus", "worm", "security", "hacker", "patch", "microsoft", "windows", "linux", "apple", "ipod", "mac", "google", "yahoo", "intel", "amd", "chip", "processor", "server", "network", "wireless", "wifi", "broadband", "mobile", "phone", "cellphone", "cellular", "telecom", "biotech", "biology", "gene", "genome", "stem cell", "cloning", "research", "study", "discovery", "drug", "pharmaceutical", "medicine", "health", "disease", "cancer", "aids", "hiv", "fda"
    ]
}

# Precompile regex for speed? Or just simple lowercase check.
# Regex might be better for word boundaries.
# Construct regex for each category
regex_patterns = {}
for cat, words in keywords.items():
    # Sort by length desc to match longer phrases first if needed, but here they are mostly single words.
    # Escape words just in case
    pattern_str = r'\b(' + '|'.join(re.escape(w) for w in words) + r')\b'
    regex_patterns[cat] = re.compile(pattern_str, re.IGNORECASE)

region_counts = collections.defaultdict(int)
world_article_count = 0

for art in all_articles:
    try:
        aid = int(art['article_id'])
    except:
        continue
        
    if aid in target_ids:
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        
        scores = {}
        for cat, pattern in regex_patterns.items():
            # Count matches
            matches = pattern.findall(text)
            scores[cat] = len(matches)
            
        # Determine max score
        if not scores:
            continue
            
        max_score = -1
        max_cat = None
        
        # Priority: World > others? Or just simple max.
        # Let's find cats with max score
        m_val = max(scores.values())
        if m_val == 0:
            # Default or Unknown.
            # If "oil" is in text, but categorized as Business? 
            # If no keywords found, maybe look at title again? 
            # We skip if 0?
            continue
            
        candidates = [c for c, s in scores.items() if s == m_val]
        
        # Tie breaking
        # If World is in candidates, pick World?
        if "World" in candidates:
            final_cat = "World"
        else:
            final_cat = candidates[0]
            
        if final_cat == "World":
            reg = id_to_region[aid]
            region_counts[reg] += 1
            world_article_count += 1

print("__RESULT__:")
print(json.dumps({"counts": region_counts, "total_world": world_article_count}))"""

env_args = {'var_function-call-14621584579191841765': 'file_storage/function-call-14621584579191841765.json', 'var_function-call-7803509644995873515': 6696, 'var_function-call-6632200024076563961': 'file_storage/function-call-6632200024076563961.json', 'var_function-call-11326914846194858501': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14573584342887086246': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
