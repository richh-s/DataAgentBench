code = """import json
import re

# Load metadata
with open(locals()['var_function-call-6478820518397450019'], 'r') as f:
    metadata_list = json.load(f)
metadata_ids = set(str(item['article_id']) for item in metadata_list)

# Load articles
with open(locals()['var_function-call-8772719174433401329'], 'r') as f:
    articles_list = json.load(f)
articles_map = {str(item['article_id']): item for item in articles_list}
articles_ids = set(articles_map.keys())

intersection = metadata_ids.intersection(articles_ids)

print("__RESULT__:")
debug_info = {
    "metadata_count": len(metadata_ids),
    "articles_count": len(articles_ids),
    "intersection_count": len(intersection),
    "sample_intersection": list(intersection)[:5] if intersection else []
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-9850316120653619328': ['authors', 'article_metadata'], 'var_function-call-9850316120653621663': ['articles'], 'var_function-call-6478820518397450019': 'file_storage/function-call-6478820518397450019.json', 'var_function-call-83190611252947939': 6696, 'var_function-call-1618363836141742396': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8772719174433401329': 'file_storage/function-call-8772719174433401329.json', 'var_function-call-17003818754982913757': {}}

exec(code, env_args)
