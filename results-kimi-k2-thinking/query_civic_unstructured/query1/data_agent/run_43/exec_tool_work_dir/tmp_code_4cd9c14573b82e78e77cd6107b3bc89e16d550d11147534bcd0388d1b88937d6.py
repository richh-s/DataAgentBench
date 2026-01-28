code = """import json

# Load data from the JSON files
f_file = open(var_functions.query_db:5)
funding_records = json.load(f_file)
f_file.close()

c_file = open(var_functions.query_db:6)
civic_docs = json.load(c_file)
c_file.close()

# Count funding records > 50000
large_funding = [item for item in funding_records if int(item['Amount']) > 50000]

# Create a simple project extraction
project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        # Extract lines that look like project names
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 5 and not any(w in line.lower() for w in ['page', 'schedule', 'updates', 'project description']):
                if line[0].isalpha() or line.startswith('•'):
                    project_names.append(line.replace('• ', '').strip())

# Remove duplicates
unique_projects = list(set(project_names))

# Build funding map
funding_map = {}
for item in large_funding:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Count matches 
count = 0
for project in unique_projects:
    for funded_name in funding_map:
        # Check if names match closely
        p = project.lower()
        f = funded_name.lower()
        if p in f or f in p:
            if abs(len(project) - len(funded_name)) < 40:
                count += 1
                break

print('__RESULT__:')
print(json.dumps({'count': count, 'total_design_projects': len(unique_projects), 'total_funded_projects': len(large_funding)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
