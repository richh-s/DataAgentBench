code = """import json
import datetime
import re

funding_path = locals()['var_function-call-9221482571475141474']
docs_path = locals()['var_function-call-17488906604846225691']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

candidates = set()
for row in funding_data:
    try:
        amt = float(row['Amount'])
        if amt > 50000:
            p_name = row['Project_Name'].strip()
            if p_name:
                candidates.add(p_name)
    except:
        pass

def parse_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        d_str = match.group(1)
        try:
            return datetime.datetime.strptime(d_str, '%m%d%Y')
        except:
            return datetime.datetime.min
    return datetime.datetime.min

civic_docs.sort(key=lambda x: parse_date(x['filename']))

project_status = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_section = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        if 'Capital Improvement Projects (Design)' in line_clean:
            current_section = 'CAP_DESIGN'
            continue
        elif 'Capital Improvement Projects (Construction)' in line_clean:
            current_section = 'CAP_OTHER'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line_clean:
            current_section = 'CAP_OTHER'
            continue
        elif 'Disaster Recovery Projects' in line_clean:
            current_section = 'DISASTER'
            continue
        
        if current_section and line_clean in candidates:
            if current_section == 'CAP_DESIGN':
                project_status[line_clean] = ('design', 'capital')
            elif current_section == 'CAP_OTHER':
                project_status[line_clean] = ('other', 'capital')
            elif current_section == 'DISASTER':
                project_status[line_clean] = ('other', 'disaster')

count = 0
result_projects = []
for p, (stat, typ) in project_status.items():
    if stat == 'design' and typ == 'capital':
        count += 1
        result_projects.append(p)

print('__RESULT__:')
print(json.dumps({'count': count, 'projects': result_projects}))"""

env_args = {'var_function-call-12957010085961315651': ['Funding'], 'var_function-call-12957010085961315256': ['civic_docs'], 'var_function-call-9221482571475141474': 'file_storage/function-call-9221482571475141474.json', 'var_function-call-9221482571475141387': 'file_storage/function-call-9221482571475141387.json', 'var_function-call-17488906604846225691': 'file_storage/function-call-17488906604846225691.json'}

exec(code, env_args)
