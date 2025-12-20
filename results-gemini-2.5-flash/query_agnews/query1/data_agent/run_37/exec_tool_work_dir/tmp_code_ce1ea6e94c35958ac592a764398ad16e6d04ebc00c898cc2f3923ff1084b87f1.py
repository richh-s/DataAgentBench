code = """import json
import re

# Assume locals()['var_function-call-3265969682324267093'] directly contains the list of result strings
result_strings_list = locals()['var_function-call-3265969682324267093']['query_db_response']['results']

# Take the first (and likely only) string from the list
raw_json_containing_string = result_strings_list[0]

# Use regex to find the JSON array part in the string
match = re.search(r'\[.*\]', raw_json_containing_string, re.DOTALL)
if match:
    json_array_string = match.group(0)
    data = json.loads(json_array_string)
else:
    data = [] # Handle case where no JSON array is found

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
