code = """import json
import re
from collections import Counter

# Load metadata
# This was confirmed to be a file path
with open(locals()['var_function-call-12371501432647915462'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
# Check if it's a list or a string (file path)
articles_var = locals()['var_function-call-4746464685426923532']
if isinstance(articles_var, str) and (articles_var.endswith('.json') or len(articles_var) < 200): 
    # Heuristic: if it's a string and looks like a path or very short (key name?), it might be a path.
    # But usually if it's a path, the system message says so. 
    # If it's a list, it's the data.
    # If the previous output showed the JSON content, it's likely the list.
    # However, if the result was truncated in display, it might still be passed as a full object in the variable?
    # Wait, the system prompt says: "If a tool result is large, the next message will include a preview ... and the storage entry will be the .json file path".
    # The message for articles query showed a preview. So it SHOULD be a file path.
    # But the message text didn't explicitly say "stored in a file".
    # Let's try to see if it's a string.
    try:
        with open(articles_var, 'r') as f:
            articles_list = json.load(f)
    except:
        # If open fails, maybe it's not a path.
        if isinstance(articles_var, list):
            articles_list = articles_var
        else:
            # Maybe it is a string containing JSON?
            try:
                articles_list = json.loads(articles_var)
            except:
                 articles_list = [] # Should not happen
else:
    articles_list = articles_var

# If articles_list is still not a list (e.g. dict or something), handle it.
if isinstance(articles_list, dict) and 'result' in articles_list:
     articles_list = articles_list['result'] # Just in case

# Create a map article_id -> year
meta_map = {str(item['article_id']): item['year'] for item in metadata_list}

# Keywords (same as before)
categories = {
    "Business": ["market", "stock", "trade", "economy", "economic", "business", "company", "companies", "bank", "profit", "revenue", "loss", "invest", "investment", "investor", "share", "dollar", "euro", "yen", "currency", "ceo", "cfo", "merger", "acquisition", "deal", "oil", "price", "prices", "sales", "corp", "corporate", "inc", "ltd", "exchange", "wall", "street", "fed", "federal", "reserve", "rate", "inflation", "ipo", "dow", "nasdaq", "bond", "futures", "yield", "earning", "earnings", "dividend", "forecast", "analyst", "retail", "consumer"],
    "Sports": ["sport", "sports", "game", "games", "team", "teams", "play", "player", "players", "win", "won", "winner", "loss", "lost", "beat", "defeat", "score", "cup", "league", "season", "champion", "championship", "olympic", "olympics", "medal", "coach", "football", "soccer", "baseball", "basketball", "hockey", "tennis", "golf", "rugby", "cricket", "race", "racing", "driver", "athlete", "stadium", "match", "tournament"],
    "Sci/Tech": ["technology", "tech", "science", "computer", "computers", "software", "hardware", "internet", "web", "website", "online", "net", "mobile", "phone", "cellphone", "wireless", "chip", "processor", "microsoft", "google", "apple", "ibm", "intel", "linux", "windows", "virus", "security", "hacker", "space", "nasa", "satellite", "orbit", "robot", "robotics", "digital", "electronic", "device", "gadget", "network", "server", "browser", "search", "engine", "biotech", "biology", "physics", "astronomy", "research", "scientist"],
    "World": ["world", "international", "war", "peace", "president", "minister", "prime", "government", "official", "election", "vote", "poll", "country", "countries", "nation", "nations", "state", "iraq", "afghanistan", "palestinian", "israel", "iran", "china", "russia", "eu", "europe", "un", "united", "nations", "military", "army", "troop", "troops", "police", "attack", "bomb", "blast", "explosion", "kill", "killed", "dead", "death", "hostage", "terror", "terrorist", "terrorism", "rebel", "insurgent", "conflict", "crisis", "disaster", "earthquake", "tsunami", "flood", "hurricane", "typhoon", "storm"]
}

year_counts = Counter()
processed_count = 0
match_count = 0

for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_map:
        processed_count += 1
        year = meta_map[aid]
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        tokens = re.findall(r'\w+', text)
        
        scores = {cat: 0 for cat in categories}
        for token in tokens:
            for cat, kws in categories.items():
                if token in kws:
                    scores[cat] += 1
        
        # Tie breaking: prioritize Business > World > Sci/Tech > Sports if tied?
        # Or just use the one with max score.
        best_cat = max(scores, key=scores.get)
        if scores[best_cat] > 0:
            category = best_cat
        else:
            category = "Other" 
            
        if category == "Business":
            year_counts[year] += 1
            match_count += 1

total_business = sum(year_counts.values())
average = total_business / 11.0

print(f"Processed articles: {processed_count}")
print(f"Matched Business articles: {match_count}")
print(f"Year counts: {year_counts}")
print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-12371501432647915462': 'file_storage/function-call-12371501432647915462.json', 'var_function-call-702335989468777751': 14860, 'var_function-call-1127075526552130781': [{'_id': '6944e792b459843e876ccea6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e792b459843e876ccea7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e792b459843e876ccea8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e792b459843e876ccea9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e792b459843e876cceaa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4746464685426923532': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
