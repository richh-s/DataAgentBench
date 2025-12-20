code = """import json
import pandas as pd

# The result from the query_db tool is stored directly as a dictionary in locals().
tool_output_dict = locals()['var_function-call-16199537621126657501']

# The actual articles data is contained within a string that is the first element
# of the 'results' list, which is nested under 'query_db_response'.
raw_result_string_with_metadata = tool_output_dict['query_db_response']['results'][0]

# We need to extract the pure JSON array string from raw_result_string_with_metadata.
# The JSON array starts with '[' and ends with ']'.
json_array_start_index = raw_result_string_with_metadata.find('[')
json_array_end_index = raw_result_string_with_metadata.rfind(']')

# Check if valid JSON array boundaries were found.
if json_array_start_index == -1 or json_array_end_index == -1 or json_array_start_index >= json_array_end_index:
    result = "Error: Could not extract valid JSON array from the query result string. Brackets not found or incorrectly placed."
else:
    # Extract the pure JSON array string.
    json_articles_string = raw_result_string_with_metadata[json_array_start_index : json_array_end_index + 1]
    
    # Parse the extracted JSON string into a Python list of dictionaries.
    articles = json.loads(json_articles_string)
    
    # Create a Pandas DataFrame for easier data manipulation.
    df = pd.DataFrame(articles)
    
    # Filter for sports articles. This is done by checking if 'Sports' (case-insensitive)
    # appears in either the 'title' or 'description' columns. `na=False` handles NaN values.
    sports_articles = df[
        df['title'].str.contains('Sports', case=False, na=False) |
        df['description'].str.contains('Sports', case=False, na=False)
    ]
    
    # Check if any sports articles were found.
    if not sports_articles.empty:
        # Calculate the length of the 'description' for each sports article.
        # Use .copy() to avoid SettingWithCopyWarning when adding a new column.
        sports_articles_with_length = sports_articles.copy()
        sports_articles_with_length['description_length'] = sports_articles_with_length['description'].str.len()
        
        # Find the article (row) with the maximum description length.
        longest_description_article = sports_articles_with_length.loc[sports_articles_with_length['description_length'].idxmax()]
        
        # The result is the 'title' of this article.
        result = longest_description_article['title']
    else:
        result = "No sports articles found matching the criteria."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16199537621126657501': [{'_id': '6943b044c5cd65f08665be76', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b044c5cd65f08665be77', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b044c5cd65f08665be78', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b044c5cd65f08665be79', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b044c5cd65f08665be7a', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4047325946189911135': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-15561205082229652986': "Error: 'query_db_response' or 'results' key missing or malformed in tool output.", 'var_function-call-5140327464620276115': "Error: 'query_db_response' or 'results' key missing or malformed in tool output."}

exec(code, env_args)
