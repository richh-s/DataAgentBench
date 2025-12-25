code = """import json

with open(locals()['var_function-call-7730568976014147704'], 'r') as f:
    metadata_list = json.load(f)

with open(locals()['var_function-call-6981073237739771094'], 'r') as f:
    articles_list = json.load(f)

metadata_ids = set(str(m['article_id']) for m in metadata_list)
article_ids = set(str(a['article_id']) for a in articles_list)

overlap = metadata_ids.intersection(article_ids)
print(f"Metadata Count: {len(metadata_ids)}")
print(f"Article Count (Fetched): {len(article_ids)}")
print(f"Overlap: {len(overlap)}")
print(f"Missing: {len(metadata_ids) - len(overlap)}")

# Check range of missing IDs
missing = metadata_ids - article_ids
if missing:
    missing_list = sorted([int(x) for x in missing])
    print(f"Missing IDs range: {missing_list[0]} to {missing_list[-1]}")
    print(f"Sample missing: {missing_list[:10]}")

print("__RESULT__:")
print(json.dumps({"overlap": len(overlap)}))"""

env_args = {'var_function-call-7730568976014147704': 'file_storage/function-call-7730568976014147704.json', 'var_function-call-17267860317809745023': 'file_storage/function-call-17267860317809745023.json', 'var_function-call-16112416981574014912': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6981073237739771094': 'file_storage/function-call-6981073237739771094.json', 'var_function-call-3205073669013618760': [['Africa', 106], ['South America', 92], ['Asia', 85], ['North America', 79], ['Europe', 76]], 'var_function-call-17108972308054004622': [['Africa', 117], ['South America', 111], ['Asia', 97], ['Europe', 89], ['North America', 89]], 'var_function-call-2586345171542887921': {'Business': 314, 'Sci_Tech': 243, 'Unknown': 140, 'World': 503, 'Sports': 287}}

exec(code, env_args)
