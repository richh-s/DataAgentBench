code = """import json

with open('id_chunks.json', 'r') as f:
    chunks = json.load(f)

query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": chunks[0]}
    }
}
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-12051989784931741793': ['authors', 'article_metadata'], 'var_function-call-8881788724553702350': 'file_storage/function-call-8881788724553702350.json', 'var_function-call-15834934156015708964': 'file_storage/function-call-15834934156015708964.json', 'var_function-call-241652876630569464': 14860, 'var_function-call-13057485116789306292': [{'_id': '6944d765bc50274a4486b1ca', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d765bc50274a4486b1cb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d765bc50274a4486b1cc', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d765bc50274a4486b1cd', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d765bc50274a4486b1ce', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3033909346262757513': 127583, 'var_function-call-16449323081972518628': 3}

exec(code, env_args)
