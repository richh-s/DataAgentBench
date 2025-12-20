code = """import json
import os

# Load filtered metadata
meta_var = locals()['var_function-call-5517223453251049220']
if isinstance(meta_var, str) and os.path.exists(meta_var):
    with open(meta_var, 'r') as f:
        metadata_list = json.load(f)
else:
    metadata_list = meta_var

# Load articles
articles_var = locals()['var_function-call-3456426640295154631']
if isinstance(articles_var, str) and os.path.exists(articles_var):
    with open(articles_var, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = articles_var

# Check lengths
meta_ids = set(str(m['article_id']) for m in metadata_list)
art_ids = set(str(a['article_id']) for a in articles_list)

intersection = meta_ids.intersection(art_ids)

print("__RESULT__:")
print(json.dumps({
    "metadata_count": len(metadata_list),
    "articles_fetched_count": len(articles_list),
    "intersection_count": len(intersection),
    "sample_meta_id": list(meta_ids)[0] if meta_ids else "None",
    "sample_art_id": list(art_ids)[0] if art_ids else "None"
}))"""

env_args = {'var_function-call-5517223453251049220': 'file_storage/function-call-5517223453251049220.json', 'var_function-call-10913154760749403926': 'file_storage/function-call-10913154760749403926.json', 'var_function-call-2633958125002449470': [{'_id': '6944cee63429fba040671429', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cee63429fba04067142a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cee63429fba04067142b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cee63429fba04067142c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cee63429fba04067142d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14966595658088174430': [{'_id': '6944cee63429fba040671429', 'article_id': '0'}], 'var_function-call-3456426640295154631': [{'_id': '6944cee63429fba040671429', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cee63429fba04067142a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cee63429fba04067142b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cee63429fba04067142c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cee63429fba04067142d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10445686298075355025': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'average': 0.0}}

exec(code, env_args)
