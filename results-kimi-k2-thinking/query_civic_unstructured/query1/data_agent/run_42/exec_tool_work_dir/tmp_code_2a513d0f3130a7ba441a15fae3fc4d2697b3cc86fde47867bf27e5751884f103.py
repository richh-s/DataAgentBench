code = """import json

# Access variables using the correct identifiers
mongo_path = var_functions.query_db_2
funding_path = var_functions.query_db_6

# Load and analyze funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Filter funding > $50,000
funding_over_50k = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        funding_over_50k.append(f['Project_Name'])

# Load and analyze mongo data
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Extract projects with design status
design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find project names in design section
        lines = text.split('\n')
        in_design_section = False
        for line in lines:
            clean = line.strip()
            if 'Capital Improvement Projects (Design)' in clean:
                in_design_section = True
            elif '(Construction)' in clean or '(Not Started)' in clean:
                in_design_section = False
            elif in_design_section and clean and not clean.startswith('(') and not clean.startswith('•'):
                # Filter out non-project lines
                skip_keywords = ['Updates:', 'Schedule:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION']
                staff_words = ['Consultant', 'Staff is', 'Staff will', 'City is', 'Project is', 'Plans are', 'Bids are']
                if not any(kw in clean for kw in skip_keywords) and not any(word in clean for word in staff_words):
                    if len(clean) > 5 and not clean.isupper():
                        design_projects.append(clean.strip('•- '))

# Find intersection
matching_projects = []
for project_name in funding_over_50k:
    # Check if project name or a close variation appears in design_projects
    for design_name in design_projects:
        if project_name.lower() in design_name.lower() or design_name.lower() in project_name.lower():
            matching_projects.append((project_name, design_name))
            break

# Output results
result_count = len(matching_projects)
print('Total matching projects:', result_count)
print('\nSample matches:')
for i, (p1, p2) in enumerate(matching_projects[:10]):
    print(str(i+1) + '. Funding:', p1, '| Design:', p2)

__RESULT__:
print(json.dumps(result_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
