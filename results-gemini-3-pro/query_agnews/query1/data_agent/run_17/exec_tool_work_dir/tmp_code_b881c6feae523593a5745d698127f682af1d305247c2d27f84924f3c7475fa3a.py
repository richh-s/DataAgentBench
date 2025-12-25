code = """import json
import re

# Load data
data_key = 'var_function-call-3846196706058509729'
data = locals().get(data_key)
if isinstance(data, str):
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    articles = data

# Define keywords
strong_sports_keywords = [
    "olympic", "olympics", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "athens", 
    "wimbledon", "super bowl", "world series", "stanley cup", "ryder cup",
    "tour de france", "formula one", "nascar", "pga", "lpga",
    "red sox", "yankees", "lakers", "pistons", "spurs", "pacers", 
    "patriots", "eagles", "colts", "real madrid", "manchester united", "arsenal",
    "chelsea", "ac milan", "juventus", "inter milan", "barcelona",
    "michael phelps", "lance armstrong", "roger federer", "andy roddick", 
    "serena williams", "venus williams", "tiger woods", "kobe bryant", 
    "gold medal", "silver medal", "bronze medal"
]

generic_sports_keywords = [
    "sport", "sports", "football", "soccer", "basketball", "baseball", "tennis", 
    "hockey", "cricket", "rugby", "golf", "athlete", "athletes", "medal", "medals",
    "championship", "tournament", "league", "playoff", "stadium", "quarterback",
    "goalkeeper", "striker", "pitcher", "touchdown", "homerun", "slamdunk"
]

# Tech keywords to avoid false positives (e.g. "driver", "game", "team" can be tech)
tech_keywords = [
    "software", "hardware", "windows", "linux", "unix", "microsoft", "google", 
    "internet", "web", "computer", "processor", "server", "virus", "technology",
    "broadband", "wireless", "telecom", "space", "nasa", "orbit", "astronomy",
    "biological", "genome", "stem cell"
]

business_keywords = [
    "stocks", "market", "economy", "investment", "profit", "quarterly", "earnings",
    "oil prices", "wall st", "nasdaq", "dow jones", "interest rates", "fed", "inflation"
]

def get_category_score(text, keywords):
    score = 0
    for kw in keywords:
        # Use word boundary
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            score += 1
    return score

candidates = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    sports_score = get_category_score(text, strong_sports_keywords) * 3 + \
                   get_category_score(text, generic_sports_keywords)
    
    tech_score = get_category_score(text, tech_keywords)
    business_score = get_category_score(text, business_keywords)
    
    # If sports score is dominant
    if sports_score > 0 and sports_score >= tech_score and sports_score >= business_score:
        candidates.append(art)

# Find longest description
max_len = -1
best_article = None

for art in candidates:
    desc = art.get('description', '')
    if len(desc) > max_len:
        max_len = len(desc)
        best_article = art

result = {}
if best_article:
    result = {
        "title": best_article['title'],
        "length": max_len,
        "description_snippet": best_article['description'][:100]
    }
else:
    result = {"error": "No sports articles found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10490437154642486884': ['articles'], 'var_function-call-16060478269300868870': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9311861591054791868': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2138815974854363807': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16333879224723824131': 'No sports articles found.', 'var_function-call-3846196706058509729': 'file_storage/function-call-3846196706058509729.json', 'var_function-call-16733021958024539417': {'title': "Why Windows isn't Unix", 'length': 708, 'description_snippet': '\\\\"I first heard about this from one of the develo'}}

exec(code, env_args)
