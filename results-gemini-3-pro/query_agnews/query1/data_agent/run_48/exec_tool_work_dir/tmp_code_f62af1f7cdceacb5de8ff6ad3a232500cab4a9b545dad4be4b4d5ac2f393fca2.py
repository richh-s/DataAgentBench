code = """import json

file_path = locals()['var_function-call-303762971753374915']

with open(file_path, 'r') as f:
    articles = json.load(f)

# Expanded Keywords
sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 
    'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'tournament', 
    'championship', 'medal', 'olympic', 'olympics', 'athens', 'cup', 'racing', 'prix', 
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
    'weightlifting', 'triathlon', 'pentathlon', 'decathlon', 'heptathlon', 'games'
}

business_keywords = {
    'market', 'stock', 'price', 'oil', 'economy', 'business', 'company', 'corp', 'inc', 
    'profit', 'loss', 'quarter', 'earnings', 'share', 'invest', 'bank', 'finance', 'trade', 
    'dollar', 'euro', 'yen', 'ceo', 'manager', 'audit', 'revenue', 'sale', 'deal', 'merger', 
    'acquisition', 'wall st', 'nasdaq', 'dow', 'index', 'fed', 'rates', 'inflation', 'growth',
    'u.s.', 'imf', 'wto', 'budget', 'debt', 'deficit', 'employment', 'job', 'retail', 'sales'
}

sci_tech_keywords = {
    'technology', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
    'space', 'nasa', 'moon', 'mars', 'virus', 'microsoft', 'google', 'apple', 'intel', 'chip', 
    'phone', 'mobile', 'wireless', 'network', 'satellite', 'digital', 'research', 'study', 
    'scientist', 'discovery', 'launch', 'orbit', 'astronomer', 'biotech', 'genome', 'linux', 
    'windows', 'server', 'broadband', 'spam', 'hacker', 'unix', 'dos', 'bug', 'code', 'developer',
    'application', 'system', 'program', 'memory', 'processor', 'search', 'engine', 'browser'
}

world_keywords = {
    'world', 'war', 'iraq', 'iran', 'president', 'election', 'government', 'minister', 
    'official', 'police', 'military', 'army', 'bomb', 'attack', 'kill', 'peace', 'treaty', 
    'un', 'united nations', 'country', 'state', 'region', 'china', 'russia', 'usa', 'uk', 
    'bush', 'kerry', 'palestinian', 'israel', 'gaza', 'baghdad', 'afghanistan', 'blast', 
    'troops', 'security', 'nuclear', 'politics', 'parliament', 'vote', 'rebel', 'darfur', 
    'sudan', 'crisis', 'hostage', 'kidnap', 'terror', 'qaeda'
}

def get_category_score(text, keywords):
    score = 0
    # Improved tokenization
    words = text.lower().replace('.', ' ').replace(',', ' ').replace("'", " ").replace('"', ' ').replace('-', ' ').split()
    for word in words:
        if word in keywords:
            score += 1
    return score

classified_articles = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    s_score = get_category_score(text, sports_keywords)
    b_score = get_category_score(text, business_keywords)
    st_score = get_category_score(text, sci_tech_keywords)
    w_score = get_category_score(text, world_keywords)
    
    scores = {'Sports': s_score, 'Business': b_score, 'Sci/Tech': st_score, 'World': w_score}
    best_cat = max(scores, key=scores.get)
    max_score = scores[best_cat]
    
    # We only care if it is sports.
    # Check if Sports is the clear winner or tied for winner with a significant score.
    if best_cat == 'Sports' and max_score > 0:
        # Check if tied with others
        tied = [k for k, v in scores.items() if v == max_score]
        if len(tied) == 1:
            # Clear winner
            classified_articles.append(art)
        else:
            # Tied. If tied with World/Business, it's ambiguous.
            # But let's look at the tied categories.
            # If Sports is tied with Tech (e.g. "game"), we might need to check specific words.
            # For now, let's include it, but maybe verify later.
            classified_articles.append(art)

if not classified_articles:
    print('__RESULT__:')
    print(json.dumps({"error": "No sports articles found"}))
else:
    # Sort by description length
    classified_articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)
    best = classified_articles[0]
    
    print('__RESULT__:')
    print(json.dumps({
        "title": best['title'],
        "len": len(best['description']),
        "desc_preview": best['description']
    }))"""

env_args = {'var_function-call-13425849250340165156': ['articles'], 'var_function-call-13425849250340165453': ['authors', 'article_metadata'], 'var_function-call-17951318789273803263': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6587525704781607090': {'error': 'No sports articles found'}, 'var_function-call-11688380307488085183': [{'_id': '6944891d88e03095837aa408', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944891d88e03095837aa409', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944891d88e03095837aa40a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944891d88e03095837aa40b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944891d88e03095837aa40c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-303762971753374915': 'file_storage/function-call-303762971753374915.json', 'var_function-call-1054896516764720812': {'title': "Why Windows isn't Unix", 'len': 708, 'desc_preview': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}}

exec(code, env_args)
