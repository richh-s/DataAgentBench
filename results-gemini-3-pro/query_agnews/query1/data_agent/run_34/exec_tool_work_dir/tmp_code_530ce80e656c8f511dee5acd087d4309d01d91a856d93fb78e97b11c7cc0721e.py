code = """import json
import re

# Load the data
file_path = locals()['var_function-call-7183472748245529967']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = [
    "sport", "sports", "game", "games", "team", "teams", "olympic", "olympics", "medal", "medals", 
    "gold", "silver", "bronze", "football", "basketball", "baseball", "soccer", "hockey", "tennis", 
    "golf", "champion", "champions", "championship", "tournament", "league", "cup", "score", "scores", 
    "win", "wins", "winner", "lose", "lost", "loss", "victory", "defeat", "player", "players", 
    "coach", "stadium", "match", "matches", "race", "racing", "runner", "sprint", "swimming", "swimmer", 
    "athletics", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", "grand slam",
    "touchdown", "quarterback", "striker", "goalkeeper", "pitcher", "batter", "inning",
    "athens", "greece", "summer games"
]

business_keywords = [
    "oil", "price", "prices", "stock", "stocks", "market", "markets", "economy", "economic", 
    "company", "companies", "corp", "inc", "profit", "profits", "loss", "losses", "revenue", 
    "deal", "merger", "acquisition", "bank", "banks", "dollar", "euro", "yen", 
    "inflation", "rate", "rates", "fed", "treasury", "ceo", "cfo", "wall street", "nasdaq",
    "dow jones", "invest", "investment", "trade", "deficit", "ipo"
]

world_keywords = [
    "president", "minister", "prime minister", "iraq", "iraqi", "iran", "war", "military", 
    "bomb", "bombing", "attack", "attacks", "peace", "treaty", "un", "united nations", 
    "country", "countries", "election", "elections", "vote", "voters", "parliament", 
    "government", "official", "officials", "troops", "rebel", "rebels", "blast", "kill", "killed",
    "police", "crash", "palestinian", "israel", "gaza"
]

tech_keywords = [
    "computer", "computers", "software", "internet", "web", "google", "microsoft", "apple", 
    "space", "nasa", "virus", "study", "research", "science", "technology", "phone", "mobile", 
    "chip", "processor", "online", "network", "server", "linux", "windows", "spam", "hacker",
    "digital", "wireless", "broadband"
]

def count_keywords(text, keywords):
    count = 0
    # Use regex to match whole words only
    for word in keywords:
        # Escape special chars if any, though keywords are simple
        pattern = r'\b' + re.escape(word) + r'\b'
        matches = re.findall(pattern, text)
        count += len(matches)
    return count

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {
        "Sports": count_keywords(text, sports_keywords),
        "Business": count_keywords(text, business_keywords),
        "World": count_keywords(text, world_keywords),
        "Sci/Tech": count_keywords(text, tech_keywords)
    }
    
    # If no keywords match, return Unknown
    if sum(scores.values()) == 0:
        return "Unknown"
        
    return max(scores, key=scores.get)

sports_candidates = []

for article in articles:
    cat = classify(article['title'], article['description'])
    if cat == "Sports":
        sports_candidates.append({
            "title": article['title'],
            "desc": article['description'],
            "len": len(article['description'])
        })

# Sort by length descending
sports_candidates.sort(key=lambda x: x['len'], reverse=True)

# Pick the top one
if sports_candidates:
    result = sports_candidates[0]
    print(f"Top Candidate Title: {result['title']}")
    print(f"Top Candidate Length: {result['len']}")
    print(f"Top Candidate Desc: {result['desc']}")
else:
    print("No sports articles found.")

print("__RESULT__:")
print(json.dumps(sports_candidates[0]['title'] if sports_candidates else None))"""

env_args = {'var_function-call-14006709642830065521': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14006709642830061862': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-13273772338279766106': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11371123564863916700': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7183472748245529967': 'file_storage/function-call-7183472748245529967.json', 'var_function-call-9596134104357642270': 'Pretty Log4J'}

exec(code, env_args)
