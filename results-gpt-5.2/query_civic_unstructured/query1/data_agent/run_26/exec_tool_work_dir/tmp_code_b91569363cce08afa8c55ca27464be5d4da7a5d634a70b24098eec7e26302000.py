code = """import json, re, pandas as pd

def read_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

funding = read_json_maybe(var_call_sxyneLngtKU5Eoz7k6gs6jFQ)
docs = read_json_maybe(var_call_E083IjTW5X5sV0ONQ9Hf7ori)

# Funding projects with total funding > 50000
funding_projects = {r['Project_Name'] for r in funding}

# Extract projects listed under 'Capital Improvement Projects (Design)'
cap_design = set()
for d in docs:
    text = d.get('text','') or ''
    # isolate section if present
    m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)', text, flags=re.I|re.S)
    if not m:
        continue
    sec = m.group(1)
    # Split into lines and pick candidate project title lines: non-empty, not bullets, not schedule/updates
    for line in sec.splitlines():
        l = line.strip()
        if not l:
            continue
        if l.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'page ', 'agenda item', '•','(cid')):
            continue
        if re.match(r'^(complete design|advertise|begin construction|final design)\s*:', l, flags=re.I):
            continue
        # likely headings are short-ish and not ending with ':'
        if ':' in l:
            continue
        # exclude obvious non-project headings
        if re.search(r'capital improvement projects', l, flags=re.I):
            continue
        # heuristics: require at least 2 words or contains Road/PCH/Park/etc.
        if len(l.split()) < 2 and not re.search(r'(PCH|Road|Park|Storm|Drain|Civic|Center|Beach|Canyon|Skate|Warning|Water)', l, flags=re.I):
            continue
        cap_design.add(l)

# Count those with funding > 50k
count = sum(1 for p in cap_design if p in funding_projects)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_E083IjTW5X5sV0ONQ9Hf7ori': 'file_storage/call_E083IjTW5X5sV0ONQ9Hf7ori.json', 'var_call_sxyneLngtKU5Eoz7k6gs6jFQ': 'file_storage/call_sxyneLngtKU5Eoz7k6gs6jFQ.json'}

exec(code, env_args)
