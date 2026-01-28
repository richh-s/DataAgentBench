code = """import json
import pandas as pd

# Load review aggregation results from storage
reviews = var_call_sArzEfEjkJDSWoo1ytWvHK7b

# Load books_info full result from the JSON file path stored in var_call_HNUI5sZKYpC9NEbPgDtsSybo
books_file_path = var_call_HNUI5sZKYpC9NEbPgDtsSybo
with open(books_file_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Build set of book_ids that have perfect average rating 5.0 by mapping purchaseid_X to bookid_X
book_ids_with_5 = set()
for r in reviews:
    pid = r.get('purchase_id', '')
    if '_' in pid:
        suffix = pid.split('_', 1)[1]
        mapped = 'bookid_' + suffix
    else:
        # fallback
        mapped = pid.replace('purchaseid', 'bookid')
    book_ids_with_5.add(mapped)

# Filter books for category contains 'Literature & Fiction' and details mention English (case-insensitive)
matches = []
for b in books:
    bid = b.get('book_id', '')
    if bid not in book_ids_with_5:
        continue
    categories = b.get('categories', '') or ''
    details = b.get('details', '') or ''
    if 'Literature & Fiction' in categories and 'english' in details.lower():
        matches.append({
            'book_id': bid,
            'title': b.get('title'),
            'categories': categories,
            'details': details,
            'rating_number': b.get('rating_number')
        })

# Prepare JSON-serializable string output
output = json.dumps(matches)

print("__RESULT__:")
print(output)"""

env_args = {'var_call_CrNQq72lqNEUqerz03rdmLmz': ['review'], 'var_call_sArzEfEjkJDSWoo1ytWvHK7b': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'num_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'num_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'num_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'num_reviews': '1'}], 'var_call_PNHw7dhMHAEYLL9K39Ahevgb': ['books_info'], 'var_call_HNUI5sZKYpC9NEbPgDtsSybo': 'file_storage/call_HNUI5sZKYpC9NEbPgDtsSybo.json'}

exec(code, env_args)
