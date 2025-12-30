code = """import json
funding_path = locals()["var_function-call-8778761271394130701"]
civic_path = locals()["var_function-call-17737362930517738246"]
with open(funding_path, 'r') as f: funding_data = json.load(f)
with open(civic_path, 'r') as f: civic_docs = json.load(f)
funded = set()
for r in funding_data:
    try:
        if float(r['Amount']) > 50000: funded.add(r['Project_Name'])
    except: pass
extracted = set()
for doc in civic_docs:
    lines = doc['text'].split(chr(10))
    active = False
    for i, line in enumerate(lines):
        l = line.strip()
        if 'Capital Improvement Projects' in l and 'Design' in l:
            active = True
            continue
        if active:
            if 'Capital Improvement Projects' in l and 'Design' not in l:
                active = False
                continue
            if not l: continue
            if l.startswith('Page') or l.startswith('Agenda'): continue
            if 'cid:' in l: continue
            is_p = False
            for k in range(i+1, min(i+5, len(lines))):
                if 'cid:' in lines[k]:
                    is_p = True
                    break
            if is_p: extracted.add(l)
final = extracted.intersection(funded)
print('__RESULT__:')
print(json.dumps({'count': len(final), 'projects': list(final), 'extracted': list(extracted)}))"""

env_args = {'var_function-call-8778761271394130701': 'file_storage/function-call-8778761271394130701.json', 'var_function-call-8778761271394130352': 'file_storage/function-call-8778761271394130352.json', 'var_function-call-17737362930517738246': 'file_storage/function-call-17737362930517738246.json'}

exec(code, env_args)
