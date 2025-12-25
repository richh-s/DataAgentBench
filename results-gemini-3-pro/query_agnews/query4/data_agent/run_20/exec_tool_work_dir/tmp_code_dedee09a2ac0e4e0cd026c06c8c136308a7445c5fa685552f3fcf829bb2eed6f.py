code = """import json
import collections
import re

# Load 2015 metadata
with open(locals()['var_function-call-121859605526448438'], 'r') as f:
    meta_list = json.load(f)

# Map article_id (str) -> region (str)
# Ensure article_id is string to match the articles file
meta_map = {str(item['article_id']): item['region'] for item in meta_list}
ids_2015 = set(meta_map.keys())

# Load all articles
with open(locals()['var_function-call-9929434618377718204'], 'r') as f:
    articles_list = json.load(f)

# Keywords
categories = {
    "Business": ["market", "stock", "dow", "nasdaq", "nyse", "wall street", "share", "profit", "earning", "revenue", "dividend", "quarter", "analyst", "economy", "economic", "bank", "fed", "rate", "dollar", "euro", "yen", "currency", "trade", "deal", "merger", "acquisition", "company", "corp", "inc", "ltd", "ceo", "cfo", "business", "industry", "sector", "oil", "gas", "price", "crude", "barrel", "investor", "sales"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "net", "google", "apple", "microsoft", "ibm", "intel", "linux", "windows", "server", "mobile", "phone", "cell", "wireless", "network", "satellite", "space", "nasa", "astronomer", "galaxy", "planet", "mars", "biology", "physics", "chemistry", "study", "research", "cancer", "disease", "virus", "flu", "health", "medical", "drug", "gene", "genome", "gadget", "device", "browser", "spam", "hacker"],
    "Sports": ["sport", "game", "match", "team", "player", "coach", "manager", "win", "won", "lose", "lost", "draw", "score", "goal", "point", "cup", "trophy", "medal", "olympic", "champion", "league", "tournament", "season", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby", "racing", "f1", "nascar", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "stadium"],
    "World": ["world", "international", "nation", "country", "state", "government", "parliament", "congress", "senate", "election", "vote", "poll", "candidate", "president", "prime minister", "minister", "official", "leader", "dictator", "king", "queen", "prince", "pope", "vatican", "police", "military", "army", "navy", "air force", "soldier", "troop", "rebel", "guerrilla", "terrorist", "terrorism", "attack", "bomb", "blast", "explosion", "kill", "dead", "injure", "casualty", "victim", "war", "peace", "conflict", "fight", "battle", "truce", "treaty", "accord", "agreement", "summit", "talk", "negotiation", "diplomacy", "foreign", "ambassador", "un", "united nations", "security council", "nato", "eu", "european union", "commission", "court", "trial", "judge", "prison", "jail", "hostage", "kidnap", "protest", "strike", "riot", "demonstrate", "disaster", "quake", "flood", "storm", "hurricane", "typhoon", "crash", "accident", "iraq", "iran", "syria", "israel", "palestin", "gaza", "lebanon", "egypt", "libya", "sudan", "darfur", "africa", "asia", "europe", "russia", "china", "japan", "korea", "afghanistan", "pakistan", "india", "baghdad", "tehran", "kabul", "moscow", "beijing", "ukraine", "putin", "obama", "bush", "clinton", "yasser", "arafat", "sharon"]
}

region_counts = collections.defaultdict(int)

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in ids_2015:
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        scores = {cat: 0 for cat in categories}
        words = re.findall(r'\w+', text)
        
        for word in words:
            for cat, kws in categories.items():
                if word in kws:
                    scores[cat] += 1
        
        # Check for multi-word keywords (simple check)
        for cat, kws in categories.items():
            for kw in kws:
                if " " in kw and kw in text:
                     scores[cat] += 1
        
        # Determine category
        best_cat = max(scores, key=scores.get)
        # If all 0, default to World? Or skip?
        # If max is 0, it means no keywords found.
        if scores[best_cat] > 0:
            assigned_cat = best_cat
        else:
            # Fallback or skip. Let's assume World if ambiguous? No, that biases.
            # Let's check if 'world' is in text? Already covered.
            # Let's count it as Unknown.
            assigned_cat = "Unknown"
        
        if assigned_cat == "World":
            reg = meta_map[aid]
            region_counts[reg] += 1

# Find max region
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
    max_count = region_counts[max_region]
else:
    max_region = "None"
    max_count = 0

print("__RESULT__:")
print(json.dumps({"max_region": max_region, "count": max_count, "all_counts": region_counts}))"""

env_args = {'var_function-call-121859605526448438': 'file_storage/function-call-121859605526448438.json', 'var_function-call-951208037007644572': 'file_storage/function-call-951208037007644572.json', 'var_function-call-8352185799025476041': [{'count(*)': '127600'}], 'var_function-call-6206586464072558012': 47788, 'var_function-call-12195274356503434995': {'min': 13, 'max': 127570}, 'var_function-call-16754112173434574181': 'file_storage/function-call-16754112173434574181.json', 'var_function-call-9929434618377718204': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
