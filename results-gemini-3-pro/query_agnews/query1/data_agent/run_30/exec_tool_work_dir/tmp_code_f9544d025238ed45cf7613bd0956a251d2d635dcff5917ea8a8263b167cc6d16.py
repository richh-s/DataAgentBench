code = """import json
import re

with open(locals()['var_function-call-2994061000156864416'], 'r') as f:
    articles = json.load(f)

debug_info = {}
debug_info['total_articles'] = len(articles)

# Keywords
sports_keywords = {
    'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 
    'olympic', 'olympics', 'medal', 'game', 'match', 'tournament', 'championship', 'league', 
    'team', 'athlete', 'player', 'coach', 'stadium', 'racing', 'f1', 'formula 1', 'nascar', 
    'cricket', 'rugby', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 
    'wimbledon', 'grand slam', 'touchdown', 'homerun', 'score', 'scored', 'winning', 'losing', 'victory', 'defeat',
    'athens', 'gold', 'silver', 'bronze', 'cup'
}

potential_sports_matches = []
sports_count = 0

for a in articles:
    text = (a.get('title', '') + " " + a.get('description', '')).lower()
    tokens = set(re.findall(r'\b\w+\b', text))
    
    matches = []
    for k in sports_keywords:
        if k in tokens:
            matches.append(k)
    
    if matches:
        sports_count += 1
        if len(potential_sports_matches) < 10:
            potential_sports_matches.append({
                'title': a['title'],
                'matches': matches
            })

debug_info['sports_count'] = sports_count
debug_info['samples'] = potential_sports_matches

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10263163882729604573': ['articles'], 'var_function-call-10263163882729604264': ['authors', 'article_metadata'], 'var_function-call-17900817817497807775': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15939149844553677031': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-526178464523967050': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11607585572360918056': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2994061000156864416': 'file_storage/function-call-2994061000156864416.json', 'var_function-call-18200326237114442273': {}, 'var_function-call-4417731754548929407': {'info': 'debug'}}

exec(code, env_args)
