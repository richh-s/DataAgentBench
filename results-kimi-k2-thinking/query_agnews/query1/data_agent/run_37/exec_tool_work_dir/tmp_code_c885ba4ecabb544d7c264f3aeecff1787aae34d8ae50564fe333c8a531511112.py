code = """import json

# Access and load articles
articles_data = locals()['var_functions.query_db:48']
if isinstance(articles_data, str):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_data

# Define very specific sports keywords that are unlikely to be false positives
sports_keywords = [
    "nba", "nfl", "mlb", "nhl",  # Major leagues
    "olympics", "olympic",  # Olympic games
    "playoffs", "playoff",  # Sports postseason
    "super bowl", "world series", "world cup",  # Major events
    "championship game", "championship series"  # Championship events
]

# Also check for sports names that must appear with explicit sports context
sport_names = [
    "football", "basketball", "soccer", "baseball", 
    "hockey", "tennis", "golf", "cricket", "rugby"
]

# Context words that make it clear we're talking about sports
sports_context = [
    "game", "games", "match", "matches", "team", "teams", 
    "player", "players", "coach", "coaches", "season", "league", "leagues"
]

longest_title = "No sports articles found"
max_length = 0
sports_articles = []

for article in articles:
    title = article.get("title", "").lower()
    description = article.get("description", "").lower()
    full_text = title + " " + description
    desc_len = len(article.get("description", ""))
    
    # Check for unambiguous sports terms
    is_sports = False
    
    # First check specific leagues/events
    for keyword in sports_keywords:
        if keyword in full_text:
            is_sports = True
            break
    
    # If not found, check for sport + context combination
    if not is_sports:
        has_sport = any(sport in full_text for sport in sport_names)
        has_context = any(context in full_text for context in sports_context)
        if has_sport and has_context:
            # Additional check: avoid business/sports metaphors
            business_context = ["stock market", "economy", "business", "trade", "finance"]
            if not any(biz in full_text for biz in business_context):
                is_sports = True
    
    if is_sports:
        sports_articles.append((desc_len, article.get("title")))
        if desc_len > max_length:
            max_length = desc_len
            longest_title = article.get("title")

# Show some examples for debugging
if sports_articles:
    sports_articles.sort(reverse=True)
    print(f"Found {len(sports_articles)} sports articles")
    print(f"Longest: {max_length} chars - {longest_title}")
    print("\\nTop 5:")
    for i in range(min(5, len(sports_articles))):
        print(f"{sports_articles[i][0]} chars: {sports_articles[i][1]}")

result = longest_title
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:14': ['articles'], 'var_functions.execute_python:26': 'No sports articles found', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'count': '127600'}], 'var_functions.query_db:34': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:36': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:38': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:46': 'IBM to market Sybase Linux database', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'total': 127600, 'sample_count': 50}, 'var_functions.execute_python:54': 'IBM to market Sybase Linux database', 'var_functions.execute_python:58': 'Bush Visits Canada On Fence-Mending Tour', 'var_functions.execute_python:60': 'Bush Visits Canada On Fence-Mending Tour'}

exec(code, env_args)
