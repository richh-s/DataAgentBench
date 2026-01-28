code = """import json, re
# Load data from storage variables
books_path = var_call_0HEkoVq8k6eWujgiGb3y3w5L
reviews = var_call_DoVDVQdiY1MhuCmRKOwD76LP
# Read the books JSON file
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Build dict for quick lookup by book_id
books_by_id = {b['book_id']: b for b in books}

matches = []
for r in reviews:
    pid = r.get('purchase_id')
    m = re.search(r"_(\d+)$", pid)
    if not m:
        continue
    num = m.group(1)
    bookid = f"bookid_{num}"
    book = books_by_id.get(bookid)
    if not book:
        continue
    details = (book.get('details') or '').lower()
    # Check English-language mention
    if 'english' not in details:
        continue
    # Confirm category includes Literature & Fiction (already filtered earlier)
    cats = (book.get('categories') or '').lower()
    if 'literature & fiction' not in cats:
        continue
    matches.append({
        'purchase_id': pid,
        'book_id': bookid,
        'title': book.get('title'),
        'categories': book.get('categories'),
        'details': book.get('details'),
        'num_reviews_for_avg': int(r.get('num_reviews')) if r.get('num_reviews') is not None else None
    })

# Remove duplicates if multiple purchase_ids map to same book (unlikely) - but purchaseids unique
# Sort by book_id numeric
def sort_key(x):
    m = re.search(r"_(\d+)$", x['book_id'])
    return int(m.group(1)) if m else 0
matches_sorted = sorted(matches, key=sort_key)

output = json.dumps(matches_sorted)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_rdf5a3biTDtK3gfuB7hkeUz5': ['review'], 'var_call_eH5UFukmIKtDY9NGxtbOuR7q': ['books_info'], 'var_call_0HEkoVq8k6eWujgiGb3y3w5L': 'file_storage/call_0HEkoVq8k6eWujgiGb3y3w5L.json', 'var_call_DoVDVQdiY1MhuCmRKOwD76LP': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'num_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'num_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'num_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'num_reviews': '1'}]}

exec(code, env_args)
