code = """import json
with open(var_call_c8DwRj64MtSJYZW92sSCp2Oh, 'r') as f:
    businesses = json.load(f)
out = []
for b in businesses[:30]:
    out.append({'business_id': b.get('business_id'), 'description_repr': repr(b.get('description'))[:200]})
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DyWkhUZrWhEw6LixAvfowfDs': ['business', 'checkin'], 'var_call_ZcivhTR0krr3WaNsPaY0wwdP': ['review', 'tip', 'user'], 'var_call_c8DwRj64MtSJYZW92sSCp2Oh': 'file_storage/call_c8DwRj64MtSJYZW92sSCp2Oh.json', 'var_call_n0S2syUfDJf7pjVSheCo8pDc': 'file_storage/call_n0S2syUfDJf7pjVSheCo8pDc.json', 'var_call_9oeTCPeOCg4UFqZcFJE93muh': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_1laMVn0AMpbLxhZPrd1MMgLu': 'file_storage/call_1laMVn0AMpbLxhZPrd1MMgLu.json', 'var_call_PIvy8zBP7dGQZSYICadzOpOw': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_7ADW41m5U9ZxsbGIPjXgxYYP': {'total_businesses': 100, 'with_description': 100, 'matched_state_count': 0, 'samples': []}}

exec(code, env_args)
