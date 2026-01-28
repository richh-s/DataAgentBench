code = """import json, re

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

funding = load_tool_result(var_call_x5Dq3BPmSxMSJJkFAEFYCbFa)
docs = load_tool_result(var_call_XZR607pOoE04uUfEB3nYrmmg)

fund_names = set(r.get('Project_Name') for r in funding if r.get('Project_Name') is not None)

patterns = [
    r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)",
    r"Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects|$)",
]

stop_starts = (
    'updates', 'project schedule', 'estimated schedule', 'project description', 'project updates',
    'recommended action', 'discussion', 'subject', 'to', 'prepared by', 'approved by'
)

seen_design_projects = set()

for d in docs:
    text = d.get('text') or ''
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE|re.DOTALL):
            block = m.group(1).replace('\r', '\n')
            for raw in block.split('\n'):
                ln = re.sub(r"\s+", " ", raw.strip())
                if not ln:
                    continue
                if ln.startswith('(cid:'):
                    continue
                low = ln.lower()
                if low.startswith(stop_starts):
                    continue
                if 'capital improvement projects' in low or 'disaster recovery projects' in low:
                    continue
                if ':' in ln:
                    continue
                if len(ln) > 120:
                    continue
                if re.match(r"^page \d+ of \d+", low):
                    continue
                if low.startswith('agenda item'):
                    continue
                if not re.search(r"[A-Za-z]", ln):
                    continue
                if ln.isupper() and len(ln.split()) <= 6:
                    continue
                seen_design_projects.add(ln)

matched = sorted([n for n in seen_design_projects if n in fund_names])

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'matched_projects_sample': matched[:50], 'design_projects_extracted': len(seen_design_projects)}))"""

env_args = {'var_call_p6YtyvGZLWOIyxYMVdF9lIib': [{'cnt': '276'}], 'var_call_XZR607pOoE04uUfEB3nYrmmg': 'file_storage/call_XZR607pOoE04uUfEB3nYrmmg.json', 'var_call_x5Dq3BPmSxMSJJkFAEFYCbFa': 'file_storage/call_x5Dq3BPmSxMSJJkFAEFYCbFa.json'}

exec(code, env_args)
