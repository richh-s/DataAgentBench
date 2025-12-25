code = """import json
import re

file_path = locals()['var_function-call-16150427591355603199']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
sports_kw = {"sport", "sports", "football", "soccer", "basketball", "baseball", "tennis", "hockey", "olympic", "olympics", "game", "match", "team", "player", "coach", "score", "win", "loss", "victory", "defeat", "nfl", "nba", "mlb", "nhl", "medal", "champion", "tournament", "athlete", "racing", "driver", "cup", "league", "athletics", "marathon", "rugby", "cricket", "boxing", "wrestling"}
business_kw = {"market", "stock", "price", "company", "profit", "economy", "bank", "trade", "dollar", "oil", "invest", "share", "revenue", "business", "deal", "ceo", "wall st", "dow", "nasdaq", "inflation", "sales"}
scitech_kw = {"technology", "science", "computer", "software", "internet", "web", "phone", "mobile", "space", "nasa", "google", "microsoft", "chip", "network", "virus", "study", "research"}
world_kw = {"war", "peace", "president", "government", "election", "country", "iraq", "china", "usa", "police", "attack", "bomb", "minister", "military", "crisis", "nuclear", "killed", "dead"}

def get_category(text):
    text = text.lower()
    scores = {"Sports": 0, "Business": 0, "Sci/Tech": 0, "World": 0}
    
    words = re.findall(r'\w+', text)
    for w in words:
        if w in sports_kw: scores["Sports"] += 1
        if w in business_kw: scores["Business"] += 1
        if w in scitech_kw: scores["Sci/Tech"] += 1
        if w in world_kw: scores["World"] += 1
    
    # Simple heuristics for disambiguation
    if "oil" in text and "price" in text: scores["Business"] += 2
    if "iraq" in text and "oil" in text: scores["World"] += 1
    if "game" in text and "video" in text: scores["Sci/Tech"] += 3
    if "olympic" in text: scores["Sports"] += 5 
    
    # Return category with max score
    best = max(scores, key=scores.get)
    if scores[best] == 0: return "Unknown"
    return best

max_len = -1
best_title = None

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    if not desc: continue
    
    # Combine title and description for classification
    text = title + " " + desc
    cat = get_category(text)
    
    if cat == "Sports":
        # Check description length
        if len(desc) > max_len:
            max_len = len(desc)
            best_title = title

print("__RESULT__:")
print(json.dumps(best_title))"""

env_args = {'var_function-call-16506696001246171495': ['articles'], 'var_function-call-16238021228284893753': [{'_id': '6944729e341d2706dd78f649', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-12806958727600017459': ['authors', 'article_metadata'], 'var_function-call-6156227315711757339': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-14223567582029322341': [{'_id': '6944729e341d2706dd78f649', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944729e341d2706dd78f64a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944729e341d2706dd78f64b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944729e341d2706dd78f64c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944729e341d2706dd78f64d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16150427591355603199': 'file_storage/function-call-16150427591355603199.json'}

exec(code, env_args)
