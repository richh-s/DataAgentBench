code = """import json

# Access the variables using locals() to handle the special characters in variable names
data_funding = locals()['var_functions.query_db_6']
data_mongo = locals()['var_functions.query_db_2']

# Load the funding data
with open(data_funding) as f:
    funding_records = json.load(f)

# Load the mongo data  
with open(data_mongo) as f:
    mongo_documents = json.load(f)

# Get projects with funding > $50,000
funding_projects_50k = []
for record in funding_records:
    if record['Amount'] > 50000:
        funding_projects_50k.append(record['Project_Name'])

# Extract projects with design status from mongo documents
projects_in_design = []
for doc in mongo_documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        
        # Check if we're entering the design section
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
            continue
        
        # Check if we're leaving the design section  
        if in_design_section and ('(Construction)' in clean_line or '(Not Started)' in clean_line):
            in_design_section = False
            continue
        
        # Extract project name if in design section
        if in_design_section and clean_line and not clean_line.startswith('(') and not clean_line.startswith('•'):
            # Skip non-project lines
            skip_terms = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 
                         'To:', 'Subject:', 'Page', 'Prepared by:', 'Approved by:', 
                         'Date prepared:', 'RECOMMENDED ACTION', 'DISCUSSION:', 
                         'Consultant', 'Staff is', 'Staff will', 'City is', 'City will', 
                         'Project is', 'Plans are', 'Bids are']
            
            should_skip = any(term in clean_line for term in skip_terms)
            if not should_skip and len(clean_line) > 5 and not clean_line.isupper():
                project_name = clean_line.strip('•- ')
                projects_in_design.append(project_name)

# Find matching projects between funding and design
matching_projects = []
for funding_name in funding_projects_50k:
    for design_name in projects_in_design:
        # Case-insensitive partial matching
        if (funding_name.lower() in design_name.lower() or 
            design_name.lower() in funding_name.lower()):
            if funding_name not in matching_projects:
                matching_projects.append(funding_name)
                break

result = len(matching_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
