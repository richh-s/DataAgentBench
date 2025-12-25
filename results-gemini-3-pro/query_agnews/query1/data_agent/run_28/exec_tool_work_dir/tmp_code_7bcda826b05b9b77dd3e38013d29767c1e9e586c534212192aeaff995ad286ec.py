code = """import json
import re

# Load the full list of articles
file_path = locals()['var_function-call-5992979480702397850']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = set([
    'sport', 'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 
    'cricket', 'rugby', 'boxing', 'olympics', 'olympic', 'medal', 'athlete', 'championship', 
    'tournament', 'league', 'stadium', 'team', 'coach', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 
    'world cup', 'super bowl', 'grand slam', 'wimbledon', 'us open', 'australian open', 'french open', 
    'nascar', 'f1', 'formula 1', 'racing', 'driver', 'quarterback', 'striker', 'goalkeeper', 
    'pitcher', 'batter', 'homerun', 'touchdown', 'slam dunk', 'athens', 'gold medal', 'silver medal', 
    'bronze medal', 'phelps', 'thorpe', 'dream team', 'red sox', 'yankees', 'lakers', 'bulls', 
    'manchester united', 'arsenal', 'chelsea', 'real madrid', 'barcelona', 'ac milan', 'juventus',
    'tiger woods', 'lance armstrong', 'doping', 'cup', 'match', 'game', 'score', 'win', 'loss', 'victory', 'defeat'
])

business_keywords = set([
    'market', 'stock', 'price', 'oil', 'economy', 'fund', 'company', 'profit', 'bank', 'rate', 
    'dollar', 'trade', 'deficit', 'ipo', 'share', 'investor', 'wall st', 'dow', 'nasdaq', 'fed', 
    'inflation', 'job', 'ceo', 'revenue', 'sale', 'deal', 'merger', 'acquisition', 'corp', 'inc'
])

tech_keywords = set([
    'computer', 'software', 'internet', 'web', 'google', 'microsoft', 'technology', 'space', 'nasa', 
    'science', 'online', 'search', 'virus', 'security', 'chip', 'intel', 'linux', 'windows', 'apple', 'ipod'
])

world_keywords = set([
    'iraq', 'president', 'minister', 'official', 'nuclear', 'war', 'conflict', 'bomb', 'kill', 'police', 
    'government', 'election', 'bush', 'kerry', 'palestinian', 'israel', 'gaza', 'baghdad', 'iran', 'darfur'
])

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    
    scores = {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}
    
    for word in words:
        if word in sports_keywords:
            scores['Sports'] += 1
        if word in business_keywords:
            scores['Business'] += 1
        if word in tech_keywords:
            scores['Sci/Tech'] += 1
        if word in world_keywords:
            scores['World'] += 1
            
    # Heuristic adjustment
    # "game" can be tech (video game). Check if "video" or "computer" is near.
    # "team" can be business.
    # "win" can be election.
    
    # If scores are all 0, default to something? Or unknown.
    if max(scores.values()) == 0:
        return 'Unknown'
    
    # Return category with max score
    return max(scores, key=scores.get)

sports_articles = []
for a in articles:
    cat = classify(a['title'], a['description'])
    if cat == 'Sports':
        sports_articles.append(a)

# Find the one with max description length
if not sports_articles:
    result = "No sports articles found."
else:
    # Sort by length descending
    sports_articles.sort(key=lambda x: len(x['description']), reverse=True)
    top_article = sports_articles[0]
    result = {
        "title": top_article['title'],
        "description_length": len(top_article['description']),
        "description": top_article['description']
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17474201203646605766': [{'_id': '694477c2c05dceb7dbb2a37f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-17474201203646605649': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-4380353603905367895': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-489200824219056741': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)'], 'var_function-call-5182264313968244438': [{'_id': '694477c2c05dceb7dbb2a37f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694477c2c05dceb7dbb2a380', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694477c2c05dceb7dbb2a381', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694477c2c05dceb7dbb2a382', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694477c2c05dceb7dbb2a383', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5992979480702397850': 'file_storage/function-call-5992979480702397850.json'}

exec(code, env_args)
