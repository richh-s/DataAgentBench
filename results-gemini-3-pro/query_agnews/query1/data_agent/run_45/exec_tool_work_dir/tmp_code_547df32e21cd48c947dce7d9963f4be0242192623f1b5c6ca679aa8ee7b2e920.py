code = """import json
import re

# Load the articles from the file
file_path = locals()['var_function-call-18177868496750435891']
with open(file_path, 'r') as f:
    data = json.load(f)

# Define keywords
keywords = {
    "Business": {
        "business", "economy", "market", "stock", "trade", "profit", "loss", "dollar", "euro", "yen", "bank", 
        "company", "corp", "inc", "shares", "invest", "price", "oil", "gas", "energy", "sales", "revenue", 
        "deal", "merger", "acquisition", "ceo", "cfo", "wall st", "nasdaq", "dow", "index", "finance", "money",
        "inflation", "recession", "fed", "federal reserve", "imf", "wto", "deficit", "surplus", "bond", "yield"
    },
    "Sci/Tech": {
        "technology", "science", "computer", "internet", "software", "hardware", "web", "online", "digital", 
        "phone", "mobile", "wireless", "space", "nasa", "orbit", "robot", "virus", "worm", "microsoft", "google", 
        "apple", "intel", "linux", "windows", "browser", "server", "chip", "research", "study", "scientist", 
        "discovery", "astronomy", "biology", "physics", "tech", "gadget", "cyber", "hacker", "network", "data"
    },
    "World": {
        "world", "international", "politics", "government", "president", "prime minister", "minister", "official", 
        "election", "vote", "war", "peace", "treaty", "military", "army", "navy", "police", "attack", "bomb", 
        "blast", "terror", "killed", "injured", "dead", "iraq", "iran", "china", "russia", "us", "uk", "un", 
        "united nations", "eu", "european union", "protest", "court", "law", "judge", "security", "diplomat", "crisis",
        "israel", "palestine", "gaza", "afghanistan", "syria", "korea", "nuclear", "weapon", "parliament", "congress"
    },
    "Sports": {
        "sport", "olympic", "game", "match", "team", "player", "coach", "win", "lose", "draw", "score", "goal", 
        "touchdown", "homerun", "basket", "medal", "championship", "tournament", "league", "cup", "final", 
        "semi-final", "quarter-final", "playoff", "nba", "nfl", "mlb", "nhl", "fifa", "football", "baseball", 
        "basketball", "soccer", "tennis", "golf", "hockey", "racing", "driver", "f1", "nascar", "athens", 
        "games", "gold", "silver", "bronze", "record", "champion", "athlete", "squad", "club", "manager", "run",
        "stadium", "field", "court", "pitch", "wicket", "inning", "bat", "ball", "striker", "defender", "goalkeeper",
        "quarterback", "receiver", "umpire", "referee", "boxing", "wrestling", "cycling", "tour de france", "wimbledon",
        "open", "grand slam", "masters", "pga", "lpga", "formula one", "super bowl", "world series", "stanley cup"
    }
}

sports_articles = []

for article in data:
    title = article.get("title", "") or ""
    desc = article.get("description", "") or ""
    text = (title + " " + desc).lower()
    
    # Tokenization
    tokens = set(re.findall(r'\b[a-z]+\b', text))
    
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        scores[cat] = len(tokens.intersection(kws))
    
    # Heuristics
    if "olympic" in tokens or "olympics" in tokens:
        scores["Sports"] += 5
    if "iraq" in tokens:
        scores["World"] += 5
    if "stocks" in tokens or "wall street" in text:
        scores["Business"] += 5
    if "microsoft" in tokens or "google" in tokens:
        scores["Sci/Tech"] += 5
        
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] > 0:
        if best_cat == "Sports":
            sports_articles.append(article)
    # If tie or 0, ignore

# Find max description length
max_len = -1
best_article = None

for sa in sports_articles:
    desc = sa.get("description", "")
    if desc is None:
        desc = ""
    desc_len = len(desc)
    if desc_len > max_len:
        max_len = desc_len
        best_article = sa

result = {
    "total_sports": len(sports_articles),
    "best_title": best_article['title'] if best_article else None,
    "max_len": max_len
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17820231337409902993': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11407415087239536050': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-357563551933968648': {'total_articles': 5, 'sports_articles_count': 0, 'best_article_title': None, 'max_length': -1}, 'var_function-call-4127149747257172605': [{'cnt': '127600'}], 'var_function-call-18177868496750435891': 'file_storage/function-call-18177868496750435891.json'}

exec(code, env_args)
