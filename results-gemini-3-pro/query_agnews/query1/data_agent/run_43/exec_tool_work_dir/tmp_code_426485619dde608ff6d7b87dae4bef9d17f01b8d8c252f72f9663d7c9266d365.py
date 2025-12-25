code = """import json
import re

file_path = locals().get('var_function-call-5317808320419996611')
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define sports keywords (expanded)
sports_keywords = {
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
    'olympic', 'olympics', 'nfl', 'nba', 'mlb', 'nhl', 'racing', 'hockey', 'cricket', 
    'rugby', 'boxing', 'medal', 'athlete', 'stadium', 'championship', 'tournament', 
    'wrestling', 'swimming', 'marathon', 'sprint', 'coach', 'referee', 'score', 'match',
    'win', 'loss', 'victory', 'defeat', 'team', 'player', 'game', 'league', 'cup'
}

# Define non-sports keywords (to downweight business/tech/world)
non_sports_keywords = {
    'market', 'stock', 'company', 'profit', 'shares', 'investor', 'economy', 'bank',
    'trade', 'industry', 'corp', 'inc', 'ceo', 'dollar', 'price', 'oil', 'sales',
    'software', 'computer', 'technology', 'internet', 'web', 'microsoft', 'google',
    'president', 'minister', 'war', 'peace', 'treaty', 'government', 'election', 
    'police', 'military', 'iraq', 'iran', 'china', 'us', 'uk', 'un', 'official',
    'security', 'satellite', 'nasa', 'space'
}

def is_sports(title, desc):
    text = (title + " " + desc).lower()
    words = re.findall(r'\w+', text)
    score = 0
    for w in words:
        if w in sports_keywords:
            score += 1
        elif w in non_sports_keywords:
            score -= 1
    return score > 0

# Calculate length and filter
candidates = []
for a in articles:
    desc = a.get('description', '')
    title = a.get('title', '')
    length = len(desc)
    # Check if it looks like sports
    if is_sports(title, desc):
        candidates.append({
            'title': title,
            'description': desc,
            'length': length
        })

# Sort by length desc
candidates.sort(key=lambda x: x['length'], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:10])) # Print top 10 to inspect"""

env_args = {'var_function-call-16887170130600162820': ['articles'], 'var_function-call-16887170130600164689': ['authors', 'article_metadata'], 'var_function-call-1667594192334497282': [{'_id': '694485990904476d73566a93', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-1667594192334496969': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2349551306723075946': [{'_id': '694485990904476d73566a93', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694485990904476d73566a94', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694485990904476d73566a95', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694485990904476d73566a96', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694485990904476d73566a97', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14283972282363124164': [{'_id': '694485990904476d73566a93', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694485990904476d73566a94', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694485990904476d73566a95', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694485990904476d73566a96', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694485990904476d73566a97', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5718934265307158286': 5, 'var_function-call-14251754240139237849': [{'count(*)': '127600'}], 'var_function-call-5317808320419996611': 'file_storage/function-call-5317808320419996611.json'}

exec(code, env_args)
