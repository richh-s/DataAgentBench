code = """import json
import os

# Load the file from the stored path
file_path = locals()['var_functions.query_db:32']

with open(file_path, 'r') as f:
    articles = json.load(f)

print('Loaded {} articles'.format(len(articles)))

# Print first 30 titles to see what we're working with
print('\nFirst 30 titles:')
for i in range(min(30, len(articles))):
    print('{}. {}'.format(i+1, articles[i]['title']))

# Check if any articles contain sports-related content
sports_keywords = [
    'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 
    'racing', 'race', 'game', 'team', 'player', 'coach', 'match', 'athlete',
    'olympic', 'championship', 'tournament'
]

# Use a scoring system to find sports articles
potential_sports = []

for idx, article in enumerate(articles):
    title = article['title'].lower()
    desc = article['description'].lower()
    combined = title + ' ' + desc
    
    # Count sports keywords
    score = 0
    words_found = []
    for keyword in sports_keywords:
        if keyword in combined:
            score += 1
            words_found.append(keyword)
    
    if score > 0:
        potential_sports.append({
            'index': idx,
            'title': article['title'],
            'score': score,
            'keywords': words_found,
            'desc_length': len(article['description'])
        })

print('\nFound {} articles with sports keywords'.format(len(potential_sports)))

if potential_sports:
    # Sort by description length
    potential_sports.sort(key=lambda x: x['desc_length'], reverse=True)
    
    print('\nTop 10 articles with sports keywords (by desc length):')
    for i, article in enumerate(potential_sports[:10]):
        print('{}. "{}" (score: {}, length: {})'.format(
            i+1, article['title'][:70], article['score'], article['desc_length']))
        print('   Keywords: {}'.format(', '.join(article['keywords'])))

if potential_sports:
    answer = potential_sports[0]['title']
else:
    answer = 'No sports articles found'

print('\n__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:4': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\x08and of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\x07bout the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\x0clows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': "Why Windows isn't Unix", 'var_functions.execute_python:22': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'var_functions.query_db:24': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_functions.execute_python:28': "Why Windows isn't Unix", 'var_functions.list_db:30': ['articles'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:46': 'No sports found', 'var_functions.execute_python:52': 'Canadian Ansari X Prize Entrant Takes the Plunge in Test (SPACE.com)', 'var_functions.execute_python:58': "Why Windows isn't Unix", 'var_functions.execute_python:62': "Why Windows isn't Unix", 'var_functions.query_db:65': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:66': "Why Windows isn't Unix", 'var_functions.execute_python:70': "Why Windows isn't Unix", 'var_functions.execute_python:74': "Why Windows isn't Unix", 'var_functions.execute_python:78': "Why Windows isn't Unix"}

exec(code, env_args)
