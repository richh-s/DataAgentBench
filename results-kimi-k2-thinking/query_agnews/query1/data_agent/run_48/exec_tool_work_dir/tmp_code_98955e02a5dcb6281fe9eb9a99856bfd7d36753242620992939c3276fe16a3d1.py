code = """import json
articles_file = locals()['var_functions.query_db:6']

# Read all articles data
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Define comprehensive sports filtering
sports_keywords = [
    # Major sports
    'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 
    'golf', 'volleyball', 'cricket', 'rugby', 'boxing', 'wrestling',
    'swimming', 'track', 'athletics', 'olympic', 'olympics',
    
    # Professional leagues
    'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'soccer', 'major league',
    'premier league', 'world cup', 'super bowl', 'playoff', 'playoffs',
    
    # Sports contexts
    'championship', 'tournament', 'season', 'coach', 'quarterback',
    'pitcher', 'goalkeeper', 'mvp', 'all-star', 'finals', 'semifinal',
    'medal', 'gold medal', 'silver medal', 'bronze medal',
    
    # Specific sports events
    'world series', 'stanley cup', 'nba finals', 'superbowl', 'march madness',
    'wimbledon', 'us open', 'masters tournament', 'kentucky derby'
]

# Avoid these in isolation (cause false positives)
ambiguous_terms = ['game', 'match', 'player', 'team', 'sport', 'sports', 'coach']

sports_articles = []

for article in all_articles:
    title = article.get('title', '')
    title_lower = title.lower()
    description = article.get('description', '')
    desc_lower = description.lower()
    
    # Score based on sports indicators
    sports_score = 0
    indicators_found = []
    
    # Check for strong sports keywords
    for keyword in sports_keywords:
        pattern = f' {keyword} '  # Add spaces for word boundaries
        if pattern in f' {title_lower} ' or pattern in f' {desc_lower} ':
            sports_score += 3
            indicators_found.append(keyword)
    
    # Check for ambiguous terms only if we already have some sports context
    # or if they appear with sports-related words
    if sports_score > 0:
        for term in ambiguous_terms:
            pattern = f' {term} '
            if pattern in f' {title_lower} ' or pattern in f' {desc_lower} ':
                sports_score += 1
                indicators_found.append(term)
    
    # If we found strong sports indicators, include the article
    if sports_score >= 3:  # Need at least one strong indicator
        sports_articles.append({
            'article_id': article.get('article_id', 'N/A'),
            'title': title,
            'description': description,
            'description_length': len(description),
            'sports_score': sports_score,
            'indicators': indicators_found
        })

# Find the article with maximum description length
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    
    # Also get top 10 for verification
    top_10 = sorted(sports_articles, key=lambda x: x['description_length'], reverse=True)[:10]
    
    result = {
        'longest_article': longest_article,
        'top_10_candidates': top_10,
        'total_sports_articles': len(sports_articles)
    }
    
    print("__RESULT__:")
    print(json.dumps(result, ensure_ascii=False))
else:
    print("__RESULT__:")
    print(json.dumps({'error': 'No sports articles found with current criteria'}, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': [{'_id': '696981f543fc64c07afdc7ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696981f543fc64c07afdc7ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696981f543fc64c07afdc7ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696981f543fc64c07afdc7af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696981f543fc64c07afdc7b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'title': '2004 US Senate Outlook', 'article_id': '69024', 'description_length': 944, 'total_sports_articles_found': 16719}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
