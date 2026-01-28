code = """# More precise sports identification
import json

# Load the full articles data
articles_data = locals()['var_functions.query_db:5']

# For file path case, read the JSON file
if isinstance(articles_data, str) and articles_data.endswith('.json'):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_data

# Very specific sports indicators - more restrictive
sports_indicators = [
    # Team sports with leagues
    'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'fifa', 'premier league',
    # Specific sports terms
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
    'hockey', 'cricket', 'rugby', 'wrestling', 'boxing', 'volleyball',
    # Events
    'olympics', 'olympic', 'world cup', 'super bowl', 'wimbledon',
    'championship', 'tournament', 'playoffs', 'finals', 'medal',
    # Roles/positions
    'quarterback', 'pitcher', 'goalkeeper', 'coach', 'player', 'athlete',
    # Actions
    'touchdown', 'home run', 'goal', 'quarter', 'inning', 'match'
]

sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    
    # Check for sports indicators
    has_sports_indicator = any(indicator in title or indicator in desc for indicator in sports_indicators)
    
    # Exclude if it has clear non-sports terms
    non_sports_indicators = ['chip', 'processor', 'technology', 'software', 'stock', 'economy', 'oil', 'dollar', 'trade', 'space', 'flu', 'vaccine']
    has_non_sports = any(indicator in title or indicator in desc for indicator in non_sports_indicators)
    
    if has_sports_indicator and not has_non_sports:
        description_text = article.get('description', '')
        sports_articles.append({
            'article_id': article.get('article_id'),
            'title': article.get('title'),
            'description': description_text,
            'description_length': len(description_text)
        })

# If no results, try a different approach - look for word "sports" explicitly
if not sports_articles:
    for article in articles:
        title = article.get('title', '').lower()
        desc = article.get('description', '').lower()
        
        if 'sports' in title or 'sports' in desc:
            description_text = article.get('description', '')
            sports_articles.append({
                'article_id': article.get('article_id'),
                'title': article.get('title'),
                'description': description_text,
                'description_length': len(description_text)
            })

# Find the longest sports article
if sports_articles:
    sports_articles.sort(key=lambda x: x['description_length'], reverse=True)
    longest = sports_articles[0]
    
    result = {
        'title': longest['title'],
        'description_length': longest['description_length'],
        'article_id': longest['article_id']
    }
else:
    # Sample some articles to see what we're working with
    sample_articles = articles[:50]
    result = {
        'message': 'No clear sports articles found',
        'sample_titles': [article.get('title') for article in sample_articles[:10]]
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'description_length': 94, 'is_sports': False}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'description_length': 214, 'is_sports': False}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'description_length': 184, 'is_sports': False}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'description_length': 195, 'is_sports': False}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'description_length': 160, 'is_sports': False}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': {'title': 'AMD starts shipping 90-nanometer chips to customers', 'description_length': 810, 'article_id': '368', 'total_sports_articles_found': 372}, 'var_functions.execute_python:8': {'longest_title': 'China Begins Countdown for Next Manned Space Flight', 'longest_description_length': 580, 'longest_article_id': '279', 'total_sports_articles_found': 122, 'top_5_sports_articles': [{'title': 'China Begins Countdown for Next Manned Space Flight', 'length': 580}, {'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'length': 483}, {'title': "Last Year's Flu Shot Imperfect But Effective", 'length': 440}, {'title': 'They flocked from Games', 'length': 406}, {'title': 'Rehabbing his career', 'length': 402}]}}

exec(code, env_args)
