code = """import json

raw_output_string = locals()['var_function-call-18049962149930704651']['query_db_response']['results'][0]

# Find the actual JSON array string within the raw output
json_start = raw_output_string.find('[')
json_end = raw_output_string.rfind(']')

articles = []
if json_start != -1 and json_end != -1:
    articles_json_string = raw_output_string[json_start : json_end + 1] # +1 to include the closing bracket
    articles = json.loads(articles_json_string)

sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    # Check for sports-related keywords in title or description
    if any(keyword in title for keyword in ['sport', 'team', 'game', 'match', 'league', 'championship', 'olympic', 'cup', 'ball', 'player']) or \
       any(keyword in description for keyword in ['sport', 'team', 'game', 'match', 'league', 'championship', 'olympic', 'cup', 'ball', 'player']):
        sports_articles.append(article)

if not sports_articles:
    result = "No sports articles found in the provided data sample using the defined keywords."
else:
    max_desc_len = -1
    title_with_max_desc = ""
    for article in sports_articles:
        description_length = len(article.get('description', ''))
        if description_length > max_desc_len:
            max_desc_len = description_length
            title_with_max_desc = article.get('title', '')
    result = title_with_max_desc

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-18049962149930704651': [{'_id': '6943d0cc9889312376f31a3b', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d0cc9889312376f31a3c', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d0cc9889312376f31a3d', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d0cc9889312376f31a3e', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d0cc9889312376f31a3f', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
