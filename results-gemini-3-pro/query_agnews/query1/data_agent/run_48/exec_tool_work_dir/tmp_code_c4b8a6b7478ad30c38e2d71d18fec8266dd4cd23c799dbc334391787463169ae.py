code = """import json

file_path = locals()['var_function-call-303762971753374915']

with open(file_path, 'r') as f:
    articles = json.load(f)

sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 
    'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'tournament', 
    'championship', 'medal', 'olympic', 'olympics', 'athens', 'games', 'cup', 'racing', 'prix', 
    'driver', 'athlete', 'coach', 'squad', 'team', 'match', 'score', 'win', 'defeat', 
    'victory', 'gold', 'silver', 'bronze', 'record', 'league', 'club', 'manager', 
    'player', 'season', 'title', 'final', 'semi-final', 'quarter-final', 'wimbledon', 
    'us open', 'tour de france', 'stadium', 'field', 'court', 'pitch', 'referee', 'umpire',
    'sox', 'yankees', 'mets', 'bulls', 'pistons', 'pacers', 'lakers', 'spurs', 'heat', 
    'arsenal', 'chelsea', 'united', 'real madrid', 'barcelona', 'milan', 'juventus',
    'grand slam', 'touchdown', 'homerun', 'strikeout', 'f1', 'schumacher', 'armstrong',
    'phelps', 'gymnastics', 'swimming', 'track', 'marathon', 'sprint', 'relay', 'diving',
    'boxing', 'wrestling', 'volleyball', 'handball', 'badminton', 'archery', 'shooting',
    'rowing', 'canoe', 'kayak', 'sailing', 'equestrian', 'fencing', 'judo', 'taekwondo',
    'weightlifting', 'triathlon', 'pentathlon', 'decathlon', 'heptathlon'
}

# I'll rely mainly on scoring.
def is_sports(text):
    text = text.lower()
    score = 0
    words = text.replace('.', ' ').replace(',', ' ').replace("'", " ").replace('"', ' ').split()
    for w in words:
        if w in sports_keywords:
            score += 1
    return score

candidates = []

for art in articles:
    # Combine title and description for classification context
    full_text = art.get('title', '') + " " + art.get('description', '')
    score = is_sports(full_text)
    
    # We need to distinguish from Business/World.
    # Words like 'record', 'win', 'loss' can be business.
    # Words like 'team', 'squad', 'coach', 'player', 'athlete', 'olympic' are very sports specific.
    # Let's check for strong sports keywords.
    strong_sports = {'olympic', 'olympics', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 
                     'wimbledon', 'athens', 'medal', 'athlete', 'player', 'coach', 'team', 
                     'tournament', 'championship', 'cup', 'soccer', 'basketball', 'baseball', 
                     'football', 'tennis', 'hockey', 'cricket', 'rugby', 'racing', 'prix'}
    
    strong_hits = sum(1 for w in full_text.lower().split() if w in strong_sports)
    
    # Simple heuristic: if strong hits > 0 or score > 2, consider it.
    # But filtering strictly might be better.
    if strong_hits > 0 or score >= 2:
        candidates.append(art)

if not candidates:
    print('__RESULT__:')
    print(json.dumps({"error": "No sports articles found"}))
else:
    # Sort by description length
    candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)
    best = candidates[0]
    print('__RESULT__:')
    print(json.dumps({
        "title": best['title'],
        "len": len(best['description']),
        "desc_preview": best['description']
    }))"""

env_args = {'var_function-call-13425849250340165156': ['articles'], 'var_function-call-13425849250340165453': ['authors', 'article_metadata'], 'var_function-call-17951318789273803263': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6587525704781607090': {'error': 'No sports articles found'}, 'var_function-call-11688380307488085183': [{'_id': '6944891d88e03095837aa408', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944891d88e03095837aa409', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944891d88e03095837aa40a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944891d88e03095837aa40b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944891d88e03095837aa40c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-303762971753374915': 'file_storage/function-call-303762971753374915.json'}

exec(code, env_args)
