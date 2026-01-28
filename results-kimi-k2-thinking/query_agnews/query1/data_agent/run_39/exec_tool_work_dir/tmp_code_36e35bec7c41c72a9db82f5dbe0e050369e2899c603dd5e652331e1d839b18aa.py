code = """import json

# Access the articles data from the stored variable
articles_data = locals()['var_functions.query_db:5']

# Process each article to find sports articles and calculate description lengths
# Note: The data contains backslash characters which will be handled properly
sports_articles = []

for article in articles_data:
    title_lower = article['title'].lower()
    description_lower = article['description'].lower()
    
    # Check if this is a sports article
    sports_keywords = [
        'sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis',
        'golf', 'olympics', 'athletes', 'coach', 'game', 'match', 'player',
        'team', 'season', 'league', 'championship', 'tournament', 'race',
        'hockey', 'cricket', 'rugby', 'boxing', 'mma', 'ufc', 'nfl', 'nba',
        'mlb', 'nhl', 'ncaa', 'world cup', 'coach', 'quarterback', 'pitcher'
    ]
    
    is_sports = False
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in description_lower:
            is_sports = True
            break
    
    if is_sports:
        desc_length = len(article['description'])
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'description_length': desc_length
        })

print('Number of sports articles found:', len(sports_articles))

# Find the sports article with the longest description
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    print(f"Longest sports article: {longest_article['title']}")
    print(f"Description length: {longest_article['description_length']}")
else:
    print("No sports articles found in the sample")

# Let's also check all articles and find the one with max description length
titles_with_lengths = []
for article in articles_data:
    titles_with_lengths.append({
        'title': article['title'],
        'length': len(article['description'])
    })

max_article = max(titles_with_lengths, key=lambda x: x['length'])
print(f"\nOverall longest description: {max_article['title']}")
print(f"Length: {max_article['length']}")

print('__RESULT__:')
result = {
    'sports_articles_found': len(sports_articles),
    'sports_articles': sports_articles,
    'overall_longest': max_article
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697ba17e0b0da1bb12f773', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ba17e0b0da1bb12f774', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ba17e0b0da1bb12f775', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ba17e0b0da1bb12f776', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ba17e0b0da1bb12f777', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '69697ba17e0b0da1bb12f778', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '69697ba17e0b0da1bb12f779', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '69697ba17e0b0da1bb12f77a', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697ba17e0b0da1bb12f77b', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '69697ba17e0b0da1bb12f77c', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:2': [{'_id': '69697ba17e0b0da1bb12f773', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ba17e0b0da1bb12f774', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ba17e0b0da1bb12f775', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ba17e0b0da1bb12f776', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ba17e0b0da1bb12f777', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'_id': '69697ba17e0b0da1bb12f773', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ba17e0b0da1bb12f774', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ba17e0b0da1bb12f775', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ba17e0b0da1bb12f776', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ba17e0b0da1bb12f777', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': [{'_id': '69697ba17e0b0da1bb12f773', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697ba17e0b0da1bb12f774', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697ba17e0b0da1bb12f775', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697ba17e0b0da1bb12f776', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697ba17e0b0da1bb12f777', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
