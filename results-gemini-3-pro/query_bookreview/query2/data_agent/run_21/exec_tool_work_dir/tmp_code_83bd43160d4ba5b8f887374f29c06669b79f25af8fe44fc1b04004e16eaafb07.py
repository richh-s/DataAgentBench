code = """import json
import pandas as pd

# Load books data
file_path = locals()['var_function-call-8197625269191316784']
with open(file_path, 'r') as f:
    books_data = json.load(f)

# Load reviews data
reviews_data = locals()['var_function-call-8413620125965824253']

# Normalize IDs
# pattern seems to be prefix_ID
# book_id: bookid_X
# purchase_id: purchaseid_X

perfect_rating_ids = set()
for item in reviews_data:
    pid = item['purchase_id']
    if '_' in pid:
        suffix = pid.split('_')[1]
        perfect_rating_ids.add(suffix)

matching_books = []
for book in books_data:
    bid = book['book_id']
    if '_' in bid:
        suffix = bid.split('_')[1]
        if suffix in perfect_rating_ids:
            matching_books.append(book['title'])

print("__RESULT__:")
print(json.dumps(matching_books))"""

env_args = {'var_function-call-8197625269191316784': 'file_storage/function-call-8197625269191316784.json', 'var_function-call-9165940783062567952': ['review'], 'var_function-call-8413620125965824253': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0'}]}

exec(code, env_args)
