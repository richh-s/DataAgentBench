code = """import json
import re

funding_path = locals()['var_function-call-11583348027309783975']
civic_docs_path = locals()['var_function-call-7486836115047757941']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

target_projects = set()
for record in funding_data:
    try:
        amt = float(record.get('Amount', 0))
    except:
        amt = 0
    if amt > 50000:
        name = record.get('Project_Name', '').strip()
        is_disaster = False
        suffixes = ['(FEMA', '(CalJPIA', '(CalOES', 'FEMA Project', 'CalOES Project']
        for s in suffixes:
            if s in name:
                is_disaster = True
                break
        if not is_disaster and name:
            target_projects.add(name)

def get_date_str(filename):
    match = re.search('(\\d{8})', filename)
    if match:
        return match.group(1)
    return '00000000'

def sort_key(doc):
    d = get_date_str(doc.get('filename', ''))
    if len(d) == 8:
        return d[4:] + d[:2] + d[2:4]
    return '00000000'

civic_docs.sort(key=sort_key, reverse=True)

headers_design = ['Capital Improvement Projects (Design)']
headers_other = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']

found_status = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_status = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        is_header = False
        for h in headers_design:
            if h in line_clean:
                current_status = 'Design'
                is_header = True
                break
        if not is_header:
            for h in headers_other:
                if h in line_clean:
                    current_status = 'Other'
                    is_header = True
                    break
        
        if is_header:
            continue
            
        if current_status is not None:
            if line_clean in target_projects:
                if line_clean not in found_status:
                    found_status[line_clean] = current_status

count = sum(1 for s in found_status.values() if s == 'Design')

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-11583348027309783975': 'file_storage/function-call-11583348027309783975.json', 'var_function-call-11583348027309784792': 'file_storage/function-call-11583348027309784792.json', 'var_function-call-7486836115047757941': 'file_storage/function-call-7486836115047757941.json'}

exec(code, env_args)
