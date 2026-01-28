code = """import json, re
with open(var_call_c8DwRj64MtSJYZW92sSCp2Oh, 'r') as f:
    businesses = json.load(f)

state_codes = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
pattern = re.compile(r'\b(' + '|'.join(state_codes) + r')\b')

total = len(businesses)
with_desc = sum(1 for b in businesses if b.get('description'))
matched = 0
samples = []
for b in businesses:
    desc = b.get('description') or ''
    m = pattern.search(desc)
    if m:
        matched += 1
        if len(samples) < 20:
            samples.append({'business_id': b.get('business_id'), 'description': desc, 'state': m.group(1)})

res = {'total_businesses': total, 'with_description': with_desc, 'matched_state_count': matched, 'samples': samples}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_DyWkhUZrWhEw6LixAvfowfDs': ['business', 'checkin'], 'var_call_ZcivhTR0krr3WaNsPaY0wwdP': ['review', 'tip', 'user'], 'var_call_c8DwRj64MtSJYZW92sSCp2Oh': 'file_storage/call_c8DwRj64MtSJYZW92sSCp2Oh.json', 'var_call_n0S2syUfDJf7pjVSheCo8pDc': 'file_storage/call_n0S2syUfDJf7pjVSheCo8pDc.json', 'var_call_9oeTCPeOCg4UFqZcFJE93muh': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_1laMVn0AMpbLxhZPrd1MMgLu': 'file_storage/call_1laMVn0AMpbLxhZPrd1MMgLu.json', 'var_call_PIvy8zBP7dGQZSYICadzOpOw': {'state': None, 'total_reviews': 0, 'average_rating': None}}

exec(code, env_args)
