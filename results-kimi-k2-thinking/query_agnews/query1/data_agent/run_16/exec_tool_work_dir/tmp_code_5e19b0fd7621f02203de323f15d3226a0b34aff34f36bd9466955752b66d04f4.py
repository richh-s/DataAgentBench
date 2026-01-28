code = """import json

# Try to fetch the full metadata JSON file path
file_path = locals().get('var_functions.query_db:6', None)
result = None
if file_path and isinstance(file_path, str):
    try:
        with open(file_path, 'r') as f:
            result = json.load(f)
    except Exception as e:
        pass
try:
    if not result:
        result = locals().get('var_functions.query_db:6')
    if not result:
        result = locals().get('var_functions.query_db:5')
    if not result:
        result = locals().get('var_functions.query_db:2')
    articles = result
except Exception as e:
    articles = []

if articles:
    sports_keywords = ["sport", "sports", "football", "soccer", "cricket", "basketball", "tennis", "volleyball", "baseball", "hockey", "rugby", "athlete", "player", "team", "coach", "league", "game", "match", "race", "olympic", "tournament", "championship", "nba", "nfl", "mlb", "nhl", "world cup", "champion", "medal"]
    sports_articles = []
    for a in articles:
        text = (a.get("title", "") + " " + a.get("description", "")).lower()
        if any(kw in text for kw in sports_keywords):
            sports_articles.append(a)
    
    max_len = -1
    max_article = None
    for a in sports_articles:
        desc = a.get("description", "")
        desc_len = len(desc) if isinstance(desc, str) else 0
        if desc_len > max_len:
            max_len = desc_len
            max_article = a
    
    title = max_article.get("title") if max_article else None
else:
    title = None

print("__RESULT__:")
print(json.dumps(title))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69696d3759fd2d20354b7e1e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696d3759fd2d20354b7e1f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696d3759fd2d20354b7e20', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696d3759fd2d20354b7e21', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696d3759fd2d20354b7e22', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': None, 'var_functions.query_db:10': [{'_id': '69696d3759fd2d20354b7e1e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696d3759fd2d20354b7e1f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696d3759fd2d20354b7e20', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696d3759fd2d20354b7e21', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696d3759fd2d20354b7e22', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'type': "<class 'list'>", 'len': 5}, 'var_functions.query_db:14': [{'_id': '69696d3759fd2d20354b7e1e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696d3759fd2d20354b7e1f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696d3759fd2d20354b7e20', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696d3759fd2d20354b7e21', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696d3759fd2d20354b7e22', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
