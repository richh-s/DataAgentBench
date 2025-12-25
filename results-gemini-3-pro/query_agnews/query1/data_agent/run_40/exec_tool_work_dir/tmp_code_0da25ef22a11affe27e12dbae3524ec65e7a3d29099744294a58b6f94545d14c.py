code = """import json
import re

# Load data
file_path = locals()['var_function-call-7170286238847941476']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
# Strong keywords strongly suggest sports
strong_keywords = [
    "olympics", "olympic", "paralympic", "medal", "athlete", 
    "football", "baseball", "basketball", "soccer", "tennis", "hockey", "golf", "cricket", "rugby",
    "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "wta", "atp", "pga", "lpga",
    "wimbledon", "us open", "french open", "australian open", "world cup", "super bowl", "world series",
    "red sox", "yankees", "lakers", "knicks", "bulls", "celtics", 
    "manchester united", "real madrid", "barcelona", "arsenal", "chelsea", "liverpool",
    "michael phelps", "lance armstrong", "serena williams", "venus williams", "tiger woods",
    "touchdown", "homerun", "slam dunk", "hat trick", "goalkeeper", "quarterback",
    "grand slam", "pole position", "formula one", "nascar"
]

# Weak keywords might be sports but also other things
weak_keywords = [
    "game", "match", "team", "score", "coach", "player", "tournament", "league", 
    "championship", "cup", "race", "racing", "stadium", "arena", "season", 
    "playoff", "semi-final", "quarter-final", "final"
]

def is_sports(title, description):
    text = (title + " " + description).lower()
    
    # Check strong keywords
    for kw in strong_keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            return True
            
    # Check weak keywords (require at least 2 for confidence)
    count = 0
    for kw in weak_keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            count += 1
    
    if count >= 2:
        return True
        
    return False

# Filter and process
sports_candidates = []
for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    if is_sports(title, desc):
        sports_candidates.append({
            'title': title,
            'description': desc,
            'len': len(desc)
        })

# Sort by description length descending
sports_candidates.sort(key=lambda x: x['len'], reverse=True)

# Print top 10 candidates to verify
print("__RESULT__:")
print(json.dumps(sports_candidates[:10]))"""

env_args = {'var_function-call-11557184172801880100': ['articles'], 'var_function-call-11557184172801882169': ['authors', 'article_metadata'], 'var_function-call-7826079083414927262': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10106188959477813962': [['Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'], ['Wall St. Bears Claw Back Into the Black (Reuters)', "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."], ["Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'], ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'], ['Carlyle Looks Toward Commercial Aerospace (Reuters)', 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.']], 'var_function-call-4330241965686352741': [{'_id': '69448279fdcb6d40b15bb2a1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69448279fdcb6d40b15bb2a2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69448279fdcb6d40b15bb2a3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69448279fdcb6d40b15bb2a4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69448279fdcb6d40b15bb2a5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7170286238847941476': 'file_storage/function-call-7170286238847941476.json'}

exec(code, env_args)
