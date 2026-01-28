code = """import json
import re

# Load funding data
f_file = str(locals()['var_functions.query_db:36'])
c_file = str(locals()['var_functions.query_db:37'])

with open(f_file) as f:
    funding = json.load(f)
with open(c_file) as f:
    docs = json.load(f)

# Create funding lookup map
fund_lookup = {}
for rec in funding:
    name = rec['Project_Name'].lower().strip()
    amount = int(rec['Amount'])
    fund_lookup[name] = amount

print('Funding records: ' + str(len(funding)))
print('Civic docs: ' + str(len(docs)))

# Extract capital design projects
design_projs = set()
for doc in docs:
    text = doc.get('text', '')
    sections = text.split('Capital Improvement Projects (Design)')
    if len(sections) > 1:
        design_section = sections[1].split('\n\n')[0]
        for line in design_section.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('('):
                low = line.lower()
                keywords = ['updates', 'schedule', 'complete design', 'advertise', 'begin construction']
                if not any(k in low for k in keywords):
                    design_projs.add(low)

print('Design projects: ' + str(len(design_projs)))

# Count funded > 50k
counter = 0
for proj in design_projs:
    if proj in fund_lookup and fund_lookup[proj] > 50000:
        counter = counter + 1
    else:
        base = re.sub(r' $', '', proj)
        if base in fund_lookup and fund_lookup[base] > 50000:
            counter = counter + 1

result = counter
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'num_docs': 5, 'num_funding': 276, 'first_doc_length': 9796}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
