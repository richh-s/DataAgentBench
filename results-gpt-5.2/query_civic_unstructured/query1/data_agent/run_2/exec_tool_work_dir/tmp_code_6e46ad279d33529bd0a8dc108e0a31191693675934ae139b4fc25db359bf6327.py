code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

fund_tot = load_records(var_call_IZAjxAM6kCwuXzlLjnZGWAZz)
docs = load_records(var_call_TvA5GaWXgY6GzyDLFsRJbJrA)

fund_names = {r['Project_Name'] for r in fund_tot}

# extract design capital project names from docs
start_re = re.compile(r'Capital Improvement Projects\s*\(Design\)', re.IGNORECASE)
end_re = re.compile(r'Capital Improvement Projects\s*\((Construction|Not Started)\)', re.IGNORECASE)

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
    # clean common bullet characters
    seg = seg.replace('\r','')
    # candidate lines
    for line in seg.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # skip headings and bullets
        if re.match(r'^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Page\s+\d+\s+of\s+\d+|Agenda Item)', line_stripped, flags=re.I):
            continue
        # keep lines that look like a title: mostly words, allow &, /, -, numbers
        if re.match(r'^[A-Za-z0-9][A-Za-z0-9\s\&\-\./\'\(\)]+$', line_stripped) and len(line_stripped) <= 120:
            # exclude lines that are clearly narrative
            if re.search(r'\b(Staff|City|Consultant|Plans|Funding|Agreement|will|working|submitted|awaiting)\b', line_stripped, flags=re.I):
                continue
            names.add(line_stripped)

# intersection with funded projects > 50k
intersection = sorted(names & fund_names)

result = {
    'count': len(intersection),
    'projects': intersection
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_K2JT7SkeWRk0ch9qUghzoKoU': [{'cnt': '276'}], 'var_call_TvA5GaWXgY6GzyDLFsRJbJrA': 'file_storage/call_TvA5GaWXgY6GzyDLFsRJbJrA.json', 'var_call_TCSJkExDjEiMVYe5oyZlO3I5': ['Funding'], 'var_call_IZAjxAM6kCwuXzlLjnZGWAZz': 'file_storage/call_IZAjxAM6kCwuXzlLjnZGWAZz.json', 'var_call_0hNKeoFFQBM5kcvHf6Y1PpUC': 'file_storage/call_0hNKeoFFQBM5kcvHf6Y1PpUC.json'}

exec(code, env_args)
