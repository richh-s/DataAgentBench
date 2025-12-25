code = """import json
import collections
import re

# Load metadata
with open(locals()['var_function-call-7730568976014147704'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-6981073237739771094'], 'r') as f:
    articles_list = json.load(f)

# Create a dictionary for articles mapping article_id -> (title, description)
# Ensure article_id is string to match metadata
articles_map = {}
for a in articles_list:
    aid = str(a.get('article_id', ''))
    title = a.get('title', '')
    desc = a.get('description', '')
    articles_map[aid] = (title + " " + desc).lower()

# Keywords
keywords = {
    "World": ["war", "military", "president", "minister", "official", "government", "united nations", "country", "nuclear", "attack", "peace", "china", "russia", "iran", "iraq", "syria", "korea", "afghanistan", "isis", "terror", "protest", "court", "law", "election", "parliament", "foreign", "international", "security", "treaty", "ambassador", "diplomat", "refugee", "crisis", "bomb", "blast", "kill", "dead", "wound", "police", "shoot", "prime minister", "leader", "state", "troops", "army", "navy", "air force", "rebel", "conflict", "explosion", "strike", "hostage", "sanction", "gaza", "israel", "palestine", "ukraine", "putin", "obama", "bush", "clinton", "yemen", "libya", "egypt", "venezuela", "pakistan", "india", "border", "migrant", "crash", "plane", "disaster", "storm", "hurricane", "typhoon", "earthquake", "tsunami"],
    "Sports": ["game", "match", "score", "win", "loss", "defeat", "victory", "team", "player", "coach", "season", "league", "champion", "medal", "olympic", "race", "cup", "tournament", "sport", "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "stadium", "rugby", "cricket", "f1", "formula one", "driver", "club", "manager", "quarterback", "touchdown", "goal", "points", "ranking", "title", "gold", "silver", "bronze"],
    "Business": ["market", "stock", "dow", "nasdaq", "sp500", "economy", "dollar", "euro", "yen", "bank", "fed", "rate", "profit", "earnings", "revenue", "loss", "company", "corp", "inc", "ceo", "merger", "deal", "acquisition", "trade", "oil", "gold", "price", "invest", "share", "business", "industry", "finance", "financial", "wall st", "sales", "retail", "consumer", "inflation", "job", "unemployment", "hiring", "tax", "budget", "deficit", "ipo", "bid", "offer", "bankrupt", "debt", "loan", "mortgage", "fund", "equity", "asset"],
    "Sci_Tech": ["technology", "tech", "science", "research", "study", "space", "nasa", "launch", "orbit", "computer", "software", "hardware", "internet", "web", "online", "app", "mobile", "phone", "google", "apple", "microsoft", "facebook", "twitter", "amazon", "ibm", "intel", "chip", "device", "gadget", "virus", "cancer", "disease", "health", "gene", "robot", "ai", "artificial intelligence", "biotech", "lab", "scientist", "astronomer", "physicist", "discovery", "planet", "galaxy", "telescope", "mission", "satellite", "broadband", "wireless", "network", "server", "data", "cyber", "hack", "security", "update", "version", "windows", "linux", "android", "ios", "iphone", "ipad", "mac", "pc", "laptop", "tablet", "screen", "pixel", "camera", "video game", "console", "nintendo", "sony", "xbox", "playstation"]
}

def classify(text):
    scores = {k: 0 for k in keywords}
    words = re.findall(r'\w+', text)
    for w in words:
        for cat, kws in keywords.items():
            if w in kws:
                scores[cat] += 1
    
    # Heuristics for ties or zeros
    # If "oil" is present, favor Business unless "iraq"/"war" etc.
    if scores["World"] == scores["Business"] and scores["World"] > 0:
        # Check context? simpler: favor World if conflict words
        pass 
    
    # Pick max
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

region_counts = collections.defaultdict(int)
world_counts = collections.defaultdict(int)

debug_classifications = []

for m in metadata_list:
    aid = str(m['article_id'])
    region = m['region']
    
    if aid in articles_map:
        text = articles_map[aid]
        cat = classify(text)
        if cat == "World":
            world_counts[region] += 1
            if len(debug_classifications) < 10:
                debug_classifications.append((text[:50], region, cat))
    else:
        # Article content missing?
        pass

# Find region with max World articles
sorted_regions = sorted(world_counts.items(), key=lambda x: x[1], reverse=True)

print("Top regions for World articles:")
print(json.dumps(sorted_regions))
print("Debug samples:")
print(json.dumps(debug_classifications))

print("__RESULT__:")
print(json.dumps(sorted_regions))"""

env_args = {'var_function-call-7730568976014147704': 'file_storage/function-call-7730568976014147704.json', 'var_function-call-17267860317809745023': 'file_storage/function-call-17267860317809745023.json', 'var_function-call-16112416981574014912': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6981073237739771094': 'file_storage/function-call-6981073237739771094.json'}

exec(code, env_args)
