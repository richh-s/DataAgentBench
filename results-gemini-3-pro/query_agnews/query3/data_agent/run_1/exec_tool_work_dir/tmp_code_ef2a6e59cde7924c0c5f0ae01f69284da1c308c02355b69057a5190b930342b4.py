code = """import json
import re

with open(locals()['var_function-call-16473785254101418274'], 'r') as f:
    meta = json.load(f)
articles = locals()['var_function-call-16666979674709341157']

articles_map = {str(a['article_id']): a for a in articles}
meta_ids = set(str(m['article_id']) for m in meta)
article_ids = set(articles_map.keys())
common = list(meta_ids.intersection(article_ids))

debug_info = {
    "meta_count": len(meta),
    "articles_count": len(articles),
    "common_count": len(common),
    "samples": []
}

# Check a few samples
for aid in common[:5]:
    art = articles_map[aid]
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    tokens = re.findall(r'[a-z]+', text)
    debug_info['samples'].append({"id": aid, "text": text, "tokens": tokens[:10]})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16473785254101418274': 'file_storage/function-call-16473785254101418274.json', 'var_function-call-5763965642417162801': 14860, 'var_function-call-16666979674709341157': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8695913703810418745': 0.0, 'var_function-call-10400349986440466755': 'debug done'}

exec(code, env_args)
