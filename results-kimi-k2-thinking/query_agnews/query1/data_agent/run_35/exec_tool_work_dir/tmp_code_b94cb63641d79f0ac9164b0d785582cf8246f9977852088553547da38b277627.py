code = """import json

# Load the articles from the previous query
articles = var_functions.query_db:0

# Define keywords to identify sports articles
sports_keywords = ['sports', 'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'olympics', 'athlete', 'athletes', 'game', 'games', 'match', 'matches']

# Find all sports articles and their description lengths
sports_articles = []

for article in articles:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    # Check if any sports keyword appears in title or description
    is_sports = any(keyword in title_lower or keyword in desc_lower for keyword in sports_keywords)
    
    if is_sports:
        desc_length = len(article.get('description', ''))
        sports_articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_length': desc_length
        })

# If no sports articles found, check manually for sports-related content
if not sports_articles:
    # Look at all articles to see if any might be sports (the keywords might be too narrow)
    for article in articles:
        title = article.get('title', '').lower()
        desc = article.get('description', '').lower()
        
        # Check for sports indicators
        if 'nba' in title or 'nfl' in title or 'mlb' in title or 'nhl' in title:
            is_sports = True
        elif 'world cup' in title or 'world cup' in desc:
            is_sports = True
        else:
            continue
            
        if is_sports:
            desc_length = len(article.get('description', ''))
            sports_articles.append({
                'title': article.get('title'),
                'description': article.get('description'),
                'desc_length': desc_length
            })

# Find the sports article with the longest description
if sports_articles:
    max_desc_article = max(sports_articles, key=lambda x: x['desc_length'])
    result_title = max_desc_article['title']
    result_length = max_desc_article['desc_length']
    result = f"{result_title} (description length: {result_length})"
else:
    result = "No sports articles found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697811190e2e64cc8a20ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697811190e2e64cc8a20eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697811190e2e64cc8a20ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697811190e2e64cc8a20ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697811190e2e64cc8a20ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
