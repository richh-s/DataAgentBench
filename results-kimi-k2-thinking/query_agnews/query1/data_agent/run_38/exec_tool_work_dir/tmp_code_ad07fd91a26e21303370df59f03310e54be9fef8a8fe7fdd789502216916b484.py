code = """import json
import os
import re

# Get all articles - check all variable keys
articles = []

# Find the actual articles data
for key, value in locals().items():
    if isinstance(value, list) and len(value) > 0:
        if isinstance(value[0], dict) and 'title' in value[0]:
            articles = value
            print(f'Found articles in variable: {key}, count: {len(articles)}')
            break

# Also try to load from file
if not articles:
    file_var = locals().get('var_functions.query_db:22')
    if file_var and os.path.exists(str(file_var)):
        with open(str(file_var), 'r') as f:
            articles = json.load(f)
            print(f'Loaded articles from file, count: {len(articles)}')

# Define refined sports keywords - more specific
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
    'cricket', 'hockey', 'rugby', 'athlete', 'olympic', 'olympics',
    'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'world cup',
    'stadium', 'arena', 'pitch', 'court', 'track and field',
    'championship', 'tournament', 'match', 'game', 'score',
    'victory', 'defeat', 'medal', 'gold medal', 'silver medal', 'bronze medal'
]

# Keywords to avoid false positives (business terms)
business_terms = [
    'wall st', 'stock', 'shares', 'ipo', 'company', 'firm', 'market',
    'economy', 'business', 'trade', 'deficit', 'oil', 'google', 'dell'
]

def is_clear_sports_article(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = title + ' ' + description
    
    # Count sports terms vs business terms
    sports_count = sum(1 for keyword in sports_keywords if keyword in text)
    business_count = sum(1 for term in business_terms if term in text)
    
    # If sports terms significantly outnumber business terms, it's likely sports
    return sports_count > business_count and sports_count > 0

# Analyze articles
sports_articles = []
business_articles = []
tech_articles = []
world_articles = []

for article in articles:
    if is_clear_sports_article(article):
        sports_articles.append(article)
    elif any(term in (article.get('title', '').lower() + article.get('description', '').lower()) for term in 
             ['technology', 'chip', 'software', 'hardware', 'internet', 'google', 'dell', 'hp']):
        tech_articles.append(article)
    elif any(term in (article.get('title', '').lower() + article.get('description', '').lower()) for term in 
             ['economy', 'stock', 'market', 'trade', 'oil', 'business']):
        business_articles.append(article)
    else:
        world_articles.append(article)

# Find sports article with longest description
longest_sports = None
max_length = 0

for article in sports_articles:
    desc_len = len(article.get('description', ''))
    if desc_len > max_length:
        max_length = desc_len
        longest_sports = article

# Show some sample sports articles
print(f'Total articles: {len(articles)}')
print(f'Sports articles: {len(sports_articles)}')
print(f'Business articles: {len(business_articles)}')
print(f'Tech articles: {len(tech_articles)}')
print(f'World articles: {len(world_articles)}')

if sports_articles:
    print('\nSample sports articles:')
    for i, article in enumerate(sports_articles[:5]):
        print(f"{i+1}. ID: {article.get('article_id')}, Title: {article.get('title')}")
    
    if longest_sports:
        print(f'\nSports article with longest description:')
        print(f"Title: {longest_sports.get('title')}")
        print(f"Description length: {max_length}")
        print(f"Description: {longest_sports.get('description')[:100]}...")
else:
    print('No clear sports articles found')
    # Show some samples to understand the data better
    print('\nSample articles:')
    for i, article in enumerate(articles[:10]):
        print(f"{i+1}. ID: {article.get('article_id')}, Title: {article.get('title')}")

result = {
    'total_articles': len(articles),
    'sports_count': len(sports_articles),
    'longest_sports_title': longest_sports.get('title') if longest_sports else None,
    'longest_sports_length': max_length if longest_sports else None
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:14': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:20': {'test': 'data loaded successfully', 'count': 5}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_articles': 0, 'sports_articles_found': 0, 'sports_article_with_longest_description': None, 'max_description_length': 0, 'top_5_sports_by_length': []}, 'var_functions.query_db:26': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:28': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:30': {'article_count': 5, 'has_sports_articles': False}, 'var_functions.query_db:32': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:34': [{'_id': '69697a5e4601b4c0c4095502', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697a5e4601b4c0c4095518', 'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'_id': '69697a5e4601b4c0c4095521', 'article_id': '38', 'title': 'Researchers seek to untangle the e-mail thread', 'description': "E-mail is a victim of its own success. That's the conclusion of IBM Corp. researchers in Cambridge, who have spent nearly a decade conducting field tests at IBM and other companies about how employees work and use electronic mail. It's clear to them that e-mail has become the Internet's killer application."}, {'_id': '69697a5e4601b4c0c4095533', 'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'_id': '69697a5e4601b4c0c4095540', 'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:36': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:38': {'article_count': 5, 'status': 'loaded'}, 'var_functions.execute_python:40': {'total_articles': 1000, 'sports_articles_count': 359, 'longest_sports_article_title': 'AMD starts shipping 90-nanometer chips to customers', 'longest_sports_article_length': 810}}

exec(code, env_args)
