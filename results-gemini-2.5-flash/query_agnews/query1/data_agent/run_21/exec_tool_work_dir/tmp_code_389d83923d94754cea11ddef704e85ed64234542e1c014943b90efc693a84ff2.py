code = """import pandas as pd
import json

# Correctly access the raw string output from the query_db tool.
# Based on the debug output, locals()['var_function-call-3102122510052250243'] is a list.
# The first element of this list is the dictionary containing 'query_db_response'.
raw_tool_output_list = locals()['var_function-call-3102122510052250243']
query_response_dict = raw_tool_output_list[0]
full_output_string = query_response_dict['query_db_response']['results'][0]

# Find the actual start and end of the JSON array within the string.
json_start_index = full_output_string.find('[')
json_end_index = full_output_string.rfind(']')

result_title = "Error: Could not process articles or find sports articles."

if json_start_index != -1 and json_end_index != -1 and json_start_index < json_end_index:
    json_string = full_output_string[json_start_index : json_end_index + 1]

    try:
        articles_data = json.loads(json_string)
        articles_df = pd.DataFrame(articles_data)

        def is_sports_article(title, description):
            keywords = [
                "sport", "game", "team", "match", "play", "league", "athlet",
                "cup", "championship", "coach", "player", "olympic", "football",
                "basketball", "baseball", "tennis", "golf", "cricket", "rugby",
                "boxing", "racing", "medal", "tournament", "score", "victory",
                "athlete", "fan", "stadium", "track", "field", "runner", "swimmer",
                "goal", "penalty", "referee", "umpire", "final", "semi-final", "quarter-final"
            ]
            title_lower = str(title).lower() if title else ""
            description_lower = str(description).lower() if description else ""
            for keyword in keywords:
                if keyword in title_lower or keyword in description_lower:
                    return True
            return False

        articles_df["is_sports"] = articles_df.apply(lambda row: is_sports_article(row["title"], row["description"]), axis=1)
        sports_articles_df = articles_df[articles_df["is_sports"]]

        if not sports_articles_df.empty:
            # Make a copy to avoid SettingWithCopyWarning
            sports_articles_df = sports_articles_df.copy()
            sports_articles_df["description_length"] = sports_articles_df["description"].apply(lambda x: len(str(x)) if x else 0)
            longest_description_article = sports_articles_df.loc[sports_articles_df["description_length"].idxmax()]
            result_title = longest_description_article["title"]
        else:
            result_title = "No sports articles found matching the criteria."
    except json.JSONDecodeError as e:
        result_title = f"JSON decoding error: {e}. String was: {json_string[:200]}..."
    except Exception as e:
        result_title = f"An unexpected error occurred during processing: {e}"
else:
    result_title = "Could not extract JSON data from the query result."

print("__RESULT__:")
print(json.dumps(result_title))"""

env_args = {'var_function-call-3102122510052250243': [{'_id': '6943c0e59c9b5ec76c27095d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c0e59c9b5ec76c27095e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c0e59c9b5ec76c27095f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c0e59c9b5ec76c270960', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c0e59c9b5ec76c270961', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4006476781967917474': {'type_raw_data': "<class 'list'>", 'keys_raw_data': 'Not a dict'}, 'var_function-call-7897004986572678261': 'An unexpected error occurred during processing: the JSON object must be str, bytes or bytearray, not list'}

exec(code, env_args)
