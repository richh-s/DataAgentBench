code = """import json
import re
from datetime import datetime

# Load data
with open(locals()['var_function-call-10971295442504843932'], 'r') as f:
    metadata = json.load(f)

with open(locals()['var_function-call-12410638508946799314'], 'r') as f:
    articles = json.load(f)

# Join data
meta_dict = {}
for m in metadata:
    # Ensure article_id is int
    try:
        aid = int(m['article_id'])
        meta_dict[aid] = m['publication_date']
    except ValueError:
        continue

joined = []
for a in articles:
    try:
        aid = int(a['article_id'])
        if aid in meta_dict:
            joined.append({
                'title': a.get('title', ''),
                'description': a.get('description', ''),
                'year': int(meta_dict[aid].split('-')[0])
            })
    except (ValueError, IndexError, AttributeError):
        continue

# Keywords
categories = {
    'Business': [
        "business", "economy", "economic", "market", "stock", "wall street", "dow", "nasdaq",
        "finance", "financial", "invest", "investment", "investor", "trade", "currency", "dollar", "euro",
        "bank", "banking", "rates", "inflation", "recession", "gdp", "tax", "profit", "revenue", 
        "earnings", "debt", "shares", "ipo", "merger", "acquisition", "company", "corporate", "industry", 
        "oil", "crude", "gold", "fed", "federal reserve", "treasury", "bond", "loan", "sales", "retail", 
        "ceo", "cfo", "manager", "imf", "wto", "price", "prices", "cost"
    ],
    'Sports': [
        "sport", "sports", "football", "soccer", "basketball", "nba", "baseball", "mlb", "hockey", "nhl", 
        "tennis", "golf", "cricket", "rugby", "team", "game", "match", "cup", "league", "season", 
        "coach", "player", "athlete", "olympic", "champion", "tournament", "win", "won", "lose", "lost", 
        "score", "victory", "defeat", "medal", "f1", "racing", "driver"
    ],
    'Sci/Tech': [
        "technology", "tech", "science", "computer", "software", "hardware", "internet", "web", "mobile", 
        "phone", "smartphone", "apple", "google", "microsoft", "ibm", "intel", "linux", "windows", "virus", 
        "security", "hacker", "space", "nasa", "orbit", "mars", "moon", "astronomy", "biology", "physics", 
        "research", "study", "scientist", "discovery", "online", "digital", "network", "server", "chip"
    ],
    'World': [
        "world", "international", "president", "minister", "prime minister", "election", "vote", "war", 
        "military", "army", "troop", "soldier", "bomb", "attack", "blast", "kill", "police", "court", 
        "government", "parliament", "congress", "senate", "official", "nuclear", "treaty", "peace", 
        "conflict", "crisis", "disaster", "storm", "quake", "earthquake", "flood", "un", "united nations", 
        "eu", "european union", "protest", "strike", "terror", "terrorism", "rebel", "insurgent"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    
    # Simple tokenization by splitting on non-alphanumeric
    tokens = re.findall(r'\w+', text)
    
    for token in tokens:
        for cat, keywords in categories.items():
            if token in keywords:
                scores[cat] += 1
                
    # Prioritize Business if Oil/Prices/Economy mentions
    # "Oil prices soar" -> Oil(Biz), prices(Biz), soar. Business=2.
    # "Iraq War" -> Iraq, War(World). World=1.
    
    # Find max score
    max_score = -1
    best_cat = "World" # Default fallback
    
    # Check if all 0
    if all(s == 0 for s in scores.values()):
        return "World" # Or Unknown
        
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            # Tie breaking logic?
            # If Business vs World, and keywords like 'market', 'economy' -> Business.
            # If 'war', 'killed' -> World.
            # For now, just take first or define priority. 
            # Priority: Business > Sci/Tech > Sports > World (World is most generic)
            if cat == 'Business':
                best_cat = 'Business'
            elif cat == 'Sci/Tech' and best_cat != 'Business':
                best_cat = 'Sci/Tech'
            elif cat == 'Sports' and best_cat not in ['Business', 'Sci/Tech']:
                best_cat = 'Sports'
                
    return best_cat

# Count
business_counts = {y: 0 for y in range(2010, 2021)}

for item in joined:
    cat = classify(item['title'] + " " + item['description'])
    if cat == 'Business':
        if 2010 <= item['year'] <= 2020:
            business_counts[item['year']] += 1

avg = sum(business_counts.values()) / 11.0

print("__RESULT__:")
print(json.dumps({"counts": business_counts, "average": avg}))"""

env_args = {'var_function-call-10971295442504843932': 'file_storage/function-call-10971295442504843932.json', 'var_function-call-12801721283441403514': 'file_storage/function-call-12801721283441403514.json', 'var_function-call-5853784756770378776': 14860, 'var_function-call-12959133723405479980': [{'_id': '6944c4cc44a403dfe45c066e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c4cc44a403dfe45c066f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c4cc44a403dfe45c0670', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c4cc44a403dfe45c0671', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c4cc44a403dfe45c0672', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12410638508946799314': [{'_id': '6944c4cc44a403dfe45c066e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c4cc44a403dfe45c066f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c4cc44a403dfe45c0670', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c4cc44a403dfe45c0671', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c4cc44a403dfe45c0672', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
