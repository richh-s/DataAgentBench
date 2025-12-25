code = """import json
import re

# Load metadata
with open(locals()['var_function-call-16473785254101418274'], 'r') as f:
    meta = json.load(f)

# Load articles
articles = locals()['var_function-call-16666979674709341157']

articles_map = {str(a['article_id']): a for a in articles}

print(f"Meta sample: {meta[:3]}")
print(f"Article sample: {articles[:3]}")

# Check intersection
meta_ids = set(str(m['article_id']) for m in meta)
article_ids = set(articles_map.keys())
common = meta_ids.intersection(article_ids)
print(f"Common IDs count: {len(common)}")

# Check classification on a sample common ID
if common:
    sample_id = list(common)[0]
    art = articles_map[sample_id]
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    print(f"Sample Text ({sample_id}): {text}")
    
    # Keywords (subset for test)
    business_keywords = {'market', 'oil', 'stocks', 'economy', 'business', 'company'}
    world_keywords = {'war', 'iraq', 'president'}
    
    tokens = re.findall(r'[a-z]+', text)
    print(f"Tokens: {tokens}")
    
    scores = {'Business': 0, 'World': 0}
    for t in tokens:
        if t in business_keywords: scores['Business'] += 1
        if t in world_keywords: scores['World'] += 1
    print(f"Scores: {scores}")

print("__RESULT__:")
print(json.dumps("debug done"))"""

env_args = {'var_function-call-16473785254101418274': 'file_storage/function-call-16473785254101418274.json', 'var_function-call-5763965642417162801': 14860, 'var_function-call-16666979674709341157': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8695913703810418745': 0.0}

exec(code, env_args)
