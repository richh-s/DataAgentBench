code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic = load_json_maybe(var_call_rLW5gezVtiFhnxQGJJmptqiQ)
fund = load_json_maybe(var_call_rF5vpxY4fcip4qdu2WuQYyee)

# Build set of funded projects > 50k
funded = set([r['Project_Name'] for r in fund])

# Extract design projects from civic docs: look for section header and collect subsequent project names

design_projects = set()
for doc in civic:
    text = doc.get('text','')
    # normalize line breaks
    lines = [ln.strip() for ln in text.splitlines()]
    # find index of 'Capital Improvement Projects (Design)' then collect name lines until next section header
    for i,ln in enumerate(lines):
        if re.fullmatch(r'Capital Improvement Projects \(Design\)', ln, flags=re.IGNORECASE):
            j=i+1
            while j < len(lines):
                l=lines[j].strip()
                # stop at next major section
                if re.fullmatch(r'Capital Improvement Projects \(Construction\)', l, flags=re.IGNORECASE) or \
                   re.fullmatch(r'Capital Improvement Projects \(Not Started\)', l, flags=re.IGNORECASE) or \
                   re.fullmatch(r'Disaster Recovery Projects.*', l, flags=re.IGNORECASE):
                    break
                # project name lines: non-empty and not bullets/labels
                if l and not l.startswith('(cid') and not re.match(r'^(Updates:|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|Page \d+)', l, flags=re.IGNORECASE):
                    # heuristics: treat standalone line followed by blank or bullet as project name
                    # exclude obvious non-names
                    if len(l) < 120 and not re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|Agenda Item)', l, flags=re.IGNORECASE):
                        # skip if line ends with ':'
                        if not l.endswith(':') and not re.fullmatch(r'[0-9\-./ ]+', l):
                            # Many names are title case; accept
                            design_projects.add(l)
                j+=1

# Intersect and count
count = len(design_projects & funded)

print('__RESULT__:')
print(json.dumps({'count': count, 'design_projects_found': sorted(list(design_projects & funded))[:50], 'design_projects_found_total': sorted(list(design_projects & funded))}))"""

env_args = {'var_call_qGJ7DYqEy9N155c4gSY8zK9K': ['Funding'], 'var_call_F7cVLgQxIu4VcV9Oi6IJ1wIy': ['civic_docs'], 'var_call_rLW5gezVtiFhnxQGJJmptqiQ': 'file_storage/call_rLW5gezVtiFhnxQGJJmptqiQ.json', 'var_call_rF5vpxY4fcip4qdu2WuQYyee': 'file_storage/call_rF5vpxY4fcip4qdu2WuQYyee.json'}

exec(code, env_args)
