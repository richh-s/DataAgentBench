code = """import json
import re

# Get the filename from the variable
filename = locals()['var_function-call-8531003678679978584']

with open(filename, 'r') as f:
    articles = json.load(f)

# Define keywords
strong_keywords = [
    'olympic', 'olympics', 'athens', 'medal', 'gold medal', 'silver medal', 'bronze medal',
    'nba', 'nfl', 'nhl', 'mlb', 'fifa', 'uefa', 'world cup', 'super bowl', 'wimbledon',
    'grand slam', 'us open', 'tour de france', 'formula 1', 'f1', 'nascar', 'pga', 'lpga',
    'doping', 'drug test', 'marathon', 'sprint', 'relay', 'gymnastics', 'swimming', 'diving',
    'basketball', 'baseball', 'football', 'soccer', 'tennis', 'cricket', 'rugby', 'hockey',
    'volleyball', 'boxing', 'wrestling', 'badminton', 'archery', 'fencing', 'judo', 'rowing',
    'sailing', 'shooting', 'softball', 'taekwondo', 'triathlon', 'weightlifting', 'cycling', 
    'equestrian', 'handball', 'pentathlon', 'table tennis', 'water polo'
]

weak_keywords = [
    'sport', 'sports', 'game', 'games', 'match', 'tournament', 'championship', 'league',
    'team', 'coach', 'player', 'athlete', 'score', 'win', 'loss', 'victory', 'defeat',
    'standings', 'playoff', 'final', 'semifinal', 'quarterfinal', 'stadium', 'arena',
    'record', 'champion', 'title', 'cup'
]

candidates = []

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    text = (title + " " + desc).lower()
    
    score = 0
    # Check strong keywords
    for k in strong_keywords:
        if re.search(r'\b' + re.escape(k) + r'\b', text):
            score += 2
    
    # Check weak keywords
    for k in weak_keywords:
        if re.search(r'\b' + re.escape(k) + r'\b', text):
            score += 1
            
    if score >= 2: # At least one strong or two weak
        candidates.append({
            'title': title,
            'description': desc,
            'len': len(desc),
            'score': score
        })

# Sort by length desc
candidates.sort(key=lambda x: x['len'], reverse=True)

# Print top 5
print("__RESULT__:")
print(json.dumps(candidates[:5], indent=2))"""

env_args = {'var_function-call-16533696639845188657': ['articles'], 'var_function-call-2103226498786508374': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15250911564119915383': {'type': "<class 'list'>", 'is_list': True, 'is_str': False, 'length': 5}, 'var_function-call-15277994356047519449': [{'_id': '6944639e4e0d87200b7b6ce7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944639e4e0d87200b7b6ce8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944639e4e0d87200b7b6ce9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944639e4e0d87200b7b6cea', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944639e4e0d87200b7b6ceb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8531003678679978584': 'file_storage/function-call-8531003678679978584.json'}

exec(code, env_args)
