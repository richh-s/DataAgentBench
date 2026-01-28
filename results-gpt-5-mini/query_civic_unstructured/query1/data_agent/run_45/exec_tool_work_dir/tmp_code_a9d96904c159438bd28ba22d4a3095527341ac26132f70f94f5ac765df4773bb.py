code = """import json
import re

with open(var_call_JB6TQEL3z93YnYHK9rnGpkHo, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_qNKgQ52ocQxIOP8yjhn1GgPu, 'r') as f:
    funding_rows = json.load(f)

def normalize_name(name):
    if not isinstance(name, str):
        return ''
    name = re.sub(r"\(.*?\)", "", name)
    name = re.sub(r"[^\w\s&-]", " ", name)
    name = re.sub(r"\s+", " ", name).strip().lower()
    return name

# Extract project names under 'Capital Improvement Projects (Design)'
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    low = text.lower()
    marker = 'capital improvement projects (design)'
    idx = low.find(marker)
    if idx == -1:
        continue
    start = idx + len(marker)
    # find end by next known section headers
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)']
    end = len(text)
    for em in end_markers:
        j = low.find(em, start)
        if j != -1 and j < end:
            end = j
    section = text[start:end]
    lines = [ln.strip() for ln in section.splitlines()]
    for ln in lines:
        if not ln:
            continue
        lnl = ln.lower()
        exclude = ['updates', 'project schedule', 'page', 'agenda', 'item', 'subject', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'cid:', 'begin construction', 'complete design', 'advertise', 'estimated schedule', 'project description', 'project updates']
        if any(k in lnl for k in exclude):
            continue
        if lnl.endswith(':'):
            continue
        if len(ln.split()) > 0 and len(ln.split()) <= 12 and re.search('[A-Za-z]', ln):
            clean_ln = re.sub(r'^[\d\.\n\)\s]+', '', ln).strip()
            if len(clean_ln) < 3:
                continue
            # remove trailing periods
            clean_ln = clean_ln.rstrip('.')
            design_projects.append(clean_ln)

# dedupe
seen = set()
design_projects_unique = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        design_projects_unique.append(p)

# funding map
funding_map = {}
for r in funding_rows:
    pname = r.get('Project_Name', '')
    amt = r.get('Amount', 0)
    try:
        amt_int = int(str(amt))
    except:
        continue
    norm = normalize_name(pname)
    funding_map.setdefault(norm, []).append({'original': pname, 'amount': amt_int})

matched = []
for p in design_projects_unique:
    normp = normalize_name(p)
    if normp in funding_map:
        if any(entry['amount'] > 50000 for entry in funding_map[normp]):
            matched.append({'project_name': p, 'normalized_name': normp, 'funding_records': funding_map[normp]})

result = {'count': len(matched), 'matched_projects': [m['project_name'] for m in matched]}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qNKgQ52ocQxIOP8yjhn1GgPu': 'file_storage/call_qNKgQ52ocQxIOP8yjhn1GgPu.json', 'var_call_JB6TQEL3z93YnYHK9rnGpkHo': 'file_storage/call_JB6TQEL3z93YnYHK9rnGpkHo.json'}

exec(code, env_args)
