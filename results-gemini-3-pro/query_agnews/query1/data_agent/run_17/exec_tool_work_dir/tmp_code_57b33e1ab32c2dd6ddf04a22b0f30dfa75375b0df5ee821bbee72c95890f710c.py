code = """import json

# Check the type of the result from the previous tool call
data_key = 'var_function-call-3846196706058509729'
data = locals().get(data_key)

if isinstance(data, str) and (data.endswith('.json') or '/' in data):
    # It's a file path
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    # It's the data itself
    articles = data

# Define keywords for classification
strong_sports_keywords = [
    "olympic", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "athens", 
    "wimbledon", "us open", "french open", "australian open", "davis cup",
    "super bowl", "world series", "stanley cup", "ryder cup",
    "tour de france", "formula one", "nascar", "pga", "lpga",
    "red sox", "yankees", "lakers", "pistons", "spurs", "pacers", 
    "patriots", "eagles", "colts", "real madrid", "manchester united", "arsenal",
    "chelsea", "ac milan", "juventus", "inter milan", "barcelona",
    "michael phelps", "lance armstrong", "roger federer", "andy roddick", 
    "serena williams", "venus williams", "tiger woods", "vijay singh",
    "ichiro", "barry bonds", "shatrap", "kobe", "shaq", "lebron", 
    "dream team", "gold medal", "silver medal", "bronze medal"
]

generic_sports_keywords = [
    "sport", "football", "soccer", "basketball", "baseball", "tennis", 
    "hockey", "cricket", "rugby", "golf", "athlete", "medal", "game", 
    "match", "team", "score", "cup", "racing", "driver", "championship",
    "tournament", "league", "playoff", "stadium", "coach", "quarterback"
]

sports_articles = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    is_sport = False
    
    # Check strong keywords first
    for kw in strong_sports_keywords:
        if kw in text:
            is_sport = True
            break
            
    if not is_sport:
        # Check combination of generic sports terms
        # E.g. "team" AND "game", "player" AND "coach"
        # Or just presence of "sport"
        if "sport" in text:
            is_sport = True
        else:
            generic_count = 0
            for kw in generic_sports_keywords:
                if kw in text:
                    generic_count += 1
            if generic_count >= 2:
                is_sport = True

    if is_sport:
        sports_articles.append(art)

# Find the one with the longest description
max_len = -1
best_article = None

for art in sports_articles:
    desc_len = len(art.get('description', ''))
    if desc_len > max_len:
        max_len = desc_len
        best_article = art

result = {}
if best_article:
    result = {
        "title": best_article['title'],
        "length": max_len,
        "description_snippet": best_article['description'][:50]
    }
else:
    result = {"error": "No sports articles found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10490437154642486884': ['articles'], 'var_function-call-16060478269300868870': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9311861591054791868': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2138815974854363807': [{'_id': '69447092d43dab771ac0dd01', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447092d43dab771ac0dd02', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447092d43dab771ac0dd03', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447092d43dab771ac0dd04', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447092d43dab771ac0dd05', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16333879224723824131': 'No sports articles found.', 'var_function-call-3846196706058509729': 'file_storage/function-call-3846196706058509729.json'}

exec(code, env_args)
