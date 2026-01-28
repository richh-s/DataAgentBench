code = """import json

# Get the articles from the previous query result
articles = locals().get('var_functions.query_db:2', [])

# Check if we got any articles
if not articles:
    result = "No articles found"
    print('__RESULT__:')
    print(json.dumps(result))
else:
    # Calculate description lengths
    articles_with_lengths = []
    for article in articles:
        desc_length = len(article.get('description', ''))
        articles_with_lengths.append({
            'article_id': article.get('article_id'),
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': desc_length
        })
    
    # Sort by description length (descending)
    sorted_articles = sorted(articles_with_lengths, key=lambda x: x['desc_length'], reverse=True)
    
    # Check for sports-related keywords
    sports_keywords = ['sport', 'game', 'team', 'player', 'league', 'match', 'score', 'season', 'champion', 'tournament', 'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf']
    
    # Categorize articles
    sports_articles = []
    for article in sorted_articles:
        title_lower = article['title'].lower()
        desc_lower = article['description'].lower()
        
        has_sports_keyword = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
        
        if has_sports_keyword:
            sports_articles.append(article)
    
    result = {
        'total_articles': len(articles),
        'sports_articles_found': len(sports_articles),
        'sports_articles': sports_articles,
        'longest_description': sorted_articles[0] if sorted_articles else None
    }
    
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
