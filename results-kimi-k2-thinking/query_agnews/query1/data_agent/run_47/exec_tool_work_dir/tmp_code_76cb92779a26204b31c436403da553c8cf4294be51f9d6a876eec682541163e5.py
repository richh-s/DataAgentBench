code = """# Load the articles data
articles = locals()['var_functions.query_db:0']

# Check if we have articles
if not articles:
    result = "No articles found"
else:
    # Calculate description lengths and check for sports keywords
    sports_keywords = ['sports', 'sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'olympic', 'game', 'team']
    
    processed_articles = []
    for article in articles:
        desc_length = len(article.get('description', ''))
        title_lower = article.get('title', '').lower()
        desc_lower = article.get('description', '').lower()
        
        is_sports = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
        
        processed_articles.append({
            'article_id': article.get('article_id'),
            'title': article.get('title'),
            'description': article.get('description'),
            'description_length': desc_length,
            'is_sports': is_sports
        })
    
    result = processed_articles

import json
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
