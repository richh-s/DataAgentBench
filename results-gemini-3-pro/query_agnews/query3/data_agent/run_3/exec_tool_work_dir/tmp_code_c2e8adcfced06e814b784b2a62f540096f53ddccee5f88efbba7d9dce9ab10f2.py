code = """import json
import re

# Load metadata
with open(locals()['var_function-call-7230959688738805590'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-16295593414804423020'], 'r') as f:
    articles_list = json.load(f)

articles_dict = {str(item['article_id']): item for item in articles_list}

debug_info = []

# Check first 5 matches
matches = 0
for entry in metadata_list:
    aid = str(entry['article_id'])
    if aid in articles_dict:
        art = articles_dict[aid]
        title = art.get('title', '')
        desc = art.get('description', '')
        # Re-run classification logic locally to see what happens
        # (Simplified version of logic for debug)
        text = (title + " " + description).lower() if 'description' in locals() else (title + " " + desc).lower()
        
        debug_info.append({
            "id": aid,
            "title": title,
            "found": True
        })
        matches += 1
        if matches >= 5:
            break
    else:
        # Check type mismatch
        debug_info.append({"id": aid, "found": False, "type_in_meta": str(type(entry['article_id']))})
        if len(debug_info) > 5: break

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7230959688738805590': 'file_storage/function-call-7230959688738805590.json', 'var_function-call-10820393096766796138': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'file_path_used': 'file_storage/function-call-7230959688738805590.json'}, 'var_function-call-1252885495403344339': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7038289333483106192': 5, 'var_function-call-15983958513975732915': ['articles'], 'var_function-call-7425021987037564653': [{'_id': '6944c26316c3efdda9fc9184', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c26316c3efdda9fc918a', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6944c26316c3efdda9fc918e', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-14402555524284394332': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-16295593414804423020': 'file_storage/function-call-16295593414804423020.json', 'var_function-call-7439365376240442064': {'counts_per_year': {}, 'total': 0, 'average': 0.0}}

exec(code, env_args)
