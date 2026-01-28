code = """import json

funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']

# Find design section
design_start = text.find('Capital Improvement Projects (Design)')
construction_start = text.find('Capital Improvement Projects (Construction)')

project_names = []

if design_start > 0 and construction_start > design_start:
    design_section = text[design_start:construction_start]
    lines = design_section.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        if line.startswith('(cid:'):
            continue
        if line.startswith('Page'):
            continue
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if '(cid:' in next_line and 'Updates:' in next_line:
                project_names.append(line)

unique_projects = list(set(project_names))

print('__RESULT__:')
print(json.dumps({
    'extracted_projects': unique_projects,
    'count': len(unique_projects),
    'funding_records': len(funding_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
