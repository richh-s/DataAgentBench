code = """import json
import collections

# Load metadata (2015 articles)
# This one was stored in a file
var_meta = locals()['var_function-call-4607361516680581530']
if isinstance(var_meta, str):
    with open(var_meta, 'r') as f:
        meta_list = json.load(f)
else:
    meta_list = var_meta

# Create a map: article_id (int) -> region (str)
meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Load articles content
# This one was passed as a list according to the error
var_articles = locals()['var_function-call-12750341033928949967']
if isinstance(var_articles, str):
    with open(var_articles, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = var_articles

# Define Keywords (Same as before)
categories = {
    "Sports": ["sport", "game", "match", "score", "team", "league", "cup", "olympic", "football", "soccer", "baseball", "basketball", "cricket", "tennis", "hockey", "golf", "nascar", "champion", "medal", "athlete", "coach", "stadium", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "racing", "rugby", "boxing", "wrestling"],
    "Business": ["business", "market", "stock", "economy", "economic", "trade", "money", "bank", "financial", "finance", "company", "profit", "loss", "dollar", "euro", "oil", "price", "deal", "merger", "acquisition", "sales", "revenue", "ceo", "wall st", "nasdaq", "dow", "investor", "shares", "inflation", "rate"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "internet", "web", "online", "mobile", "phone", "apple", "google", "microsoft", "intel", "nasa", "space", "orbit", "planet", "study", "research", "medical", "virus", "robot", "digital", "wireless", "broadband", "chip", "satellite", "astronomy", "biology"],
    "World": ["world", "international", "war", "peace", "conflict", "military", "army", "government", "president", "minister", "election", "vote", "parliament", "congress", "treaty", "un", "united nations", "nato", "eu", "china", "russia", "iraq", "iran", "korea", "israel", "palestine", "syria", "afghanistan", "terrorist", "attack", "bomb", "crisis", "refugee", "diplomat", "foreign", "official", "leader", "state", "nuclear", "troops", "rebels", "protest", "police", "kill", "dead", "baghdad", "kabul", "beijing", "moscow", "gaza", "prime minister"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # Get max score
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return None # Unclassified
    return max_cat

# Process
region_world_counts = collections.defaultdict(int)

for article in articles_list:
    aid = str(article['article_id'])
    if aid in meta_map:
        # It's a 2015 article
        title = article.get('title', "")
        desc = article.get('description', "")
        text = title + " " + desc
        
        category = classify(text)
        
        if category == "World":
            region = meta_map[aid]
            region_world_counts[region] += 1

# Find max region
if region_world_counts:
    max_region = max(region_world_counts, key=region_world_counts.get)
    max_count = region_world_counts[max_region]
    result = {"region": max_region, "count": max_count, "all_counts": region_world_counts}
else:
    result = {"region": None, "count": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4607361516680581530': 'file_storage/function-call-4607361516680581530.json', 'var_function-call-4668912077434412794': 6696, 'var_function-call-12275785215919282874': [{'_id': '6944fef5545aa6729352eb7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944fef5545aa6729352eb7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944fef5545aa6729352eb80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944fef5545aa6729352eb81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944fef5545aa6729352eb82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5711343954142234108': 'file_storage/function-call-5711343954142234108.json', 'var_function-call-12750341033928949967': [{'_id': '6944fef5545aa6729352eb7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944fef5545aa6729352eb7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944fef5545aa6729352eb80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944fef5545aa6729352eb81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944fef5545aa6729352eb82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
