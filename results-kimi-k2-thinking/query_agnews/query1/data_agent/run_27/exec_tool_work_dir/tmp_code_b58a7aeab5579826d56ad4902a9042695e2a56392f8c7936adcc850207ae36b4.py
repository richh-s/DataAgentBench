code = """import json
import os

# Read the full articles data from the file
file_path = '/home/user/tmp/tmp_mongo_result_2dfbe8c8.json'

with open(file_path, 'r') as f:
    all_articles = json.load(f)

print('Total articles: {}'.format(len(all_articles)))

# Define category indicators
sports_terms = [
    'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis','golf',
    'race', 'racing', 'olympic', 'game', 'team', 'player', 'coach', 'match',
    'athlete', 'championship', 'tournament', 'marathon', 'sprint', 'medal',
    'quarterback', 'pitcher', 'defender', 'striker', 'goalkeeper', 'fielder',
    'batter', 'hitter', 'runner', 'f1', 'formula one', 'grand prix', 'lap',
    'victory', 'defeat', 'win', 'lose', 'score', 'season', 'league'
]

business_terms = [
    'stocks', 'stock market', 'wall st', 'wall street', 'economy', 'economic',
    'finance', 'financial', 'business', 'trade', 'deficit', 'company',
    'investment', 'bank', 'banking', 'interest rates', 'oil prices', 'shares',
    'profit', 'loss', 'revenue', 'sales', 'market', 'fund', 'funds',
    'money', 'currency', 'dollar', 'euro', 'yen', 'bond', 'stock'
]

world_terms = [
    'iraq', 'iraqi', 'war', 'peace', 'united nations', 'government',
    'president', 'prime minister', 'election', 'country', 'international',
    'global', 'foreign', 'diplomatic', 'treaty', 'conflict', 'refugee',
    'aid', 'embassy', 'military', 'un', 'world', 'nation', 'national',
    'policy', 'administration', 'official', 'authorities', 'border'
]

tech_terms = [
    'google', 'technology', 'tech', 'software', 'hardware', 'computer',
    'internet', 'web', 'online', 'digital', 'chip', 'semiconductor',
    'microsoft', 'windows', 'unix', 'linux', 'apple', 'intel', 'hp',
    'hewlett-packard', 'mobile', 'phone', 'wireless', 'network',
    'website', 'search engine', 'browser', 'email', 'server'
]

# Categorize articles
sports_articles = []
business_articles = []
world_articles = []
tech_articles = []
categorized_count = 0

for article in all_articles:
    title = article['title'].lower()
    desc = article['description'].lower()
    text = title + ' ' + desc
    
    # Check each category
    sports_score = sum(1 for term in sports_terms if term in text)
    business_score = sum(1 for term in business_terms if term in text)
    world_score = sum(1 for term in world_terms if term in text)
    tech_score = sum(1 for term in tech_terms if term in text)
    
    # Assign to category with highest score
    scores = [
        ('sports', sports_score, sports_articles),
        ('business', business_score, business_articles),
        ('world', world_score, world_articles),
        ('tech', tech_score, tech_articles)
    ]
    
    # Sort by score and assign
    scores.sort(key=lambda x: x[1], reverse=True)
    if scores[0][1] > 0:  # Only categorize if there's at least one match
        scores[0][2].append({
            'title': article['title'],
            'description': article['description'],
            'length': len(article['description'])
        })
        categorized_count += 1

print('Categorized: {} out of {} articles'.format(categorized_count, len(all_articles)))
print('Sports: {}, Business: {}, World: {}, Tech: {}'.format(
    len(sports_articles), len(business_articles), len(world_articles), len(tech_articles)))

# Find sports article with longest description
if sports_articles:
    longest_sports = max(sports_articles, key=lambda x: x['length'])
    answer = longest_sports['title']
    print('\nLongest sports article: {} ({} chars)'.format(answer, longest_sports['length']))
else:
    answer = 'No sports articles found'

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:4': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\x08and of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\x07bout the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\x0clows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': "Why Windows isn't Unix", 'var_functions.execute_python:22': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'var_functions.query_db:24': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_functions.execute_python:28': "Why Windows isn't Unix", 'var_functions.list_db:30': ['articles'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:46': 'No sports found'}

exec(code, env_args)
