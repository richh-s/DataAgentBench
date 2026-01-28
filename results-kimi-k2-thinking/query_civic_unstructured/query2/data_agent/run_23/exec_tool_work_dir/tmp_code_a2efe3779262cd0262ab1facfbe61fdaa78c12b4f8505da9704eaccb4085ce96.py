code = """import json
import re

# Read civic documents from the stored file path
civic_docs_path = "mongo_result_civic_docs.json"
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents")

# First, let's identify projects completed in 2022
completed_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for completion patterns
    matches = re.findall(r'([^\n]{0,100})\n[^\n]*completed[^\n]*2022[^\n]*', text, re.IGNORECASE)
    if matches:
        for match in matches:
            # Extract project name and completion details
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if 'completed' in line.lower() and '2022' in line:
                    # Look backward for project name
                    project_name = None
                    for j in range(max(0, i-5), i):
                        prev_line = lines[j].strip()
                        if prev_line and not prev_line.startswith(('(', '●', '■', '·')):
                            if 'Updates:' not in prev_line and 'Project Schedule:' not in prev_line:
                                if len(prev_line) < 100:
                                    project_name = prev_line
                                    break
                    
                    if project_name:
                        completed_2022_projects.append({
                            'project_name': project_name,
                            'completion_note': line.strip()
                        })
                        break

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in completed_2022_projects:
    if proj['project_name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['project_name'])

print(f"\nFound {len(unique_projects)} unique projects completed in 2022:")
for proj in unique_projects:
    print(f"- {proj['project_name']}")
    print(f"  {proj['completion_note']}")

result = {
    'all_completed_2022': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
