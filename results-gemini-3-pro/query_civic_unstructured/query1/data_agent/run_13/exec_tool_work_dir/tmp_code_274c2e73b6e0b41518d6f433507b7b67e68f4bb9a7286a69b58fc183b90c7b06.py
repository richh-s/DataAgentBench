code = """import json
import sys

print('Starting script...')

try:
    with open('var_function-call-2725984221883882111.json', 'r') as f:
        funding_data = json.load(f)
except Exception as e:
    print('Error loading funding')
    exit()

try:
    with open('var_function-call-2725984221883882726.json', 'r') as f:
        docs_data = json.load(f)
except Exception as e:
    print('Error loading docs')
    exit()

if not docs_data:
    print('Docs data empty')
    exit()

text = docs_data[0]['text']
print(f'Text length: {len(text)}')

start_marker = 'Capital Improvement Projects (Design)'
start_idx = text.find(start_marker)
print(f'Start idx: {start_idx}')

if start_idx == -1:
    print('__RESULT__:')
    print(json.dumps({'count': 0, 'error': 'Marker not found'}))
    sys.exit(0)

end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
end_idx = len(text)
for marker in end_markers:
    idx = text.find(marker, start_idx + len(start_marker))
    if idx != -1 and idx < end_idx:
        end_idx = idx

section_text = text[start_idx + len(start_marker):end_idx]
print(f'Section text length: {len(section_text)}')

lines = section_text.split(chr(10))
candidate_projects = []
funded_projects_set = set()

for item in funding_data:
    try:
        amt = float(item.get('Amount', 0))
        if amt > 50000:
            funded_projects_set.add(item['Project_Name'])
    except:
        pass

for line in lines:
    line = line.strip()
    if not line:
        continue
    if 'Updates:' in line or '(cid:' in line or 'Project Schedule:' in line or 'Agenda Item' in line or 'Page ' in line:
        continue
    if line.startswith('Complete Design') or line.startswith('Advertise') or line.startswith('Begin Construction'):
        continue
    
    candidate_projects.append(line)

confirmed_projects = []
for proj in candidate_projects:
    if proj in funded_projects_set:
        confirmed_projects.append(proj)

unique_projects = list(set(confirmed_projects))

print('__RESULT__:')
print(json.dumps({'count': len(unique_projects), 'projects': unique_projects}))"""

env_args = {'var_function-call-2725984221883880881': ['Funding'], 'var_function-call-2725984221883881496': ['civic_docs'], 'var_function-call-2725984221883882111': 'file_storage/function-call-2725984221883882111.json', 'var_function-call-2725984221883882726': 'file_storage/function-call-2725984221883882726.json', 'var_function-call-1453355728292058709': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
