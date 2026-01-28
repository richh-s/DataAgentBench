code = """import json

# Load the articles from the most recent query
articles = locals()['var_functions.query_db:36']

# Define sports keywords for categorization
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
    'cricket', 'hockey', 'rugby', 'athlete', 'olympic',
    'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'world cup',
    'stadium', 'arena', 'championship', 'tournament', 'match',
    'victory', 'medal', 'coach', 'player', 'team', 'game', 'sports'
]

# Define business keywords for categorization
business_keywords = [
    'wall st', 'stock', 'market', 'economy', 'business', 'trade', 
    'deficit', 'oil', 'company', 'firm', 'ipo', 'shares', 'reuters'
]

# Define world keywords
world_keywords = [
    'iraq', 'iran', 'war', 'conflict', 'refugee', 'peace', 'diplomatic'
]

# Define science/tech keywords  
tech_keywords = [
    'technology', 'chip', 'software', 'hardware', 'internet', 'google',
    'computer', 'digital', 'research', 'science', 'scientist'
]

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Check for sports
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    
    # Check for tech
    if any(keyword in text for keyword in tech_keywords):
        return 'Science/Technology'
    
    # Check for business
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    
    # Check for world news
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Default based on common patterns
    if 'reuters' in text or 'afp' in text and ('oil' in text or 'stock' in text):
        return 'Business'
    
    return 'Uncategorized'

# Analyze the 5 articles
print('Analyzing articles:')
sports_articles = []

for i, article in enumerate(articles):
    article_id = article.get('article_id')
    title = article.get('title', '')
    description = article.get('description', '')
    
    category = categorize_article(title, description)
    desc_length = len(description)
    
    print(f"\n{i+1}. ID: {article_id}")
    print(f"   Title: {title}")
    print(f"   Category: {category}")
    print(f"   Description length: {desc_length}")
    
    if category == 'Sports':
        sports_articles.append({
            'article_id': article_id,
            'title': title,
            'description': description,
            'length': desc_length
        })

print(f'\n\nTotal Sports articles found: {len(sports_articles)}')

if sports_articles:
    # Sort by description length
    sports_articles.sort(key=lambda x: x['length'], reverse=True)
    
    print('\nSports articles sorted by description length:')
    for i, article in enumerate(sports_articles):
        print(f"{i+1}. Title: {article['title']}")
        print(f"   Description length: {article['length']}")
        
    longest = sports_articles[0]
    print(f'\nArticle with longest description:')
    print(f"Title: {longest['title']}")
    print(f"Description length: {longest['length']}")
else:
    print('No sports articles found in this dataset')
    # Show all articles sorted by description length
    all_sorted = sorted(articles, key=lambda x: len(x.get('description', '')), reverse=True)
    print('\nAll articles sorted by description length:')
    for i, article in enumerate(all_sorted):
        title = article.get('title', '')
        length = len(article.get('description', ''))
        category = categorize_article(title, article.get('description', ''))
        print(f"{i+1}. Title: {title[:60]}...")
        print(f"   Category: {category}, Length: {length}")

result = {
    'sports_articles_count': len(sports_articles),
    'longest_sports_title': sports_articles[0]['title'] if sports_articles else None,
    'longest_sports_length': sports_articles[0]['length'] if sports_articles else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:14': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:20': {'test': 'data loaded successfully', 'count': 5}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_articles': 0, 'sports_articles_found': 0, 'sports_article_with_longest_description': None, 'max_description_length': 0, 'top_5_sports_by_length': []}, 'var_functions.query_db:26': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:28': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:30': {'article_count': 5, 'has_sports_articles': False}, 'var_functions.query_db:32': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:34': [{'_id': '69697a5e4601b4c0c4095502', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697a5e4601b4c0c4095518', 'article_id': '29', 'title': 'Chad seeks refugee aid from IMF', 'description': 'Chad asks the IMF for a loan to pay for looking after more than 100,000 refugees from conflict-torn Darfur in western Sudan.'}, {'_id': '69697a5e4601b4c0c4095521', 'article_id': '38', 'title': 'Researchers seek to untangle the e-mail thread', 'description': "E-mail is a victim of its own success. That's the conclusion of IBM Corp. researchers in Cambridge, who have spent nearly a decade conducting field tests at IBM and other companies about how employees work and use electronic mail. It's clear to them that e-mail has become the Internet's killer application."}, {'_id': '69697a5e4601b4c0c4095533', 'article_id': '56', 'title': 'Stoking the Steamroller', 'description': 'No other recording artist can channel American middle-class tastes quite like Chip Davis and his best-selling band'}, {'_id': '69697a5e4601b4c0c4095540', 'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'description': 'Autodesk  this week unwrapped an updated version of its hosted project collaboration service targeted at the construction and manufacturing industries. Autodesk Buzzsaw lets multiple, dispersed project participants -- including building owners, developers, architects, construction teams, and facility managers -- share and manage data throughout the life of a project, according to Autodesk officials.'}], 'var_functions.query_db:36': [{'_id': '69697a5e4601b4c0c40954fb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697a5e4601b4c0c40954fc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697a5e4601b4c0c40954fd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697a5e4601b4c0c40954fe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697a5e4601b4c0c40954ff', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:38': {'article_count': 5, 'status': 'loaded'}, 'var_functions.execute_python:40': {'total_articles': 1000, 'sports_articles_count': 359, 'longest_sports_article_title': 'AMD starts shipping 90-nanometer chips to customers', 'longest_sports_article_length': 810}, 'var_functions.execute_python:48': {'status': 'loaded', 'count': 5}}

exec(code, env_args)
