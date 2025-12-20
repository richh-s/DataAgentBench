code = """import json
raw_result_string = locals()['var_function-call-8009334219944431032']['query_db_response']['results'][0]
start_index = raw_result_string.find('[')
end_index = raw_result_string.rfind(']')
json_string = raw_result_string[start_index : end_index+1]
articles = json.loads(json_string)

sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics', 'game', 'match', 'athlete', 'team', 'league', 'championship', 'cup']

max_desc_length = -1
sports_article_title = ''

for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    
    is_sports_article = False
    for keyword in sports_keywords:
        if keyword in title or keyword in description:
            is_sports_article = True
            break

    if is_sports_article:
        desc_length = len(article.get('description', ''))
        if desc_length > max_desc_length:
            max_desc_length = desc_length
            sports_article_title = article.get('title', '')

print('__RESULT__:')
print(json.dumps(sports_article_title))"""

env_args = {'var_function-call-8009334219944431032': [{'_id': '6943aab942b29793b81b3167', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943aab942b29793b81b3168', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943aab942b29793b81b3169', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943aab942b29793b81b316a', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943aab942b29793b81b316b', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
