code = """import json

# Load the data
file_path = locals()['var_function-call-10228615712224783799']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords (simplified)
sports_keywords = [
    "sport", "game", "team", "olympic", "medal", "gold", "silver", "bronze", 
    "football", "basketball", "baseball", "soccer", "hockey", "tennis", 
    "golf", "champion", "tournament", "league", "cup", "score", "win", "victory", 
    "defeat", "player", "coach", "stadium", "match", "race", "running", "swimming", 
    "athletics", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon",
    "touchdown", "quarterback", "striker", "goalkeeper", "pitcher", "athens"
]

business_keywords = [
    "oil", "price", "stock", "market", "economy", "company", "profit", "loss", 
    "revenue", "deal", "merger", "acquisition", "bank", "dollar", "euro", 
    "inflation", "rate", "fed", "treasury", "ceo", "invest", "trade", "deficit", "ipo"
]

world_keywords = [
    "president", "minister", "iraq", "iran", "war", "military", "bomb", "attack", 
    "peace", "un", "nation", "country", "election", "vote", "parliament", 
    "government", "official", "troops", "rebel", "blast", "kill", "police", "crash"
]

tech_keywords = [
    "computer", "software", "internet", "web", "google", "microsoft", "apple", 
    "space", "nasa", "virus", "study", "research", "science", "technology", "phone", 
    "mobile", "chip", "online", "network", "server", "linux", "windows"
]

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {
        "Sports": 0,
        "Business": 0,
        "World": 0,
        "Sci/Tech": 0
    }
    
    for word in sports_keywords:
        if word in text:
            scores["Sports"] += 1
            
    for word in business_keywords:
        if word in text:
            scores["Business"] += 1
            
    for word in world_keywords:
        if word in text:
            scores["World"] += 1
            
    for word in tech_keywords:
        if word in text:
            scores["Sci/Tech"] += 1
            
    if sum(scores.values()) == 0:
        return "Unknown"
        
    # Prioritize Sports if tied? 
    # Or just return max
    return max(scores, key=scores.get)

sports_candidates = []
counts = {"Sports": 0, "Business": 0, "World": 0, "Sci/Tech": 0, "Unknown": 0}

for article in articles:
    cat = classify(article['title'], article['description'])
    counts[cat] += 1
    if cat == "Sports":
        sports_candidates.append({
            "title": article['title'],
            "desc": article['description'],
            "len": len(article['description'])
        })

sports_candidates.sort(key=lambda x: x['len'], reverse=True)

result = {
    "counts": counts,
    "top_sports": sports_candidates[:3] if sports_candidates else []
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14006709642830065521': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14006709642830061862': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-13273772338279766106': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11371123564863916700': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7183472748245529967': 'file_storage/function-call-7183472748245529967.json', 'var_function-call-9596134104357642270': 'Pretty Log4J', 'var_function-call-1112962506276459453': None, 'var_function-call-29683656630397164': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10228615712224783799': 'file_storage/function-call-10228615712224783799.json', 'var_function-call-14774662353111638022': None, 'var_function-call-6919485285260926270': {'counts': {'Sports': 0, 'Business': 0, 'World': 0, 'Sci/Tech': 0, 'Unknown': 120000}, 'top_sports': [], 'sample_unknown': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}}

exec(code, env_args)
