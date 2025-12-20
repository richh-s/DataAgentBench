code = """import json
import pandas as pd

# Load the data
file_path = locals()['var_function-call-7183472748245529967']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = [
    "sport", "game", "team", "olympic", "medal", "gold", "silver", "bronze", 
    "football", "basketball", "baseball", "soccer", "hockey", "tennis", "golf", 
    "champion", "tournament", "league", "cup", "score", "win", "lose", "victory", 
    "defeat", "player", "coach", "stadium", "match", "race", "running", "swimming", 
    "athletics", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", "grand slam",
    "touchdown", "quarterback", "striker", "goalkeeper", "pitcher", "batter", "inning",
    "athens", "greece", "summer games" # Context specific: 2004 Olympics?
]

business_keywords = [
    "oil", "price", "stock", "market", "economy", "company", "corp", "inc", "profit", 
    "loss", "revenue", "deal", "merger", "acquisition", "bank", "dollar", "euro", 
    "yen", "inflation", "rate", "fed", "treasury", "ceo", "cfo", "wall street", "nasdaq",
    "dow jones", "invest", "trade", "deficit", "ipo"
]

world_keywords = [
    "president", "minister", "prime minister", "iraq", "iran", "war", "military", 
    "bomb", "attack", "peace", "treaty", "un", "united nations", "country", "election", 
    "vote", "parliament", "government", "official", "troops", "rebel", "blast", "kill",
    "police", "crash"
]

tech_keywords = [
    "computer", "software", "internet", "web", "google", "microsoft", "apple", "space", 
    "nasa", "virus", "study", "research", "science", "technology", "phone", "mobile", 
    "chip", "processor", "online", "network", "server", "linux", "windows", "spam", "hacker"
]

def classify(text):
    text = text.lower()
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
            
    # Return category with max score
    # If tie, return the one that appears first in list order or prioritize specific ones
    # However, usually the correct category dominates
    if scores["Sports"] == 0 and scores["Business"] == 0 and scores["World"] == 0 and scores["Sci/Tech"] == 0:
        return "Unknown"
        
    return max(scores, key=scores.get)

max_len = -1
target_title = None
sports_articles = []

for article in articles:
    text = article['title'] + " " + article['description']
    category = classify(text)
    
    if category == "Sports":
        desc_len = len(article['description'])
        sports_articles.append({
            "title": article['title'],
            "len": desc_len,
            "desc": article['description']
        })
        if desc_len > max_len:
            max_len = desc_len
            target_title = article['title']

print("__RESULT__:")
print(json.dumps(target_title))"""

env_args = {'var_function-call-14006709642830065521': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14006709642830061862': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-13273772338279766106': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11371123564863916700': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7183472748245529967': 'file_storage/function-call-7183472748245529967.json'}

exec(code, env_args)
