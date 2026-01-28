code = """import json, re

# Load large inputs
import pathlib

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json') and pathlib.Path(path_or_obj).exists():
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

funding_projects = load_json_maybe(var_call_vk44TPRlZjKA5H83DF0V7etI)
docs = load_json_maybe(var_call_bIEc6Nex4ZTCwQ9L8ujDUST5)

funding_set = {r['Project_Name'] for r in funding_projects if r.get('Project_Name')}

# Parse project names under 'Capital Improvement Projects (Design)'
status_map = {}

header_pat = re.compile(r'^\s*Capital Improvement Projects\s*\(\s*Design\s*\)\s*$', re.IGNORECASE)
# stop when another capital/disaster section begins
stop_pat = re.compile(r'^\s*(Capital Improvement Projects\s*\(|Disaster Recovery Projects\s*\()\s*', re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    in_design = False
    for ln in lines:
        if not in_design and header_pat.match(ln.strip()):
            in_design = True
            continue
        if in_design:
            if stop_pat.match(ln.strip()) and not header_pat.match(ln.strip()):
                # next section
                break
            s = ln.strip()
            if not s:
                continue
            # skip bullets/labels
            if re.match(r'^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Project Description|Page\s+\d+\s+of\s+\d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:)', s, re.IGNORECASE):
                continue
            # likely a project name line: no colon, not too long, and not starting with punctuation
            if ':' in s:
                continue
            if len(s) > 120:
                continue
            # must contain a letter
            if not re.search(r'[A-Za-z]', s):
                continue
            # exclude generic headings
            if re.match(r'^(Capital Improvement Projects|Disaster Recovery Projects)\b', s, re.IGNORECASE):
                continue
            # store as design
            status_map[s] = 'design'

# Count projects that are capital + design + funding > 50k
# Here 'capital projects' interpreted as those appearing under Capital Improvement Projects section.
count = sum(1 for name, st in status_map.items() if st=='design' and name in funding_set)

print('__RESULT__:')
print(json.dumps({'count': count, 'matched_projects': sorted([n for n in status_map if n in funding_set])}))"""

env_args = {'var_call_IYKQ7ZC2iFkBeRPtoFx20rgi': [{'cnt': '276'}], 'var_call_bIEc6Nex4ZTCwQ9L8ujDUST5': 'file_storage/call_bIEc6Nex4ZTCwQ9L8ujDUST5.json', 'var_call_vk44TPRlZjKA5H83DF0V7etI': 'file_storage/call_vk44TPRlZjKA5H83DF0V7etI.json'}

exec(code, env_args)
