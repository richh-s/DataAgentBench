code = """import json
civic_docs_path = locals()['var_functions.query_db:4']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Find all lines mentioning Spring 2022 to identify projects
spring_2022_lines = []
project_candidates = set()

for doc_idx, doc in enumerate(civic_docs):
    text = doc['text']
    lines = text.split('\n')
    visited_lines = set()
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean or line_clean in visited_lines:
            continue
        visited_lines.add(line_clean)
        
        # Look for Spring 2022 patterns
        lower_line = line_clean.lower()
        if ('spring' in lower_line and '2022' in lower_line) or \
           ('2022-spring' in lower_line) or \
           ('2022' in lower_line and any(m in lower_line for m in ['mar', 'apr', 'may'])):
            
            spring_2022_lines.append({
                'doc': doc['filename'],
                'line': line_clean,
                'line_number': i
            })
            
            # Look backwards for project name
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if len(prev_line) > 15 and prev_line[0].isupper() and \
                   not prev_line.startswith('Page') and not prev_line.startswith('Item') and \
                   'COMMISSION' not in prev_line and 'AGENDA' not in prev_line:
                    project_candidates.add(prev_line)
                    break

# Filter and clean project names
valid_projects = []
for proj in project_candidates:
    # Remove common headers and footers
    if any(x in proj for x in ['Page', 'Item #', 'PUBLIC WORKS', 'COMMISSION MEETING', 'AGENDA REPORT']):
        continue
    if len(proj) < 10:
        continue
    valid_projects.append(proj)

# Remove duplicates while preserving order
unique_projects = []
seen = set()
for p in valid_projects:
    if p not in seen:
        unique_projects.append(p)
        seen.add(p)

result = {
    'spring_2022_projects': len(unique_projects),
    'project_names': unique_projects,
    'spring_lines_count': len(spring_2022_lines)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}]}

exec(code, env_args)
