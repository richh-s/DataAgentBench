code = """import json
# The result is a list with a single string element, which is the actual JSON array
json_string = locals()['var_function-call-3265969682324267093']['query_db_response']['results'][0]
# Extract the actual JSON array part from the string
start_index = json_string.find('[')
end_index = json_string.rfind(']')
clean_json_string = json_string[start_index : end_index + 1]
data = json.loads(clean_json_string)

sports_keywords = ['sport', 'game', 'match', 'team', 'player', 'olympic', 'championship', 'cup', 'league', 'athletic', 'football', 'basketball', 'tennis', 'golf', 'baseball', 'racing', 'race', 'track', 'field', 'win', 'lose', 'defeat', 'victory', 'score', 'goal', 'foul', 'referee', 'coach', 'season', 'tournament', 'medal']
longest_description_title = None
max_description_length = -1

for article in data:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()

    is_sports_article = False
    for keyword in sports_keywords:
        if keyword in title or keyword in description:
            is_sports_article = True
            break
    
    if is_sports_article:
        description_length = len(article.get('description', ''))
        if description_length > max_description_length:
            max_description_length = description_length
            longest_description_title = article.get('title')

print('__RESULT__:')
print(json.dumps(longest_description_title))"""

env_args = {'var_function-call-3265969682324267093': [{'_id': '6943d0495ea2345f83fba716', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d0495ea2345f83fba717', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d0495ea2345f83fba718', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d0495ea2345f83fba719', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d0495ea2345f83fba71a', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
