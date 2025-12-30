code = """import json
import re
import datetime

k1 = 'var_function-call-9221482571475141474'
k2 = 'var_function-call-17488906604846225691'

with open(locals()[k1], 'r') as f:
    funding_data = json.load(f)

with open(locals()[k2], 'r') as f:
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

# Sort docs
def get_date(doc):
    fn = doc.get('filename', '')
    # malibucity_agenda__01262022-1835.txt
    match = re.search(r'(\d{8})', fn)
    if match:
        return match.group(1) # string comparison for YYYYMMDD is wrong, need MMDDYYYY -> YYYYMMDD or datetime
    return '00000000'

def parse_date_obj(d_str):
    if len(d_str) == 8:
        return datetime.datetime.strptime(d_str, '%m%d%Y')
    return datetime.datetime.min

civic_docs.sort(key=lambda x: parse_date_obj(get_date(x)))

# Headers
H_CAP_DES = "Capital Improvement Projects (Design)"
H_CAP_CON = "Capital Improvement Projects (Construction)"
H_CAP_NOT = "Capital Improvement Projects (Not Started)"
H_DISASTER = "Disaster Recovery Projects"

project_status = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    curr = None
    
    for line in lines:
        ln = line.strip()
        if not ln:
            continue
        
        if H_CAP_DES in ln:
            curr = 'DES'
            continue
        elif H_CAP_CON in ln:
            curr = 'OTH'
            continue
        elif H_CAP_NOT in ln:
            curr = 'OTH'
            continue
        elif H_DISASTER in ln:
            curr = 'DIS'
            continue
            
        if curr and ln in candidates:
            # We found a candidate in a section
            if curr == 'DES':
                project_status[ln] = 'DESIGN'
            elif curr == 'OTH':
                project_status[ln] = 'OTHER'
            elif curr == 'DIS':
                project_status[ln] = 'DISASTER'

count = 0
found_projects = []
for p, s in project_status.items():
    if s == 'DESIGN':
        count += 1
        found_projects.append(p)

print("__RESULT__:")
print(json.dumps({"count": count, "projects": found_projects}))"""

env_args = {'var_function-call-12957010085961315651': ['Funding'], 'var_function-call-12957010085961315256': ['civic_docs'], 'var_function-call-9221482571475141474': 'file_storage/function-call-9221482571475141474.json', 'var_function-call-9221482571475141387': 'file_storage/function-call-9221482571475141387.json', 'var_function-call-17488906604846225691': 'file_storage/function-call-17488906604846225691.json', 'var_function-call-5601184432078709408': 'Success'}

exec(code, env_args)
