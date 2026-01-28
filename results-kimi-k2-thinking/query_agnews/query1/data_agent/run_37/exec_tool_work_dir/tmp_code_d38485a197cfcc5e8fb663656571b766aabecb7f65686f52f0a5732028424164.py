code = """import json

articles_path = locals()['var_functions.query_db:48']

# Load all articles
with open(articles_path, 'r') as f:
    articles = json.load(f)

# Only use very specific sports indicators
specific_terms = [
    "nba ", "nfl ", "mlb ", "nhl ",  # leagues (with space to avoid false matches)
    "olympics", "olympic games",  # specific events
    "world cup", "super bowl",  # major events
    "playoffs",  # sports terminology
]

# For manual review, let's find articles with these terms
matches = []

for article in articles:
    title_lower = article.get("title", "").lower()
    desc_lower = article.get("description", "").lower()
    
    for term in specific_terms:
        if term in title_lower or term in desc_lower:
            matches.append({
                "term": term,
                "title": article.get("title"),
                "desc_len": len(article.get("description", ""))
            })
            break

print(f"Found {len(matches)} articles with specific sports terms")

# Sort by description length
if matches:
    matches.sort(key=lambda x: x["desc_len"], reverse=True)
    print("\nTop 10 longest:")
    for i in range(min(10, len(matches))):
        print(f"{matches[i]['desc_len']} chars - Term: '{matches[i]['term']}' - Title: {matches[i]['title']}")

# Also try very specific sports names with context
sports_names = ["football", "basketball", "soccer", "baseball", "hockey", "tennis", "golf", "cricket", "rugby"]
sports_with_context = []

for article in articles:
    title_lower = article.get("title", "").lower()
    desc_lower = article.get("description", "").lower()
    desc = article.get("description", "")
    
    # Look for sports names with game/sports context words
    context_words = ["game", "games", "match", "matches", "play", "team", "player", "players", "season", "league"]
    full_text = title_lower + " " + desc_lower
    
    has_sport = any(sport in full_text for sport in sports_names)
    has_context = any(context in full_text for context in context_words)
    
    if has_sport and has_context:
        sports_with_context.append({
            "title": article.get("title"),
            "desc_len": len(desc)
        })

print(f"\nFound {len(sports_with_context)} articles with both sport names and context words")

if sports_with_context:
    sports_with_context.sort(key=lambda x: x["desc_len"], reverse=True)
    print("\nTop 10 longest with context:")
    for i in range(min(10, len(sports_with_context))):
        print(f"{sports_with_context[i]['desc_len']} chars - Title: {sports_with_context[i]['title']}")

result = sports_with_context[0]['title'] if sports_with_context else "No clear sports articles found"
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:14': ['articles'], 'var_functions.execute_python:26': 'No sports articles found', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'count': '127600'}], 'var_functions.query_db:34': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:36': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:38': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:46': 'IBM to market Sybase Linux database', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'total': 127600, 'sample_count': 50}, 'var_functions.execute_python:54': 'IBM to market Sybase Linux database', 'var_functions.execute_python:58': 'Bush Visits Canada On Fence-Mending Tour', 'var_functions.execute_python:60': 'Bush Visits Canada On Fence-Mending Tour'}

exec(code, env_args)
