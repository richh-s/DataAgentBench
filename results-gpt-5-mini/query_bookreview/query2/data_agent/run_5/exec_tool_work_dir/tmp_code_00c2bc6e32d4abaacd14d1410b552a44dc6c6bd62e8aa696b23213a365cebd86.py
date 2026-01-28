code = """import json
import pandas as pd

# Load review aggregation results
reviews = var_call_XudvoX6a8lXqrg6mvBPFv4cr

# Load books results (this variable is a filepath to a .json when large)
books_path = var_call_cWgfsG8CaxSsSQ35xiJksa1y
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Normalize review mapping: map purchase_id -> count and average
review_map = {}
for r in reviews:
    pid = r.get('purchase_id')
    # convert avg_rating and cnt to numeric
    try:
        avg = float(r.get('avg_rating'))
    except:
        avg = None
    try:
        cnt = int(r.get('cnt'))
    except:
        cnt = None
    review_map[pid] = {'avg_rating': avg, 'cnt': cnt}

# Build possible mapping from purchase_id to book_id
mapped_book_ids = {}
for pid in review_map.keys():
    bid = None
    if pid.startswith('purchaseid_'):
        bid = 'bookid_' + pid.split('purchaseid_')[-1]
    elif pid.startswith('purchase_'):
        bid = 'book_' + pid.split('purchase_')[-1]
    else:
        # generic replace
        bid = pid.replace('purchase', 'book')
    mapped_book_ids[pid] = bid

# Index books by book_id
books_index = {b.get('book_id'): b for b in books}

# Find matches where mapped book id exists in books_index
results = []
for pid, bid in mapped_book_ids.items():
    if bid in books_index:
        b = books_index[bid]
        # Confirm category contains Literature & Fiction
        cats = b.get('categories') or ''
        details = b.get('details') or ''
        if 'Literature & Fiction' in cats:
            entry = {
                'book_id': b.get('book_id'),
                'title': b.get('title'),
                'author': b.get('author'),
                'categories': b.get('categories'),
                'details': b.get('details'),
                'rating_number': int(b.get('rating_number')) if b.get('rating_number') and str(b.get('rating_number')).isdigit() else b.get('rating_number'),
                'avg_rating': review_map[pid]['avg_rating'],
                'review_count_in_reviews_table': review_map[pid]['cnt']
            }
            results.append(entry)

# Also check for any books in the books list that have book_id matching any purchaseid without mapping
# (redundant but safe)
purchase_ids = set(review_map.keys())
for b in books:
    bid = b.get('book_id')
    # derive corresponding purchase id
    possible_pid = None
    if bid and bid.startswith('bookid_'):
        possible_pid = 'purchaseid_' + bid.split('bookid_')[-1]
    elif bid and bid.startswith('book_'):
        possible_pid = 'purchase_' + bid.split('book_')[-1]
    if possible_pid and possible_pid in review_map:
        # ensure not already included
        if not any(r['book_id']==bid for r in results):
            entry = {
                'book_id': bid,
                'title': b.get('title'),
                'author': b.get('author'),
                'categories': b.get('categories'),
                'details': b.get('details'),
                'rating_number': int(b.get('rating_number')) if b.get('rating_number') and str(b.get('rating_number')).isdigit() else b.get('rating_number'),
                'avg_rating': review_map[possible_pid]['avg_rating'],
                'review_count_in_reviews_table': review_map[possible_pid]['cnt']
            }
            results.append(entry)

# Sort results by title
results_sorted = sorted(results, key=lambda x: (x.get('title') or '').lower())

# Output JSON string
out = json.dumps(results_sorted)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zLMXTL5hYJbV9CwLXlEaegIp': ['review'], 'var_call_XudvoX6a8lXqrg6mvBPFv4cr': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'cnt': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'cnt': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'cnt': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'cnt': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'cnt': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'cnt': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'cnt': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'cnt': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'cnt': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'cnt': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'cnt': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'cnt': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'cnt': '1'}], 'var_call_YY7V2g6HbdYf5WOY5kB6nQDa': ['books_info'], 'var_call_cWgfsG8CaxSsSQ35xiJksa1y': 'file_storage/call_cWgfsG8CaxSsSQ35xiJksa1y.json'}

exec(code, env_args)
