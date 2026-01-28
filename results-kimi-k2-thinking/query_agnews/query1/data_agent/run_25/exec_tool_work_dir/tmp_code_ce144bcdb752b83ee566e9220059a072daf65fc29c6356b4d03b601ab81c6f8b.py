code = """import json

# Load the full dataset
result_data = locals().get('var_functions.query_db:10')
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        articles = json.load(f)
else:
    articles = result_data

# Comprehensive sports keywords list
sports_keywords = [
    'sport', 'sports', 'game', 'games', 'team', 'player', 'players', 'athlete', 'athletes',
    'coach', 'season', 'championship', 'tournament', 'league', 'match', 'football', 'basketball',
    'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'olympics', 'medal',
    'win', 'winning', 'victory', 'defeat', 'score', 'competition', 'competing', 'quarterback',
    'pitcher', 'stadium', 'arena', 'playoff', 'finals', 'world cup', 'draft', 'offense', 'defense'
]

# Find sports articles
sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = title + ' ' + description
    
    # Count how many sports keywords appear in the article
    keyword_matches = sum(1 for keyword in sports_keywords if keyword in text)
    
    # If at least 2 sports keywords appear, consider it a sports article
    if keyword_matches >= 2:
        sports_articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': len(article.get('description', '')),
            'keyword_matches': keyword_matches
        })

# Sort by description length to find the longest
if sports_articles:
    sports_articles.sort(key=lambda x: x['desc_length'], reverse=True)
    
    # Debug: show top candidates
    print(f"Found {len(sports_articles)} potential sports articles")
    print("\nTop 5 sports articles by description length:")
    for i, article in enumerate(sports_articles[:5]):
        print(f"{i+1}. {article['title']}")
        print(f"   Length: {article['desc_length']} chars, Keywords: {article['keyword_matches']}")
        print(f"   Description: {article['description']}")
    
    result = sports_articles[0]['title']
else:
    # Fallback: if no clear sports articles found, return a message
    print("No sports articles found with current criteria")
    result = "No sports articles found"

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697267cd44fb462c76c361', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697267cd44fb462c76c362', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697267cd44fb462c76c363', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697267cd44fb462c76c364', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697267cd44fb462c76c365', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'_id': '69697267cd44fb462c76c361', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697267cd44fb462c76c362', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697267cd44fb462c76c363', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697267cd44fb462c76c364', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697267cd44fb462c76c365', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': [{'_id': '69697267cd44fb462c76c361', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697267cd44fb462c76c362', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697267cd44fb462c76c363', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697267cd44fb462c76c364', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697267cd44fb462c76c365', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': [{'_id': '69697267cd44fb462c76c361', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697267cd44fb462c76c362', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697267cd44fb462c76c363', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697267cd44fb462c76c364', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697267cd44fb462c76c365', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': "Why Windows isn't Unix", 'var_functions.execute_python:16': 'Enough to make you flip', 'var_functions.execute_python:18': 'Technology as Fashion', 'var_functions.execute_python:22': "Why Windows isn't Unix"}

exec(code, env_args)
