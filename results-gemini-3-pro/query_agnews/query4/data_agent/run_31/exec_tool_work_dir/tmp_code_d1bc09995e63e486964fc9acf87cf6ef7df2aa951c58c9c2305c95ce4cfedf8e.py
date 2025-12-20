code = """import json
import re
from collections import Counter

# Load metadata
with open(locals()['var_function-call-6478820518397450019'], 'r') as f:
    metadata_list = json.load(f)

# Create a map: article_id -> region
# Ensure article_id is string, as seen in previous outputs
article_region = {item['article_id']: item['region'] for item in metadata_list}

# Load articles
with open(locals()['var_function-call-8772719174433401329'], 'r') as f:
    articles_list = json.load(f)

# Define keywords
categories = {
    "World": [
        "president", "minister", "prime", "official", "police", "military", "security", "war", "iraq", "israel", 
        "palestinian", "iran", "nuclear", "government", "election", "party", "vote", "leader", "talks", "peace", 
        "treaty", "un", "united nations", "bomb", "attack", "kill", "blast", "troops", "forces", "rebel", "strike", 
        "crash", "disaster", "storm", "hurricane", "china", "russia", "north korea", "syria", "afghanistan", 
        "pakistan", "baghdad", "gaza", "cairo", "moscow", "beijing", "parliament", "senate", "law", "court", "trial",
        "judge", "protest", "demonstration", "riot", "crisis", "conflict", "diplomat", "embassy", "foreign", "international"
    ],
    "Sports": [
        "sport", "game", "match", "team", "win", "lose", "victory", "defeat", "score", "cup", "league", "season", 
        "champion", "title", "medal", "olympic", "football", "soccer", "basketball", "baseball", "tennis", "golf", 
        "hockey", "coach", "player", "athlete", "club", "stadium", "points", "record", "final", "round", "tournament", 
        "racing", "driver", "f1", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", "open", "series"
    ],
    "Business": [
        "business", "company", "market", "stock", "share", "price", "profit", "loss", "earn", "bank", "economy", 
        "trade", "dollar", "euro", "yen", "oil", "gas", "energy", "corp", "inc", "ltd", "merger", "acquisition", 
        "deal", "sale", "buy", "sell", "invest", "fund", "rate", "inflation", "fed", "federal reserve", "wall st", 
        "nasdaq", "dow", "ceo", "cfo", "budget", "finance", "revenue", "analyst", "forecast", "growth", "sector"
    ],
    "Sci/Tech": [
        "technology", "science", "computer", "software", "hardware", "internet", "web", "online", "net", "google", 
        "microsoft", "apple", "intel", "ibm", "virus", "worm", "hacker", "security", "space", "nasa", "orbit", 
        "mars", "moon", "launch", "satellite", "phone", "mobile", "wireless", "network", "chip", "processor", 
        "server", "game", "video", "digital", "research", "study", "cancer", "disease", "drug", "health", "hospital", 
        "doctor", "patient", "treatment", "biotech", "genetics", "physics", "astronomy", "lab", "experiment"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple substring check or regex word boundary?
            # Regex is safer to avoid 'wing' in 'growing'
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Get max score
    if sum(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

# Process
world_counts = Counter()

for article in articles_list:
    aid = str(article['article_id'])
    
    # Check if this article is in our 2015 metadata list
    if aid in article_region:
        # Classify
        content = (article.get('title', '') + " " + article.get('description', ''))
        category = classify(content)
        
        if category == "World":
            region = article_region[aid]
            world_counts[region] += 1

print("__RESULT__:")
print(json.dumps(world_counts))"""

env_args = {'var_function-call-9850316120653619328': ['authors', 'article_metadata'], 'var_function-call-9850316120653621663': ['articles'], 'var_function-call-6478820518397450019': 'file_storage/function-call-6478820518397450019.json', 'var_function-call-83190611252947939': 6696, 'var_function-call-1618363836141742396': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8772719174433401329': 'file_storage/function-call-8772719174433401329.json'}

exec(code, env_args)
