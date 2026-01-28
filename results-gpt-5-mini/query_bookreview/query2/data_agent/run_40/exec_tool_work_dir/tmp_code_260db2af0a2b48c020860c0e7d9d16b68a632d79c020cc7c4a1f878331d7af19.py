code = """import json
import pandas as pd

# Access stored variables from previous tool calls
reviews = var_call_BUKR4TBVVWNfEWibrJuuEfOy  # list of dicts with purchase_id, avg_rating, n_reviews
books_file = var_call_6EyguY6JML38gQxKWg2ouQNy  # path to JSON file with books_info rows (LIMIT 200)

# Load books data
with open(books_file, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Build a map from book_id to book record for quick lookup
book_map = {b.get('book_id'): b for b in books}

results = []
for r in reviews:
    purchase_id = r.get('purchase_id')
    if not purchase_id:
        continue
    # map purchaseid_### -> bookid_###
    book_id = purchase_id.replace('purchaseid_', 'bookid_')
    book = book_map.get(book_id)
    if not book:
        # try alternative mapping: maybe numbers padded differently or purchaseid_X maps to bookid_X
        # try direct match
        book = book_map.get(purchase_id)
    if not book:
        continue
    categories = book.get('categories') or ''
    details = book.get('details') or ''
    # Check for 'Literature & Fiction' in categories and 'English' in details (indicating English-language)
    if 'Literature & Fiction' in categories and 'English' in details:
        # prepare author field: sometimes it's a JSON string, sometimes None
        author = book.get('author')
        try:
            if isinstance(author, str) and author.strip().startswith('{'):
                # try parse JSON
                auth_json = json.loads(author)
                # prefer name
                author = auth_json.get('name') or author
        except Exception:
            pass
        results.append({
            'title': book.get('title'),
            'author': author,
            'book_id': book.get('book_id'),
            'categories': categories,
            'details': details,
            'avg_rating': float(r.get('avg_rating')) if r.get('avg_rating') is not None else None,
            'n_reviews': int(r.get('n_reviews')) if r.get('n_reviews') is not None else None
        })

# Also check if there are purchase ids that map to bookids not in the first 200 rows; try to handle by also checking var_call_xKKp6EtC... if present
# If var_call_xKKp6EtCwuxtzrxOJwGUVWL8 exists in the environment, load and check
try:
    extra_file = var_call_xKKp6EtCwuxtzrxOJwGUVWL8
    with open(extra_file, 'r', encoding='utf-8') as f:
        extra_books = json.load(f)
    for b in extra_books:
        book_map[b.get('book_id')] = b
    # re-run matching for any reviews not yet matched
    matched_ids = {res['book_id'] for res in results}
    for r in reviews:
        purchase_id = r.get('purchase_id')
        book_id = purchase_id.replace('purchaseid_', 'bookid_')
        if book_id in matched_ids:
            continue
        book = book_map.get(book_id)
        if not book:
            continue
        categories = book.get('categories') or ''
        details = book.get('details') or ''
        if 'Literature & Fiction' in categories and 'English' in details:
            author = book.get('author')
            try:
                if isinstance(author, str) and author.strip().startswith('{'):
                    auth_json = json.loads(author)
                    author = auth_json.get('name') or author
            except Exception:
                pass
            results.append({
                'title': book.get('title'),
                'author': author,
                'book_id': book.get('book_id'),
                'categories': categories,
                'details': details,
                'avg_rating': float(r.get('avg_rating')) if r.get('avg_rating') is not None else None,
                'n_reviews': int(r.get('n_reviews')) if r.get('n_reviews') is not None else None
            })
except NameError:
    # extra file not available
    pass

# Deduplicate results by book_id
seen = set()
uniq_results = []
for item in results:
    bid = item.get('book_id')
    if bid in seen:
        continue
    seen.add(bid)
    uniq_results.append(item)

# Prepare JSON string
output = json.dumps(uniq_results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_QWHTBRONp1RTk7pvnVdZFxk4': ['review'], 'var_call_YNh9GP0mMfW0emPNgq7I3KJQ': ['books_info'], 'var_call_BUKR4TBVVWNfEWibrJuuEfOy': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'n_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'n_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'n_reviews': '1'}], 'var_call_om3GN2QL0L9TkwrpoNzFbX7c': [], 'var_call_6EyguY6JML38gQxKWg2ouQNy': 'file_storage/call_6EyguY6JML38gQxKWg2ouQNy.json', 'var_call_xKKp6EtCwuxtzrxOJwGUVWL8': 'file_storage/call_xKKp6EtCwuxtzrxOJwGUVWL8.json'}

exec(code, env_args)
