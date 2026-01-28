code = """import json

# The query_db:10 result is stored as a JSON string, let's parse it first
json_string = locals()['var_functions.query_db:10']

# Parse the JSON string to get the actual data
all_articles = json.loads(json_string)

# Process articles to find sports articles
sports_keywords = [
    'game', 'games', 'season', 'player', 'players', 'team', 'teams', 'coach', 
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf',
    'cricket', 'rugby', 'volleyball', 'swimming', 'cycling', 'athlete', 'athletes',
    'championship', 'tournament', 'match', 'matches', 'score', 'victory', 'defeat',
    'medal', 'olympic', 'olympics', 'world cup', 'league', 'cup', 'final', 'semifinal',
    'quarterfinal', 'racing', 'marathon', 'sports', 'sport'
]

# Function to check if article is about sports
def is_sports_article(title, description):
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in sports_keywords)

# Find sports articles and their description lengths
sports_articles = []

for article in all_articles:
    title = article.get('title', '')
    description = article.get('description', '')
    
    if is_sports_article(title, description):
        desc_length = len(description)
        sports_articles.append({
            'title': title,
            'description': description,
            'desc_length': desc_length,
            'article_id': article.get('article_id')
        })

# Sort by description length (descending)
sports_articles_sorted = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)

# Create result
result = {
    'total_articles_processed': len(all_articles),
    'sports_articles_found': len(sports_articles),
    'longest_sports_article': sports_articles_sorted[0] if sports_articles_sorted else None,
    'all_sports_articles': [(a['title'], a['desc_length']) for a in sports_articles_sorted[:10]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.execute_python:8': {'message': 'No sports articles found', 'total_sports_articles_found': 0}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:14': [{'_id': '69698264236002a1bb5b856a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69698264236002a1bb5b856b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69698264236002a1bb5b856c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69698264236002a1bb5b856d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69698264236002a1bb5b856e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}]}

exec(code, env_args)
