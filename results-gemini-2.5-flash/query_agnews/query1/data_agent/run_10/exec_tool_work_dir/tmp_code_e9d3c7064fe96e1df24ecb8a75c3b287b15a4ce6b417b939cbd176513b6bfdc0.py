code = """import json
import pandas as pd

raw_output_string = locals()['var_function-call-8451715818363324170']['query_db_response']['results'][0]

start_idx = raw_output_string.find('[')
end_idx = raw_output_string.rfind(']')

result_value = "Error: JSON extraction failed."

if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
    json_array_str = raw_output_string[start_idx : end_idx + 1]

    try:
        articles = json.loads(json_array_str)
        df = pd.DataFrame(articles)

        df['title_lower'] = df['title'].str.lower()
        df['description_lower'] = df['description'].str.lower()

        sports_keywords = ['sport', 'team', 'game', 'match', 'playoff', 'league', 'championship', 'cup', 'olympics', 'athlete', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'racing', 'boxing', 'wrestling', 'track', 'field', 'medal', 'score', 'win', 'lose', 'player', 'coach']

        df_sports = df[df['title_lower'].apply(lambda x: any(keyword in x for keyword in sports_keywords)) |
                       df['description_lower'].apply(lambda x: any(keyword in x for keyword in sports_keywords))]

        df_sports = df_sports.dropna(subset=['description'])
        df_sports['description_length'] = df_sports['description'].str.len()

        if not df_sports.empty:
            longest_description_article = df_sports.loc[df_sports['description_length'].idxmax()]
            result_value = longest_description_article['title']
        else:
            result_value = "No sports articles found matching the criteria."

    except json.JSONDecodeError as e:
        # Avoid f-string here to prevent potential issues with content of e or json_array_str
        result_value = "JSON decoding error: " + str(e) + ". Extracted string starts with: " + json_array_str[:100]

else:
    result_value = "Could not find a valid JSON array in the tool output string."

print('__RESULT__:')
print(json.dumps(result_value))"""

env_args = {'var_function-call-8451715818363324170': [{'_id': '6943b425257e8027af603603', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943b425257e8027af603604', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943b425257e8027af603605', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943b425257e8027af603606', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943b425257e8027af603607', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
