code = """import json
import re
from collections import Counter

# Load Metadata
with open(locals()['var_function-call-2683070877417335365'], 'r') as f:
    sql_results = json.load(f)

meta_map = {}
for row in sql_results:
    try:
        aid = int(row['article_id'])
        meta_map[aid] = row['region']
    except:
        pass

# Load Articles
with open(locals()['var_function-call-12084950105935105518'], 'r') as f:
    articles = json.load(f)

# Expanded Keywords
keywords = {
    "World": [
        "world", "international", "un", "nation", "global", "china", "iraq", "iran", "korea", 
        "afghanistan", "palestine", "israel", "ukraine", "russia", "eu", "europe", "africa", 
        "asia", "middle east", "latin america", "diplomacy", "treaty", "peace", "war", "military", 
        "president", "minister", "parliament", "foreign", "overseas", "terrorist", "bomb", "attack", 
        "government", "official", "authority", "election", "prime minister", "baghdad", "gaza",
        "troops", "hostage", "kill", "blast", "explosion", "nuclear", "weapon", "crisis", "talks",
        "leader", "vote", "poll", "protest", "riot", "party", "state", "border", "security", 
        "council", "union", "human rights", "refugee", "migration", "syria", "egypt", "libya", 
        "sudan", "yemen", "nigeria", "pakistan", "india", "venezuela", "brazil", "argentina",
        "mexico", "canada", "australia", "germany", "france", "uk", "britain", "spain", "italy",
        "greece", "turkey", "saudi", "arabia", "isis", "isil", "al-qaeda", "taliban", "bokoharam",
        "jihad", "coup", "sanctions", "embassy", "ambassador", "nato", "kofi annan", "ban ki-moon"
    ],
    "Sports": [
        "sport", "game", "match", "cup", "league", "team", "score", "win", "lose", "olympic", 
        "championship", "football", "baseball", "basketball", "soccer", "tennis", "golf", 
        "athlete", "coach", "medal", "tournament", "player", "season", "club", "nba", "nfl", 
        "mlb", "nhl", "fifa", "run", "race", "title", "final", "victory", "defeat", "boxing",
        "wrestling", "hockey", "cricket", "rugby", "stadium", "points", "record"
    ],
    "Business": [
        "business", "market", "stock", "economy", "trade", "money", "deal", "profit", "loss", 
        "bank", "financial", "wall st", "corporate", "company", "industry", "price", "rate", 
        "investor", "ceo", "merger", "acquisition", "dollar", "euro", "inflation", "earnings",
        "share", "revenue", "sales", "fed", "federal reserve", "exchange", "dow", "nasdaq",
        "job", "hiring", "unemployment", "tax", "budget", "deficit", "gdp", "consumer", "retail",
        "gm", "ford", "toyota", "boeing", "airbus"
    ],
    "Sci/Tech": [
        "science", "technology", "tech", "computer", "web", "internet", "software", "hardware", 
        "space", "nasa", "study", "research", "medical", "health", "virus", "disease", "cancer", 
        "new", "innovation", "gadget", "phone", "apple", "google", "microsoft", "linux", "biology", 
        "physics", "astronomy", "scientist", "discovery", "drug", "fda", "online", "digital",
        "launch", "mission", "satellite", "orbit", "moon", "mars", "robot", "ai", "artificial intelligence",
        "climate", "environment", "global warming", "carbon", "fossil" # Maybe World? usually Sci/Tech or World.
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    words = re.findall(r'\w+', text)
    for word in words:
        for cat, kws in keywords.items():
            if word in kws:
                scores[cat] += 1
    
    # Specific bigrams
    if "prime minister" in text: scores["World"] += 2
    if "wall street" in text: scores["Business"] += 2
    if "united nations" in text: scores["World"] += 2
    if "white house" in text: scores["World"] += 1 # or Politics/World
    
    if all(v == 0 for v in scores.values()):
        return "Unclassified"
        
    return max(scores, key=scores.get)

# Process
region_cat_counts = {}

for art in articles:
    try:
        aid = int(art['article_id'])
    except:
        continue
        
    if aid in meta_map:
        text = (art.get('title', '') + " " + art.get('description', ''))
        category = classify(text)
        
        r = meta_map[aid]
        if r not in region_cat_counts:
            region_cat_counts[r] = Counter()
        region_cat_counts[r][category] += 1

print("__RESULT__:")
print(json.dumps(region_cat_counts))"""

env_args = {'var_function-call-2683070877417335365': 'file_storage/function-call-2683070877417335365.json', 'var_function-call-7837263819668175178': 6696, 'var_function-call-14907435017980586290': [{'_id': '6944f3d4dccdaaaa57646236', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f3d4dccdaaaa57646237', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f3d4dccdaaaa57646238', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f3d4dccdaaaa57646239', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f3d4dccdaaaa5764623a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4342570047527953099': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-9448599737516148075': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-530398534050118018': 'Done', 'var_function-call-12158221531579383913': {'count': 5, 'is_file': False}, 'var_function-call-12084950105935105518': 'file_storage/function-call-12084950105935105518.json', 'var_function-call-17835602813264065294': {'South America': 600, 'Africa': 587, 'Asia': 570, 'North America': 592, 'Europe': 598}, 'var_function-call-8415515240364671108': {'Europe': {'Sci/Tech': 256, 'Business': 236, 'Sports': 267, 'Unclassified': 226, 'World': 372}, 'South America': {'Business': 215, 'World': 384, 'Sci/Tech': 275, 'Sports': 242, 'Unclassified': 216}, 'Africa': {'Sci/Tech': 234, 'Unclassified': 213, 'World': 374, 'Sports': 277, 'Business': 247}, 'Asia': {'World': 372, 'Sci/Tech': 256, 'Business': 238, 'Unclassified': 198, 'Sports': 269}, 'North America': {'Unclassified': 225, 'Business': 215, 'Sci/Tech': 255, 'World': 367, 'Sports': 267}}}

exec(code, env_args)
