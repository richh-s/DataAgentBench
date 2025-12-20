code = """import json
import collections
import re

# Load metadata and articles
with open(locals()['var_function-call-7730568976014147704'], 'r') as f:
    metadata_list = json.load(f)

with open(locals()['var_function-call-6981073237739771094'], 'r') as f:
    articles_list = json.load(f)

articles_map = {}
for a in articles_list:
    aid = str(a.get('article_id', ''))
    title = a.get('title', '')
    desc = a.get('description', '')
    articles_map[aid] = (title + " " + desc).lower()

# Keywords (same as before)
world_kws = [
    "war", "military", "president", "minister", "official", "government", "united nations", "country", "nuclear", 
    "attack", "peace", "china", "russia", "iran", "iraq", "syria", "korea", "afghanistan", "isis", "terror", 
    "protest", "court", "law", "election", "parliament", "foreign", "international", "security", "treaty", 
    "ambassador", "diplomat", "refugee", "crisis", "bomb", "blast", "kill", "dead", "wound", "police", "shoot", 
    "prime minister", "leader", "state", "troops", "army", "navy", "air force", "rebel", "conflict", "explosion", 
    "strike", "hostage", "sanction", "gaza", "israel", "palestine", "ukraine", "putin", "obama", "bush", "clinton", 
    "yemen", "libya", "egypt", "venezuela", "pakistan", "india", "border", "migrant", "crash", "plane", "disaster", 
    "storm", "hurricane", "typhoon", "earthquake", "tsunami", "politics", "political", "democracy", "human rights", 
    "un", "nato", "eu", "african union", "au", "nation", "global", "usa", "america", "uk", "britain", "france", 
    "germany", "japan", "turkey", "saudi arabia", "sudan", "somalia", "congo", "kenya", "zimbabwe", "greece", "italy", 
    "spain", "brazil", "mexico", "canada", "australia", "vatican", "pope", "boko haram", "taliban", "al qaeda"
]
sports_kws = ["game", "match", "score", "win", "loss", "defeat", "victory", "team", "player", "coach", "season", "league", "champion", "medal", "olympic", "race", "cup", "tournament", "sport", "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "stadium", "rugby", "cricket", "f1", "formula one", "driver", "club", "manager", "quarterback", "touchdown", "goal", "points", "ranking", "title", "gold", "silver", "bronze", "wimbledon", "us open", "super bowl", "world cup"]
business_kws = ["market", "stock", "dow", "nasdaq", "sp500", "economy", "dollar", "euro", "yen", "bank", "fed", "rate", "profit", "earnings", "revenue", "loss", "company", "corp", "inc", "ceo", "merger", "deal", "acquisition", "trade", "oil", "gold", "price", "invest", "share", "business", "industry", "finance", "financial", "wall st", "sales", "retail", "consumer", "inflation", "job", "unemployment", "hiring", "tax", "budget", "deficit", "ipo", "bid", "offer", "bankrupt", "debt", "loan", "mortgage", "fund", "equity", "asset", "imf", "world bank", "gm", "ford", "toyota", "boeing", "airbus", "walmart", "exxon", "chevron", "bp", "shell"]
scitech_kws = ["technology", "tech", "science", "research", "study", "space", "nasa", "launch", "orbit", "computer", "software", "hardware", "internet", "web", "online", "app", "mobile", "phone", "google", "apple", "microsoft", "facebook", "twitter", "amazon", "ibm", "intel", "chip", "device", "gadget", "virus", "cancer", "disease", "health", "gene", "robot", "ai", "artificial intelligence", "biotech", "lab", "scientist", "astronomer", "physicist", "discovery", "planet", "galaxy", "telescope", "mission", "satellite", "broadband", "wireless", "network", "server", "data", "cyber", "hack", "security", "update", "version", "windows", "linux", "android", "ios", "iphone", "ipad", "mac", "pc", "laptop", "tablet", "screen", "pixel", "camera", "video game", "console", "nintendo", "sony", "xbox", "playstation", "mars", "moon", "solar", "climate", "warming"]

keywords = {"World": world_kws, "Sports": sports_kws, "Business": business_kws, "Sci_Tech": scitech_kws}

def classify(text):
    scores = {k: 0 for k in keywords}
    words = re.findall(r'\w+', text)
    for w in words:
        for cat, kws in keywords.items():
            if w in kws:
                scores[cat] += 1
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0: return "Unknown"
    return best_cat

cat_counts = collections.defaultdict(int)
unknowns = []

for m in metadata_list:
    aid = str(m['article_id'])
    if aid in articles_map:
        text = articles_map[aid]
        cat = classify(text)
        cat_counts[cat] += 1
        if cat == "Unknown":
            if len(unknowns) < 10:
                unknowns.append(text[:100])

print("Category Counts:")
print(json.dumps(cat_counts))
print("Unknown examples:")
print(json.dumps(unknowns))

print("__RESULT__:")
print(json.dumps(cat_counts))"""

env_args = {'var_function-call-7730568976014147704': 'file_storage/function-call-7730568976014147704.json', 'var_function-call-17267860317809745023': 'file_storage/function-call-17267860317809745023.json', 'var_function-call-16112416981574014912': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6981073237739771094': 'file_storage/function-call-6981073237739771094.json', 'var_function-call-3205073669013618760': [['Africa', 106], ['South America', 92], ['Asia', 85], ['North America', 79], ['Europe', 76]], 'var_function-call-17108972308054004622': [['Africa', 117], ['South America', 111], ['Asia', 97], ['Europe', 89], ['North America', 89]]}

exec(code, env_args)
