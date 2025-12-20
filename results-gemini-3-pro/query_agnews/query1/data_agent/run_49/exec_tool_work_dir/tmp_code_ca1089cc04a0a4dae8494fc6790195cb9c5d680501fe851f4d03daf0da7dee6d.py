code = """import json
import re

# Load data
file_path = locals()['var_function-call-7746759629844681813']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Calculate length
for a in articles:
    a['len'] = len(a.get('description', ''))

# Sort
articles.sort(key=lambda x: x['len'], reverse=True)

# Keywords
sports_keywords = {
    "sport", "baseball", "basketball", "football", "soccer", "hockey", "tennis", "golf", "olympic", 
    "game", "match", "team", "win", "won", "loss", "lost", "score", "cup", "league", "champion", 
    "athlete", "player", "coach", "manager", "stadium", "medal", "gold", "silver", "bronze", 
    "record", "final", "playoff", "super bowl", "world series", "stanley cup", 
    "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "wta", "atp", "pga", "nascar", "f1", 
    "formula one", "driver", "racing", "red sox", "yankees", "lakers", "pistons", "arsenal", 
    "real madrid", "barcelona", "manchester", "chelsea", "liverpool", "milan", "juventus", 
    "bayern", "dortmund", "psg", "ferrari", "schumacher", "williams", "serena", "venus", 
    "federer", "nadal", "roddick", "hewitt", "mickelson", "woods", "singh", "earnhardt", "gordon",
    "johnson", "newman", "kahne", "mayfield", "mcmurray", "marlin", "jarrett", "labonte", 
    "hamilton", "riggs", "nemechek", "rudd", "craven", "petty", "andretti", "tracy", "vasser", 
    "junqueira", "bourdais", "carpentier", "tagliani", "dominguez", "lavin", "servia", "wilson", 
    "gonzalez", "gidley", "manning", "barron", "rice", "meira", "scheckter", "castro-neves", 
    "kanaan", "dixon", "franchitti", "hornish", "wheldon", "herta", "matsuura", "sharp", "renna", 
    "simmons", "foyt", "cheever", "unser", "lazier", "fisher", "salles", "enge", "giebler", "barber", 
    "beechler", "buhl", "calkins", "dare", "ferran", "diniz", "dottin", "giaffone", "gosek", 
    "gregoire", "gugelmin", "haberfeld", "hearn", "herbert", "hollansworth", "hunter-reay", 
    "jourdain", "kite", "luyendyk", "marques", "mcgehee", "minassian", "montoya", "nakano", "nearn", 
    "papis", "ribbs", "roe", "salazar", "schroeder", "scott", "steele", "takagi", "velez", 
    "ward", "wattles", "yasukawa", "zampedri", "zanardi", "olympics", "paralympics", "tournament",
    "quarterback", "touchdown", "goal", "striker", "midfielder", "defender", "goalkeeper",
    "pitcher", "catcher", "infielder", "outfielder", "homerun", "inning", "puck", "rink"
}

non_sports_keywords = {
    "market", "stock", "company", "profit", "quarter", "price", "oil", "bank", "economy", "sales", 
    "corp", "inc", "deal", "shares", "dollar", "trade", "billion", "million", "growth", "revenue", 
    "investment", "firm", "ceo", "technology", "software", "computer", "internet", "google", "microsoft", 
    "president", "minister", "iraq", "war", "government", "official", "police", "military", "election",
    "ibm", "oracle", "linux", "java", "server", "wireless", "broadband", "telecom", "intel"
}

def is_sports(text):
    text = text.lower()
    # Simple tokenization
    tokens = set(re.findall(r'\w+', text))
    
    s_score = len(tokens.intersection(sports_keywords))
    n_score = len(tokens.intersection(non_sports_keywords))
    
    # Heuristic: significantly more sports keywords or high sports count
    # Also check specific combinations if needed
    if s_score > n_score and s_score >= 2:
        return True
    return False

candidates = []
for a in articles:
    # Combine title and description for classification
    text = a['title'] + " " + a['description']
    if is_sports(text):
        candidates.append(a)
        if len(candidates) >= 5:
            break

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-12752202253382073496': [{'_id': '694489eb5027e9acdee6a000', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694489eb5027e9acdee6a001', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694489eb5027e9acdee6a002', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694489eb5027e9acdee6a003', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694489eb5027e9acdee6a004', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1346593239618808557': [{'_id': '694489eb5027e9acdee6a000', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694489eb5027e9acdee6a001', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694489eb5027e9acdee6a002', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694489eb5027e9acdee6a003', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694489eb5027e9acdee6a004', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16063990782779180289': [{'_id': '694489eb5027e9acdee6a000', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694489eb5027e9acdee6a001', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694489eb5027e9acdee6a002', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694489eb5027e9acdee6a003', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694489eb5027e9acdee6a004', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1820344401618325712': 'file_storage/function-call-1820344401618325712.json', 'var_function-call-7746759629844681813': 'file_storage/function-call-7746759629844681813.json', 'var_function-call-15125357494140859655': 'file_storage/function-call-15125357494140859655.json'}

exec(code, env_args)
