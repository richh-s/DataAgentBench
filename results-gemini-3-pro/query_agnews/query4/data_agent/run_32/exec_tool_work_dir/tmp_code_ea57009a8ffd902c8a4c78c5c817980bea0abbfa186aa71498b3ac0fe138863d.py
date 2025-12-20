code = """import json

# Load metadata
with open(locals()['var_function-call-5900547977647289407'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
content_list = locals()['var_function-call-11413350339637926914']

print(f"Meta Sample: {metadata_list[0]}")
print(f"Content Sample: {content_list[0]}")

print(f"Meta ID Type: {type(metadata_list[0]['article_id'])}")
print(f"Content ID Type: {type(content_list[0]['article_id'])}")

# Check if content list covers the range
meta_ids_int = [int(x['article_id']) for x in metadata_list]
content_ids_int = [int(x['article_id']) for x in content_list]

print(f"Meta ID Range: {min(meta_ids_int)} - {max(meta_ids_int)}")
print(f"Content ID Range: {min(content_ids_int)} - {max(content_ids_int)}")

# Intersection check with ints
common = set(meta_ids_int).intersection(set(content_ids_int))
print(f"Common count (int): {len(common)}")

print("__RESULT__:")
print(json.dumps({"common_int": len(common)}))"""

env_args = {'var_function-call-5900547977647289407': 'file_storage/function-call-5900547977647289407.json', 'var_function-call-8253439238580865499': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52]}, 'var_function-call-11413350339637926914': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6748392322076207893': {'counts': {}, 'debug': []}, 'var_function-call-11835655730956261158': {'common': 0}}

exec(code, env_args)
