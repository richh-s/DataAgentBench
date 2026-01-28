code = """import json

# Access the articles from the previous query
articles = var_functions.query_db:0
print("Article count:", len(articles))

# Store all article info
all_articles = []
sports_articles = []
sport_keywords = ["nba", "nfl", "mlb", "nhl", "soccer", "football", "basketball", "baseball", "hockey", "tennis", "golf", "olympics", "athlete", "coach", "team", "player", "league", "championship", "tournament", "game", "match"]

for article in articles:
    title = article.get("title", "").lower()
    desc = article.get("description", "").lower()
    desc_len = len(article.get("description", ""))
    
    # Check if article is sports-related
    is_sports = any(keyword in title or keyword in desc for keyword in sport_keywords)
    
    all_articles.append({
        "article_id": article.get("article_id"),
        "title": article.get("title"),
        "description": article.get("description"),
        "desc_len": desc_len,
        "is_sports": is_sports
    })

# Identify sports articles
for article in all_articles:
    if article["is_sports"]:
        sports_articles.append(article)

# Debug output
print("Found", len(sports_articles), "sports articles")
for s in sports_articles:
    print(f"Sports: {s['desc_len']} chars - {s['title']}")

# Show all articles by description length
sorted_articles = sorted(all_articles, key=lambda x: x["desc_len"], reverse=True)
print("\nAll articles sorted by description length:")
for a in sorted_articles:
    print(f"Length: {a['desc_len']} chars, Sports: {a['is_sports']}, Title: {a['title'][:80]}")

result = json.dumps(sports_articles if sports_articles else [])
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '6969795b8a86433736289d7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969795b8a86433736289d7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969795b8a86433736289d80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969795b8a86433736289d81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969795b8a86433736289d82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:14': ['articles']}

exec(code, env_args)
