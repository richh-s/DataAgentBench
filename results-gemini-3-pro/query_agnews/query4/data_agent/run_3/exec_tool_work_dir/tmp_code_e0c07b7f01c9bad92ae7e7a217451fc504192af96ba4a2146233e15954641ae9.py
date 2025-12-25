code = """import json

with open(locals()['var_function-call-7730568976014147704'], 'r') as f:
    metadata_list = json.load(f)

ids = [int(m['article_id']) for m in metadata_list]
print(f"Metadata ID Range: {min(ids)} - {max(ids)}")

with open(locals()['var_function-call-6981073237739771094'], 'r') as f:
    articles_list = json.load(f)

fetched_ids = [int(a['article_id']) for a in articles_list if 'article_id' in a]
if fetched_ids:
    print(f"Fetched ID Range: {min(fetched_ids)} - {max(fetched_ids)}")
else:
    print("No IDs in fetched articles?")

print("__RESULT__:")
print(json.dumps({"max_meta": max(ids), "max_fetched": max(fetched_ids) if fetched_ids else 0}))"""

env_args = {'var_function-call-7730568976014147704': 'file_storage/function-call-7730568976014147704.json', 'var_function-call-17267860317809745023': 'file_storage/function-call-17267860317809745023.json', 'var_function-call-16112416981574014912': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6981073237739771094': 'file_storage/function-call-6981073237739771094.json', 'var_function-call-3205073669013618760': [['Africa', 106], ['South America', 92], ['Asia', 85], ['North America', 79], ['Europe', 76]], 'var_function-call-17108972308054004622': [['Africa', 117], ['South America', 111], ['Asia', 97], ['Europe', 89], ['North America', 89]], 'var_function-call-2586345171542887921': {'Business': 314, 'Sci_Tech': 243, 'Unknown': 140, 'World': 503, 'Sports': 287}, 'var_function-call-1992657977849178575': {'overlap': 1487}}

exec(code, env_args)
