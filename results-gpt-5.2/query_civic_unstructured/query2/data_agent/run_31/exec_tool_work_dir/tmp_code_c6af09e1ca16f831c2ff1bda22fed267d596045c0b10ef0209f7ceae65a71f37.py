code = """import json

src = var_call_eCYT6mwb8a9Kpa5X4KBBvjMo
if isinstance(src, str):
    docs = json.load(open(src, 'r', encoding='utf-8'))
else:
    docs = src

text = docs[0]['text']
lines = text.splitlines()
# find completion lines with 2022 and park context
hits=[]
for i,ln in enumerate(lines):
    if '2022' in ln and ('completed' in ln.lower() or 'complete' in ln.lower()):
        ctx=' | '.join([l.strip() for l in lines[max(0,i-2):i+3]])
        hits.append(ctx)

print('__RESULT__:')
print(json.dumps({'n_hits': len(hits), 'hits': hits[:10]}))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json', 'var_call_fwrAlLIXYuEkd3dLsbunT5gs': {'n_docs': 19, 'first_filename': 'malibucity_agenda_03222023-2060.txt', 'first_text_len': 9796}, 'var_call_Yp5C5xwexk7Gz27AO43Jgc7n': {'compiled': True, 'pattern': '(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\x08'}, 'var_call_dwH69q9JQE7Bb8lXVgihbvm3': {'compiled': True, 'pattern': '(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\x08[^\n\r]{0,80}2022'}}

exec(code, env_args)
