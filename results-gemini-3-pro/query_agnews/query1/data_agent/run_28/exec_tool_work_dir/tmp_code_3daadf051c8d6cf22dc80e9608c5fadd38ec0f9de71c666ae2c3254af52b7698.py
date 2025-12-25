code = """import json
import re

file_path = locals()['var_function-call-5992979480702397850']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
strong_sports = set([
    'olympics', 'olympic', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'world cup', 
    'super bowl', 'wimbledon', 'nascar', 'f1', 'formula 1', 'quarterback', 'touchdown', 
    'slam dunk', 'homerun', 'athens', 'phelps', 'thorpe', 'red sox', 'yankees', 'lakers', 
    'bulls', 'manchester united', 'real madrid', 'tiger woods', 'lance armstrong', 'pga', 
    'tour de france', 'davis cup', 'ryder cup', 'stanley cup', 'medal', 'gold medal', 
    'basketball', 'football', 'baseball', 'soccer', 'tennis', 'hockey', 'rugby', 'cricket', 
    'boxing', 'swimming', 'gymnastics', 'volleyball', 'athlete'
])

weak_sports = set([
    'sport', 'sports', 'team', 'coach', 'game', 'match', 'score', 'win', 'loss', 'victory', 
    'defeat', 'champion', 'championship', 'tournament', 'league', 'stadium', 'player', 
    'race', 'driver', 'squad', 'club', 'cup'
])

business = set([
    'market', 'stock', 'price', 'oil', 'economy', 'fund', 'company', 'profit', 'bank', 
    'dollar', 'trade', 'deficit', 'ipo', 'share', 'investor', 'wall st', 'revenue', 'sale', 'corp', 'inc'
])

tech = set([
    'computer', 'software', 'internet', 'web', 'google', 'microsoft', 'technology', 'space', 
    'nasa', 'science', 'online', 'search', 'chip', 'linux', 'windows', 'apple', 'rocket', 'launch', 'satellite'
])

world = set([
    'iraq', 'president', 'minister', 'official', 'nuclear', 'war', 'conflict', 'bomb', 
    'government', 'election', 'bush', 'kerry', 'palestinian', 'israel', 'gaza', 'iran'
])

entertainment = set([
    'movie', 'film', 'actor', 'actress', 'star', 'hollywood', 'cinema', 'director', 
    'drama', 'comedy', 'series', 'television', 'tv', 'show', 'music', 'album', 'song', 'singer', 'band'
])

def classify(title, desc):
    text = (title + " " + desc).lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    
    scores = {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0, 'Entertainment': 0}
    
    for word in words:
        if word in strong_sports:
            scores['Sports'] += 3
        elif word in weak_sports:
            scores['Sports'] += 1
            
        if word in business:
            scores['Business'] += 2
            
        if word in tech:
            scores['Sci/Tech'] += 2
            
        if word in world:
            scores['World'] += 2
            
        if word in entertainment:
            scores['Entertainment'] += 2

    # Analyze scores
    # If Entertainment is high, it's likely not Sports unless Sports is very high
    # In AG News, Entertainment is usually not a separate category, but "World" often contains it or it's mixed.
    # But here we want strictly "Sports".
    
    # Heuristic: If Tech > Sports, likely Tech.
    # If Business > Sports, likely Business.
    # If World > Sports, likely World.
    # If Entertainment > Sports, likely not Sports (could be World).
    
    # Let's find the max score.
    # But prioritize Strong Sports.
    
    # Adjust scores:
    # If "space" or "rocket" is present, penalize Sports (to fix Ansari X Prize).
    if 'space' in words or 'rocket' in words or 'nasa' in words:
        scores['Sci/Tech'] += 5
        
    # If "actor" or "movie" is present, penalize Sports?
    # Dean Cain article: "actor" (no), "movie" (yes), "television" (yes), "drama" (yes).
    # It also has "football", "sportsman", "baseball".
    # Let's see the scores.
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown'
        
    return best_cat

candidates = []
for a in articles:
    # Debug Dean Cain
    if a['title'] == "THECHAT":
        # Calculate scores for debugging
        pass
        
    cat = classify(a['title'], a['description'])
    if cat == 'Sports':
        candidates.append(a)

candidates.sort(key=lambda x: len(x['description']), reverse=True)

top_5 = []
for a in candidates[:5]:
    top_5.append({
        "title": a['title'],
        "len": len(a['description']),
        "snippet": a['description'][:100]
    })

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-17474201203646605766': [{'_id': '694477c2c05dceb7dbb2a37f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-17474201203646605649': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-4380353603905367895': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-489200824219056741': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)'], 'var_function-call-5182264313968244438': [{'_id': '694477c2c05dceb7dbb2a37f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694477c2c05dceb7dbb2a380', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694477c2c05dceb7dbb2a381', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694477c2c05dceb7dbb2a382', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694477c2c05dceb7dbb2a383', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5992979480702397850': 'file_storage/function-call-5992979480702397850.json', 'var_function-call-7174997949604402314': {'title': 'THECHAT', 'description_length': 631, 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;'}, 'var_function-call-9166078951978711109': [{'title': 'THECHAT', 'len': 631, 'snippet': "&lt;em&gt; Dean Cain has spent much of his life in a uniform. He's done time as an all-American safe"}, {'title': 'Canadian Ansari X Prize Entrant Takes the Plunge in Test (SPACE.com)', 'len': 552, 'snippet': 'SPACE.com - A Canadian team of rocketeers has moved one step closer to\\launching its own manned spac'}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'len': 532, 'snippet': "ATHENS, Greece - Lamar Odom made a key defensive play on Greece's Dimitris Pipanikoulaou, preventing"}, {'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'len': 483, 'snippet': 'AP - Chris DiMarco and Chris Riley faced knee-knocking pressure in the last round of the PGA Champio'}, {'title': 'TCU, Louisville Try to Leave C-USA Champs (AP)', 'len': 461, 'snippet': 'AP - TCU helped change the Bowl Championship Series, even though its season ended at home. The Horne'}]}

exec(code, env_args)
