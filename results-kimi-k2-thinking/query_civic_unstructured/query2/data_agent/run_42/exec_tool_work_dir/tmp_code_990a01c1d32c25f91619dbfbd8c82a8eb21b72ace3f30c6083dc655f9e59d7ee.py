code = """import json, re

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

project_names_completed_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Heuristic: project names are usually short (<150 chars) and contain 'park' but not typical headers
        if 'park' in stripped.lower() and len(stripped) < 150:
            # Skip common header lines or bullet markers
            if any(header in stripped.lower() for header in ['capital improvement', 'disaster recovery', 'status report', 'discussion:', 'recommended action:', 'projects', 'agenda item']):
                continue
            # Skip lines that are just numbering or bullets like '4.B.'
            if re.match(r'^\s*\(?cid:\d+\)?.*$', stripped):
                continue
            if re.match(r'^\s*\d+\s*$', stripped):
                continue
            if stripped.startswith('(') and stripped.endswith(')'):
                continue
            # Skip lines with only special characters
            if not re.search(r'[A-Za-z]', stripped):
                continue
            # Now look ahead for status containing 'completed' and '2022'
            for j in range(i, min(len(lines), i+6)):
                status_line = lines[j].strip()
                lower_status = status_line.lower()
                # Look for completed and 2022
                if 'completed' in lower_status and '2022' in status_line:
                    # Ensure not referring to a different project
                    project_names_completed_2022.add(stripped)
                    break

# Convert set to list for JSON serialization
completed_project_list = sorted(list(project_names_completed_2022))

result = {
    'completed_projects': completed_project_list,
    'count': len(completed_project_list)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:26': {'potential_docs_with_2022_completion': 5, 'park_projects_in_funding': 20}}

exec(code, env_args)
