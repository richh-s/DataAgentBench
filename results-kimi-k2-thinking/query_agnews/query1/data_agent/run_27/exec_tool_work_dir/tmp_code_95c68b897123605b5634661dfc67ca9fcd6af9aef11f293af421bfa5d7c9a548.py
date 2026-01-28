code = """import json
import os

# Load all articles to analyze
articles_path = locals()['var_functions.query_db:32']
with open(articles_path, 'r') as f:
    all_articles = json.load(f)

# Sports-related terms
sports_terms = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'athlete', 'athletics', 'coach', 'player', 'team', 'game',
    'championship', 'tournament', 'competition', 'race', 'racing',
    'marathon', 'olympic', 'olympics', 'medal', 'victory', 'defeat'
]

# Find articles that match sports terms
sports_matches = []

for article in all_articles:
    text_combined = article['title'].lower() + ' ' + article['description'].lower()
    
    # Find which sports terms appear
    found_terms = []
    for term in sports_terms:
        if term in text_combined:
            found_terms.append(term)
    
    if found_terms:
        sports_matches.append({
            'title': article['title'],
            'desc_length': len(article['description']),
            'terms': found_terms
        })

print('Total sports-related articles: %d' % len(sports_matches))

if sports_matches:
    # Sort by description length
    sports_matches.sort(key=lambda x: x['desc_length'], reverse=True)
    
    print('\nTop 5 sports articles by description length:')
    for i, match in enumerate(sports_matches[:5]):
        print('%d. %s (%d chars)' % (i+1, match['title'][:60], match['desc_length']))
    
    answer = sports_matches[0]['title']
else:
    answer = 'No sports articles found'

print('\nAnswer: %s' % answer)
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:4': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\x08and of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\x07bout the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\x0clows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': "Why Windows isn't Unix", 'var_functions.execute_python:22': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'var_functions.query_db:24': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_functions.execute_python:28': "Why Windows isn't Unix", 'var_functions.list_db:30': ['articles'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:46': 'No sports found', 'var_functions.execute_python:52': 'Canadian Ansari X Prize Entrant Takes the Plunge in Test (SPACE.com)', 'var_functions.execute_python:58': "Why Windows isn't Unix", 'var_functions.execute_python:62': "Why Windows isn't Unix", 'var_functions.query_db:65': [{'_id': '69697320b467a4cfc8231184', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697320b467a4cfc8231185', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697320b467a4cfc8231186', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697320b467a4cfc8231187', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697320b467a4cfc8231188', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:66': "Why Windows isn't Unix", 'var_functions.execute_python:70': "Why Windows isn't Unix", 'var_functions.execute_python:74': "Why Windows isn't Unix", 'var_functions.execute_python:78': "Why Windows isn't Unix", 'var_functions.execute_python:86': "Why Windows isn't Unix", 'var_functions.execute_python:90': "Why Windows isn't Unix", 'var_functions.execute_python:96': "Why Windows isn't Unix", 'var_functions.execute_python:100': "Why Windows isn't Unix"}

exec(code, env_args)
