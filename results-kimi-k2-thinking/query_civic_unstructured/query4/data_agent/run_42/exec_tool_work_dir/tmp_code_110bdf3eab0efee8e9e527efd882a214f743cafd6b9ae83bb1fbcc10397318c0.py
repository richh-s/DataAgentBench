code = """import json
import re

# Access the MongoDB results file path
mongo_path = var_functions.query_db:14

# Read the MongoDB results
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

print(f"MongoDB documents: {len(mongo_docs)}")

# Find projects with Spring 2022 dates
spring_2022_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for project sections
    # Pattern to find project names followed by schedule info with Spring 2022
    patterns = [
        r'([^\n]+?)\n\s*\(cid\:190\) Project Schedule\:.*?\n\s*\(cid\:131\) [^\n]*Spring[^\n]*2022',
        r'([^\n]+?)\n\s*\(cid\:190\) Estimated Schedule\:.*?\n\s*\(cid\:131\) [^\n]*Spring[^\n]*2022',
        r'Begin Construction\:\s*Spring[^\n]*2022',
        r'Complete Final Design\:\s*Spring[^\n]*2022',
        r'Advertise\:\s*Spring[^\n]*2022'
    ]
    
    # Extract potential project names from the text
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Look for schedule lines mentioning Spring 2022
        if 'Spring' in line and '2022' in line:
            # Look backward to find the project name (usually 5-10 lines back)
            for j in range(i-1, max(0, i-15), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('Page'):
                    if len(prev_line) > 3 and 'Project Schedule' not in prev_line:
                        # Clean up the project name
                        proj_name = prev_line.replace('\u2019', "'").strip()
                        if proj_name not in spring_2022_projects:
                            spring_2022_projects.append(proj_name)
                        break

print(f"Found {len(spring_2022_projects)} potential projects:")
for proj in spring_2022_projects:
    print(f"  - {proj}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
