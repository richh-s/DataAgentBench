code = """import pandas as pd
import json
import re

# Assume var_function-call-9277599381154460855 is the raw string output of the tool call
raw_tool_output_string = locals()['var_function-call-9277599381154460855']

# This string itself is a JSON object. Parse it.
try:
    parsed_output = json.loads(raw_tool_output_string)
    # Now access the 'query_db_response' and then 'results'
    raw_articles_data_list_with_extra_text = parsed_output['query_db_response']['results'][0]

    # Extract the actual JSON array from this string
    match = re.search(r'\[.*\]', raw_articles_data_list_with_extra_text, re.DOTALL)

    if match:
        json_data_array_str = match.group(0)
        articles_list = json.loads(json_data_array_str)

        df = pd.DataFrame(articles_list)

        df['title'] = df['title'].astype(str)
        df['description'] = df['description'].astype(str)

        df['description_length'] = df['description'].str.len()

        sports_articles_df = df[
            df['title'].str.contains('sport', case=False, na=False) |
            df['description'].str.contains('sport', case=False, na=False)
        ]

        if not sports_articles_df.empty:
            longest_description_sports_article = sports_articles_df.loc[
                sports_articles_df['description_length'].idxmax()
            ]
            result_title = longest_description_sports_article['title']
        else:
            result_title = "No sports articles found."
    else:
        result_title = "Failed to extract JSON array from results string."

except Exception as e:
    result_title = f"Error processing tool output: {str(e)}"

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-9277599381154460855': [{'_id': '6943aee16e3a71ad0310bf58', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943aee16e3a71ad0310bf59', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943aee16e3a71ad0310bf5a', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943aee16e3a71ad0310bf5b', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943aee16e3a71ad0310bf5c', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
