code = """import json

business_article_ids = locals()['var_function-call-8411052872557816197']

# Convert article_id to integers to match the expected type in SQL IN clause
# Assuming article_id in business_article_ids are strings, convert them to integers.
# If they are already integers, this step will not change them.
business_article_ids_int = [int(aid) for aid in business_article_ids]

# Format the list of IDs into a string suitable for a SQL IN clause
ids_str = ', '.join(map(str, business_article_ids_int))

# Construct the SQL query
sql_query = f"SELECT article_id, region, publication_date FROM article_metadata WHERE article_id IN ({ids_str}) AND region = 'Europe' AND STRFTIME('%Y', publication_date) BETWEEN '2010' AND '2020';"

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-5014513872523189925': [{'_id': '6943efbe567a959f6dfa279a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943efbe567a959f6dfa279b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943efbe567a959f6dfa279c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943efbe567a959f6dfa279d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943efbe567a959f6dfa279e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8411052872557816197': ['1', '2', '4']}

exec(code, env_args)
