code = """import json
with open(var_call_imMVVH4ydlnQiLitue5achAa, 'r') as f:
    funding = json.load(f)
with open(var_call_LsS5gYiobVLdbl1d1c1xS3Ye, 'r') as f:
    civic = json.load(f)
texts = [d.get('text','').lower() for d in civic]
full = ' '.join(texts)
park_keywords = ['park','playground','walkway','shade','bench','benches','bluffs','point dume','legacy park']
matched = []
for r in funding:
    name = r.get('Project_Name','').lower()
    if not any(kw in name for kw in park_keywords):
        continue
    norm = name.split('(')[0].strip()
    if norm in full:
        idx = full.find(norm)
        if idx != -1:
            start = idx-200 if idx-200>0 else 0
            window = full[start: idx+500]
            if '2022' in window and ('complete' in window or 'construction was completed' in window or 'notice of completion' in window):
                try:
                    amt = int(r.get('Amount',0))
                except:
                    try:
                        amt = int(float(r.get('Amount',0)))
                    except:
                        amt = 0
                matched.append({'Project_Name': r.get('Project_Name',''), 'Amount': amt})

total = sum(m['Amount'] for m in matched)
print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_call_NnUo40dHHTLYgcQTqlojtfqg': ['civic_docs'], 'var_call_UjP3tQXtgm9tRd9gDjbiDPvo': ['Funding'], 'var_call_LsS5gYiobVLdbl1d1c1xS3Ye': 'file_storage/call_LsS5gYiobVLdbl1d1c1xS3Ye.json', 'var_call_imMVVH4ydlnQiLitue5achAa': 'file_storage/call_imMVVH4ydlnQiLitue5achAa.json', 'var_call_jTbIoLYTmACc319xO44IBupV': {'funding_count': 500}}

exec(code, env_args)
