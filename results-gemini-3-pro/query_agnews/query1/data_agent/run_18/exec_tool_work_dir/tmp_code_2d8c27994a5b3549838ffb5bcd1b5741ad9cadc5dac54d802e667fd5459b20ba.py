code = """import json
import re

# Load the data
file_path = locals()['var_function-call-12173091752223318367']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = [
    "sport", "game", "match", "team", "league", "cup", "championship", "tournament", 
    "olympic", "athens", "medal", "gold", "silver", "bronze", "football", "basketball", 
    "baseball", "soccer", "tennis", "golf", "hockey", "cricket", "rugby", "athlete", 
    "player", "coach", "score", "win", "loss", "victory", "defeat", "nba", "nfl", 
    "mlb", "nhl", "fifa", "uefa", "wimbledon", "open", "series", "sox", "yankees", 
    "lakers", "pistons", "spurs", "heat", "suns", "united", "city", "real", "barcelona", 
    "milan", "juventus", "chelsea", "arsenal", "liverpool", "manchester", "ferrari", 
    "schumacher", "armstrong", "tour de france", "doping", "balco", "giant", "giants",
    "cowboys", "patriots", "eagles", "colts", "red sox", "cardinals", "dodgers", "mets"
]

# Business keywords to filter out false positives (e.g. "team" in business context)
business_keywords = [
    "stock", "market", "price", "oil", "economy", "dollar", "trade", "profit", 
    "loss", "investment", "fund", "company", "corp", "inc", "ltd", "ceo", "cfo", 
    "bank", "sales", "revenue", "deal", "merger", "acquisition", "shares", "investor",
    "fed", "rates", "inflation", "nasdaq", "dow", "wall st", "wall street"
]

def is_sports(title, description):
    text = (title + " " + description).lower()
    
    # Simple score: +1 for sport keyword, -1 for business keyword
    score = 0
    for kw in sports_keywords:
        if kw in text:
            score += 1
    for kw in business_keywords:
        if kw in text:
            score -= 1
            
    return score > 0

candidates = []
for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    if is_sports(title, desc):
        candidates.append({
            'title': title,
            'description': desc,
            'len': len(desc)
        })

# Sort by length descending
candidates.sort(key=lambda x: x['len'], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:5]))"""

env_args = {'var_function-call-13738244287138652048': [{'_id': '6944714e37ec0e16a06ea28a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944714e37ec0e16a06ea28b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944714e37ec0e16a06ea28c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944714e37ec0e16a06ea28d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944714e37ec0e16a06ea28e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7138079574602777101': [{'_id': '6944714e37ec0e16a06ea28a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944714e37ec0e16a06ea28b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944714e37ec0e16a06ea28c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944714e37ec0e16a06ea28d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944714e37ec0e16a06ea28e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-802148529694265141': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-7137058214765669900': [{'_id': '6944714e37ec0e16a06ea28a', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944714e37ec0e16a06ea28b', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944714e37ec0e16a06ea28c', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944714e37ec0e16a06ea28d', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944714e37ec0e16a06ea28e', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6923536160074764247': 5, 'var_function-call-12173091752223318367': 'file_storage/function-call-12173091752223318367.json'}

exec(code, env_args)
