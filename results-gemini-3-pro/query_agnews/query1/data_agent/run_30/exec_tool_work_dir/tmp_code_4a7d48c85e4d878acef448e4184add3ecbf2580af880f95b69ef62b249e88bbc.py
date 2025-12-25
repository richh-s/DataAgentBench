code = """import json
import pandas as pd

# Load the data
with open(locals()['var_function-call-2994061000156864416'], 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = {
    'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 
    'olympic', 'olympics', 'medal', 'game', 'match', 'tournament', 'championship', 'league', 
    'team', 'athlete', 'player', 'coach', 'stadium', 'racing', 'f1', 'formula 1', 'nascar', 
    'cricket', 'rugby', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 
    'wimbledon', 'grand slam', 'touchdown', 'homerun', 'score', 'scored', 'winning', 'losing', 'victory', 'defeat',
    'athens', 'gold', 'silver', 'bronze' # Athens 2004 Olympics might be relevant given the dates in preview (2004)
}

business_keywords = {
    'stock', 'market', 'economy', 'oil', 'price', 'company', 'corp', 'profit', 'investment', 
    'dollar', 'euro', 'bank', 'trade', 'deficit', 'inflation', 'wall st', 'ipo', 'fed', 'rates', 
    'ceo', 'executive', 'shares', 'revenue', 'quarter', 'business', 'industry', 'investor'
}

scitech_keywords = {
    'computer', 'software', 'technology', 'tech', 'internet', 'web', 'google', 'microsoft', 
    'space', 'nasa', 'science', 'chip', 'virus', 'phone', 'mobile', 'online', 'digital', 'network',
    'apple', 'ibm', 'intel', 'server', 'satellite', 'launch'
}

world_keywords = {
    'iraq', 'war', 'president', 'election', 'minister', 'gov', 'un', 'official', 'police', 
    'bomb', 'kill', 'attack', 'military', 'security', 'nuclear', 'peace', 'treaty', 'politics',
    'baghdad', 'bush', 'kerry', 'palestinian', 'israel', 'gaza', 'force', 'blast'
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {'Sports': 0, 'Business': 0, 'SciTech': 0, 'World': 0}
    
    words = set(text.split())
    # A simple token check might be enough, but substring matching is safer for variations.
    # However, whole word matching is better to avoid false positives (e.g. "team" in "steam").
    # Let's clean text and split.
    import re
    tokens = re.findall(r'\b\w+\b', text)
    token_set = set(tokens)

    for k in sports_keywords:
        if k in token_set: scores['Sports'] += 1
    for k in business_keywords:
        if k in token_set: scores['Business'] += 1
    for k in scitech_keywords:
        if k in token_set: scores['SciTech'] += 1
    for k in world_keywords:
        if k in token_set: scores['World'] += 1

    # Heuristic adjustments:
    # "Oil" is strongly Business/World.
    # "Iraq" is strongly World.
    # "Olympics" is strongly Sports.
    
    # Get max score
    if max(scores.values()) == 0:
        return 'Unknown'
    return max(scores, key=scores.get)

sports_articles = []
for a in articles:
    cat = classify(a.get('title', ''), a.get('description', ''))
    if cat == 'Sports':
        sports_articles.append(a)

print(f"Total articles: {len(articles)}")
print(f"Identified Sports articles: {len(sports_articles)}")

# Find longest description
longest_article = None
max_len = -1

for a in sports_articles:
    desc_len = len(a.get('description', ''))
    if desc_len > max_len:
        max_len = desc_len
        longest_article = a

result = {}
if longest_article:
    result = {
        'title': longest_article['title'],
        'description_length': max_len,
        'description': longest_article['description'] # For verification
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10263163882729604573': ['articles'], 'var_function-call-10263163882729604264': ['authors', 'article_metadata'], 'var_function-call-17900817817497807775': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15939149844553677031': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-526178464523967050': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11607585572360918056': [{'_id': '69447955723e56e91976cc69', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447955723e56e91976cc6a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447955723e56e91976cc6b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447955723e56e91976cc6c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447955723e56e91976cc6d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2994061000156864416': 'file_storage/function-call-2994061000156864416.json'}

exec(code, env_args)
