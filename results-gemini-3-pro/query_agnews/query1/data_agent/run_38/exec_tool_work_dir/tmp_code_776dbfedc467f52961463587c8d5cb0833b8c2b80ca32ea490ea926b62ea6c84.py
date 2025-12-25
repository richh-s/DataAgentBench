code = """import json

# Load the file
file_path = locals()['var_function-call-15783133266262002332']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
strict_sports = [
    "olympics", "olympic", "athens", "medal", "nba", "nfl", "mlb", "nhl", 
    "fifa", "uefa", "wimbledon", "super bowl", "world cup", "euro 2004", 
    "championship", "quarterback", "touchdown", "homerun", "slam dunk", 
    "gold medal", "silver medal", "bronze medal", "grand slam", "pga tour", 
    "formula one", "nascar", "doping", "dream team", "sprinter", "gymnast", 
    "swimmer", "marathon", "triathlon", "red sox", "yankees", "lakers", "pistons"
]

general_sports = [
    "sport", "football", "baseball", "basketball", "hockey", "tennis", "soccer", "golf", 
    "rugby", "cricket", "boxing", "f1", "team", "coach", "player", "athlete", 
    "game", "match", "cup", "league", "win", "loss", "victory", "defeat", 
    "score", "race", "driver", "playoff", "final", "semifinal"
]

negative_keywords = [
    "stocks", "stock market", "economy", "oil", "prices", "profit", "earnings", 
    "investment", "shares", "dollar", "trade", "deficit", "iraq", "war", 
    "election", "president", "minister", "gaza", "israel", "palestinian", 
    "nuclear", "blast", "attack", "rebel", "militia", "bomb", "killed", 
    "government", "microsoft", "google", "intel", "linux", "software", "virus"
]

def get_score(text):
    text = text.lower()
    score = 0
    
    # Check strict
    for kw in strict_sports:
        if kw in text:
            score += 5
            
    # Check general
    for kw in general_sports:
        score += text.count(kw)
        
    # Check negative
    for kw in negative_keywords:
        if kw in text:
            score -= 5 # Penalty
            
    return score

# Process articles
candidates = []
for art in articles:
    # Combine title and description
    content = art['title'] + " " + art['description']
    score = get_score(content)
    
    # Filter
    if score > 0:
        candidates.append({
            "title": art['title'],
            "description": art['description'],
            "len": len(art['description']),
            "score": score
        })

# Sort by length descending
candidates.sort(key=lambda x: x['len'], reverse=True)

# Output the top 5
print("__RESULT__:")
print(json.dumps(candidates[:5], indent=2))"""

env_args = {'var_function-call-10047601114484748362': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9571403557217770297': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17685011732054669785': [{'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'desc_len': 214, 'sports_score': 0, 'is_strict_sports': False}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'desc_len': 195, 'sports_score': 0, 'is_strict_sports': False}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'desc_len': 184, 'sports_score': 0, 'is_strict_sports': False}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'desc_len': 160, 'sports_score': 2, 'is_strict_sports': False}, {'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'desc_len': 94, 'sports_score': 1, 'is_strict_sports': False}], 'var_function-call-6235476327425017915': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15783133266262002332': 'file_storage/function-call-15783133266262002332.json'}

exec(code, env_args)
