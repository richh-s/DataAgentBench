code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_maybe_path(var_call_CKQy1yYqE00HG4E4NvH5y24x)
texts = load_maybe_path(var_call_L813GpYG3zwR2hsg5JZQCn2G)

fund_projects = {r['Project_Name'] for r in funding}

status_design = set()
heading_pat = re.compile(r'(Capital Improvement Projects \(Design\)|Disaster Recovery Projects \(Design\))', re.IGNORECASE)
stop_pat = re.compile(r'\n\s*(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\))', re.IGNORECASE)

for doc in texts:
    t_norm = (doc.get('text','') or '').replace('\r','')
    for m in heading_pat.finditer(t_norm):
        block = t_norm[m.end():m.end()+8000]
        block = stop_pat.split(block)[0]
        for pn in fund_projects:
            if pn in status_design:
                continue
            if re.search(r'(^|\n)\s*' + re.escape(pn) + r'\s*(\n|$)', block):
                status_design.add(pn)

count = len(status_design)
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_WYAvWXVdv7pRjgQ5V9NV5NcB': [{'cnt': '276'}], 'var_call_L813GpYG3zwR2hsg5JZQCn2G': 'file_storage/call_L813GpYG3zwR2hsg5JZQCn2G.json', 'var_call_CKQy1yYqE00HG4E4NvH5y24x': 'file_storage/call_CKQy1yYqE00HG4E4NvH5y24x.json'}

exec(code, env_args)
