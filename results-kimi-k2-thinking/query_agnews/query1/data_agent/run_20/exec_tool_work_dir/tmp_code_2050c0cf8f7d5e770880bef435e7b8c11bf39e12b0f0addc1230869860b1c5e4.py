code = """import json

# Read the full results from the file
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    all_articles = json.load(f)

# Define strong sports indicators - only use very specific terms
sports_indicators = [
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
    'olympic', 'olympics', 'hockey', 'cricket', 'rugby', 'boxing',
    'wrestling', 'swimming', 'skiing', 'cycling', 'marathon', 'sprint',
    'championship', 'tournament', 'coach', 'stadium', 'arena', 'medal',
    # Video games context (sports video games are sports-related)
    'madden nfl', 'ea sports', 'video game', 'gaming console'
]

# Business/tech terms to avoid false positives
false_positive_terms = [
    'season' in ['back-to-school', 'fashion season', 'holiday season'],
    'racing' in ['arms race', 'racing to market', 'space race'],
    'final' in ['final quarter', 'final results', 'final version'],
    'field' in ['field of study', 'magnetic field', 'oil field'],
    'ski' in ['skill', 'skills']
]

# Manual inspection of some articles suggests we need better filtering
# Let's scan for articles that are clearly sports-related
sports_articles = []

for article in all_articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    # Score the article based on sports indicators
    score = 0
    matches = []
    
    for indicator in sports_indicators:
        if indicator in title_lower or indicator in desc_lower:
            score += 1
            matches.append(indicator)
    
    # Only accept if it has strong sports indicators
    # Avoid false positives by requiring at least 2 indicators or very specific ones
    if score >= 2 or ('olympic' in matches) or ('olympics' in matches) or ('football' in matches and 'madden' in matches):
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'desc_length': len(article['description']),
            'score': score,
            'matches': matches
        })

if sports_articles:
    # Sort by description length
    sorted_articles = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)
    
    # Get top 10 to verify manually
    result = {
        'total_sports': len(sports_articles),
        'top_10_longest': sorted_articles[:10]
    }
else:
    result = {'error': 'No sports articles found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696f2adab40c1ef731f1d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696f2adab40c1ef731f1d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696f2adab40c1ef731f1d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696f2adab40c1ef731f1da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696f2adab40c1ef731f1db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '69696f2adab40c1ef731f1d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696f2adab40c1ef731f1d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696f2adab40c1ef731f1d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696f2adab40c1ef731f1da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696f2adab40c1ef731f1db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': [{'_id': '69696f2adab40c1ef731f1d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696f2adab40c1ef731f1d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696f2adab40c1ef731f1d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696f2adab40c1ef731f1da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696f2adab40c1ef731f1db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'article_id': '368', 'title': 'AMD starts shipping 90-nanometer chips to customers', 'description_length': 810}, 'var_functions.execute_python:12': {'article_id': '368', 'title': 'AMD starts shipping 90-nanometer chips to customers', 'description_length': 810, 'total_sports_found': 226, 'sample_matches': [{'title': 'Kids Rule for Back-to-School', 'matched': ['season']}, {'title': "Shell 'could be target for Total'", 'matched': ['racing']}, {'title': 'HP shares tumble on profit news', 'matched': ['final']}, {'title': 'Indians fill rail skills shortage', 'matched': ['ski']}, {'title': 'Researchers seek to untangle the e-mail thread', 'matched': ['field']}]}}

exec(code, env_args)
