code = """import json

path_meta = locals()['var_function-call-4524539130792533253']
path_articles = locals()['var_function-call-17275925162365337320']

with open(path_meta, 'r') as f:
    meta_list = json.load(f)
meta_ids = set(str(item['article_id']) for item in meta_list)

with open(path_articles, 'r') as f:
    articles_list = json.load(f)

# Check overlap
mongo_ids = set(str(art['article_id']) for art in articles_list)
overlap = meta_ids.intersection(mongo_ids)

print("__RESULT__:")
print(json.dumps({
    "meta_count": len(meta_ids),
    "mongo_count": len(mongo_ids),
    "overlap_count": len(overlap),
    "sample_meta_id": list(meta_ids)[0] if meta_ids else None,
    "sample_mongo_id": list(mongo_ids)[0] if mongo_ids else None,
    "sample_overlap": list(overlap)[:5] if overlap else []
}))"""

env_args = {'var_function-call-4524539130792533253': 'file_storage/function-call-4524539130792533253.json', 'var_function-call-12841960327215520545': 'file_storage/function-call-12841960327215520545.json', 'var_function-call-17275925162365337320': [{'_id': '6944ea9ed4512ac83e64878c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ea9ed4512ac83e64878d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ea9ed4512ac83e64878e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ea9ed4512ac83e64878f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ea9ed4512ac83e648790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-845048519728556146': {'top_region': 'None', 'count': 0, 'all_counts': {}}}

exec(code, env_args)
