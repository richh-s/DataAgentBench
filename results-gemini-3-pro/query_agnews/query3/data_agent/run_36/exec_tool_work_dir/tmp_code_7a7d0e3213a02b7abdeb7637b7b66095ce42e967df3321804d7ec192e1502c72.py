code = """import json

def load_data(data_var):
    if isinstance(data_var, str):
        with open(data_var, 'r') as f:
            return json.load(f)
    elif isinstance(data_var, list):
        return data_var
    else:
        return []

meta_list = load_data(locals()['var_function-call-14838360778106258720'])
articles_list = load_data(locals()['var_function-call-1633174315725084248'])

meta_ids = set(str(m['article_id']) for m in meta_list)
article_ids = set(str(a['article_id']) for a in articles_list)

intersection = meta_ids.intersection(article_ids)

print("__RESULT__:")
print(json.dumps({
    "meta_count": len(meta_list),
    "articles_count": len(articles_list),
    "intersection_count": len(intersection),
    "sample_meta_ids": list(meta_ids)[:5],
    "sample_article_ids": list(article_ids)[:5]
}))"""

env_args = {'var_function-call-14838360778106258720': 'file_storage/function-call-14838360778106258720.json', 'var_function-call-10623188398356643492': {'count': 14860, 'sample_ids': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63']}, 'var_function-call-1633174315725084248': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11527900083983285698': {'average': 0.09090909090909091, 'counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}}}

exec(code, env_args)
