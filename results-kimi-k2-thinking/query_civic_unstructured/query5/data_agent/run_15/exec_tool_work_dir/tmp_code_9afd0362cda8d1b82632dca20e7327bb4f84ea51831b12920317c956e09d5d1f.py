code = """import json
import re

# Load the MongoDB results file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    documents = json.load(f)

# Extract disaster-related projects that started in 2022
disaster_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for disasters projects
    if re.search(r'disaster|FEMA|CalOES|CalJPIA|Woolsey Fire', text, re.IGNORECASE):
        # Split into lines for processing
        lines = text.split('\n')
        for idx, line in enumerate(lines):
            # Look for 2022 dates
            if re.search(r'2022', line) and not re.search(r'2022-2023|FY 2022', line):
                # Look for project context
                for i in range(max(0, idx-5), idx):
                    prev_line = lines[i].strip()
                    if prev_line and len(prev_line) > 10:
                        # Check if it's likely a project name
                        has_project_indicators = re.search(r'Project|Repair|Improvement|Construction', prev_line, re.IGNORECASE)
                        if has_project_indicators:
                            disaster_projects_2022.append({
                                'project': prev_line,
                                'date_info': line.strip(),
                                'filename': filename
                            })
                            break

# Get unique projects
unique_projects = []
seen = set()
for proj in disaster_projects_2022:
    key = proj['project']
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

result_text = f"Found {len(unique_projects)} disaster-related projects from 2022:\n"
for p in unique_projects[:10]:
    result_text += f"- {p['project']}\n"

print('__RESULT__:')
print(json.dumps(result_text))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
