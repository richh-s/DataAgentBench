code = """import json, ast

# Load data from storage variables
reviews = var_call_qKrQDO9ywTvg1yqciP5ZLaym
books_var = var_call_sTmuDQqGooPEayVqSqG3VNOU

# If books_var is a path to a json file, load it
if isinstance(books_var, str):
    with open(books_var, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_var

# Ensure reviews is loaded (should be a list already)
if isinstance(reviews, str):
    with open(reviews, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

# Build mapping from numeric id to book record
books_map = {}
for b in books:
    bid = b.get('book_id')
    if not bid:
        continue
    # extract numeric suffix
    if '_' in bid:
        key = bid.split('_', 1)[1]
    else:
        key = bid
    books_map[key] = b

results = []
for r in reviews:
    pid = r.get('purchase_id')
    if not pid:
        continue
    if '_' in pid:
        key = pid.split('_', 1)[1]
    else:
        key = pid
    try:
        avg = float(r.get('avg_rating'))
    except Exception:
        continue
    try:
        cnt = int(r.get('review_count'))
    except Exception:
        cnt = None
    if avg >= 4.5:
        book = books_map.get(key)
        if not book:
            continue
        cats_raw = book.get('categories')
        cats = []
        if cats_raw:
            try:
                cats = ast.literal_eval(cats_raw)
            except Exception:
                # fallback: try json loads
                try:
                    cats = json.loads(cats_raw)
                except Exception:
                    # leave as empty
                    cats = []
        # Check if "Children's Books" in categories
        if any((isinstance(c, str) and c == "Children's Books") for c in cats):
            results.append({
                'book_id': book.get('book_id'),
                'title': book.get('title'),
                'categories': cats,
                'avg_rating': avg,
                'review_count': cnt
            })

# Deduplicate by book_id (in case multiple entries) and sort by avg_rating desc
unique = {}
for r in results:
    bid = r['book_id']
    if bid not in unique or r['avg_rating'] > unique[bid]['avg_rating']:
        unique[bid] = r
final_list = list(unique.values())
final_list.sort(key=lambda x: (-x['avg_rating'], - (x['review_count'] or 0)))

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_call_EXMSCM1v3DiG5CPvzsXEkIm9': ['review'], 'var_call_41WnFkMTT40hCSD0OVr6fRQN': 'file_storage/call_41WnFkMTT40hCSD0OVr6fRQN.json', 'var_call_zFLLIlFWw07X4AOTMZ3Uazm8': ['books_info'], 'var_call_sTmuDQqGooPEayVqSqG3VNOU': 'file_storage/call_sTmuDQqGooPEayVqSqG3VNOU.json', 'var_call_qKrQDO9ywTvg1yqciP5ZLaym': [{'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_107', 'avg_rating': '4.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_109', 'avg_rating': '1.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_11', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_137', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_140', 'avg_rating': '4.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_145', 'avg_rating': '4.0', 'review_count': '5'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_155', 'avg_rating': '1.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_167', 'avg_rating': '4.0', 'review_count': '12'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_189', 'avg_rating': '2.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_193', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_20', 'avg_rating': '3.875', 'review_count': '16'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_25', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_31', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_32', 'avg_rating': '3.5714285714285716', 'review_count': '7'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_45', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_5', 'avg_rating': '3.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_62', 'avg_rating': '4.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_67', 'avg_rating': '3.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_85', 'avg_rating': '3.8333333333333335', 'review_count': '12'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_93', 'avg_rating': '3.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_99', 'avg_rating': '4.4', 'review_count': '5'}]}

exec(code, env_args)
