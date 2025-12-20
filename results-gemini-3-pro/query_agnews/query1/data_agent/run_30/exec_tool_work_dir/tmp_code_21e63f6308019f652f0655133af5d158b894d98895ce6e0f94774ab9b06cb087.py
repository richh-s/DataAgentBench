code = """import json

with open(locals()['var_function-call-2994061000156864416'], 'r') as f:
    articles = json.load(f)

# (Include the keywords and logic again or simplify for debugging)
strong_sports = {
    'olympic', 'olympics', 'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf', 
    'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'nascar', 'f1', 'rugby', 'cricket', 
    'athens', 'superbowl', 'worldcup', 'touchdown', 'homerun', 'grandslam', 'pga', 'lpga', 'atp', 'wta',
    'doping', 'medal', 'medalist', 'gold', 'silver', 'bronze', 'marathon', 'sprint', 'relay', 'swimming', 
    'gymnastics', 'volleyball', 'boxing', 'wrestling', 'judo', 'taekwondo', 'cycling', 'rowing', 'diving'
}

weak_sports = {
    'sport', 'sports', 'game', 'match', 'team', 'win', 'won', 'loss', 'lost', 'score', 'scored', 
    'victory', 'defeat', 'coach', 'player', 'stadium', 'champion', 'championship', 'league', 
    'tournament', 'cup', 'race', 'athlete'
}

non_sports = {
    'stock', 'market', 'economy', 'oil', 'price', 'company', 'corp', 'profit', 'investment', 
    'dollar', 'euro', 'bank', 'trade', 'deficit', 'inflation', 'wall', 'street', 'ipo', 'fed', 
    'shares', 'revenue', 'business', 'industry', 'investor', 'sales', 'retail', 'earnings', 
    'computer', 'software', 'technology', 'tech', 'internet', 'web', 'google', 'microsoft', 
    'science', 'nasa', 'nuclear', 'phone', 'mobile', 'wireless', 'network', 'digital', 'device', 
    'linux', 'unix', 'windows', 'apple', 'ibm', 'intel', 'chip', 'virus', 'security',
    'iraq', 'war', 'president', 'election', 'minister', 'gov', 'un', 'official', 'police', 
    'bomb', 'kill', 'military', 'attack', 'force', 'troops', 'army', 'soldier', 'baghdad', 
    'bush', 'kerry', 'senate', 'congress', 'vote', 'law', 'legal', 'court', 'trial', 'prison'
}

candidates = []

for a in articles:
    text = (a.get('title', '') + " " + a.get('description', '')).lower()
    tokens = []
    for t in text.split():
        t = ''.join(c for c in t if c.isalnum())
        if t: tokens.append(t)
    token_set = set(tokens)
    
    score = 0
    for t in token_set:
        if t in strong_sports: score += 5
        elif t in weak_sports: score += 1
    
    penalty = 0
    for t in token_set:
        if t in non_sports: penalty += 3
    
    if score > penalty:
        candidates.append(a)

# Sort by description length descending
candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

top_5 = []
for i in range(min(5, len(candidates))):
    top_5.append({
        'title': candidates[i]['title'],
        'len': len(candidates[i]['description']),
        'desc_preview': candidates[i]['description'][:100]
    })

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-10263163882729604573': ['articles'], 'var_function-call-10263163882729604264': ['authors', 'article_metadata'], 'var_function-call-17900817817497807775': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15939149844553677031': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-526178464523967050': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11607585572360918056': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2994061000156864416': 'file_storage/function-call-2994061000156864416.json', 'var_function-call-18200326237114442273': {}, 'var_function-call-4417731754548929407': {'info': 'debug'}, 'var_function-call-14408650637155143513': {'total_articles': 10000, 'sports_count': 0, 'samples': []}, 'var_function-call-4474884383524625212': {'first_article': {'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'first_article_text_lower': "wall st. bears claw back into the black (reuters) reuters - short-sellers, wall street's dwindling\\band of ultra-cynics, are seeing green again.", 'first_article_tokens': [], 'contains_the': False}, 'var_function-call-9427981795056471964': {'split_tokens': ['wall', 'st.', 'bears', 'claw', 'back', 'into', 'the', 'black', '(reuters)', 'reuters', '-', 'short-sellers,', 'wall', "street's", 'dwindling\\band', 'of', 'ultra-cynics,', 'are', 'seeing', 'green', 'again.'], 'clean_tokens': ['wall', 'st', 'bears', 'claw', 'back', 'into', 'the', 'black', 'reuters', 'reuters', 'shortsellers', 'wall', 'streets', 'dwindlingband', 'of', 'ultracynics', 'are', 'seeing', 'green', 'again']}, 'var_function-call-16852696022568568483': {'title': "Why Windows isn't Unix", 'description_length': 708, 'matched_sports_count': 1775}, 'var_function-call-7985043121924685008': {'title': 'Pretty Log4J', 'description_length': 708, 'matched_sports_count': 2402}}

exec(code, env_args)
