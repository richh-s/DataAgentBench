code = """import json

file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define category keywords
sports_keywords = [
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'cricket', 'rugby',
    'olympics', 'olympic', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'fifa',
    'quarterback', 'pitcher', 'goalkeeper', 'striker', 'defender', 'midfielder', 'point guard',
    'championship', 'tournament', 'marathon', 'athlete', 'athletes', 'coach', 'player', 'team',
    'game', 'match', 'score', 'victory', 'defeat', 'win', 'lose', 'medal', 'competition',
    'quarterfinal', 'semifinal', 'final', 'quarter-final', 'semi-final',
    'stadium', 'arena', 'field', 'court', 'track', 'coach', 'season', 'playoff', 'play-off'
]

business_keywords = [
    'stocks', 'stock', 'wall st', 'wall street', 'economy', 'economic', 'market', 'markets',
    'trade', 'deficit', 'bank', 'investment', 'finance', 'financial', 'shares', 'profit', 'loss',
    'oil', 'crude', 'energy', 'prices', 'fed', 'federal reserve', 'interest rates', 'dollar',
    'capital', 'company', 'companies', 'business', 'industry', 'sector'
]

world_keywords = [
    'iraq', 'iran', 'japan', 'china', 'india', 'saudi', 'israel', 'palestine', 'afghanistan',
    'war', 'conflict', 'peace', 'government', 'president', 'minister', 'election', 'refugee',
    'pipeline', 'export', 'import', 'diplomatic', 'united nations', 'un', 'treaty', 'border'
]

# Classify articles and find sports articles
sports_articles = []

for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = title + ' ' + description
    
    # Skip articles that are clearly business or world news
    business_score = sum(1 for keyword in business_keywords if keyword in text)
    world_score = sum(1 for keyword in world_keywords if keyword in text)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text)
    
    # If sports score is highest and at least 1, classify as sports
    if sports_score > 0 and sports_score > business_score and sports_score > world_score:
        sports_articles.append({
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'desc_length': len(article.get('description', ''))
        })

# Find the sports article with the longest description
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    result = longest_article['title']
    desc_len = longest_article['desc_length']
    
    # Debug info
    print('Found ' + str(len(sports_articles)) + ' sports articles')
    print('Longest has description length: ' + str(desc_len))
else:
    result = "No sports articles found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696948203b0b87ea9f48a0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696948203b0b87ea9f48a1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696948203b0b87ea9f48a2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696948203b0b87ea9f48a3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696948203b0b87ea9f48a4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': 'Technology as Fashion', 'var_functions.execute_python:22': 'Technology as Fashion', 'var_functions.execute_python:26': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.execute_python:28': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:30': 'Technology as Fashion'}

exec(code, env_args)
