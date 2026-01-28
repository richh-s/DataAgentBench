code = """import json
import re

civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:2

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_dict = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        funding_dict[name] = amt

design_projects = set()

for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        parts = txt.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            for line in section.split('\n'):
                line = line.strip()
                if len(line) < 5:
                    continue
                if 'Complete Design:' in line or 'Advertise:' in line or 'Begin Construction:' in line:
                    continue
                if 'Final Design:' in line or 'Project Schedule:' in line or 'Updates:' in line:
                    continue
                if line.startswith('cid:') or line.startswith('(cid:'):
                    continue
                if line.startswith('●') or line.startswith('•'):
                    continue
                if 'Project is' in line:
                    continue
                clean_line = re.sub(r'\(cid:\d+\)', '', line).strip()
                if clean_line in funding_dict:
                    design_projects.add(clean_line)

for proj_name in funding_dict:
    if proj_name in design_projects:
        continue
    for doc in civic_docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            idx = txt.find(proj_name)
            context = txt[max(0, idx-300):min(len(txt), idx+len(proj_name)+300)].lower()
            if 'design' in context and not 'fema' in proj_name.lower():
                design_projects.add(proj_name)
                break

count = len(design_projects)
print('__RESULT__:')
print(json.dumps(str(count)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
