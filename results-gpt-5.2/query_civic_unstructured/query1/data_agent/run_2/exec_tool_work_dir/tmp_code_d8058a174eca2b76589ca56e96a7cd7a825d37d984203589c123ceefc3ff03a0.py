code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

fund_tot = load_records(var_call_IZAjxAM6kCwuXzlLjnZGWAZz)
docs = load_records(var_call_TvA5GaWXgY6GzyDLFsRJbJrA)

fund_names = {r['Project_Name'] for r in fund_tot}

start_re = re.compile(r'Capital Improvement Projects\s*\(Design\)', re.IGNORECASE)
end_re = re.compile(r'Capital Improvement Projects\s*\((Construction|Not Started)\)', re.IGNORECASE)
name_line_re = re.compile(r'^[A-Za-z0-9][A-Za-z0-9\s&\-\./()]+$')

skip_prefix_re = re.compile(r'^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Page\s+\d+\s+of\s+\d+|Agenda Item)', re.IGNORECASE)
skip_word_re = re.compile(r'\b(Staff|Consultant|Plans|Funding|Agreement|will|working|submitted|awaiting)\b', re.IGNORECASE)

names = set()
for d in docs:
    text = d.get('text','')
    m = start_re.search(text)
    if not m:
        continue
    seg = text[m.end():]
    m2 = end_re.search(seg)
    if m2:
        seg = seg[:m2.start()]
    for line in seg.replace('\r','').split('\n'):
        s = line.strip()
        if not s:
            continue
        if skip_prefix_re.match(s):
            continue
        if len(s) <= 120 and name_line_re.match(s) and not skip_word_re.search(s):
            names.add(s)

intersection = sorted(names & fund_names)
result = {'count': len(intersection), 'projects': intersection}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_K2JT7SkeWRk0ch9qUghzoKoU': [{'cnt': '276'}], 'var_call_TvA5GaWXgY6GzyDLFsRJbJrA': 'file_storage/call_TvA5GaWXgY6GzyDLFsRJbJrA.json', 'var_call_TCSJkExDjEiMVYe5oyZlO3I5': ['Funding'], 'var_call_IZAjxAM6kCwuXzlLjnZGWAZz': 'file_storage/call_IZAjxAM6kCwuXzlLjnZGWAZz.json', 'var_call_0hNKeoFFQBM5kcvHf6Y1PpUC': 'file_storage/call_0hNKeoFFQBM5kcvHf6Y1PpUC.json'}

exec(code, env_args)
