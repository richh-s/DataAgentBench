code = """import json, re
import pandas as pd

# Load civic docs
civic = var_call_kVHKp5Gn36NSE5VfB3QXWBh5
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)

# Extract Capital Improvement Projects (Design) sections and project names
project_status = {}
for doc in civic:
    text = doc.get('text','') or ''
    # find blocks under 'Capital Improvement Projects (Design)'
    for m in re.finditer(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)', text, flags=re.S|re.I):
        block = m.group(1)
        # project names are standalone lines; take lines with letters and not bullets/updates/schedule
        for line in block.splitlines():
            line=line.strip()
            if not line:
                continue
            if any(line.lower().startswith(x) for x in ['updates', 'project schedule', 'estimated schedule','complete design','advertise','begin construction','final design','project description','project updates','page','agenda item']):
                continue
            if line.startswith(('(cid', '•','-','2')):
                continue
            # likely project name: has letters, not too long, not all caps headings, not contains ':'
            if ':' in line:
                continue
            if re.search(r'[A-Za-z]', line) and len(line) <= 120:
                # exclude obvious non-project headers
                if re.fullmatch(r'Capital Improvement Projects.*', line, flags=re.I):
                    continue
                if re.fullmatch(r'\(?Design\)?', line, flags=re.I):
                    continue
                # some lines like 'Malibu Canyon Road Traffic Study' should be included
                project_status[line] = 'design'

# Load funding projects with max_amount > 50000
fund = var_call_hnXANFUSZwYoW7B3WZWDj20n
if isinstance(fund, str):
    with open(fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)

fund_names = {r['Project_Name'] for r in fund}

# Count capital projects (type inferred by being in CIP design section) with funding > 50000
count = sum(1 for name in project_status.keys() if name in fund_names)

out = json.dumps({'count': int(count)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_4kZL2lsq1m0EXfEWk7Oj3kfX': [{'cnt': '276'}], 'var_call_kVHKp5Gn36NSE5VfB3QXWBh5': 'file_storage/call_kVHKp5Gn36NSE5VfB3QXWBh5.json', 'var_call_hnXANFUSZwYoW7B3WZWDj20n': 'file_storage/call_hnXANFUSZwYoW7B3WZWDj20n.json'}

exec(code, env_args)
