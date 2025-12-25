code = """import json
import pandas as pd
import re

# Extract numeric part from perfect_rating_purchase_ids
perfect_rating_purchase_ids_raw = locals()['var_function-call-12715643371615181665']
perfect_rating_numeric_ids = set()
for pid in perfect_rating_purchase_ids_raw:
    match = re.search(r'\d+', pid)
    if match:
        perfect_rating_numeric_ids.add(int(match.group(0)))

# Load books data
books_data = pd.read_json(locals()['var_function-call-7197307457514771804'])

matching_books = []

for index, row in books_data.iterrows():
    categories_str = str(row['categories'])
    details_str = str(row['details'])
    book_id_raw = str(row['book_id'])

    # Extract numeric part from book_id
    book_id_match = re.search(r'\d+', book_id_raw)
    if book_id_match:
        book_numeric_id = int(book_id_match.group(0))
    else:
        book_numeric_id = None

    # Check all conditions
    if 'Literature & Fiction' in categories_str and \
       ('English' in details_str or 'english' in details_str) and \
       book_numeric_id is not None and \
       book_numeric_id in perfect_rating_numeric_ids:
        matching_books.append(row.to_dict())

result_titles = [book['title'] for book in matching_books]

print('__RESULT__:')
print(json.dumps(result_titles))"""

env_args = {'var_function-call-8798033520098159115': ['review'], 'var_function-call-4956483226493947139': [{'purchase_id': 'purchaseid_101', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_105', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_108', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_110', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_114', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_116', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_117', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_118', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_12', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_121', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_122', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_123', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_124', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_126', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_127', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_128', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_130', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_132', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_133', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_134', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_14', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_143', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_144', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_146', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_150', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_151', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_152', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_153', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_156', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_16', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_160', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_163', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_166', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_168', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_170', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_171', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_172', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_174', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_177', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_180', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_181', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_182', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_184', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_192', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_195', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_197', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_2', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_21', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_24', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_26', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_28', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_29', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_33', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_34', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_38', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_39', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_40', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_41', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_42', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_47', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_54', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_56', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_57', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_59', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_6', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_60', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_64', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_7', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_71', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_73', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_74', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_75', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_79', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_80', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_82', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_83', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_84', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_88', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_9', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_90', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_91', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_97', 'average_rating': '5.0'}, {'purchase_id': 'purchaseid_98', 'average_rating': '5.0'}], 'var_function-call-12715643371615181665': ['purchaseid_101', 'purchaseid_105', 'purchaseid_108', 'purchaseid_110', 'purchaseid_114', 'purchaseid_116', 'purchaseid_117', 'purchaseid_118', 'purchaseid_12', 'purchaseid_121', 'purchaseid_122', 'purchaseid_123', 'purchaseid_124', 'purchaseid_126', 'purchaseid_127', 'purchaseid_128', 'purchaseid_130', 'purchaseid_132', 'purchaseid_133', 'purchaseid_134', 'purchaseid_14', 'purchaseid_143', 'purchaseid_144', 'purchaseid_146', 'purchaseid_150', 'purchaseid_151', 'purchaseid_152', 'purchaseid_153', 'purchaseid_156', 'purchaseid_16', 'purchaseid_160', 'purchaseid_163', 'purchaseid_166', 'purchaseid_168', 'purchaseid_170', 'purchaseid_171', 'purchaseid_172', 'purchaseid_174', 'purchaseid_177', 'purchaseid_180', 'purchaseid_181', 'purchaseid_182', 'purchaseid_184', 'purchaseid_192', 'purchaseid_195', 'purchaseid_197', 'purchaseid_2', 'purchaseid_21', 'purchaseid_24', 'purchaseid_26', 'purchaseid_28', 'purchaseid_29', 'purchaseid_33', 'purchaseid_34', 'purchaseid_38', 'purchaseid_39', 'purchaseid_40', 'purchaseid_41', 'purchaseid_42', 'purchaseid_47', 'purchaseid_54', 'purchaseid_56', 'purchaseid_57', 'purchaseid_59', 'purchaseid_6', 'purchaseid_60', 'purchaseid_64', 'purchaseid_7', 'purchaseid_71', 'purchaseid_73', 'purchaseid_74', 'purchaseid_75', 'purchaseid_79', 'purchaseid_80', 'purchaseid_82', 'purchaseid_83', 'purchaseid_84', 'purchaseid_88', 'purchaseid_9', 'purchaseid_90', 'purchaseid_91', 'purchaseid_97', 'purchaseid_98'], 'var_function-call-2268683401667932018': [], 'var_function-call-7197307457514771804': 'file_storage/function-call-7197307457514771804.json', 'var_function-call-2332349317433107444': [], 'var_function-call-9768360895412800474': []}

exec(code, env_args)
