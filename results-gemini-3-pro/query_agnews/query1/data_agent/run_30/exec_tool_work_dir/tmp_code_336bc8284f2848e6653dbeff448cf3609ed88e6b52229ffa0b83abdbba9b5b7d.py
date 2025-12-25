code = """import json
import re

with open(locals()['var_function-call-2994061000156864416'], 'r') as f:
    articles = json.load(f)

print(f"Loaded {len(articles)} articles.")

# Debug: check for potential sports words in all articles
potential_sports = []
for a in articles:
    text = (a.get('title', '') + " " + a.get('description', '')).lower()
    if 'sport' in text or 'game' in text or 'olympic' in text or 'football' in text:
        potential_sports.append(a['title'])

print(f"Articles containing 'sport', 'game', 'olympic', 'football': {len(potential_sports)}")
if potential_sports:
    print(f"Sample titles: {potential_sports[:5]}")

# Debug: print classification counts
sports_keywords = {
    'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 
    'olympic', 'olympics', 'medal', 'game', 'match', 'tournament', 'championship', 'league', 
    'team', 'athlete', 'player', 'coach', 'stadium', 'racing', 'f1', 'formula 1', 'nascar', 
    'cricket', 'rugby', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 
    'wimbledon', 'grand slam', 'touchdown', 'homerun', 'score', 'scored', 'winning', 'losing', 'victory', 'defeat',
    'athens', 'gold', 'silver', 'bronze', 'red sox', 'yankees', 'lakers', 'arsenal', 'man utd'
}
# (Simplified for debug)

counts = {'Sports': 0, 'Other': 0}
for a in articles:
    text = (a.get('title', '') + " " + a.get('description', '')).lower()
    tokens = set(re.findall(r'\b\w+\b', text))
    
    # Check if any sports keyword is in tokens
    is_sport = False
    for k in sports_keywords:
        if k in tokens:
            is_sport = True
            break
    
    if is_sport:
        counts['Sports'] += 1
    else:
        counts['Other'] += 1

print(f"Counts: {counts}")

print("__RESULT__:")
print(json.dumps({"info": "debug"}))"""

env_args = {'var_function-call-10263163882729604573': ['articles'], 'var_function-call-10263163882729604264': ['authors', 'article_metadata'], 'var_function-call-17900817817497807775': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15939149844553677031': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-526178464523967050': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11607585572360918056': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2994061000156864416': 'file_storage/function-call-2994061000156864416.json', 'var_function-call-18200326237114442273': {}}

exec(code, env_args)
