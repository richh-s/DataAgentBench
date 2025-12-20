code = """import json

# Load articles
with open(locals()['var_function-call-17951318789273803263'], 'r') as f:
    articles = json.load(f)

# Define keywords for categories to help disambiguate
sports_keywords = {
    'sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 
    'cricket', 'rugby', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'tournament', 
    'championship', 'medal', 'olympic', 'athens', 'games', 'cup', 'racing', 'prix', 
    'driver', 'athlete', 'coach', 'squad', 'team', 'match', 'score', 'win', 'defeat', 
    'victory', 'gold', 'silver', 'bronze', 'record', 'league', 'club', 'manager', 
    'player', 'season', 'title', 'final', 'semi-final', 'quarter-final', 'wimbledon', 
    'us open', 'tour de france', 'stadium', 'field', 'court', 'pitch', 'referee', 'umpire'
}

business_keywords = {
    'market', 'stock', 'price', 'oil', 'economy', 'business', 'company', 'corp', 'inc', 
    'profit', 'loss', 'quarter', 'earnings', 'share', 'invest', 'bank', 'finance', 'trade', 
    'dollar', 'euro', 'yen', 'ceo', 'manager', 'audit', 'revenue', 'sale', 'deal', 'merger', 
    'acquisition', 'wall st', 'nasdaq', 'dow', 'index'
}

sci_tech_keywords = {
    'technology', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
    'space', 'nasa', 'moon', 'mars', 'virus', 'microsoft', 'google', 'apple', 'intel', 'chip', 
    'phone', 'mobile', 'wireless', 'network', 'satellite', 'digital', 'research', 'study', 
    'scientist', 'discovery', 'launch', 'orbit'
}

world_keywords = {
    'world', 'war', 'iraq', 'iran', 'president', 'election', 'government', 'minister', 
    'official', 'police', 'military', 'army', 'bomb', 'attack', 'kill', 'peace', 'treaty', 
    'un', 'united nations', 'country', 'state', 'region', 'china', 'russia', 'usa', 'uk', 
    'bush', 'kerry', 'palestinian', 'israel', 'gaza', 'baghdad'
}

def get_category_score(text, keywords):
    score = 0
    words = text.lower().replace('.', ' ').replace(',', ' ').split()
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
    
    # If tie, prioritize Sports if score > 0, else maybe World?
    # Actually, let's just keep those where Sports is strictly the winner or tied with high score.
    # A simple max is a good start.
    
    if best_cat == 'Sports' and s_score > 0:
        art['cat'] = 'Sports'
        classified_articles.append(art)
    elif s_score > b_score and s_score > st_score and s_score > w_score:
         art['cat'] = 'Sports'
         classified_articles.append(art)

# Find the one with max description length
if not classified_articles:
    print('__RESULT__:')
    print(json.dumps("No sports articles found"))
else:
    best_article = max(classified_articles, key=lambda x: len(x.get('description', '')))
    print('__RESULT__:')
    print(json.dumps({
        "title": best_article['title'],
        "len": len(best_article['description']),
        "desc_preview": best_article['description'][:50]
    }))"""

env_args = {'var_function-call-13425849250340165156': ['articles'], 'var_function-call-13425849250340165453': ['authors', 'article_metadata'], 'var_function-call-17951318789273803263': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
