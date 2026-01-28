code = """import json
import ast

# Load review aggregation results from storage variable
reviews = var_call_9TcUExwekZilcVnnzVQ1e5K8

# Load books results from JSON file path stored in var_call_rFl6Eu6XwAYljh4XyxKhXtQu
books_file_path = var_call_rFl6Eu6XwAYljh4XyxKhXtQu
with open(books_file_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Build mapping from numeric id to book entry
book_map = {}
for b in books:
    bid = b.get('book_id')
    if not bid:
        continue
    # extract numeric suffix after last underscore
    parts = bid.split('_')
    num = parts[-1]
    book_map[num] = b

# Target category
target = "Children's Books"

results = []
for r in reviews:
    purchase_id = r.get('purchase_id')
    if not purchase_id:
        continue
    parts = purchase_id.split('_')
    num = parts[-1]
    book = book_map.get(num)
    if not book:
        continue
    # parse categories string
    cats_str = book.get('categories')
    cats = []
    if cats_str:
        try:
            cats = ast.literal_eval(cats_str)
        except Exception:
            # fallback: try json
            try:
                cats = json.loads(cats_str)
            except Exception:
                cats = []
    # Check membership
    if target in cats:
        # convert avg_rating and review_count to numeric
        try:
            avg_rating = float(r.get('avg_rating'))
        except Exception:
            avg_rating = None
        try:
            review_count = int(r.get('review_count'))
        except Exception:
            review_count = None
        results.append({
            'title': book.get('title'),
            'book_id': book.get('book_id'),
            'purchase_id': purchase_id,
            'avg_rating': avg_rating,
            'review_count': review_count,
            'categories': cats
        })

# Sort results by avg_rating desc, then review_count desc
results.sort(key=lambda x: ((x['avg_rating'] if x['avg_rating'] is not None else 0), x['review_count'] if x['review_count'] is not None else 0), reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_qFdV1HnA5oes28CyJKs23J9N': ['review'], 'var_call_qc6INQOj3H9PUaRRjD2E3wi0': ['books_info'], 'var_call_9TcUExwekZilcVnnzVQ1e5K8': [{'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}], 'var_call_rFl6Eu6XwAYljh4XyxKhXtQu': 'file_storage/call_rFl6Eu6XwAYljh4XyxKhXtQu.json'}

exec(code, env_args)
