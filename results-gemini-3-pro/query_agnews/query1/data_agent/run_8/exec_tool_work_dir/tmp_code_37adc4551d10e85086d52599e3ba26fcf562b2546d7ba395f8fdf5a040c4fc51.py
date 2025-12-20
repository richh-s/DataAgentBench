code = """import json
import re

with open(locals()['var_function-call-8284316981365420739'], 'r') as f:
    articles = json.load(f)

# Keywords
sp = set(["sport", "sports", "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", "olympic", "olympics", "medal", "tournament", "championship", "league", "cup", "athlete", "player", "coach", "team", "match", "score", "game", "playoff", "finals", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "quarterback", "touchdown", "goal", "red sox", "yankees", "lakers", "bulls", "athens", "swimming", "track", "field", "cycling", "doping", "marathon", "sprint", "race", "racing", "driver", "nascar", "f1", "rugby", "cricket"])

biz = set(["stock", "market", "price", "company", "profit", "revenue", "investment", "share", "economy", "trade", "dollar", "euro", "bank", "fed", "inflation", "job", "manager", "ceo", "oil", "gas", "energy", "merger", "ipo", "finance"])

tech = set(["software", "internet", "computer", "microsoft", "google", "apple", "linux", "virus", "space", "nasa", "science", "technology", "tech", "web", "online", "digital", "chip", "wireless"])

world = set(["iraq", "president", "election", "war", "peace", "government", "minister", "official", "un", "police", "court", "military", "army", "bomb", "attack", "kill", "politics", "vote", "palestinian", "israel"])

def classify(text):
    words = re.findall(r'\w+', text.lower())
    scores = {"S": 0, "B": 0, "T": 0, "W": 0}
    for w in words:
        if w in sp: scores["S"] += 1
        if w in biz: scores["B"] += 1
        if w in tech: scores["T"] += 1
        if w in world: scores["W"] += 1
    
    if max(scores.values()) == 0: return "U"
    return max(scores, key=scores.get)

articles.sort(key=lambda x: len(x['description']), reverse=True)

found = None
for art in articles:
    ft = art['title'] + " " + art['description']
    c = classify(ft)
    if c == "S":
        found = art
        break

print("__RESULT__:")
print(json.dumps(found))"""

env_args = {'var_function-call-5600887256776046897': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6243788860290969808': ['authors', 'article_metadata'], 'var_function-call-621124544545937450': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-14125888797793058960': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-371116049882488257': [{'author_id': '0', 'name': 'Felicia Miles'}, {'author_id': '1', 'name': 'Stacy Hunt'}, {'author_id': '2', 'name': 'Carol Reed'}, {'author_id': '3', 'name': 'Dr. Daniel Brown'}, {'author_id': '4', 'name': 'Andre Lam MD'}], 'var_function-call-16428439284826624530': [{'_id': '694468d48f62606ef06538a3', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7895339117705645390': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-15665066354817605845': 'file_storage/function-call-15665066354817605845.json', 'var_function-call-4236206756542118061': {'count': 10000}, 'var_function-call-8284316981365420739': 'file_storage/function-call-8284316981365420739.json'}

exec(code, env_args)
