code = """import json
# Load previous tool results available as variables
books_file_path = var_call_wr6x2tgkcvVBL9wUh11QBxlt
reviews = var_call_6bVuRlItzhgrPnM9vsjtrIkn

# Read books data from the JSON file
with open(books_file_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Normalize reviews into dict mapping purchase_id -> avg_rating, num_reviews
rev_map = {r['purchase_id']: {'avg_rating': float(r['avg_rating']), 'num_reviews': int(r['num_reviews'])} for r in reviews}

# Find books whose categories contain "Children's Books"
children_books = []
for b in books:
    cats = b.get('categories') or ''
    if "Children's Books" in cats:
        # derive expected purchase_id from book_id by replacing prefix
        book_id = b.get('book_id')
        purchase_id = None
        if isinstance(book_id, str) and book_id.startswith('bookid_'):
            purchase_id = 'purchaseid_' + book_id.split('_',1)[1]
        entry = {
            'book_id': book_id,
            'purchase_id': purchase_id,
            'title': b.get('title'),
            'categories': cats,
            'details': b.get('details')
        }
        # attach review info if available
        if purchase_id and purchase_id in rev_map:
            entry.update(rev_map[purchase_id])
        children_books.append(entry)

# Filter to those with avg_rating >= 4.5
result = [
    {'book_id': e['book_id'], 'purchase_id': e['purchase_id'], 'title': e['title'], 'avg_rating': e.get('avg_rating'), 'num_reviews': e.get('num_reviews')}
    for e in children_books if e.get('avg_rating') is not None and e.get('avg_rating') >= 4.5
]

# Sort descending by avg_rating then num_reviews
result.sort(key=lambda x: (-x['avg_rating'], -(x['num_reviews'] or 0)))

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6IJhI8D5vlD9cCIqK4DnceNq': ['review'], 'var_call_6bVuRlItzhgrPnM9vsjtrIkn': [{'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'num_reviews': '14'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'num_reviews': '13'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'num_reviews': '10'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'num_reviews': '49'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'num_reviews': '31'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'num_reviews': '24'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'num_reviews': '2'}], 'var_call_RNpopTpWrcvl5KNGNACAPx5D': ['books_info'], 'var_call_wr6x2tgkcvVBL9wUh11QBxlt': 'file_storage/call_wr6x2tgkcvVBL9wUh11QBxlt.json'}

exec(code, env_args)
