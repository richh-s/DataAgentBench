code = """import json

# Load both datasets from file paths
funding_path = 'var_functions.query_db_6'
mongo_path = 'var_functions.query_db_2'

# Access the actual variables using locals() since they have special characters in names
funding_data = json.load(open(locals()['var_functions.query_db_6']))
mongo_docs = json.load(open(locals()['var_functions.query_db_2']))

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(mongo_docs), 'mongo docs')

# Get projects with funding > $50,000
funding_over_50k = {}
for record in funding_data:
    if record['Amount'] > 50000:
        funding_over_50k[record['Project_Name']] = record

print('Projects with funding > $50k:', len(funding_over_50k))

# Extract design projects from mongo docs
design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for i, line in enumerate(lines):
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
            # Skip obvious non-project lines
            skip_patterns = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 
                           'Advertise:', 'Begin Construction:', 'To:', 'Subject:', 'Page', 
                           'Prepared by:', 'Approved by:', 'Date prepared:', 'RECOMMENDED ACTION', 
                           'DISCUSSION:', 'Consultant', 'Staff is', 'Staff will', 'City is', 
                           'City will', 'Project is', 'Plans are', 'Bids are', 'Construction']
            
            should_skip = any(pattern in clean_line for pattern in skip_patterns)
            
            if not should_skip and len(clean_line) > 5 and not clean_line.isupper():
                project_name = clean_line.strip('•- ')
                design_projects.append({
                    'name': project_name,
                    'status': 'design',
                    'type': 'capital',
                    'funding_potential': funding_over_50k.get(project_name) is not None
                })

print('Design projects extracted:', len(design_projects))
print('Sample design projects:', [p['name'] for p in design_projects[:10]])

# Find matches with funding > $50k
matches = []
for design_proj in design_projects:
    design_name = design_proj['name']
    
    # Check for direct match or partial match
    for funding_name in funding_over_50k.keys():
        # Case-insensitive partial matching
        if (funding_name.lower() in design_name.lower() or 
            design_name.lower() in funding_name.lower()):
            if funding_name not in matches:
                matches.append(funding_name)
                break

print('Final matching count:', len(matches))
print('Sample matches:', matches[:10])

__RESULT__:
print(json.dumps(len(matches)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
