code = """import json
from collections import Counter
meta_path = var_call_uhQeRuiHYv64OeMnsHMjVwST
with open(meta_path, 'r') as f:
    meta2015 = json.load(f)
articles = var_call_YaNxlXQuU2itwNfMIHtzuSc6

# build article id mapping
article_text = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid] = (title + ' ' + desc).lower()

matched = 0
missing_ids = []
for rec in meta2015:
    try:
        aid = int(rec.get('article_id'))
    except:
        continue
    if aid in article_text:
        matched += 1
    else:
        missing_ids.append(aid)

sample_missing = missing_ids[:20]

res = {'meta_records': len(meta2015), 'articles_in_db': len(articles), 'matched_meta_with_article_text': matched, 'missing_sample': sample_missing}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_uhQeRuiHYv64OeMnsHMjVwST': 'file_storage/call_uhQeRuiHYv64OeMnsHMjVwST.json', 'var_call_pmlog0QfCdhKZYQG6i1DJQ6o': 'file_storage/call_pmlog0QfCdhKZYQG6i1DJQ6o.json', 'var_call_YaNxlXQuU2itwNfMIHtzuSc6': [{'_id': '6959aaa5dd937f5045d1ed74', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959aaa5dd937f5045d1ed75', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959aaa5dd937f5045d1ed76', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959aaa5dd937f5045d1ed77', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959aaa5dd937f5045d1ed78', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_fjHhFEFODe3klzs2YmwVJBXb': {'region': None, 'count': 0}}

exec(code, env_args)
