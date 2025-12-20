code = """import json

articles_data = locals()['var_function-call-14274774357462507823']['query_db_response']['results']

sports_keywords = [
    "sport", "game", "team", "match", "league", "cup", "athlet", "player", "coach",
    "football", "basketball", "baseball", "tennis", "golf", "racing", "olympic",
    "world series", "super bowl", "championship"
]

longest_description_length = -1
longest_description_title = ""

for article_str in articles_data:
    article = json.loads(article_str)
    title = article.get("title", "")
    description = article.get("description", "")
    
    is_sports_article = False
    for keyword in sports_keywords:
        if keyword.lower() in title.lower() or keyword.lower() in description.lower():
            is_sports_article = True
            break

    if is_sports_article:
        current_description_length = len(description)
        if current_description_length > longest_description_length:
            longest_description_length = current_description_length
            longest_description_title = title

print("__RESULT__:")
print(json.dumps(longest_description_title))"""

env_args = {'var_function-call-14274774357462507823': [{'_id': '6943a9fbf2a3d53d79eeb15f', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943a9fbf2a3d53d79eeb160', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943a9fbf2a3d53d79eeb161', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943a9fbf2a3d53d79eeb162', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943a9fbf2a3d53d79eeb163', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
