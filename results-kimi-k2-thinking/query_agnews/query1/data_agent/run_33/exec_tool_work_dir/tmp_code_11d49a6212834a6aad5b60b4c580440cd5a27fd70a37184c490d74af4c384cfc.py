code = """import json
import re

articles = var_functions.query_db:2

sports_keywords = [
    'sports', 'game', 'team', 'player', 'football', 'basketball', 'baseball',
    'soccer', 'tennis', 'golf', 'olympics', 'world cup', 'championship',
    'league', 'season', 'score', 'coach', 'athlete', 'match', 'race',
    'tournament', 'victory', 'defeat', 'playoff', 'final', 'quarterback',
    'pitcher', 'goalkeeper', 'medal', 'compete', 'competition'
]

def is_sports_article(title, description):
    """Determine if an article is a sports article based on title and description."""
    text = (title + ' ' + description).lower()
    
    sports_indicators = [
        'sports', 'football', 'basketball', 'soccer', 'tennis', 'golf', 
        'olympics', 'world cup', 'championship', 'league', 'baseball',
        'player', 'team', 'game', 'coach', 'athlete', 'match',
        'tournament', 'competition', 'victory', 'defeat', 'score',
        'season', 'playoff', 'quarterback', 'pitcher', 'goalkeeper',
        'medal', 'race', 'compete'
    ]
    
    text_lower = text.lower()
    for keyword in sports_indicators:
        if keyword in text_lower:
            return True
    return False

sports_articles = []

for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    article_id = article.get('article_id', '')
    
    if is_sports_article(title, description):
        char_count = len(description)
        sports_articles.append({
            'article_id': article_id,
            'title': title,
            'description': description,
            'char_count': char_count
        })

if not sports_articles:
    print('__RESULT__:')
    print(json.dumps("No sports articles found in the provided data."))
else:
    max_chars = max(article['char_count'] for article in sports_articles)
    article_with_max_desc = [a for a in sports_articles if a['char_count'] == max_chars]
    
    result = {
        'sports_articles_found': len(sports_articles),
        'longest_description_char_count': max_chars,
        'title': article_with_max_desc[0]['title'],
        'description': article_with_max_desc[0]['description']
    }
    
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '696976e1a4757cb31760c321', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696976e1a4757cb31760c322', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696976e1a4757cb31760c323', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696976e1a4757cb31760c324', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696976e1a4757cb31760c325', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
