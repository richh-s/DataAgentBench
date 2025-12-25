code = """import pandas as pd
import json
raw_output_string = locals()['var_function-call-9277599381154460855']['query_db_response']['results'][0]
json_start_idx = raw_output_string.find('[')
json_end_idx = raw_output_string.rfind(']') + 1
json_data_array_str = raw_output_string[json_start_idx:json_end_idx]
articles_list = json.loads(json_data_array_str)
df = pd.DataFrame(articles_list)
df['description_length'] = df['description'].str.len()
sports_articles_df = df[df['title'].str.contains('sport', case=False) | df['description'].str.contains('sport', case=False)]
if not sports_articles_df.empty:
    longest_description_sports_article = sports_articles_df.loc[sports_articles_df['description_length'].idxmax()]
    result_title = longest_description_sports_article['title']
else:
    result_title = "No sports articles found."
print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-9277599381154460855': [{'_id': '6943aee16e3a71ad0310bf58', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943aee16e3a71ad0310bf59', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943aee16e3a71ad0310bf5a', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943aee16e3a71ad0310bf5b', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943aee16e3a71ad0310bf5c', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
