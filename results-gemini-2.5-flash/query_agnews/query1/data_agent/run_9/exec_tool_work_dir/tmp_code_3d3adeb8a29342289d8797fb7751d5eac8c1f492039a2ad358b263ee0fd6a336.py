code = """import json
import pandas as pd

# The raw output from the tool call is a list. The actual dictionary is its first element.
raw_output_list = locals()['var_function-call-16199537621126657501']

# Ensure it's a non-empty list before proceeding.
if not isinstance(raw_output_list, list) or not raw_output_list:
    result = f"Error: Expected locals()['var_function-call-16199537621126657501'] to be a non-empty list, but got {type(raw_output_list)}."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

# The actual dictionary from the tool output is the first element of this list.
tool_output_dict = raw_output_list[0]

# Check if the extracted element is indeed a dictionary as expected.
if not isinstance(tool_output_dict, dict):
    result = f"Error: Expected the first element of the tool output list to be a dictionary, but got {type(tool_output_dict)}."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

# Now, `tool_output_dict` is a Python dictionary. Proceed with extracting the nested data.
# Extract the string containing the raw query result information.
# This string is nested within 'query_db_response' and 'results'.
# The actual JSON array of articles is embedded within this string.
if 'query_db_response' not in tool_output_dict or \
   'results' not in tool_output_dict['query_db_response'] or \
   not isinstance(tool_output_dict['query_db_response']['results'], list) or \
   len(tool_output_dict['query_db_response']['results']) == 0:
    result = "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

raw_result_info_string = tool_output_dict['query_db_response']['results'][0]

# Find the index of the first '[' and the last ']' to precisely extract the JSON array.
start_json_array_index = raw_result_info_string.find('[')
end_json_array_index = raw_result_info_string.rfind(']')

# Check if valid JSON array bounds were found.
if start_json_array_index == -1 or end_json_array_index == -1 or start_json_array_index >= end_json_array_index:
    result = "Error: Could not find a valid JSON array within the query result string."
else:
    # Extract the pure JSON array string.
    json_articles_string = raw_result_info_string[start_json_array_index : end_json_array_index + 1]
    
    # Load the extracted JSON string into a Python list of dictionaries.
    articles = json.loads(json_articles_string)
    
    # Create a DataFrame from the articles data for easier manipulation.
    df = pd.DataFrame(articles)
    
    # Filter for sports articles based on keywords in title or description.
    # Using case-insensitive search and handling potential NaN values in strings (na=False).
    sports_articles = df[
        df['title'].str.contains('Sports', case=False, na=False) |
        df['description'].str.contains('Sports', case=False, na=False)
    ]
    
    if not sports_articles.empty:
        # Calculate the length of the 'description' for each sports article.
        # Use .copy() to avoid SettingWithCopyWarning when adding a new column.
        sports_articles_copy = sports_articles.copy()
        sports_articles_copy['description_length'] = sports_articles_copy['description'].str.len()
        
        # Find the article (row) with the maximum description length.
        longest_description_article = sports_articles_copy.loc[sports_articles_copy['description_length'].idxmax()]
        
        # The final result is the 'title' of this article.
        result = longest_description_article['title']
    else:
        result = "No sports articles found matching the criteria."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16199537621126657501': [{'_id': '6943b044c5cd65f08665be76', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b044c5cd65f08665be77', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b044c5cd65f08665be78', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b044c5cd65f08665be79', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b044c5cd65f08665be7a', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4047325946189911135': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-15561205082229652986': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-5140327464620276115': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-9022247047748760948': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-11005916387853996478': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary.", 'var_function-call-16432938943425634237': 'Error: Unexpected format for tool output: <class \'list\'> - [{\'_id\': \'6943b044c5cd65f08665be76\', \'title\': \'Wall St. Bears Claw Back Into the Black (Reuters)\', \'description\': "Reuters - Short-sellers, Wall Street\'s dwindling\\\\band of ultra-cynics, are seeing green again."}, {\'_id\': \'6943b044c5cd65f08665be77\', \'title\': \'Carlyle Looks Toward Commercial Aerospace (Reuters)\', \'description\': \'Reuters - Private investment firm Carlyle Group,\\\\which has a reputation for making well-timed and occasionally\\\\controversial plays in the defense industry, has quietly placed\\\\its bets on another part of the market.\'}, {\'_id\': \'6943b044c5cd65f08665be78\', \'title\': "Oil and Economy Cloud Stocks\' Outlook (Reuters)", \'description\': \'Reuters - Soaring crude prices plus worries\\\\about the economy and the outlook for earnings are expected to\\\\hang over the stock market next week during the depth of the\\\\summer doldrums.\'}, {\'_id\': \'6943b044c5cd65f08665be79\', \'title\': \'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)\', \'description\': \'Reuters - Authorities have halted oil export\\\\flows from the main pipeline in southern Iraq after\\\\intelligence showed a rebel militia could strike\\\\infrastructure, an oil official said on Saturday.\'}, {\'_id\': \'6943b044c5cd65f08665be7a\', \'title\': \'Oil prices soar to all-time record, posing new menace to US economy (AFP)\', \'description\': \'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.\'}]'}

exec(code, env_args)
