code = """import json

# Read the full results from the file
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    all_articles = json.load(f)

# More specific sports keywords - avoid false positives for tech/business terms
sports_keywords = [
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
    'olympic', 'olympics', 'athlete', 'athletes', 'championship', 'tournament', 
    'coach', 'player', 'players', 'match', 'stadium', 'arena', 'racing', 'race',
    'competition', 'champion', 'cup', 'final', 'finals', 'medal', 'medals',
    'gold', 'silver', 'bronze', 'ski', 'skiing', 'hockey', 'cricket', 'rugby',
    'boxing', 'wrestling', 'swimming', 'track', 'field', 'hockey', 'cycling',
    'marathon', 'sprint', 'jump', 'throw', 'league', 'season', 'game'  # 'game' is tricky but context matters
]

# Filter for sports articles more carefully
sports_articles = []
sample_matches = []  # To debug what we're matching

for article in all_articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    # Check for sports keywords, but be more strict about context
    is_sports = False
    matched_terms = []
    
    for keyword in sports_keywords:
        # Skip overly broad terms unless in specific context
        if keyword in ['game', 'games', 'play', 'playing', 'team']:
            # Check if 'game' appears in sports context
            sports_context_terms = ['football', 'basketball', 'baseball', 'soccer', 'madden', 'nfl', 'nba', 'mlb', 'nhl', 'video game']
            if any(ctx in title_lower or ctx in desc_lower for ctx in sports_context_terms):
                if keyword in title_lower or keyword in desc_lower:
                    is_sports = True
                    matched_terms.append(keyword)
        else:
            if keyword in title_lower or keyword in desc_lower:
                is_sports = True
                matched_terms.append(keyword)
    
    if is_sports:
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'desc_length': len(article['description'])
        })
        if len(sample_matches) < 10:  # Just store a few for debugging
            sample_matches.append({
                'title': article['title'],
                'matched': matched_terms
            })

# Find the sports article with the longest description
if sports_articles:
    # Sort by description length to find the longest
    sorted_articles = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)
    
    longest_article = sorted_articles[0]
    
    result = {
        'article_id': longest_article['article_id'],
        'title': longest_article['title'],
        'description_length': longest_article['desc_length'],
        'total_sports_found': len(sports_articles),
        'sample_matches': sample_matches[:5]
    }
else:
    result = {'error': 'No sports articles found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696f2adab40c1ef731f1d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696f2adab40c1ef731f1d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696f2adab40c1ef731f1d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696f2adab40c1ef731f1da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696f2adab40c1ef731f1db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '69696f2adab40c1ef731f1d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696f2adab40c1ef731f1d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696f2adab40c1ef731f1d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696f2adab40c1ef731f1da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696f2adab40c1ef731f1db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': [{'_id': '69696f2adab40c1ef731f1d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696f2adab40c1ef731f1d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696f2adab40c1ef731f1d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696f2adab40c1ef731f1da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696f2adab40c1ef731f1db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'article_id': '368', 'title': 'AMD starts shipping 90-nanometer chips to customers', 'description_length': 810}}

exec(code, env_args)
