code = """import json
with open(var_call_c8DwRj64MtSJYZW92sSCp2Oh, 'r') as f:
    businesses = json.load(f)
out = []
for b in businesses[:80]:
    out.append({
        'business_id': b.get('business_id'),
        'description': b.get('description'),
        'review_count': b.get('review_count')
    })
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DyWkhUZrWhEw6LixAvfowfDs': ['business', 'checkin'], 'var_call_ZcivhTR0krr3WaNsPaY0wwdP': ['review', 'tip', 'user'], 'var_call_c8DwRj64MtSJYZW92sSCp2Oh': 'file_storage/call_c8DwRj64MtSJYZW92sSCp2Oh.json', 'var_call_n0S2syUfDJf7pjVSheCo8pDc': 'file_storage/call_n0S2syUfDJf7pjVSheCo8pDc.json', 'var_call_9oeTCPeOCg4UFqZcFJE93muh': {'state': None, 'total_reviews': 0, 'average_rating': None}}

exec(code, env_args)
