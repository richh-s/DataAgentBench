code = """import json
import os

def load_data(var_value):
    if isinstance(var_value, str) and os.path.exists(var_value):
        with open(var_value, 'r') as f:
            return json.load(f)
    elif isinstance(var_value, list):
        return var_value
    return []

meta_var = locals().get('var_function-call-1113576567256238630')
metadata_list = load_data(meta_var)

articles_var = locals().get('var_function-call-6757720913690530617')
articles_list = load_data(articles_var)

debug_info = {
    "meta_count": len(metadata_list),
    "art_count": len(articles_list),
    "meta_sample_ids": [m['article_id'] for m in metadata_list[:5]],
    "art_sample_ids": [a['article_id'] for a in articles_list[:5]],
    "art_sample_titles": [a.get('title') for a in articles_list[:5]]
}

# Check overlap
meta_ids = set(str(m['article_id']) for m in metadata_list)
art_ids = set(str(a['article_id']) for a in articles_list)
overlap = meta_ids.intersection(art_ids)
debug_info["overlap_count"] = len(overlap)
debug_info["sample_overlap"] = list(overlap)[:5]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1113576567256238630': 'file_storage/function-call-1113576567256238630.json', 'var_function-call-4504038018777674965': 6696, 'var_function-call-12536537785643237180': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6757720913690530617': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3911136318591709052': {}}

exec(code, env_args)
