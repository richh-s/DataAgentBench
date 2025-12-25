code = """import json
import re

# Load metadata (IDs and regions for 2015)
path_meta = locals()['var_function-call-11325284411578124133']
with open(path_meta, 'r') as f:
    meta_list = json.load(f)

# Map article_id to region. Ensure article_id is string.
# In metadata file, article_id is likely string or int. Check one.
# The previous output showed "article_id": "13". So string.
id_to_region = {str(item['article_id']): item['region'] for item in meta_list}

# Load articles
path_articles = locals()['var_function-call-16366507442669348325']
with open(path_articles, 'r') as f:
    articles = json.load(f)

# Keywords
world_keywords = [
    "iraq", "syria", "gaza", "israel", "palestinian", "hamas", "hezbollah", "egypt", "iran", "nuclear",
    "war", "troops", "soldiers", "rebels", "insurgents", "militia", "conflict", "fight", "battle",
    "attack", "bomb", "blast", "explosion", "kill", "dead", "wound", "injure", "crash",
    "storm", "hurricane", "flood", "earthquake", "tsunami", "virus", "ebola", "outbreak",
    "un", "united nations", "nato", "eu", "european union", "sanctions", "peace", "talks", "treaty",
    "minister", "president", "parliament", "government", "official", "leader", "vote", "election",
    "police", "protest", "riot", "refugee", "migrant", "crisis", "terror", "al-qaeda", "isis", "taliban",
    "afghanistan", "pakistan", "ukraine", "russia", "china", "korea", "sudan", "nigeria", "libya", "yemen",
    "baghdad", "cairo", "kabul", "tehran", "jerusalem", "beijing", "moscow"
]

business_keywords = [
    "profit", "quarter", "earnings", "revenue", "loss", "stock", "share", "market", "dow", "nasdaq",
    "economy", "economic", "bank", "rate", "fed", "inflation", "company", "corp", "inc", "business",
    "deal", "merger", "acquisition", "buy", "sell", "price", "oil", "gold", "dollar", "euro", "yen", "ceo"
]

sports_keywords = [
    "game", "match", "team", "club", "league", "cup", "championship", "tournament", "olympic", "medal",
    "player", "coach", "score", "win", "lose", "victory", "season", "football", "soccer", "baseball",
    "basketball", "tennis", "golf", "cricket", "rugby", "hockey", "sport"
]

tech_keywords = [
    "software", "hardware", "computer", "internet", "web", "online", "google", "apple", "microsoft",
    "technology", "science", "space", "nasa", "orbit", "research", "scientist", "phone", "mobile"
]

def classify(text):
    text = text.lower()
    scores = {
        "World": sum(1 for k in world_keywords if k in text),
        "Business": sum(1 for k in business_keywords if k in text),
        "Sports": sum(1 for k in sports_keywords if k in text),
        "Sci/Tech": sum(1 for k in tech_keywords if k in text)
    }
    # Prioritize World if specific strong keywords exist (e.g. country names in conflict)
    # But for simplicity, just take max.
    # If tie, simple priority: World > Business > Sports > Sci/Tech (arbitrary, but standard datasets are balanced)
    # Actually, let's normalize or check max.
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

region_counts = {}

processed_count = 0
world_count = 0

for art in articles:
    aid = str(art['article_id'])
    if aid in id_to_region:
        processed_count += 1
        text = art['title'] + " " + art['description']
        cat = classify(text)
        if cat == "World":
            reg = id_to_region[aid]
            region_counts[reg] = region_counts.get(reg, 0) + 1
            world_count += 1

print(f"Processed: {processed_count}, World Articles: {world_count}")
print("Region counts:", region_counts)

# Find max
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
    print("__RESULT__:")
    print(json.dumps(max_region))
else:
    print("__RESULT__:")
    print(json.dumps("None"))"""

env_args = {'var_function-call-11857698137717793773': ['articles'], 'var_function-call-11857698137717793476': ['authors', 'article_metadata'], 'var_function-call-2529652412575013352': [{'cid': '0', 'name': 'article_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'author_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'region', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'publication_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-2529652412575012341': [{'_id': '694527032437f6369c490852', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-11325284411578124133': 'file_storage/function-call-11325284411578124133.json', 'var_function-call-18150071240585189806': 'file_storage/function-call-18150071240585189806.json', 'var_function-call-11267329438680205786': [{'_id': '694527032437f6369c490852', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694527032437f6369c490853', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694527032437f6369c490854', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694527032437f6369c490855', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694527032437f6369c490856', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7489568592445506500': {'count': 6696}, 'var_function-call-16366507442669348325': 'file_storage/function-call-16366507442669348325.json'}

exec(code, env_args)
