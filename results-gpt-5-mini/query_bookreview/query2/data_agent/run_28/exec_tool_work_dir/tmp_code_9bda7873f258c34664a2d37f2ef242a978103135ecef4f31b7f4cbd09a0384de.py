code = """import json, re

reviews = var_call_BAmnKEFtm997ya973mWfHPvo
books_json_path = var_call_2gCjMhZisDs0xYp7O4HW1TVz
with open(books_json_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

def extract_num(s):
    if s is None:
        return None
    m = re.search(r"(\d+)", str(s))
    return int(m.group(1)) if m else None

review_nums = set()
for r in reviews:
    n = extract_num(r.get('purchase_id'))
    if n is not None:
        review_nums.add(n)

book_nums = set()
for b in books:
    n = extract_num(b.get('book_id'))
    if n is not None:
        book_nums.add(n)

common = sorted(list(review_nums & book_nums))

out = {
    'num_review_ids': sorted(list(review_nums))[:200],
    'num_book_ids_sample_count': len(book_nums),
    'common_numeric_ids_count': len(common),
    'common_numeric_ids_sample': common[:200]
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_XdmQJaGaU6y2ov9EJXeyokbx': ['review'], 'var_call_BAmnKEFtm997ya973mWfHPvo': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'review_count': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'review_count': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'review_count': '1'}], 'var_call_e6FbggakfO1ZCBxBopuxMhqN': ['books_info'], 'var_call_2gCjMhZisDs0xYp7O4HW1TVz': 'file_storage/call_2gCjMhZisDs0xYp7O4HW1TVz.json', 'var_call_1aD1KhDGTXgE7rY96igUXHl9': [], 'var_call_W9rq3XmWEWxx4hVTh2ZyVba2': []}

exec(code, env_args)
