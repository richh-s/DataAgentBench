code = """import json

# Access the stored results using locals() to handle special variable names
mongo_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

print('Mongo path:', mongo_path)
print('Funding path:', funding_path)

# Load funding data
with open(funding_path) as f:
    funding_data = json.load(f)

# Load mongo data
with open(mongo_path) as f:
    mongo_docs = json.load(f)

# Get projects with funding > $50,000
funding_names = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        funding_names.append(f['Project_Name'])

# Extract design projects from mongo
projects_in_design = []
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
        elif '(Construction)' in clean_line or '(Not Started)' in clean_line:
            in_design_section = False
        elif in_design_section and clean_line and not clean_line.startswith('(') and not clean_line.startswith('•'):
            # Skip non-project lines
            skip_terms = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'Approved by:', 'Date prepared:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is', 'Staff will', 'City is', 'City will', 'Project is', 'Plans are', 'Bids are']
            should_skip = any(term in clean_line for term in skip_terms)
            if not should_skip and len(clean_line) > 5 and not clean_line.isupper():
                project_name = clean_line.strip('•- ')
                projects_in_design.append(project_name)

# Find matches between funding projects and design projects
matching_count = 0
matched_names = []

for funding_name in funding_names:
    for design_name in projects_in_design:
        # Case-insensitive partial matching
        if (funding_name.lower() in design_name.lower() or 
            design_name.lower() in funding_name.lower()):
            if funding_name not in matched_names:
                matching_count += 1
                matched_names.append(funding_name)
                break

print('Total matching projects:', matching_count)
print('Sample matches:', matched_names[:10])

__RESULT__:
print(json.dumps(matching_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
