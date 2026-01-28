code = """import json, re
import pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

funding = load_tool_result(var_call_x5Dq3BPmSxMSJJkFAEFYCbFa)
docs = load_tool_result(var_call_XZR607pOoE04uUfEB3nYrmmg)

# funding project names with total funding > 50000
fund_names = set([r['Project_Name'] for r in funding if r.get('Project_Name') is not None])

# Extract project names in "Capital Improvement Projects (Design)" sections
patterns = [
    r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)",
    r"Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects|$)",
]

stop_headers = set([
    'updates', 'project schedule', 'estimated schedule', 'project description', 'project updates',
    'recommended action', 'discussion', 'subject', 'to', 'prepared by', 'approved by'
])

seen_design_projects = set()

for d in docs:
    text = d.get('text') or ''
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE|re.DOTALL):
            block = m.group(1)
            # normalize weird bullets
            block = block.replace('\r', '\n')
            lines = [re.sub(r"\s+", " ", ln.strip()) for ln in block.split('\n')]
            for ln in lines:
                if not ln:
                    continue
                # skip bullets and schedule/update lines
                if ln.startswith(('(cid:', '•', '·', '-', '–')):
                    continue
                low = ln.lower()
                if any(low.startswith(h) for h in stop_headers):
                    continue
                # exclude lines that look like section labels
                if 'capital improvement projects' in low or 'disaster recovery projects' in low:
                    continue
                # candidate project name lines: not too long, not containing ':' and not sentence-like
                if ':' in ln:
                    continue
                if len(ln) > 120:
                    continue
                # filter out page markers etc.
                if re.search(r"^page \d+ of \d+", low):
                    continue
                if re.search(r"^agenda item", low):
                    continue
                # must contain a letter
                if not re.search(r"[A-Za-z]", ln):
                    continue
                # avoid all-caps headings
                if ln.isupper() and len(ln.split())<=6:
                    continue
                seen_design_projects.add(ln)

# Intersect with funded projects > 50000
count = sum(1 for name in seen_design_projects if name in fund_names)

print('__RESULT__:')
print(json.dumps({'count': count, 'matched_projects': sorted([n for n in seen_design_projects if n in fund_names])[:50], 'design_projects_extracted': len(seen_design_projects)}))"""

env_args = {'var_call_p6YtyvGZLWOIyxYMVdF9lIib': [{'cnt': '276'}], 'var_call_XZR607pOoE04uUfEB3nYrmmg': 'file_storage/call_XZR607pOoE04uUfEB3nYrmmg.json', 'var_call_x5Dq3BPmSxMSJJkFAEFYCbFa': 'file_storage/call_x5Dq3BPmSxMSJJkFAEFYCbFa.json'}

exec(code, env_args)
