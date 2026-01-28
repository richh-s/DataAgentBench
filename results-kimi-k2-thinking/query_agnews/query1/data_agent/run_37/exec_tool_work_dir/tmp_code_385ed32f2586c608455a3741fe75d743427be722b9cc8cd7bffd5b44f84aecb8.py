code = """import json

# Access the articles data from the query
articles = var_functions.query_db:0

# Debug: understand the data structure and first few articles
print("Number of articles:", len(articles))
print("First article:", articles[0])
print("Types of articles in first article:")
for key, value in articles[0].items():
    print(f"  {key}: {type(value)}")

# Create a list to store articles with their description lengths
desc_len_list = []
sports_candidates = []

for idx, article in enumerate(articles):
    title = article['title'].lower()
    description = article['description']
    desc_len = len(description)
    
    # Check if it's a sports article
    sports_keywords = ['nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'olymp', 'athlet', 'sports', 'game', 'playoff', 'champion', 'team', 'player', 'coach']
    
    is_sports = any(keyword in title or keyword in description.lower() for keyword in sports_keywords)
    
    if is_sports:
        sports_candidates.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': description,
            'desc_len': desc_len
        })
    
    desc_len_list.append({
        'article_id': article['article_id'],
        'title': article['title'],
        'desc_len': desc_len,
        'is_sports': is_sports
    })

# Sort all articles by description length
desc_len_list_sorted = sorted(desc_len_list, key=lambda x: x['desc_len'], reverse=True)

print("\nTop 10 articles by description length:")
for art in desc_len_list_sorted[:10]:
    print(f"Length: {art['desc_len']}, Sports: {art['is_sports']}, Title: {art['title'][:80]}")

print("\nSports candidates found:")
for candidate in sports_candidates:
    print(f"Length: {candidate['desc_len']}, Title: {candidate['title']}")

result = json.dumps({
    'count': len(articles),
    'sports_candidates': sports_candidates,
    'longest_descriptions': desc_len_list_sorted[:10]
})

print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
