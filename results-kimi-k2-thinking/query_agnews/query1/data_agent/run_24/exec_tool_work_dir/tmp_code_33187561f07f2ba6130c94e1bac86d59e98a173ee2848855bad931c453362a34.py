code = """import json

# Load all articles
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    articles = json.load(f)

# More specific keywords for actual sports (excluding video games)
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'hockey', 'cricket', 'rugby', 'volleyball', 'swimming', 'track',
    'athlete', 'athletes', 'olympic', 'olympics', 'world cup',
    'championship', 'tournament', 'coach', 'coaches',
    'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'premier league',
    'race', 'racing', 'marathon', 'sprint', 'bowl', 'playoff'
]

# Filter sports articles
sports_articles = []
for article in articles:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    # Check if any sports keyword appears in title or description
    is_sports = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
    
    if is_sports:
        sports_articles.append(article)

# Find sports article with longest description
if sports_articles:
    # Calculate description length for each sports article
    for article in sports_articles:
        article['description_length'] = len(article['description'])
    
    # Find article with maximum description length
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    
    # Also get the top 5 longest for validation
    sorted_by_length = sorted(sports_articles, key=lambda x: x['description_length'], reverse=True)
    top_5 = []
    for i, article in enumerate(sorted_by_length[:5]):
        top_5.append({
            'rank': i+1,
            'title': article['title'],
            'description_length': article['description_length'],
            'article_id': article['article_id']
        })
    
    result = {
        'sports_article_count': len(sports_articles),
        'longest_sports_article': {
            'title': longest_article['title'],
            'description_length': longest_article['description_length'],
            'article_id': longest_article['article_id']
        },
        'top_5_longest': top_5
    }
else:
    result = {
        'sports_article_count': 0,
        'message': 'No sports articles found'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:7': {'article_count': 1000, 'sample_articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_functions.execute_python:12': {'sports_article_count': 210, 'longest_sports_article': {'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'description_length': 708, 'article_id': '183'}}}

exec(code, env_args)
