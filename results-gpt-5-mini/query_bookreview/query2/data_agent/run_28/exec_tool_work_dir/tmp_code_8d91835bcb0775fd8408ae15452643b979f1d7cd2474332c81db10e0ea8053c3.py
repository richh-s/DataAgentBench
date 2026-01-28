code = """import json, re

reviews = var_call_BAmnKEFtm997ya973mWfHPvo
books_json_path = var_call_2gCjMhZisDs0xYp7O4HW1TVz
with open(books_json_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# helper to extract numeric id
def extract_num(s):
    if s is None:
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

# build map of review entries by numeric id where avg_rating == 5.0
rev_map = {}
for r in reviews:
    try:
        avg = float(r.get('avg_rating'))
    except Exception:
        continue
    if avg == 5.0:
        n = extract_num(r.get('purchase_id'))
        if n is None:
            continue
        rev_map.setdefault(n, []).append({'purchase_id': r.get('purchase_id'), 'avg_rating': avg, 'review_count': int(r.get('review_count')) if r.get('review_count') is not None else None})

results = []
for b in books:
    cat = b.get('categories','') or ''
    det = b.get('details','') or ''
    if 'Literature & Fiction' not in cat:
        continue
    # check English in details or categories
    if not (re.search(r"\bEnglish\b", det, flags=re.IGNORECASE) or re.search(r"\bEnglish\b", cat, flags=re.IGNORECASE)):
        continue
    num = extract_num(b.get('book_id'))
    if num is None:
        continue
    if num in rev_map:
        # parse author
        author = b.get('author')
        author_name = None
        if isinstance(author, str):
            try:
                parsed = json.loads(author)
                if isinstance(parsed, dict) and 'name' in parsed:
                    author_name = parsed.get('name')
                else:
                    author_name = author
            except Exception:
                author_name = author
        else:
            author_name = author
        entry = {
            'book_id': b.get('book_id'),
            'title': b.get('title'),
            'author': author_name,
            'categories': cat,
            'details': det,
            'matches': rev_map.get(num)
        }
        results.append(entry)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_XdmQJaGaU6y2ov9EJXeyokbx': ['review'], 'var_call_BAmnKEFtm997ya973mWfHPvo': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'review_count': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'review_count': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'review_count': '1'}], 'var_call_e6FbggakfO1ZCBxBopuxMhqN': ['books_info'], 'var_call_2gCjMhZisDs0xYp7O4HW1TVz': 'file_storage/call_2gCjMhZisDs0xYp7O4HW1TVz.json', 'var_call_1aD1KhDGTXgE7rY96igUXHl9': [], 'var_call_W9rq3XmWEWxx4hVTh2ZyVba2': [], 'var_call_rF1vN7auXL3w41c2x0BHFbCf': {'num_review_ids': [2, 6, 7, 9, 12, 14, 16, 21, 24, 26, 28, 29, 33, 34, 38, 39, 40, 41, 42, 47, 54, 56, 57, 59, 60, 64, 71, 73, 74, 75, 79, 80, 82, 83, 84, 88, 90, 91, 97, 98, 101, 105, 108, 110, 114, 116, 117, 118, 121, 122, 123, 124, 126, 127, 128, 130, 132, 133, 134, 143, 144, 146, 150, 151, 152, 153, 156, 160, 163, 166, 168, 170, 171, 172, 174, 177, 180, 181, 182, 184, 192, 195, 197], 'num_book_ids_sample_count': 200, 'common_numeric_ids_count': 83, 'common_numeric_ids_sample': [2, 6, 7, 9, 12, 14, 16, 21, 24, 26, 28, 29, 33, 34, 38, 39, 40, 41, 42, 47, 54, 56, 57, 59, 60, 64, 71, 73, 74, 75, 79, 80, 82, 83, 84, 88, 90, 91, 97, 98, 101, 105, 108, 110, 114, 116, 117, 118, 121, 122, 123, 124, 126, 127, 128, 130, 132, 133, 134, 143, 144, 146, 150, 151, 152, 153, 156, 160, 163, 166, 168, 170, 171, 172, 174, 177, 180, 181, 182, 184, 192, 195, 197]}}

exec(code, env_args)
