code = """import json

# Read metadata file
metadata_file_path = str(locals()['var_functions.query_db:18'])
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs and region mapping
article_ids_2015 = [int(item['article_id']) for item in metadata_2015]
region_map = {int(item['article_id']): item['region'] for item in metadata_2015}

# Build MongoDB query string directly
mongo_query_str = json.dumps({
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_2015}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 20000
})

print('__RESULT__:')
print(mongo_query_str)"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'_id': '6969d601d1cec1b5f3cccc97', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d601d1cec1b5f3cccc98', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d601d1cec1b5f3cccc99', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d601d1cec1b5f3cccc9a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969d601d1cec1b5f3cccc9b', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
