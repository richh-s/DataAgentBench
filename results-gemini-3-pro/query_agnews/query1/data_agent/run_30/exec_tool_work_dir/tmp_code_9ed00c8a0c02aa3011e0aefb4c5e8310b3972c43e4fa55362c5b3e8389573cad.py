code = """import json

with open(locals()['var_function-call-2994061000156864416'], 'r') as f:
    articles = json.load(f)

# Keywords
strong_sports = {
    'olympic', 'olympics', 'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf', 
    'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'nascar', 'f1', 'rugby', 'cricket', 
    'athens', 'superbowl', 'worldcup', 'touchdown', 'homerun', 'grandslam'
}

weak_sports = {
    'sport', 'sports', 'game', 'match', 'team', 'win', 'won', 'loss', 'lost', 'score', 'scored', 
    'victory', 'defeat', 'coach', 'player', 'stadium', 'champion', 'championship', 'medal', 
    'league', 'tournament', 'cup', 'racing', 'race', 'athlete', 'gold', 'silver', 'bronze'
}

business_tech_world = {
    'stock', 'market', 'economy', 'oil', 'price', 'company', 'corp', 'profit', 'investment', 
    'dollar', 'euro', 'bank', 'trade', 'deficit', 'inflation', 'wall', 'street', 'ipo', 'fed', 
    'shares', 'revenue', 'business', 'industry', 'investor', 'iraq', 'war', 'president', 
    'election', 'minister', 'gov', 'un', 'official', 'police', 'bomb', 'kill', 'military', 
    'computer', 'software', 'technology', 'tech', 'internet', 'web', 'google', 'microsoft', 
    'science', 'nasa', 'nuclear', 'politics'
}

sports_articles = []

for a in articles:
    text = (a.get('title', '') + " " + a.get('description', '')).lower()
    
    # Tokenize
    tokens = []
    for t in text.split():
        t = ''.join(c for c in t if c.isalnum())
        if t: tokens.append(t)
    token_set = set(tokens)
    
    strong_hits = 0
    weak_hits = 0
    neg_hits = 0
    
    for t in token_set:
        if t in strong_sports:
            strong_hits += 1
        elif t in weak_sports:
            weak_hits += 1
        elif t in business_tech_world:
            neg_hits += 1
            
    # Classification Logic
    is_sports = False
    
    # If we have strong sports keywords, it's likely sports unless overridden by many negs?
    # Actually, "Olympic security concerns" might be World/Business.
    # "Football player arrested" -> Sports (usually).
    # "Game software company" -> Tech.
    
    if strong_hits > 0:
        # If it has strong sports words, likely sports.
        # Check context: if neg_hits is high, might be business/world.
        if neg_hits > strong_hits + 1:
            is_sports = False # E.g. "Olympics security budget increased by government"
        else:
            is_sports = True
    elif weak_hits >= 2 and neg_hits == 0:
        # E.g. "Team won the match" -> Sports
        # "Team managed the project" (neg=0?) -> 'managed', 'project' not in neg list. 
        # Need to be careful. 
        # But weak_hits >= 2 is a good heuristic.
        is_sports = True
    
    if is_sports:
        sports_articles.append(a)

# Find longest description among identified sports articles
longest_article = None
max_len = -1

for a in sports_articles:
    desc = a.get('description', '')
    if len(desc) > max_len:
        max_len = len(desc)
        longest_article = a

result = {}
if longest_article:
    result = {
        'title': longest_article['title'],
        'description_length': max_len,
        'matched_sports_count': len(sports_articles)
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10263163882729604573': ['articles'], 'var_function-call-10263163882729604264': ['authors', 'article_metadata'], 'var_function-call-17900817817497807775': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15939149844553677031': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-526178464523967050': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11607585572360918056': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2994061000156864416': 'file_storage/function-call-2994061000156864416.json', 'var_function-call-18200326237114442273': {}, 'var_function-call-4417731754548929407': {'info': 'debug'}, 'var_function-call-14408650637155143513': {'total_articles': 10000, 'sports_count': 0, 'samples': []}, 'var_function-call-4474884383524625212': {'first_article': {'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'first_article_text_lower': "wall st. bears claw back into the black (reuters) reuters - short-sellers, wall street's dwindling\\band of ultra-cynics, are seeing green again.", 'first_article_tokens': [], 'contains_the': False}, 'var_function-call-9427981795056471964': {'split_tokens': ['wall', 'st.', 'bears', 'claw', 'back', 'into', 'the', 'black', '(reuters)', 'reuters', '-', 'short-sellers,', 'wall', "street's", 'dwindling\\band', 'of', 'ultra-cynics,', 'are', 'seeing', 'green', 'again.'], 'clean_tokens': ['wall', 'st', 'bears', 'claw', 'back', 'into', 'the', 'black', 'reuters', 'reuters', 'shortsellers', 'wall', 'streets', 'dwindlingband', 'of', 'ultracynics', 'are', 'seeing', 'green', 'again']}}

exec(code, env_args)
