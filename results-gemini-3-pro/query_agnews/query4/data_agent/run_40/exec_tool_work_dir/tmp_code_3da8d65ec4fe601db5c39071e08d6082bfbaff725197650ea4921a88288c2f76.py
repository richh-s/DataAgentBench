code = """import json
import collections
import re

# File paths
metadata_path = locals()['var_function-call-842491368832431950']
articles_path = locals()['var_function-call-17213121137072458530']

# 1. Load Metadata
with open(metadata_path, 'r') as f:
    metadata_list = json.load(f)

# Filter for 2015 is already done in SQL, but let's double check or just map
# Create map: article_id (str) -> region
id_to_region = {}
for m in metadata_list:
    # SQL result has article_id as int likely, unless returned as string by tool
    # The preview showed "article_id": "13" (string). So it's string.
    aid = str(m['article_id'])
    id_to_region[aid] = m['region']

# 2. Load Articles
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# 3. Define Keywords
keywords_world = set([
    "politics", "minister", "ministry", "official", "parliament", "congress", "senate", "president", "premier", "governor", "leader", 
    "election", "vote", "poll", "campaign", "party", "democrat", "republican", "conservative", "labour", "liberal", "socialist", "communist", 
    "dictator", "regime", "coup", "war", "battle", "military", "army", "navy", "troop", "soldier", "rebel", "guerrilla", "militia", 
    "terror", "bomb", "attack", "kill", "dead", "wound", "injured", "death", "casualty", "victim", "hostage", "kidnap", 
    "peace", "treaty", "ceasefire", "talks", "summit", "conference", "diplomat", "embassy", "ambassador", "foreign", "international", 
    "un", "united nations", "eu", "european union", "nato", "police", "court", "judge", "trial", "prison", "jail", "arrest", 
    "crime", "murder", "human rights", "protest", "riot", "demonstration", "strike", "refugee", "migrant", "immigration", "border", 
    "disaster", "earthquake", "tsunami", "hurricane", "typhoon", "cyclone", "flood", "fire", "crash", "accident", "epidemic", 
    "virus", "outbreak", "flu", "ebola", "zika", "aids", "hiv", "health", "hospital", "education", "school", "university", 
    "religion", "pope", "church", "mosque", "temple", "islam", "muslim", "christian", "jew", "israel", "palestine", "gaza", 
    "iraq", "syria", "iran", "afghanistan", "pakistan", "india", "china", "russia", "ukraine", "korea", "africa", "asia", "europe"
])

keywords_business = set([
    "business", "company", "firm", "corporation", "inc", "ltd", "market", "stock", "share", "equity", "bond", "fund", "exchange", 
    "dow", "nasdaq", "ftse", "nikkei", "wall street", "economy", "economic", "finance", "financial", "bank", "central bank", "fed", 
    "reserve", "rate", "interest", "inflation", "deflation", "tax", "budget", "deficit", "debt", "loan", "credit", "profit", "loss", 
    "earning", "revenue", "sales", "trade", "export", "import", "tariff", "deal", "merger", "acquisition", "buyout", "bid", "offer", 
    "price", "cost", "consumer", "spending", "retail", "store", "shop", "factory", "industry", "production", "manufacturing", 
    "oil", "gas", "energy", "petroleum", "gold", "silver", "commodity", "dollar", "euro", "yen", "yuan", "currency", 
    "manager", "executive", "ceo", "cfo", "job", "employment", "unemployment"
])

keywords_sports = set([
    "sport", "game", "match", "team", "club", "player", "coach", "manager", "league", "cup", "tournament", "championship", 
    "season", "playoff", "final", "medal", "olympic", "world cup", "super bowl", "score", "win", "loss", "defeat", "victory", 
    "draw", "tie", "goal", "touchdown", "run", "basket", "point", "record", "ranking", "stadium", "arena", "field", 
    "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", "rugby", "hockey", "boxing", "wrestling", "racing", 
    "driver", "f1", "athlete"
])

keywords_scitech = set([
    "technology", "tech", "science", "scientific", "research", "study", "discovery", "invention", "innovation", "computer", 
    "software", "hardware", "program", "app", "application", "system", "network", "internet", "web", "online", "cyber", "digital", 
    "data", "database", "server", "cloud", "mobile", "phone", "smartphone", "tablet", "device", "gadget", "electronics", 
    "robot", "robotics", "ai", "artificial intelligence", "space", "nasa", "esa", "mission", "launch", "rocket", "satellite", 
    "orbit", "planet", "mars", "moon", "solar", "galaxy", "universe", "telescope", "biology", "chemistry", "physics", "medicine", 
    "medical", "drug", "treatment", "cure", "cancer", "gene", "dna", "clone", "environment", "climate", "global warming", 
    "google", "apple", "microsoft", "amazon", "facebook", "twitter"
])

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Simple tokenization
    tokens = set(re.findall(r'\b\w+\b', text))
    
    score_world = len(tokens.intersection(keywords_world))
    score_business = len(tokens.intersection(keywords_business))
    score_sports = len(tokens.intersection(keywords_sports))
    score_scitech = len(tokens.intersection(keywords_scitech))
    
    scores = {
        "World": score_world,
        "Business": score_business,
        "Sports": score_sports,
        "Sci/Tech": score_scitech
    }
    
    # Get max score
    best_cat = max(scores, key=scores.get)
    # If all 0, default to World? Or Unknown.
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

# 4. Process
world_counts = collections.defaultdict(int)

processed_count = 0
for article in articles_list:
    aid = str(article['article_id'])
    if aid in id_to_region:
        cat = classify(article.get('title', ''), article.get('description', ''))
        if cat == "World":
            region = id_to_region[aid]
            world_counts[region] += 1
        processed_count += 1

# 5. Result
# Find region with max count
if world_counts:
    max_region = max(world_counts, key=world_counts.get)
    max_val = world_counts[max_region]
    result = {"max_region": max_region, "count": max_val, "all_counts": dict(world_counts)}
else:
    result = {"max_region": None, "count": 0, "all_counts": {}}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4885082808569749260': ['articles'], 'var_function-call-4885082808569747599': ['authors', 'article_metadata'], 'var_function-call-842491368832431950': 'file_storage/function-call-842491368832431950.json', 'var_function-call-842491368832431283': [{'_id': '69451cdaa3c653854d72a5f8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451cdaa3c653854d72a5f9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451cdaa3c653854d72a5fa', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451cdaa3c653854d72a5fb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451cdaa3c653854d72a5fc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12270661439186357136': [{'_id': '69451cdaa3c653854d72a5f8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451cdaa3c653854d72a5f9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451cdaa3c653854d72a5fa', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451cdaa3c653854d72a5fb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451cdaa3c653854d72a5fc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11107782028933462935': 6696, 'var_function-call-10443133168677105019': [{'_id': '69451cdaa3c653854d72a5f8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451cdaa3c653854d72a5f9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451cdaa3c653854d72a5fa', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451cdaa3c653854d72a5fb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451cdaa3c653854d72a5fc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17213121137072458530': 'file_storage/function-call-17213121137072458530.json'}

exec(code, env_args)
