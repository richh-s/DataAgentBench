code = """import json
import os

# Load metadata
meta_var = locals()['var_function-call-2966547176505599547']
if isinstance(meta_var, str) and os.path.exists(meta_var):
    with open(meta_var, 'r') as f:
        metadata_list = json.load(f)
else:
    metadata_list = meta_var

# Get all article IDs from metadata
meta_ids = set(str(item['article_id']) for item in metadata_list)
max_meta_id = max(int(i) for i in meta_ids)

# Load articles
articles_var = locals()['var_function-call-1315168482124239170']
if isinstance(articles_var, str) and os.path.exists(articles_var):
    with open(articles_var, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = articles_var

# Get all article IDs from articles
fetched_ids = set(str(item['article_id']) for item in articles_list)

# Check coverage
missing_ids = meta_ids - fetched_ids

print("__RESULT__:")
print(json.dumps({
    "total_meta_ids": len(meta_ids),
    "max_meta_id": max_meta_id,
    "fetched_count": len(fetched_ids),
    "missing_count": len(missing_ids),
    "sample_missing": list(missing_ids)[:10]
}))"""

env_args = {'var_function-call-2966547176505599547': 'file_storage/function-call-2966547176505599547.json', 'var_function-call-17218163166465404922': {'count': 6696, 'sample_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_function-call-1597702634935355858': [{'_id': '694503fa506371ba165c4cdf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694503fa506371ba165c4ce0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694503fa506371ba165c4ce1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694503fa506371ba165c4ce2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694503fa506371ba165c4ce3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-327116729614798104': {'world_counts': {}, 'total_articles_fetched': 5, 'articles_matched_2015': 0, 'unclassified': 0}, 'var_function-call-1315168482124239170': 'file_storage/function-call-1315168482124239170.json'}

exec(code, env_args)
