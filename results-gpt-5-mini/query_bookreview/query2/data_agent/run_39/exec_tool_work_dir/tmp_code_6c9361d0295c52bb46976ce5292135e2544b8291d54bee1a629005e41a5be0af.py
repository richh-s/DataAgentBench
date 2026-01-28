code = """import json
path = var_call_BohIxG1ufPb9g9LGzycJEzpu
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

lines = []
for r in records:
    title = r.get('title') or None
    book_id = r.get('book_id') or None
    author = r.get('author') or None
    # try extract author name if author is JSON string
    auth_name = author
    try:
        if isinstance(author, str) and author.strip().startswith('{'):
            a = json.loads(author)
            auth_name = a.get('name') or author
    except Exception:
        auth_name = author
    purchase_id = r.get('purchase_id') or None
    avg = r.get('avg_rating')
    n = r.get('n_reviews')
    rec = {
        'title': title,
        'book_id': book_id,
        'author': auth_name,
        'purchase_id': purchase_id,
        'avg_rating': avg,
        'n_reviews': n
    }
    lines.append(rec)

# Build final plain-text answer as newline-separated JSON objects for readability
text_lines = [json.dumps(x, ensure_ascii=False) for x in lines]
answer_text = '\n'.join(text_lines)

print("__RESULT__:")
print(json.dumps(answer_text))"""

env_args = {'var_call_7feQSRx3g2Pi5ch1gjqxuWF0': 'file_storage/call_7feQSRx3g2Pi5ch1gjqxuWF0.json', 'var_call_8Vkqk91HG7R3FiRdVSkn8W9h': ['review'], 'var_call_l4DwNsCBn47T7e35OjJkozcb': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'n_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'n_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'n_reviews': '1'}], 'var_call_URw5S5WUEH0K4sBEUdyBSePM': 'file_storage/call_URw5S5WUEH0K4sBEUdyBSePM.json', 'var_call_BohIxG1ufPb9g9LGzycJEzpu': 'file_storage/call_BohIxG1ufPb9g9LGzycJEzpu.json'}

exec(code, env_args)
