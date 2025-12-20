code = """import json
import re

# Access the raw string from the previous tool call result
query_result_raw_string = locals()['var_function-call-2645469834901478309']['query_db_response']['results'][0]

# Find the first '[' and the last ']' to extract the JSON array string
start_index = query_result_raw_string.find('[')
end_index = query_result_raw_string.rfind(']')

articles_list = []
if start_index != -1 and end_index != -1:
    json_array_str = query_result_raw_string[start_index : end_index + 1]
    articles_list = json.loads(json_array_str)

max_description_length = -1
sports_article_title = ""

for article in articles_list:
    title = article['title']
    description = article['description']

    # Check if 'Sports' (case-insensitive) is present as a whole word in the title or description
    # Using re.IGNORECASE for case-insensitive matching and raw string for regex pattern
    if re.search(r'\\bSports\\b', title, re.IGNORECASE) or re.search(r'\\bSports\\b', description, re.IGNORECASE):
        description_length = len(description)
        if description_length > max_description_length:
            max_description_length = description_length
            sports_article_title = title

print("__RESULT__:")
print(json.dumps(sports_article_title))"""

env_args = {'var_function-call-2645469834901478309': [{'_id': '6943bb607132a18c259c32ed', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943bb607132a18c259c32ee', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943bb607132a18c259c32ef', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943bb607132a18c259c32f0', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943bb607132a18c259c32f1', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
