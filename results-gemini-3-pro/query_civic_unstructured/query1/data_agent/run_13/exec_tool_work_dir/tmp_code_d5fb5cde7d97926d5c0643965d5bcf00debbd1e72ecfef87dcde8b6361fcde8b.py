code = """import json

# Get file paths from local variables
funding_path = locals()['var_function-call-2725984221883882111']
docs_path = locals()['var_function-call-2725984221883882726']

# Load Funding Data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funded_projects_set = set()
for item in funding_data:
    try:
        amt = float(item.get('Amount', 0))
        if amt > 50000:
            funded_projects_set.add(item['Project_Name'])
    except ValueError:
        continue

# Load Civic Docs Data
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

text = docs_data[0]['text']

# Extract Capital Projects (Design)
start_marker = 'Capital Improvement Projects (Design)'
end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']

start_idx = text.find(start_marker)
if start_idx == -1:
    print('__RESULT__:')
    print(json.dumps({'count': 0, 'error': 'Marker not found'}))
    exit()

end_idx = len(text)
for marker in end_markers:
    idx = text.find(marker, start_idx + len(start_marker))
    if idx != -1 and idx < end_idx:
        end_idx = idx

section_text = text[start_idx + len(start_marker):end_idx]

lines = section_text.split(chr(10))
candidate_projects = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    # Filter junk
    if 'Updates:' in line or '(cid:' in line or 'Project Schedule:' in line or 'Agenda Item' in line or 'Page ' in line:
        continue
    if line.startswith('Complete Design') or line.startswith('Advertise') or line.startswith('Begin Construction'):
        continue
    if line.startswith('Approved by') or line.startswith('Date prepared') or line.startswith('Final Design'):
        continue
    
    candidate_projects.append(line)

confirmed_projects = []
for proj in candidate_projects:
    if proj in funded_projects_set:
        confirmed_projects.append(proj)

unique_projects = list(set(confirmed_projects))

print('__RESULT__:')
print(json.dumps({'count': len(unique_projects), 'projects': unique_projects, 'candidates': candidate_projects}))"""

env_args = {'var_function-call-2725984221883880881': ['Funding'], 'var_function-call-2725984221883881496': ['civic_docs'], 'var_function-call-2725984221883882111': 'file_storage/function-call-2725984221883882111.json', 'var_function-call-2725984221883882726': 'file_storage/function-call-2725984221883882726.json', 'var_function-call-1453355728292058709': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-15427466270111541878': 1}

exec(code, env_args)
