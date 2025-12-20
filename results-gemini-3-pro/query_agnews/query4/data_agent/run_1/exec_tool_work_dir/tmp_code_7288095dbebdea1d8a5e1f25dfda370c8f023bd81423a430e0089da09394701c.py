code = """import json
import re

with open(locals()['var_function-call-6414145257666997456'], 'r') as f:
    metadata_list = json.load(f)

with open(locals()['var_function-call-490337090254977264'], 'r') as f:
    articles_list = json.load(f)

articles_map = {int(a['article_id']): a for a in articles_list}

meta_ids = set(int(m['article_id']) for m in metadata_list)
art_ids = set(articles_map.keys())
common_ids = sorted(list(meta_ids.intersection(art_ids)))

debug_info = {
    "meta_count": len(meta_ids),
    "art_count": len(art_ids),
    "common_count": len(common_ids),
    "samples": []
}

# Check a few samples
for aid in common_ids[:5]:
    art = articles_map[aid]
    debug_info["samples"].append({
        "id": aid,
        "title": art['title'],
        "desc": art['description']
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6414145257666997456': 'file_storage/function-call-6414145257666997456.json', 'var_function-call-17387279326264468321': 'file_storage/function-call-17387279326264468321.json', 'var_function-call-10428291813963926827': 6696, 'var_function-call-4939086114809291303': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13401999490339433067': 5, 'var_function-call-2594177708310146329': ['articles'], 'var_function-call-1080993007468921455': [{'_id': '6944e918a831038495320111', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-490337090254977264': 'file_storage/function-call-490337090254977264.json', 'var_function-call-13608484779050026561': {}, 'var_function-call-7396373676834293089': 'Debug done'}

exec(code, env_args)
