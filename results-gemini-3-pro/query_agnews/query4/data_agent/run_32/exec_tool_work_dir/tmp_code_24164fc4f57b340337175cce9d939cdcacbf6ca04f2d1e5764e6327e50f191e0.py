code = """import json

# Load metadata
with open(locals()['var_function-call-5900547977647289407'], 'r') as f:
    metadata_list = json.load(f)
metadata_ids = set(str(item['article_id']) for item in metadata_list)

# Load articles
content_list = locals()['var_function-call-11413350339637926914']
content_ids = set(str(item['article_id']) for item in content_list)

# Intersection
common_ids = metadata_ids.intersection(content_ids)
print(f"Metadata IDs count: {len(metadata_ids)}")
print(f"Content IDs count: {len(content_ids)}")
print(f"Common IDs count: {len(common_ids)}")

if len(common_ids) == 0:
    print("No common IDs found! Checking samples...")
    print(f"Sample Meta: {list(metadata_ids)[:5]}")
    print(f"Sample Content: {list(content_ids)[:5]}")
else:
    # Try classification on a sample
    sample_id = list(common_ids)[0]
    sample_article = next(a for a in content_list if str(a['article_id']) == sample_id)
    text = (sample_article.get('title', '') + " " + sample_article.get('description', '')).lower()
    print(f"Sample Text: {text}")
    
    # Check keywords simple
    keywords = ["world", "war", "china", "europe", "business", "stock"]
    found = [k for k in keywords if k in text]
    print(f"Found keywords: {found}")

print("__RESULT__:")
print(json.dumps({"common": len(common_ids)}))"""

env_args = {'var_function-call-5900547977647289407': 'file_storage/function-call-5900547977647289407.json', 'var_function-call-8253439238580865499': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52]}, 'var_function-call-11413350339637926914': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6748392322076207893': {'counts': {}, 'debug': []}}

exec(code, env_args)
