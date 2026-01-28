code = """import json

# Load both data sources
funding_records = []
mongo_docs = []

# Access funding data
funding_path = var_functions.query_db_6
with open(funding_path) as f:
    funding_records = json.load(f)

# Access mongo data  
mongo_path = var_functions.query_db_2
with open(mongo_path) as f:
    mongo_docs = json.load(f)

# Get projects with funding > 50000
funding_projects_50k = []
for f in funding_records:
    if int(f['Amount']) > 50000:
        funding_projects_50k.append(f['Project_Name'])

print('Projects with funding > 50000:', len(funding_projects_50k))

# Extract design status projects from mongo
projects_in_design = []
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        
        # Check for design section header
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
            continue
        
        # Check for end of design section  
        if in_design_section and ('(Construction)' in clean_line or '(Not Started)' in clean_line):
            in_design_section = False
            continue
            
        # Extract project names within design section
        if in_design_section and clean_line and not clean_line.startswith('(') and not clean_line.startswith('•'):
            # Skip non-project lines
            skip_terms = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'To:', 'Subject:', 'Page', 'Prepared by:', 'Approved by:', 'Date prepared:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Consultant', 'Staff is', 'Staff will', 'City is', 'City will', 'Project is', 'Plans are', 'Bids are', 'Construction']
            
            should_skip = False
            for term in skip_terms:
                if term in clean_line:
                    should_skip = True
                    break
            
            if not should_skip and len(clean_line) > 5 and not clean_line.isupper():
                # Clean up project name
                project_name = clean_line.strip('•- ')
                projects_in_design.append(project_name)

print('Projects in design status found:', len(projects_in_design))

# Find matches between funding projects and design projects
matching_projects = []
for funding_name in funding_projects_50k:
    for design_name in projects_in_design:
        # Case-insensitive partial matching
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            if funding_name not in matching_projects:  # Avoid duplicates
                matching_projects.append(funding_name)
                break

result = len(matching_projects)
print('Final matching project count:', result)
print('Sample matches:', matching_projects[:10])

__RESULT__:
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
