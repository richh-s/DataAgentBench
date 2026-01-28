code = """import json

# Get the file paths from the variables
funding_file_path = locals()['var_functions.query_db:8']
civic_file_path = locals()['var_functions.query_db:10']

print('Funding file:', funding_file_path)
print('Civic file:', civic_file_path)

# Read the data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Search for capital projects with design status
# Combine all civic text for searching
all_civic_text = ' '.join([doc.get('text', '') for doc in civic_docs])

capital_design_projects = []

for project in funding_data:
    proj_name = project['Project_Name']
    amount = int(project['Amount'])
    
    # Check amount > 50000
    if amount > 50000:
        # Check if capital project (not disaster)
        is_disaster = any(x in proj_name for x in ['(FEMA', '(CalJPIA', '(CalOES)'])
        if not is_disaster:
            # Check if in design section
            design_start = all_civic_text.find('Capital Improvement Projects (Design)')
            construction_start = all_civic_text.find('Capital Improvement Projects (Construction)')
            
            if design_start >= 0 and proj_name in all_civic_text:
                # Find position of project
                proj_pos = all_civic_text.find(proj_name)
                
                # Check if in design section (between design_start and construction_start)
                if proj_pos > design_start and (construction_start < 0 or proj_pos < construction_start):
                    capital_design_projects.append(proj_name)

print('Found capital projects with design status:', len(capital_design_projects))
print('Sample:', capital_design_projects[:5])

result = {'count': len(capital_design_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
