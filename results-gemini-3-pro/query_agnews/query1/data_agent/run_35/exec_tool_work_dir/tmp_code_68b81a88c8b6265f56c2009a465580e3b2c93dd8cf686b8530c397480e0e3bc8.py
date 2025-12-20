code = """import json
import re

# Load the data
file_path = locals()['var_function-call-4072584036690662513']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = {
    "sport", "sports", "football", "baseball", "basketball", "hockey", "tennis", "golf", 
    "soccer", "olympic", "olympics", "medal", "gold", "silver", "bronze", "athens", 
    "game", "match", "tournament", "cup", "league", "championship", "champion", 
    "team", "coach", "athlete", "player", "score", "win", "victory", "defeat", 
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "nascar", "f1", "racing", "driver", 
    "swim", "gymnastics", "marathon", "sprint", "stadium", "referee", "umpire", 
    "quarterback", "touchdown", "goal", "striker", "midfielder", "defender", "goalkeeper",
    "wrestling", "boxing", "round", "knockout", "bout"
}

business_tech_world_keywords = {
    "market", "stock", "price", "oil", "economy", "business", "company", "corp", "inc", 
    "shares", "investor", "profit", "revenue", "iraq", "war", "military", "president", 
    "election", "minister", "software", "internet", "technology", "microsoft", "google", 
    "apple", "ibm", "court", "judge", "police", "bomb", "kill", "dead", "died", "attack",
    "un", "united nations", "eu", "european union", "nuclear", "terror", "terrorist"
}

# Function to score an article
def get_category_score(text):
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    words = set(text.split())
    
    sports_score = len(words.intersection(sports_keywords))
    other_score = len(words.intersection(business_tech_world_keywords))
    
    return sports_score, other_score

candidates = []

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    full_text = title + " " + desc
    
    s_score, o_score = get_category_score(full_text)
    
    # Heuristic: significantly more sports keywords than other keywords
    # Or just if sports score > 0 and sports_score > other_score
    # Also "Olympics" is very strong.
    
    if s_score > o_score and s_score > 0:
        candidates.append({
            "title": title,
            "description": desc,
            "len": len(desc),
            "s_score": s_score,
            "o_score": o_score
        })

# Sort by description length descending
candidates.sort(key=lambda x: x['len'], reverse=True)

# Print top 5 results to verify
top_candidates = candidates[:5]

print("__RESULT__:")
print(json.dumps(top_candidates))"""

env_args = {'var_function-call-17593565785959345447': [{'_id': '69447dd145be82594bde559a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447dd145be82594bde559b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447dd145be82594bde559c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447dd145be82594bde559d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447dd145be82594bde559e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17079897375883321610': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-7209232652231767810': [{'_id': '69447dd145be82594bde559a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447dd145be82594bde559b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447dd145be82594bde559c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447dd145be82594bde559d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447dd145be82594bde559e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17184403664428919554': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4072584036690662513': 'file_storage/function-call-4072584036690662513.json'}

exec(code, env_args)
