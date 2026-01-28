code = """import json
import os

# Load the articles data
result_file = locals()['var_functions.query_db:24']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        articles = json.load(f)
else:
    articles = result_file

# Define strict sports keywords - only clear sports terms
strict_sports_keywords = [
    'olympic', 'olympics', 'olympian', 'olympians', 'world cup', 'super bowl', 
    'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'soccer', 'football', 'basketball', 
    'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'boxing', 
    'wrestling', 'swimming', 'marathon', 'sprint', 'cyclist', 'cycling', 'ski', 
    'skiing', 'athlete', 'athletes', 'athletic', 'champion', 'champions', 
    'tournament', 'tournaments', 'match', 'matches', 'playoff', 'playoffs', 
    'game', 'games', 'player', 'players', 'coach', 'coaches', 'quarterback', 
    'pitcher', 'team', 'teams', 'league', 'season', 'stadium', 'arena', 
    'medal', 'gold medal', 'silver medal', 'bronze medal', 'world record', 
    'score', 'scores', 'goals', 'goal', 'points', 'victory', 'championship',
    'finals', 'semi-finals', 'quarter-finals', 'draft', 'racing', 'race', 
    'track and field', 'field event', 'track event', 'spectator', 'spectators',
    'referee', 'umpire', 'contender', 'contenders', 'qualifier', 'qualifiers',
    'professional', 'amateur', 'fan', 'fans', 'competition', 'competitions'
]

# Avoid false positives by excluding certain contexts
exclude_terms = [
    'project team', 'business team', 'software', 'construction', 
    'manufacturing', 'project collaboration', 'stock', 'oil', 'economy',
    'trade', 'market', 'finance', 'financial', 'business', 'company'
]

def is_clear_sports_article(title, description):
    text_lower = (title + ' ' + description).lower()
    
    # Check for exclusion terms that indicate false positive
    exclude_text = title + ' ' + description
    for exclude_term in exclude_terms:
        if exclude_term in exclude_text.lower():
            return False
    
    # Check if multiple sports terms are present or very clear sports terms
    sports_term_count = 0
    for keyword in strict_sports_keywords:
        if keyword in text_lower:
            sports_term_count += 1
            # Clear single-term indicators
            if keyword in ['olympic', 'olympics', 'olympian', 'nba', 'nfl', 'mlb', 
                          'nhl', 'fifa', 'soccer', 'quarterback', 'pitcher', 'stadium']:
                return True
    
    # Multiple sports-related terms likely indicate a sports article
    return sports_term_count >= 2

# Find actual sports articles
actual_sports_articles = []
for article in articles:
    if is_clear_sports_article(article['title'], article['description']):
        actual_sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'desc_length': len(article['description'])
        })

if actual_sports_articles:
    # Find the sports article with longest description
    longest_sports = max(actual_sports_articles, key=lambda x: x['desc_length'])
    result = {
        'title': longest_sports['title'],
        'article_id': longest_sports['article_id'],
        'description_length': longest_sports['desc_length'],
        'total_sports_articles': len(actual_sports_articles),
        'sample_sports_titles': [art['title'] for art in actual_sports_articles[:5]]
    }
else:
    # Look at a sample of articles to debug
    sample_articles = []
    for i in range(min(20, len(articles))):
        art = articles[i]
        sample_articles.append({
            'title': art['title'],
            'description_snippet': art['description'][:100] + '...'
        })
    result = {
        'error': 'No clear sports articles found with current criteria',
        'total_processed': len(articles),
        'sample_articles': sample_articles
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ea82fb77279caa4a8fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ea82fb77279caa4a8fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '69697ea82fb77279caa4a8fc', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '69697ea82fb77279caa4a8fd', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '69697ea82fb77279caa4a8fe', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697ea82fb77279caa4a8ff', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '69697ea82fb77279caa4a900', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:2': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ea82fb77279caa4a8fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ea82fb77279caa4a8fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:4': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ea82fb77279caa4a8fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ea82fb77279caa4a8fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': 'Test if this is working', 'var_functions.execute_python:8': {'error': 'No sports articles found'}, 'var_functions.query_db:10': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ea82fb77279caa4a8fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ea82fb77279caa4a8fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'articles_analyzed': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'is_sports': False, 'desc_length': 94}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'is_sports': False, 'desc_length': 214}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'is_sports': False, 'desc_length': 184}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'is_sports': False, 'desc_length': 195}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'is_sports': False, 'desc_length': 160}], 'total_checked': 5}, 'var_functions.execute_python:14': {'type': "<class 'list'>", 'length': 5, 'first_few': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:16': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ea82fb77279caa4a8fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ea82fb77279caa4a8fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:18': ['authors', 'article_metadata'], 'var_functions.query_db:20': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_functions.execute_python:22': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'sports_terms_found': [], 'desc_length': 94}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'sports_terms_found': [], 'desc_length': 214}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'sports_terms_found': [], 'desc_length': 184}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'sports_terms_found': [], 'desc_length': 195}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'sports_terms_found': [], 'desc_length': 160}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'title': 'Autodesk tackles project collaboration', 'article_id': '69', 'description_length': 402, 'total_sports_articles_found': 20}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'_id': '69697ea82fb77279caa4a93c', 'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:32': [{'_id': '69697ea82fb77279caa4a8f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ea82fb77279caa4a8f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ea82fb77279caa4a8f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ea82fb77279caa4a8fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ea82fb77279caa4a8fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
