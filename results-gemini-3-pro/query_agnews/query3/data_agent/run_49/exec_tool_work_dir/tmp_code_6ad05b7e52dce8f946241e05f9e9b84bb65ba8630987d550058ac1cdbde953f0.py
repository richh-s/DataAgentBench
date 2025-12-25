code = """import json
import re
from collections import Counter

# Load metadata
with open(locals()['var_function-call-12371501432647915462'], 'r') as f:
    metadata_list = json.load(f)

# Create a map article_id -> year
# Ensure IDs are strings as in MongoDB result
meta_map = {str(item['article_id']): item['year'] for item in metadata_list}

# Load articles
with open(locals()['var_function-call-4746464685426923532'], 'r') as f:
    articles_list = json.load(f)

# Keywords
categories = {
    "Business": ["market", "stock", "trade", "economy", "economic", "business", "company", "companies", "bank", "profit", "revenue", "loss", "invest", "investment", "investor", "share", "dollar", "euro", "yen", "currency", "ceo", "cfo", "merger", "acquisition", "deal", "oil", "price", "prices", "sales", "corp", "corporate", "inc", "ltd", "exchange", "wall", "street", "fed", "federal", "reserve", "rate", "inflation", "ipo", "dow", "nasdaq", "bond", "futures", "yield", "earning", "earnings", "dividend", "forecast", "analyst", "retail", "consumer"],
    "Sports": ["sport", "sports", "game", "games", "team", "teams", "play", "player", "players", "win", "won", "winner", "loss", "lost", "beat", "defeat", "score", "cup", "league", "season", "champion", "championship", "olympic", "olympics", "medal", "coach", "football", "soccer", "baseball", "basketball", "hockey", "tennis", "golf", "rugby", "cricket", "race", "racing", "driver", "athlete", "stadium", "match", "tournament"],
    "Sci/Tech": ["technology", "tech", "science", "computer", "computers", "software", "hardware", "internet", "web", "website", "online", "net", "mobile", "phone", "cellphone", "wireless", "chip", "processor", "microsoft", "google", "apple", "ibm", "intel", "linux", "windows", "virus", "security", "hacker", "space", "nasa", "satellite", "orbit", "robot", "robotics", "digital", "electronic", "device", "gadget", "network", "server", "browser", "search", "engine", "biotech", "biology", "physics", "astronomy", "research", "scientist"],
    "World": ["world", "international", "war", "peace", "president", "minister", "prime", "government", "official", "election", "vote", "poll", "country", "countries", "nation", "nations", "state", "iraq", "afghanistan", "palestinian", "israel", "iran", "china", "russia", "eu", "europe", "un", "united", "nations", "military", "army", "troop", "troops", "police", "attack", "bomb", "blast", "explosion", "kill", "killed", "dead", "death", "hostage", "terror", "terrorist", "terrorism", "rebel", "insurgent", "conflict", "crisis", "disaster", "earthquake", "tsunami", "flood", "hurricane", "typhoon", "storm"]
}

year_counts = Counter()

debug_classifications = []

for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_map:
        year = meta_map[aid]
        # Text to classify
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        # Simple tokenization
        tokens = re.findall(r'\w+', text)
        
        scores = {cat: 0 for cat in categories}
        for token in tokens:
            for cat, kws in categories.items():
                if token in kws:
                    scores[cat] += 1
        
        # Determine category
        # If max score is 0, we can't decide well, but let's check.
        # If tie, picking one (maybe sort categories to be deterministic)
        best_cat = max(scores, key=scores.get)
        
        # Tie breaking: if max is 0, default to something? Or treat as None? 
        # But hint says "All articles belong to one of four categories".
        # Let's hope max > 0. If multiple max, `max` picks the first one encountered.
        # Let's refine tie-breaking or just rely on keyword density.
        
        if scores[best_cat] > 0:
            category = best_cat
        else:
            category = "World" # Default? Or skip? Let's check a few.
            
        if category == "Business":
            year_counts[year] += 1

        if len(debug_classifications) < 5:
            debug_classifications.append({"title": art.get('title'), "scores": scores, "cat": category})

# Calculate average
# Years 2010 to 2020 inclusive = 11 years.
total_business = sum(year_counts.values())
average = total_business / 11.0

print(f"Debug classifications: {debug_classifications}")
print(f"Year counts: {year_counts}")
print(f"Total Business: {total_business}")
print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-12371501432647915462': 'file_storage/function-call-12371501432647915462.json', 'var_function-call-702335989468777751': 14860, 'var_function-call-1127075526552130781': [{'_id': '6944e792b459843e876ccea6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e792b459843e876ccea7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e792b459843e876ccea8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e792b459843e876ccea9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e792b459843e876cceaa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4746464685426923532': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
