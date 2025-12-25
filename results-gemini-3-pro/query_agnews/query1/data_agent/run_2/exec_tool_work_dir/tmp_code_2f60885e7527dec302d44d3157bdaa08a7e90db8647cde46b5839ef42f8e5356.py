code = """import json
import re

# Load data
with open(locals()['var_function-call-17062830549632021172'], 'r') as f:
    articles = json.load(f)

# Sort by description length descending
articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Keywords
categories = {
    'Sports': [
        r'sport', r'football', r'baseball', r'basketball', r'soccer', r'tennis', r'golf', r'hockey', 
        r'cricket', r'rugby', r'athlete', r'player', r'team', r'coach', r'stadium', r'match', 
        r'tournament', r'championship', r'league', r'olympic', r'medal', r'cup\b', r'nfl', r'nba', 
        r'mlb', r'nhl', r'fifa', r'uefa', r'wimbledon', r'grand slam', r'race', r'racing', r'driver', 
        r'boxing', r'wrestling', r'score', r'victory', r'defeat', r'win', r'season', r'playoff', 
        r'super bowl', r'world series', r'athens' # Athens Olympics 2004 context
    ],
    'Business': [
        r'stock', r'market', r'wall st', r'price', r'oil', r'economy', r'company', r'corp', 
        r'inc\.', r'profit', r'loss', r'dollar', r'euro', r'bank', r'trade', r'investment', 
        r'deal', r'ceo', r'share', r'investor', r'business', r'federal reserve', r'rates', 
        r'nasdaq', r'dow jones'
    ],
    'SciTech': [
        r'computer', r'software', r'internet', r'web', r'google', r'microsoft', r'technology', 
        r'science', r'space', r'nasa', r'chip', r'intel', r'linux', r'phone', r'mobile', 
        r'wireless', r'digital', r'virus', r'hacker', r'online', r'search engine', r'apple'
    ],
    'World': [
        r'war', r'iraq', r'president', r'minister', r'government', r'police', r'bomb', r'election', 
        r'united nations', r'military', r'army', r'soldier', r'peace', r'attack', r'official', 
        r'country', r'state', r'china', r'russia', r'iran', r'israel', r'palestinian', r'blast'
    ]
}

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, kws in categories.items():
        for kw in kws:
            if re.search(kw, text):
                scores[cat] += 1
                
    # Adjustments
    if "video game" in text:
        scores['SciTech'] += 5
    if "oil prices" in text:
        scores['Business'] += 3
    if "gold medal" in text:
        scores['Sports'] += 5
    
    # Get max score
    if sum(scores.values()) == 0:
        return None
    
    best_cat = max(scores, key=scores.get)
    # Ensure it's strictly better or dominant
    if scores[best_cat] == 0:
        return None
        
    return best_cat, scores

candidates = []
for art in articles:
    res = classify(art.get('title', ''), art.get('description', ''))
    if res and res[0] == 'Sports':
        # Check if score is convincing (e.g., > 1 keyword or much higher than others)
        # But for now, just collect
        candidates.append(art)
        if len(candidates) >= 5:
            break

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-2359217064653629904': ['articles'], 'var_function-call-2359217064653631391': ['authors', 'article_metadata'], 'var_function-call-12491833190208577722': [{'_id': '694464677c0ede8b60d25e3c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9351886142223050984': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-7977853732793881019': [{'_id': '694464677c0ede8b60d25e3c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694464677c0ede8b60d25e3d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694464677c0ede8b60d25e3e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694464677c0ede8b60d25e3f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694464677c0ede8b60d25e40', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17062830549632021172': 'file_storage/function-call-17062830549632021172.json', 'var_function-call-18351005198250448470': [], 'var_function-call-1529751335608792055': 'file_storage/function-call-1529751335608792055.json'}

exec(code, env_args)
