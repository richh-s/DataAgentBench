code = """import json
import pandas as pd

# Get the raw output from the tool call. This is expected to be a dictionary.
raw_tool_output = locals()['var_function-call-16199537621126657501']

# Debugging: Print the type and a preview of raw_tool_output
print('__RESULT__:')
print(json.dumps({'step': 'raw_tool_output', 'type': str(type(raw_tool_output)), 'preview': str(raw_tool_output)[:200]}))

# Ensure raw_tool_output is a dictionary before proceeding.
if not isinstance(raw_tool_output, dict):
    result = f"Error: Expected tool output to be a dictionary, but got {type(raw_tool_output)}."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

tool_output_dict = raw_tool_output

# Access 'query_db_response' and 'results' keys.
# Debugging: Print the type and a preview of tool_output_dict['query_db_response']
if 'query_db_response' not in tool_output_dict:
    result = "Error: 'query_db_response' key missing in tool output."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

query_db_response_dict = tool_output_dict['query_db_response']
print('__RESULT__:')
print(json.dumps({'step': 'query_db_response_dict', 'type': str(type(query_db_response_dict)), 'preview': str(query_db_response_dict)[:200]}))

if 'results' not in query_db_response_dict:
    result = "Error: 'results' key missing in query_db_response."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

raw_results_list = query_db_response_dict['results']
# Debugging: Print the type and a preview of raw_results_list
print('__RESULT__:')
print(json.dumps({'step': 'raw_results_list', 'type': str(type(raw_results_list)), 'preview': str(raw_results_list)[:200]}))

if not isinstance(raw_results_list, list) or not raw_results_list:
    result = "Error: 'results' is not a non-empty list."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

# The actual articles data is a string, which is the first element of the 'results' list.
raw_result_info_string = raw_results_list[0]

# Debugging: Print the type and a preview of raw_result_info_string
print('__RESULT__:')
print(json.dumps({'step': 'raw_result_info_string', 'type': str(type(raw_result_info_string)), 'preview': raw_result_info_string[:200]}))

# Find the index of the first '[' and the last ']' to precisely extract the JSON array.
start_json_array_index = raw_result_info_string.find('[')
end_json_array_index = raw_result_info_string.rfind(']')

# Check if valid JSON array boundaries were successfully found.
if start_json_array_index == -1 or end_json_array_index == -1 or start_json_array_index >= end_json_array_index:
    result = "Error: Could not extract valid JSON array from the query result string. Brackets not found or incorrectly placed."
    print('__RESULT__:')
    print(json.dumps(result))
    exit()

# Extract the pure JSON array string.
json_articles_string = raw_result_info_string[start_json_array_index : end_json_array_index + 1]

# Debugging: Print a preview of json_articles_string
print('__RESULT__:')
print(json.dumps({'step': 'json_articles_string', 'preview': json_articles_string[:200]}))

# Parse the extracted JSON string into a Python list of dictionaries.
articles = json.loads(json_articles_string)

# Create a Pandas DataFrame for easier data manipulation.
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

env_args = {'var_function-call-16199537621126657501': [{'_id': '6943b044c5cd65f08665be76', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b044c5cd65f08665be77', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b044c5cd65f08665be78', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b044c5cd65f08665be79', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b044c5cd65f08665be7a', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4047325946189911135': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-15561205082229652986': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-5140327464620276115': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-9022247047748760948': "Error: 'query_db_response' or 'results' key missing or malformed in tool output dictionary."}

exec(code, env_args)
