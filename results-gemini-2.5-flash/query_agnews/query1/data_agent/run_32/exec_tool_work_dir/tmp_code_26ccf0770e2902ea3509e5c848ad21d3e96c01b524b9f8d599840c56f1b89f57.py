code = """import json
import pandas as pd

# Access the raw string output from the previous tool call
raw_output_string = locals()['var_function-call-6653126311838177654']['query_db_response']['results'][0]

# Extract the JSON part from the raw string
# The actual JSON array starts after "The result is:\n" and ends at the last ']' character.
json_start_index = raw_output_string.find("\nThe result is:\n") + len("\nThe result is:\n")
json_end_index = raw_output_string.rfind(']') + 1
json_string = raw_output_string[json_start_index:json_end_index]

# Parse the JSON string into a Python list of dictionaries
articles_data = json.loads(json_string)

sports_keywords = ['sport', 'sports', 'game', 'team', 'match', 'athlete', 'athletic', 'league', 'championship', 'cup', 'olympic', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'boxing', 'racing']

sports_articles = []
for article in articles_data:
    is_sports_article = False
    if 'title' in article and article['title'] is not None:
        if any(keyword in article['title'].lower() for keyword in sports_keywords):
            is_sports_article = True
    if not is_sports_article and 'description' in article and article['description'] is not None:
        if any(keyword in article['description'].lower() for keyword in sports_keywords):
            is_sports_article = True
    
    if is_sports_article:
        sports_articles.append(article)


if not sports_articles:
    longest_description_title = "No sports articles found."
else:
    longest_description_title = ""
    max_description_length = -1
    
    for article in sports_articles:
        if 'description' in article and article['description'] is not None:
            description_length = len(article['description'])
            if description_length > max_description_length:
                max_description_length = description_length
                longest_description_title = article.get('title', 'No Title')

print('__RESULT__:')
print(json.dumps(longest_description_title))"""

env_args = {'var_function-call-6653126311838177654': [{'_id': '6943cc3d78202fd17f3f06ee', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943cc3d78202fd17f3f06ef', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943cc3d78202fd17f3f06f0', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943cc3d78202fd17f3f06f1', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943cc3d78202fd17f3f06f2', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
