code = """import json
import re

# Load Metadata (from file)
with open(locals()['var_function-call-12102332063729111063'], 'r') as f:
    metadata_raw = json.load(f)

# Load Articles (direct list)
articles_raw = locals()['var_function-call-1165826486750854528']
articles_dict = {str(a['article_id']): (a.get('title', '') + ' ' + a.get('description', '')) for a in articles_raw}

# Debug
print(f"Metadata Count: {len(metadata_raw)}")
print(f"Articles Count: {len(articles_raw)}")
print(f"Sample Metadata IDs: {[str(m['article_id']) for m in metadata_raw[:5]]}")
print(f"Sample Article IDs: {list(articles_dict.keys())[:5]}")

matches = 0
sample_classifications = []
for item in metadata_raw[:100]:
    aid = str(item['article_id'])
    if aid in articles_dict:
        matches += 1
        content = articles_dict[aid]
        # Basic check
        if matches <= 5:
            print(f"Match: ID={aid}, Content={content[:50]}...")
    else:
        if matches <= 5:
             print(f"No Match: ID={aid}")

print(f"Total Matches found in first 100: {matches}")

# Check content of ID '3' specifically (it was in the preview)
if '3' in articles_dict:
    print(f"ID 3 Content: {articles_dict['3']}")
else:
    print("ID 3 not in articles_dict")

print("__RESULT__:")
print(json.dumps("DEBUG"))"""

env_args = {'var_function-call-12102332063729111063': 'file_storage/function-call-12102332063729111063.json', 'var_function-call-14273295165118230531': 'file_storage/function-call-14273295165118230531.json', 'var_function-call-8294512119571345844': 14860, 'var_function-call-8320919013075805354': [{'_id': '6944dc1fe2449a6347cdc96b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dc1fe2449a6347cdc96c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dc1fe2449a6347cdc96d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dc1fe2449a6347cdc96e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dc1fe2449a6347cdc96f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1165826486750854528': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5823775745708014049': 0.09090909090909091}

exec(code, env_args)
