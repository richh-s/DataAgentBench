code = """import json
with open(var_call_mC9eh9kdqR7TFrzmoKhf7oa0, 'r') as f:
    books_data = json.load(f)
out = []
import re
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")
for i, b in enumerate(books_data[:30]):
    details = b.get('details')
    matches = []
    if isinstance(details, str):
        matches = year_re.findall(details)
    out.append({'book_id': b.get('book_id'), 'details_preview': (details[:200] if isinstance(details, str) else details), 'matches': matches})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_L3tZ220n99FgcRPeZvbhSpxY': ['review'], 'var_call_xqroN816bvY3rq0PLmDfvm3h': ['books_info'], 'var_call_clwW1HpxqxlCKDXJvn9Iim9W': 'file_storage/call_clwW1HpxqxlCKDXJvn9Iim9W.json', 'var_call_mC9eh9kdqR7TFrzmoKhf7oa0': 'file_storage/call_mC9eh9kdqR7TFrzmoKhf7oa0.json', 'var_call_PzRGmZTiF7A8yiwjsrG9INcb': None, 'var_call_9JxKxeXkrY5kd2uJfUzd5F4Y': {'num_total_books': 200, 'num_books_with_year': 0, 'num_review_purchase_ids': 200, 'num_mapped_ids_present_in_books': 200, 'num_merged_rows': 0, 'num_unique_merged_books': 0, 'decade_stats': []}}

exec(code, env_args)
