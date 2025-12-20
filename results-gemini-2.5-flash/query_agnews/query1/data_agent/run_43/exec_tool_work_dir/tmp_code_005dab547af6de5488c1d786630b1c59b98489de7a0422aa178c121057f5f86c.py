code = """import pandas as pd
import json

# Correctly access the raw output from the query_db call
# var_function-call-12516105523217112198 is the dictionary containing 'query_db_response'
query_db_output = locals()['var_function-call-12516105523217112198']

# Navigate to the 'results' list which contains the raw string output
# The actual string with JSON is at query_db_output['query_db_response']['results'][0]
json_articles_raw_string = query_db_output['query_db_response']['results'][0]

# The string contains descriptive text followed by the JSON array. 
# We need to find the start and end of the JSON array.
start_index = json_articles_raw_string.find('[')
end_index = json_articles_raw_string.rfind(']')

result_title = ""

if start_index != -1 and end_index != -1 and start_index < end_index:
    clean_json_string = json_articles_raw_string[start_index : end_index + 1]
    data = json.loads(clean_json_string)
    df = pd.DataFrame(data)

    # Define keywords to identify sports articles
    sports_keywords = ['sport', 'game', 'team', 'match', 'play', 'athlete', 'championship', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'world cup', 'race', 'score', 'win', 'lose', 'sports']

    # Function to check if an article is a sports article
    def is_sports_article(title, description):
        title_lower = title.lower()
        description_lower = description.lower()
        for keyword in sports_keywords:
            if keyword in title_lower or keyword in description_lower:
                return True
        return False

    # Filter for sports articles
    sports_articles = df[df.apply(lambda row: is_sports_article(row['title'], row['description']), axis=1)]

    if not sports_articles.empty:
        # Calculate description length and find the article with the longest description
        sports_articles.loc[:, 'description_length'] = sports_articles['description'].apply(len)
        longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
        result_title = longest_description_article['title']
    else:
        result_title = "No sports articles found."
else:
    result_title = "Could not extract valid JSON array from the query result string."

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-12516105523217112198': [{'_id': '6943d3cb8cdf87d466fd4138', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943d3cb8cdf87d466fd4139', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943d3cb8cdf87d466fd413a', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943d3cb8cdf87d466fd413b', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943d3cb8cdf87d466fd413c', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-18114881157844902793': {'type_of_var_content': "<class 'list'>", 'content_keys': 'Not a dict', 'query_db_response_type': 'N/A', 'results_type': 'N/A', 'first_result_element_type': 'N/A', 'first_result_element_snippet': 'N/A'}, 'var_function-call-15798288326661052764': "No 'query_db_response' key found or it's not a dictionary.", 'var_function-call-8540598006749243741': "No 'query_db_response' key found or it's not a dictionary in the tool output.", 'var_function-call-9028384005021752410': 'Unexpected structure of query_db_response or missing keys.'}

exec(code, env_args)
