code = """import json

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_TwTbYNooHxpb1PFzg2Mfua20)
# show first 5 details
out = [{'book_id': r.get('book_id'), 'details': r.get('details')} for r in books[:5]]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jMkFlOuc59m05cKrFcBdHNzh': 'file_storage/call_jMkFlOuc59m05cKrFcBdHNzh.json', 'var_call_bI9Q294bak9ak7apqvZONiKS': 'file_storage/call_bI9Q294bak9ak7apqvZONiKS.json', 'var_call_3DuR13sc2CwOcoAXrRhoqU4p': ['review'], 'var_call_e9DyEWiH6hw0IEZyWFFYVICh': 'file_storage/call_e9DyEWiH6hw0IEZyWFFYVICh.json', 'var_call_LqFZLY7jnubHTpUQ2uTB5OQt': {'decade': None, 'error': 'No publication years parsed from books details.'}, 'var_call_TwTbYNooHxpb1PFzg2Mfua20': 'file_storage/call_TwTbYNooHxpb1PFzg2Mfua20.json', 'var_call_95nEpNhKu65G97VKOKdm8WZn': {'decade': None, 'error': 'No publication years parsed from books details (full set).'}, 'var_call_25Pg2cBnkDZ8up4wRgPx2sFB': {'books_total_preview': 200, 'details_none': 0, 'details_with_year': 0, 'sample': []}}

exec(code, env_args)
