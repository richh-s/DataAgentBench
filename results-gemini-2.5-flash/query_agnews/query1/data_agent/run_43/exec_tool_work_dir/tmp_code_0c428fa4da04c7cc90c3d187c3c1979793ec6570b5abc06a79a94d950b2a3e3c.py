code = """import pandas as pd
import json

# Access the complex structure correctly
# Assuming var_function-call-12516105523217112198 is a list containing the tool's dictionary output
tool_output = locals()['var_function-call-12516105523217112198']

# Check if tool_output is a list and not empty
if isinstance(tool_output, list) and len(tool_output) > 0:
    # Access the dictionary from the list
    response_dict = tool_output[0]

    # Check if it contains 'query_db_response' key
    if 'query_db_response' in response_dict and isinstance(response_dict['query_db_response'], dict):
        query_db_response_content = response_dict['query_db_response']

        # Check if 'results' key exists and is a list
        if 'results' in query_db_response_content and isinstance(query_db_response_content['results'], list) and len(query_db_response_content['results']) > 0:
            # The actual JSON string of articles is the first element in the 'results' list
            json_articles_string = query_db_response_content['results'][0]

            # The string might contain leading/trailing whitespace or newlines. Strip them.
            json_articles_string = json_articles_string.strip()

            # Load the JSON string into a Python list of dictionaries
            data = json.loads(json_articles_string)
            df = pd.DataFrame(data)

            sports_keywords = ['sport', 'game', 'team', 'match', 'play', 'athlete', 'championship', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'world cup', 'race', 'score', 'win', 'lose']

            def is_sports_article(title, description):
                title_lower = title.lower()
                description_lower = description.lower()
                for keyword in sports_keywords:
                    if keyword in title_lower or keyword in description_lower:
                        return True
                return False

            sports_articles = df[df.apply(lambda row: is_sports_article(row['title'], row['description']), axis=1)]

            if not sports_articles.empty:
                sports_articles.loc[:, 'description_length'] = sports_articles['description'].apply(len)
                longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
                result = longest_description_article['title']
            else:
                result = "No sports articles found."
        else:
            result = "No 'results' found in query_db_response or it's empty."
    else:
        result = "No 'query_db_response' key found or it's not a dictionary."
else:
    result = "Tool output is empty or not a list."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-12516105523217112198': [{'_id': '6943d3cb8cdf87d466fd4138', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d3cb8cdf87d466fd4139', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d3cb8cdf87d466fd413a', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d3cb8cdf87d466fd413b', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d3cb8cdf87d466fd413c', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-18114881157844902793': {'type_of_var_content': "<class 'list'>", 'content_keys': 'Not a dict', 'query_db_response_type': 'N/A', 'results_type': 'N/A', 'first_result_element_type': 'N/A', 'first_result_element_snippet': 'N/A'}}

exec(code, env_args)
