code = """import json
import os

def load_data(var_value):
    if isinstance(var_value, str) and os.path.exists(var_value):
        with open(var_value, 'r') as f:
            return json.load(f)
    elif isinstance(var_value, list):
        return var_value
    return []

# Load chunks
chunk1 = load_data(locals().get('var_function-call-3180343222858944713'))
chunk2 = load_data(locals().get('var_function-call-428940154534076718'))

all_articles = chunk1 + chunk2
print(f"Total fetched: {len(all_articles)}")

# Check unique IDs
fetched_ids = set(str(a['article_id']) for a in all_articles)
print(f"Unique fetched IDs: {len(fetched_ids)}")

# Load metadata
meta_list = load_data(locals().get('var_function-call-1113576567256238630'))
meta_ids = set(str(m['article_id']) for m in meta_list)

# Missing
missing = meta_ids - fetched_ids
print(f"Missing count: {len(missing)}")

if missing:
    print(f"Sample missing: {list(missing)[:10]}")
    # Check if these missing IDs are larger than what we fetched?
    # Convert to int for comparison
    fetched_ints = [int(i) for i in fetched_ids if i.isdigit()]
    if fetched_ints:
        print(f"Fetched range: {min(fetched_ints)} - {max(fetched_ints)}")
    
    missing_ints = [int(i) for i in missing if i.isdigit()]
    if missing_ints:
        print(f"Missing range: {min(missing_ints)} - {max(missing_ints)}")"""

env_args = {'var_function-call-1113576567256238630': 'file_storage/function-call-1113576567256238630.json', 'var_function-call-4504038018777674965': 6696, 'var_function-call-12536537785643237180': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6757720913690530617': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3911136318591709052': {}, 'var_function-call-4960252981226212142': {'meta_count': 6696, 'art_count': 5, 'meta_sample_ids': ['13', '18', '26', '51', '52'], 'art_sample_ids': ['0', '1', '2', '3', '4'], 'art_sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)'], 'overlap_count': 0, 'sample_overlap': []}, 'var_function-call-11871230373173193569': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-3180343222858944713': 'file_storage/function-call-3180343222858944713.json', 'var_function-call-428940154534076718': 'file_storage/function-call-428940154534076718.json', 'var_function-call-8439387632348820906': {'top_region': 'North America', 'count': 461, 'all_counts': {'Africa': 459, 'North America': 461, 'Asia': 441, 'Europe': 441, 'South America': 436}, 'total_world_articles': 2238, 'total_joined': 5226, 'missing': 1470}}

exec(code, env_args)
