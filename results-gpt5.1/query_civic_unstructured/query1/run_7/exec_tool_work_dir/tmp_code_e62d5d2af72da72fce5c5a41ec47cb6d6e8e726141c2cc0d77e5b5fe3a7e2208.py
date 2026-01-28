code = """import re, json
from pathlib import Path

# Load full funding results
funding_path = var_call_auCgW1k97P8bABEnVGCSr58b
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_projects = {rec['Project_Name'] for rec in funding_records}

# Load civic docs
civic_path = var_call_6HgZ4A9u06LIfuSKtol9giQ2
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

text = "\n".join(doc['text'] for doc in civic_docs)

# Simple heuristic: any line that looks like a project name is followed by status context
projects_info = {}
for line in text.splitlines():
    clean = line.strip()
    if not clean:
        continue
    # match if line matches a known funding project name exactly
    if clean in funding_projects:
        projects_info.setdefault(clean, {'status': None, 'type': None})
        current = projects_info[clean]
    # detect status and type keywords in lines
    status = None
    if re.search(r'(?i)\bdesign\b', clean):
        status = 'design'
    elif re.search(r'(?i)completed', clean):
        status = 'completed'
    elif re.search(r'(?i)not started', clean):
        status = 'not started'
    ptype = None
    if re.search(r'(?i)capital', clean):
        ptype = 'capital'
    elif re.search(r'(?i)disaster', clean):
        ptype = 'disaster'

    if 'current' in locals() and (status or ptype):
        if status:
            current['status'] = status
        if ptype:
            current['type'] = ptype

# Count capital projects in design with funding > 50000
capital_design_projects = {name for name, info in projects_info.items() if info.get('status')=='design' and info.get('type')=='capital'}

funding_lookup = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}
count = sum(1 for name in capital_design_projects if funding_lookup.get(name,0) > 50000)

result = count

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_auCgW1k97P8bABEnVGCSr58b': 'file_storage/call_auCgW1k97P8bABEnVGCSr58b.json', 'var_call_6HgZ4A9u06LIfuSKtol9giQ2': 'file_storage/call_6HgZ4A9u06LIfuSKtol9giQ2.json'}

exec(code, env_args)
