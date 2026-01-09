code = """import json, pandas as pd, re

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_maybe_path(var_call_CKQy1yYqE00HG4E4NvH5y24x)
texts = load_maybe_path(var_call_L813GpYG3zwR2hsg5JZQCn2G)

fund_projects = {r['Project_Name'] for r in funding}

# Detect which of these projects appear under a 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)' heading
status_design = set()
for doc in texts:
    t = doc.get('text','')
    t_norm = t.replace('\r','')
    # find blocks after headings indicating design lists; capture next ~4000 chars
    for m in re.finditer(r'(Capital Improvement Projects \(Design\)|Disaster Recovery Projects \(Design\))', t_norm, flags=re.IGNORECASE):
        block = t_norm[m.end():m.end()+8000]
        # stop at next major heading
        block = re.split(r'\n\s*(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\))', block, flags=re.IGNORECASE)[0]
        # mark any funded project name that appears as a line in block
        for pn in fund_projects:
            if pn in status_design:
                continue
            # require it appears as a standalone line-ish to reduce false positives
            if re.search(r'(^|\n)\s*' + re.escape(pn) + r'\s*(\n|$)', block):
                status_design.add(pn)

count = sum(1 for pn in fund_projects if pn in status_design)

print('__RESULT__:')
print(json.dumps({'count': count, 'matched_projects': sorted(list(status_design))[:50], 'matched_projects_count': len(status_design)}))"""

env_args = {'var_call_WYAvWXVdv7pRjgQ5V9NV5NcB': [{'cnt': '276'}], 'var_call_L813GpYG3zwR2hsg5JZQCn2G': 'file_storage/call_L813GpYG3zwR2hsg5JZQCn2G.json', 'var_call_CKQy1yYqE00HG4E4NvH5y24x': 'file_storage/call_CKQy1yYqE00HG4E4NvH5y24x.json'}

exec(code, env_args)
