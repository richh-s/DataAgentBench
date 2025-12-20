code = """import json
import re
import collections

# Load Metadata (SQL result)
# path: file_storage/function-call-8192239243877575471.json
try:
    with open(locals()['var_function-call-8192239243877575471'], 'r') as f:
        metadata_list = json.load(f)
except:
    # fallback for testing if variable name changed or previous tool failed
    # In this environment I must use the exact variable name provided in history
    pass

# Load Articles (MongoDB result)
# path: file_storage/function-call-13229976580628931333.json
try:
    with open(locals()['var_function-call-13229976580628931333'], 'r') as f:
        articles_list = json.load(f)
except:
    pass

# Map article_id to content
articles_map = {}
for art in articles_list:
    aid = str(art.get('article_id', ''))
    title = art.get('title', '')
    desc = art.get('description', '')
    articles_map[aid] = title + " " + desc

# Keyword definitions
keywords = {
    "World": set([
        "president", "minister", "election", "parliament", "government", "official", "leader", 
        "war", "military", "troops", "army", "soldier", "rebel", "militia", "attack", "kill", "bomb", "blast", "explosion", 
        "terror", "hostage", "kidnap", "peace", "treaty", "nuclear", "weapon", "protest", "riot", "strike", 
        "storm", "hurricane", "flood", "earthquake", "tsunami", "crash", "disaster", "aid", "refugee", 
        "un", "nato", "eu", "iraq", "iran", "syria", "israel", "palestine", "gaza", "afghanistan", "pakistan", 
        "russia", "ukraine", "china", "korea", "sudan", "libya", "egypt"
    ]),
    "Business": set([
        "market", "stock", "dow", "nasdaq", "invest", "trade", "economy", "dollar", "euro", "bank", "fed", "rate", 
        "inflation", "profit", "loss", "sales", "deal", "merger", "acquisition", "ipo", "share", "oil", "price", 
        "company", "corp", "inc", "business", "ceo", "manager", "google", "microsoft", "yahoo", "apple", "ibm", 
        "boeing", "airbus", "walmart", "retail"
    ]),
    "Sports": set([
        "sport", "game", "match", "team", "league", "cup", "olympic", "medal", "score", "win", "lose", "victory", 
        "defeat", "champion", "coach", "player", "football", "soccer", "basketball", "baseball", "hockey", "tennis", 
        "golf", "cricket"
    ]),
    "Sci_Tech": set([
        "science", "technology", "computer", "software", "internet", "web", "online", "mobile", "phone", "wireless", 
        "chip", "data", "server", "virus", "hacker", "space", "nasa", "orbit", "planet", "galaxy", "drug", "medicine", 
        "cancer", "disease", "study", "research", "scientist", "laboratory"
    ])
}

def classify(text):
    text = text.lower()
    # Simple tokenization
    tokens = re.findall(r'\w+', text)
    scores = {k: 0 for k in keywords}
    for t in tokens:
        for cat, kws in keywords.items():
            if t in kws:
                scores[cat] += 1
    
    # Tie breaking or dominance
    # If max score is 0, default to something? Or unknown.
    # If tie, preference order?
    
    if max(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

# Process
world_counts = collections.defaultdict(int)

for item in metadata_list:
    aid = str(item.get('article_id', ''))
    region = item.get('region', 'Unknown')
    
    if aid in articles_map:
        content = articles_map[aid]
        category = classify(content)
        if category == "World":
            world_counts[region] += 1

# Find region with max count
if world_counts:
    max_region = max(world_counts, key=world_counts.get)
    max_val = world_counts[max_region]
    result = {"region": max_region, "count": max_val, "all_counts": dict(world_counts)}
else:
    result = {"region": "None", "count": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8192239243877575471': 'file_storage/function-call-8192239243877575471.json', 'var_function-call-4285467361081759445': 6696, 'var_function-call-13346176432867388839': [{'_id': '69450821ec4d8e6298d328d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450821ec4d8e6298d328d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450821ec4d8e6298d328d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450821ec4d8e6298d328da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450821ec4d8e6298d328db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-152803809967091269': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13229976580628931333': 'file_storage/function-call-13229976580628931333.json'}

exec(code, env_args)
