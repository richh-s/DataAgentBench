code = """import json

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Create dict of funded projects
funded_projects = {}
for record in funding_data:
    funded_projects[record['Project_Name'].strip().lower()] = int(record['Amount'])

# Load civic docs
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Simple parsing to find design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if 'Capital Improvement Projects' in line_clean and 'Design' in line_clean:
            in_design_section = True
            continue
        if in_design_section and ('Construction' in line_clean or 'Not Started' in line_clean or 'Disaster Recovery' in line_clean):
            break
        if in_design_section and line_clean and len(line_clean) > 10:
            if 'Updates:' in line_clean or 'Project Schedule:' in line_clean or 'Estimated Schedule:' in line_clean:
                continue
            if not any(x in line_clean for x in ['Capital Improvement', 'Page', 'Item', 'RECOMMENDED ACTION', 'DISCUSSION', '(cid:', '▪', '•']):
                design_projects.append(line_clean)

# Count matches
matched = 0
for project in design_projects:
    proj_lower = project.lower()
    if proj_lower in funded_projects and funded_projects[proj_lower] > 50000:
        matched += 1

print('__RESULT__:')
print(json.dumps({'design_projects_found': len(design_projects), 'count_over_50000': matched}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
