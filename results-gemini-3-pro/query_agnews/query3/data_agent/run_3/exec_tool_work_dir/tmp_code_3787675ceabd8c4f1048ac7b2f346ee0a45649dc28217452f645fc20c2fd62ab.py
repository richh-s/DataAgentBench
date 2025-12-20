code = """import json
import re

# Load metadata
with open(locals()['var_function-call-7230959688738805590'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-16295593414804423020'], 'r') as f:
    articles_list = json.load(f)

articles_dict = {str(item['article_id']): item for item in articles_list}

# Minimal keyword set for debug
business_keywords = ['wall st', 'market', 'oil', 'stock']
pattern = r'\b(?:' + '|'.join(map(re.escape, business_keywords)) + r')\b'
re_business = re.compile(pattern)

debug_info = []
count = 0
for entry in metadata_list:
    aid = str(entry['article_id'])
    if aid in articles_dict:
        art = articles_dict[aid]
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        matches = re_business.findall(text)
        
        if count < 5:
            debug_info.append({
                "id": aid,
                "text": text,
                "matches": matches,
                "pattern": pattern
            })
            count += 1
        else:
            break

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7230959688738805590': 'file_storage/function-call-7230959688738805590.json', 'var_function-call-10820393096766796138': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'file_path_used': 'file_storage/function-call-7230959688738805590.json'}, 'var_function-call-1252885495403344339': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7038289333483106192': 5, 'var_function-call-15983958513975732915': ['articles'], 'var_function-call-7425021987037564653': [{'_id': '6944c26316c3efdda9fc9184', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c26316c3efdda9fc918a', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6944c26316c3efdda9fc918e', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-14402555524284394332': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-16295593414804423020': 'file_storage/function-call-16295593414804423020.json', 'var_function-call-7439365376240442064': {'counts_per_year': {}, 'total': 0, 'average': 0.0}, 'var_function-call-7434129476837696971': [{'id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'found': True}, {'id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'found': True}, {'id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'found': True}, {'id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'found': True}, {'id': '21', 'title': 'Eurozone economy keeps growing', 'found': True}], 'var_function-call-5706828954881185857': {'counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total': 0, 'average': 0.0}}

exec(code, env_args)
