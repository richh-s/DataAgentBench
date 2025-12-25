code = """import json

def is_business_article(title, description):
    business_keywords = ['business', 'economy', 'market', 'stock', 'finance', 'company', 'invest', 'profit', 'economic', 'trade', 'bank', 'corporate', 'financial', 'industr', 'economy']
    title_lower = title.lower() if title else ''
    description_lower = description.lower() if description else ''

    for keyword in business_keywords:
        if keyword in title_lower or keyword in description_lower:
            return True
    return False

# Access the full tool output
raw_query_result = locals()['var_function-call-13676785764808340276']

# The 'query_db_response' is a dictionary inside the raw_query_result
query_db_response = raw_query_result.get('query_db_response', {})

# The 'results' field inside query_db_response is a list of strings
articles_raw_data_list = query_db_response.get('results', [])

business_articles_ids = set()

if articles_raw_data_list and isinstance(articles_raw_data_list, list):
    # The first element of this list contains the actual JSON string along with other text
    full_response_string = articles_raw_data_list[0]

    # Find the beginning of the JSON array. The format often includes "The result is:\n" before the JSON.
    # The JSON array itself starts with '[' and ends with ']'.
    json_start_index = full_response_string.find('[')
    json_end_index = full_response_string.rfind(']')

    if json_start_index != -1 and json_end_index != -1:
        # Extract the part of the string that contains only the JSON array
        json_data_string = full_response_string[json_start_index : json_end_index + 1]

        try:
            articles_data = json.loads(json_data_string)
            for article_dict in articles_data:
                if is_business_article(article_dict.get('title'), article_dict.get('description')):
                    # Ensure article_id is treated as an integer
                    business_articles_ids.add(int(article_dict.get('article_id')))
        except json.JSONDecodeError as e:
            # Print error if JSON decoding fails
            print('__RESULT__:')
            print(json.dumps({"error": "JSON decoding failed: " + str(e)}))

print('__RESULT__:')
print(json.dumps(list(business_articles_ids)))"""

env_args = {'var_function-call-13676785764808340276': [{'_id': '6943ecefe0113d722733aa3d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943ecefe0113d722733aa3e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943ecefe0113d722733aa3f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943ecefe0113d722733aa40', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943ecefe0113d722733aa41', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
