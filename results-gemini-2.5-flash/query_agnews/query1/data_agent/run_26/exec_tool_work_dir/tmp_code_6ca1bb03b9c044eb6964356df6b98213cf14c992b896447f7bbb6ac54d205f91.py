code = """import pandas as pd
import json

raw_result_string = locals()['var_function-call-9742216927815967350']['query_db_response']['results'][0]

start_json_index = raw_result_string.find('[')
end_json_index = raw_result_string.rfind(']') + 1

json_string = raw_result_string[start_json_index:end_json_index]

articles_data = json.loads(json_string)

articles_df = pd.DataFrame(articles_data)

sports_articles_df = articles_df[
    articles_df['title'].astype(str).str.contains('sports', case=False, na=False) |
    articles_df['description'].astype(str).str.contains('sports', case=False, na=False)
].copy()

if not sports_articles_df.empty:
    sports_articles_df['description_length'] = sports_articles_df['description'].astype(str).str.len()
    max_length_article = sports_articles_df.loc[sports_articles_df['description_length'].idxmax()]
    result_title = max_length_article['title']
else:
    result_title = "No sports articles found."

print('__RESULT__:')
print(json.dumps(result_title))"""

env_args = {'var_function-call-9742216927815967350': [{'_id': '6943c73eb133218044e65736', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c73eb133218044e65737', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c73eb133218044e65738', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c73eb133218044e65739', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c73eb133218044e6573a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
