code = """import json
import pandas as pd

# Step 1: Access the raw output from the tool call. 
# Based on the initial output preview, locals()['var_function-call-16199537621126657501'] is directly a dictionary.
tool_output_dict = locals()['var_function-call-16199537621126657501']

# Step 2: Extract the string containing the raw query result information.
# This string is nested within 'query_db_response' and 'results'.
# The actual JSON array of articles is embedded within this string.
# Perform checks for dictionary keys and list types to avoid errors.
if not isinstance(tool_output_dict, dict) or \
   'query_db_response' not in tool_output_dict or \
   not isinstance(tool_output_dict['query_db_response'], dict) or \
   'results' not in tool_output_dict['query_db_response'] or \
   not isinstance(tool_output_dict['query_db_response']['results'], list) or \
   len(tool_output_dict['query_db_response']['results']) == 0:
    result = "Error: The structure of the tool output dictionary is unexpected or incomplete."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

raw_result_info_string = tool_output_dict['query_db_response']['results'][0]

# Step 3: The `raw_result_info_string` contains descriptive text along with the JSON array.
# We need to find the starting '[' and ending ']' of the JSON array to extract it precisely.
json_array_start_index = raw_result_info_string.find('[')
json_array_end_index = raw_result_info_string.rfind(']')

# Step 4: Validate that both start and end brackets were found and in the correct order.
if json_array_start_index == -1 or json_array_end_index == -1 or json_array_start_index >= json_array_end_index:
    result = "Error: Could not extract a valid JSON array from the query result string. Brackets not found or incorrectly placed."
else:
    # Step 5: Extract the pure JSON array string, including the brackets themselves.
    json_articles_string = raw_result_info_string[json_array_start_index : json_array_end_index + 1]
    
    # Step 6: Parse the extracted JSON string into a Python list of dictionaries.
    articles = json.loads(json_articles_string)
    
    # Step 7: Create a Pandas DataFrame from the list of article dictionaries for easier manipulation.
    df = pd.DataFrame(articles)
    
    # Step 8: Filter the DataFrame to identify articles that are categorized as 'Sports'.
    # This is determined by checking if the word 'Sports' (case-insensitive) is present
    # in either the 'title' or 'description' columns. `na=False` treats any NaN (missing)
    # string values in these columns as not containing 'Sports', preventing errors.
    sports_articles = df[
        df['title'].str.contains('Sports', case=False, na=False) |
        df['description'].str.contains('Sports', case=False, na=False)
    ]
    
    # Step 9: Check if any articles were identified as sports-related.
    if not sports_articles.empty:
        # Step 10: If sports articles are found, calculate the length of their descriptions.
        # A `.copy()` is used here to explicitly create a new DataFrame slice,
        # preventing a SettingWithCopyWarning if a new column is added to a view of the original DataFrame.
        sports_articles_with_length = sports_articles.copy()
        sports_articles_with_length['description_length'] = sports_articles_with_length['description'].str.len()
        
        # Step 11: Find the single article (row) within the filtered and augmented DataFrame
        # that has the maximum 'description_length'. `.idxmax()` returns the index of the row with the max value.
        longest_description_article = sports_articles_with_length.loc[sports_articles_with_length['description_length'].idxmax()]
        
        # Step 12: The final required output is the 'title' of this specific article.
        result = longest_description_article['title']
    else:
        # Step 13: If no articles contained 'Sports' in their title or description, return an appropriate message.
        result = "No sports articles found matching the criteria."

# Print the final result as a JSON-formatted string.
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16199537621126657501': [{'_id': '6943b044c5cd65f08665be76', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b044c5cd65f08665be77', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b044c5cd65f08665be78', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b044c5cd65f08665be79', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b044c5cd65f08665be7a', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4047325946189911135': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-15561205082229652986': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-5140327464620276115': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-9022247047748760948': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-11005916387853996478': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-16432938943425634237': 'Error: Unexpected format for tool output: <class \'list\'> - [{\'_id\': \'6943b044c5cd65f08665be76\', \'title\': \'Wall St. Bears Claw Back Into the Black (Reuters)\', \'description\': "Reuters - Short-sellers, Wall Street\'s dwindling\\\\band of ultra-cynics, are seeing green again."}, {\'_id\': \'6943b044c5cd65f08665be77\', \'title\': \'Carlyle Looks Toward Commercial Aerospace (Reuters)\', \'description\': \'Reuters - Private investment firm Carlyle Group,\\\\which has a reputation for making well-timed and occasionally\\\\controversial plays in the defense industry, has quietly placed\\\\its bets on another part of the market.\'}, {\'_id\': \'6943b044c5cd65f08665be78\', \'title\': "Oil and Economy Cloud Stocks\' Outlook (Reuters)", \'description\': \'Reuters - Soaring crude prices plus worries\\\\about the economy and the outlook for earnings are expected to\\\\hang over the stock market next week during the depth of the\\\\summer doldrums.\'}, {\'_id\': \'6943b044c5cd65f08665be79\', \'title\': \'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)\', \'description\': \'Reuters - Authorities have halted oil export\\\\flows from the main pipeline in southern Iraq after\\\\intelligence showed a rebel militia could strike\\\\infrastructure, an oil official said on Saturday.\'}, {\'_id\': \'6943b044c5cd65f08665be7a\', \'title\': \'Oil prices soar to all-time record, posing new menace to US economy (AFP)\', \'description\': \'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.\'}]', 'var_function-call-1921964812876649390': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-8407405549876616282': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-17327921869734973831': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-17465425103472890151': "Error: 'query_db_response' key missing or not a dictionary in tool output.", 'var_function-call-12431608459379231836': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-12218274888686300937': "Error: Expected tool output from storage to be a dictionary, but got <class 'list'>.", 'var_function-call-4469360760498566086': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary."}

exec(code, env_args)
