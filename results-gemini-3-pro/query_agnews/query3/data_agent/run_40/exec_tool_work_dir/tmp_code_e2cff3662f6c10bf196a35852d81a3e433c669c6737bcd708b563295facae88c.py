code = """import json

# Load metadata
with open(locals()['var_function-call-13727892763181911756'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
articles_list = locals()['var_function-call-6622063249663007819']

meta_ids = set(str(item['article_id']) for item in metadata_list)
article_ids = set(str(item['article_id']) for item in articles_list)

intersection = meta_ids.intersection(article_ids)

print("__RESULT__:")
print(json.dumps({
    "meta_count": len(meta_ids),
    "articles_count": len(article_ids),
    "intersection_count": len(intersection),
    "sample_meta_id": list(meta_ids)[0] if meta_ids else None,
    "sample_article_id": list(article_ids)[0] if article_ids else None
}))"""

env_args = {'var_function-call-13727892763181911756': 'file_storage/function-call-13727892763181911756.json', 'var_function-call-14710500662845567092': 'file_storage/function-call-14710500662845567092.json', 'var_function-call-1777077423156184413': 14860, 'var_function-call-6622063249663007819': [{'_id': '6944e1bb7940ea7e4567e403', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e1bb7940ea7e4567e404', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e1bb7940ea7e4567e405', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e1bb7940ea7e4567e406', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e1bb7940ea7e4567e407', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15317023739032041550': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'average': 0.0, 'total_business_found': 0}}

exec(code, env_args)
