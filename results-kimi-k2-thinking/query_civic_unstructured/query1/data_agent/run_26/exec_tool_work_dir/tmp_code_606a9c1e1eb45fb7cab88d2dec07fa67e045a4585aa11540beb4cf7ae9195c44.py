code = """import json
import re

# Load the data
funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_documents = json.load(f)

# Create dictionary of funded projects
funded_projects = {}
for record in funding_records:
    project_name = record['Project_Name'].strip().lower()
    funded_projects[project_name] = int(record['Amount'])

# Extract capital projects with design status
design_projects = []
for doc in civic_documents:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find design section
        start_idx = text.index('Capital Improvement Projects (Design)')
        end_idx = text.find('Capital Improvement Projects (Construction)', start_idx)
        if end_idx == -1:
            end_idx = len(text)
        
        section_text = text[start_idx:end_idx]
        lines = section_text.split('\n')
        
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if line_clean and len(line_clean) > 5:
                if '▪' not in line_clean and 'Updates:' not in line_clean and 'Project Schedule:' not in line_clean:
                    if 'Capital Improvement' not in line_clean and 'Page' not in line_clean:
                        if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                            design_projects.append(line_clean.lower())

# Count projects with funding > 50000
count_over_50000 = 0
for project in design_projects:
    if project in funded_projects and funded_projects[project] > 50000:
        count_over_50000 += 1

print('__RESULT__:')
print(json.dumps(count_over_50000))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
