code = """import json

data = locals()['var_function-call-9571403557217770297']
if isinstance(data, str):
    # It's a file path
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    # It's the list itself
    articles = data

# Define sports keywords
# I will use a scoring system to help identify sports articles
sports_keywords = [
    "sport", "football", "baseball", "basketball", "hockey", "tennis", "soccer", "golf", 
    "olympics", "olympic", "medal", "athens", "game", "match", "cup", "tournament", 
    "league", "team", "coach", "player", "athlete", "win", "lose", "victory", "defeat", 
    "score", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "champion", "record", 
    "swimming", "gymnastics", "track", "field", "marathon", "sprint", "relay", 
    "doping", "drug", "gold", "silver", "bronze", "race", "driver", "prix", "boxing"
]

strict_sports_keywords = [
    "olympics", "olympic", "athens", "medal", "nba", "nfl", "mlb", "nhl", 
    "fifa", "uefa", "wimbledon", "tournament", "championship", "world cup", 
    "super bowl", "quarterback", "touchdown", "homerun", "slam dunk", 
    "gold medal", "silver medal", "bronze medal"
]

def get_sports_score(text):
    text = text.lower()
    score = 0
    for kw in sports_keywords:
        score += text.count(kw)
    return score

def is_strictly_sports(text):
    text = text.lower()
    for kw in strict_sports_keywords:
        if kw in text:
            return True
    return False

# Calculate description length and scores
processed_articles = []
for art in articles:
    text = (art['title'] + " " + art['description'])
    processed_articles.append({
        "title": art['title'],
        "description": art['description'],
        "desc_len": len(art['description']),
        "sports_score": get_sports_score(text),
        "is_strict_sports": is_strictly_sports(text)
    })

# Sort by description length descending
sorted_articles = sorted(processed_articles, key=lambda x: x['desc_len'], reverse=True)

# Let's inspect the top 20 longest articles and see which one is sports
top_candidates = sorted_articles[:20]

print("__RESULT__:")
print(json.dumps(top_candidates, indent=2))"""

env_args = {'var_function-call-10047601114484748362': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9571403557217770297': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
