code = """import json
import re

# Load the data
file_path = locals()['var_function-call-6036018550432900631']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
keywords_sports = set(["sport", "sports", "olympic", "olympics", "medal", "gold", "silver", "bronze", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "rugby", "boxing", "racing", "f1", "formula one", "nascar", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "champion", "championship", "tournament", "league", "cup", "athlete", "player", "coach", "team", "match", "game", "score", "win", "loss", "victory", "defeat", "record", "athens", "swimming", "gymnastics", "track", "field", "marathon", "stadium", "doping", "drug", "title", "bonds", "armstrong", "phelps", "woods", "williams", "federer", "roddick", "schumacher", "ferrari", "yankees", "red sox", "lakers", "pistons", "arsenal", "manchester", "chelsea", "real madrid", "barcelona", "ac milan", "juventus", "inter", "quarterback", "touchdown", "homerun", "slam", "wimbledon", "open", "masters", "cup", "bowl", "series", "playoff", "final", "semifinal"])
keywords_business = set(["business", "company", "market", "stock", "share", "economy", "finance", "bank", "investment", "profit", "revenue", "earnings", "deal", "merger", "acquisition", "ipo", "ceo", "dollar", "oil", "price", "sales", "retail", "wall street", "nasdaq", "dow", "fed", "inflation", "rate", "corp", "inc", "ltd"])
keywords_scitech = set(["science", "technology", "tech", "computer", "software", "internet", "web", "online", "net", "virus", "space", "nasa", "microsoft", "google", "intel", "linux", "windows", "server", "chip", "mobile", "phone", "wireless", "video", "game", "console"]) # "game" is ambiguous
keywords_world = set(["world", "government", "minister", "president", "official", "leader", "party", "election", "war", "peace", "military", "army", "police", "attack", "bomb", "kill", "iraq", "iran", "israel", "palestine", "afghanistan", "russia", "china", "usa", "uk", "france", "germany", "eu", "un", "nuclear", "terror"])

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Simple tokenization
    tokens = re.findall(r'\w+', text)
    
    score_sports = sum(1 for t in tokens if t in keywords_sports)
    score_business = sum(1 for t in tokens if t in keywords_business)
    score_scitech = sum(1 for t in tokens if t in keywords_scitech)
    score_world = sum(1 for t in tokens if t in keywords_world)
    
    # Adjust for ambiguous words
    if "game" in tokens and ("video" in tokens or "console" in tokens or "nintendo" in tokens or "xbox" in tokens or "sony" in tokens):
        score_scitech += 2 # Boost scitech
        score_sports -= 1
    
    if "oil" in tokens:
        score_business += 2
        
    scores = {
        "Sports": score_sports,
        "Business": score_business,
        "Sci/Tech": score_scitech,
        "World": score_world
    }
    
    # Get max score
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

sports_articles = []
for a in articles:
    cat = classify(a['title'], a['description'])
    if cat == "Sports":
        sports_articles.append(a)

# Find the one with max description length
if sports_articles:
    max_article = max(sports_articles, key=lambda x: len(x['description']))
    result = {"title": max_article['title'], "desc_len": len(max_article['description']), "description": max_article['description']}
else:
    result = "No sports articles found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9821206441971068824': ['articles'], 'var_function-call-9821206441971066019': ['authors', 'article_metadata'], 'var_function-call-9708188625832290358': [{'_id': '69446302e64442a00bf5d969', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9708188625832291827': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-5673689165236548416': [{'_id': '69446302e64442a00bf5d969', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446302e64442a00bf5d96a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446302e64442a00bf5d96b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446302e64442a00bf5d96c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446302e64442a00bf5d96d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-355172535146539447': [{'_id': '69446302e64442a00bf5d969', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446302e64442a00bf5d96a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446302e64442a00bf5d96b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446302e64442a00bf5d96c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446302e64442a00bf5d96d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16676322079434033556': 'file_storage/function-call-16676322079434033556.json', 'var_function-call-1093242531798274301': 'file_storage/function-call-1093242531798274301.json', 'var_function-call-1093242531798276056': [{'count(*)': '127600'}], 'var_function-call-6036018550432900631': 'file_storage/function-call-6036018550432900631.json'}

exec(code, env_args)
