code = """import json
import re

# Read the articles from the file
data_file = locals()['var_functions.query_db:10']
with open(data_file, 'r') as f:
    articles = json.load(f)

# More precise sports detection
def is_sports_article(title, description):
    combined = (title + ' ' + description).lower()
    
    # Tech/Science indicators (if these are prominent, it's likely not sports)
    tech_indicators = ['windows', 'unix', 'linux', 'software', 'computer', 'internet', 
                       'google', 'microsoft', 'apple', 'technology', 'tech', 'digital',
                       'online', 'server', 'website', 'data', 'satellite', 'space flight',
                       'oil prices', 'trade deficit', 'stocks', 'economy', 'federal reserve']
    
    tech_count = sum(1 for indicator in tech_indicators if indicator in combined)
    if tech_count >= 2:  # If 2+ tech indicators, definitely not sports
        return False
    
    # Strong sports indicators (these are very specific to sports)
    strong_sports_indicators = [
        # Major sports leagues and events
        'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'fifa', 'uefa', 'world cup',
        'super bowl', 'olympic games', 'olympics', 'wimbledon', 'us open',
        'masters tournament', 'world series', 'stanley cup', 'premier league',
        'champions league', 'formula one', 'f1 racing', 'nascar',
        
        # Sports-specific terms
        'touchdown', 'home run', 'goal', 'points scored', 'quarterback',
        'pitcher', 'striker', 'defender', 'midfielder', 'quarter-final',
        'semi-final', 'championship game', 'final match', 'playoff game',
        'season opener', 'game-winning', 'score', 'defeated', 'victory',
        'defeat', 'win', 'loss', 'champion', 'medalist', 
        
        # Common sports
        'football team', 'basketball team', 'baseball team', 'soccer team',
        'hockey team', 'tennis match', 'golf tournament', 'boxing match',
        'wrestling', 'cricket match', 'rugby match', 'volleyball',
        'swimming competition', 'track and field', 'gymnastics',
        
        # Sports venues
        'stadium', 'arena', 'ballpark', 'field', 'court', 'track',
        'racetrack', 'course', 'golf course'
    ]
    
    sports_count = sum(1 for indicator in strong_sports_indicators if indicator in combined)
    
    # Need at least 1 strong sports indicator and not too many tech indicators
    return sports_count >= 1 and tech_count < 2

# Find the sports article with the longest description
longest_desc_length = 0
longest_sports_article = None
sports_articles_count = 0
sports_articles_debug = []  # For debugging

for article in articles:
    if is_sports_article(article['title'], article['description']):
        sports_articles_count += 1
        desc_length = len(article['description'])
        
        # Store debug info
        sports_articles_debug.append({
            'title': article['title'],
            'length': desc_length
        })
        
        if desc_length > longest_desc_length:
            longest_desc_length = desc_length
            longest_sports_article = article

# Sort debug list by length to see what's being captured
sports_articles_debug.sort(key=lambda x: x['length'], reverse=True)

# Prepare result
if longest_sports_article:
    result = {
        'title': longest_sports_article['title'],
        'description_length': longest_desc_length,
        'total_sports_articles_found': sports_articles_count,
        'article_id': longest_sports_article['article_id'],
        'top_5_longest': sports_articles_debug[:5]  # Show top 5 for verification
    }
else:
    result = {
        'title': None,
        'message': 'No sports articles found',
        'total_sports_articles_found': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969666e3efec42e10016862', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969666e3efec42e10016863', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969666e3efec42e10016864', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969666e3efec42e10016865', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969666e3efec42e10016866', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'found_sports_articles': 0, 'message': 'No sports articles found'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 1000}, 'var_functions.execute_python:14': {'title': "Why Windows isn't Unix", 'description_length': 708, 'total_sports_articles_found': 268}, 'var_functions.execute_python:16': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'total_sports_articles_found': 136, 'article_id': '279'}}

exec(code, env_args)
