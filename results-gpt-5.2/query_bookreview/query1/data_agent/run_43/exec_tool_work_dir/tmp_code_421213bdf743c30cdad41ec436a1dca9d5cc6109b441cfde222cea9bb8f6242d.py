code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_TwTbYNooHxpb1PFzg2Mfua20)

year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

cnt_details_none = 0
cnt_year_found = 0
sample_years = []
for r in books[:2000]:
    d = r.get('details')
    if d is None:
        cnt_details_none += 1
        continue
    ys = year_re.findall(d)
    if ys:
        cnt_year_found += 1
        if len(sample_years) < 20:
            sample_years.append({'details': d[:120], 'years': ys[:5]})

out = {'books_total_preview': len(books[:2000]), 'details_none': cnt_details_none, 'details_with_year': cnt_year_found, 'sample': sample_years}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jMkFlOuc59m05cKrFcBdHNzh': 'file_storage/call_jMkFlOuc59m05cKrFcBdHNzh.json', 'var_call_bI9Q294bak9ak7apqvZONiKS': 'file_storage/call_bI9Q294bak9ak7apqvZONiKS.json', 'var_call_3DuR13sc2CwOcoAXrRhoqU4p': ['review'], 'var_call_e9DyEWiH6hw0IEZyWFFYVICh': 'file_storage/call_e9DyEWiH6hw0IEZyWFFYVICh.json', 'var_call_LqFZLY7jnubHTpUQ2uTB5OQt': {'decade': None, 'error': 'No publication years parsed from books details.'}, 'var_call_TwTbYNooHxpb1PFzg2Mfua20': 'file_storage/call_TwTbYNooHxpb1PFzg2Mfua20.json', 'var_call_95nEpNhKu65G97VKOKdm8WZn': {'decade': None, 'error': 'No publication years parsed from books details (full set).'}}

exec(code, env_args)
