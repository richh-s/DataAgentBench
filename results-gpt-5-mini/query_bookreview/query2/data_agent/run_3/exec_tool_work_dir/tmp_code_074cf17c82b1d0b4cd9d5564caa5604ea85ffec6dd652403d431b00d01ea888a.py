code = """import json
from pathlib import Path

# Load previous tool results
purchase_avg = var_call_jUjNxyHyHiTOxmVCxeWO5Zlq
books_json_path = var_call_he4GeOzFNhdoBfpZPxkmX09E

# Load full books_info result from file
with open(books_json_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create mapping from book_id to record
book_map = {b['book_id']: b for b in books}

# Map purchase_ids with avg 5.0 to book_ids
candidates = []
for rec in purchase_avg:
    pid = rec['purchase_id']
    bid = pid.replace('purchaseid_', 'bookid_')
    book = book_map.get(bid)
    if book:
        # check if categories contains 'Literature & Fiction'
        cats = book.get('categories') or ''
        if 'Literature & Fiction' in cats:
            candidates.append({'purchase_id': pid, 'book_id': bid, 'title': book.get('title'), 'categories': cats, 'description': book.get('description')})

# Prepare result
result = candidates

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HIynoCPl3mjS56Wt8eNERAuq': ['review'], 'var_call_jUjNxyHyHiTOxmVCxeWO5Zlq': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'cnt': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'cnt': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'cnt': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'cnt': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'cnt': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'cnt': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'cnt': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'cnt': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'cnt': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'cnt': '1'}], 'var_call_3am25sAshAASlMi3iFumC8aY': ['books_info'], 'var_call_he4GeOzFNhdoBfpZPxkmX09E': 'file_storage/call_he4GeOzFNhdoBfpZPxkmX09E.json'}

exec(code, env_args)
