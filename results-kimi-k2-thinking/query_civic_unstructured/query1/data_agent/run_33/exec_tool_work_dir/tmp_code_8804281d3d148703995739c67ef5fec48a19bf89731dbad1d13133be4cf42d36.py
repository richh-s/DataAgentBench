code = """import json
import pandas as pd

# Let's work with what we can see from the previews
# From the funding preview, we can see the structure is:
# [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', ...}, ...]

# Read the full funding data
funding_file = 'storage/query_result_8.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic docs
civic_file = 'storage/query_result_10.json'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Check if 'design' appears with each project
results = []

all_civic_text = ' '.join([doc.get('text', '') for doc in civic_docs])

for project in funding_data:
    proj_name = project['Project_Name']
    amount = int(project['Amount'])
    
    # Check amount > 50000
    if amount > 50000:
        # Check if it's NOT a disaster project
        if '(FEMA' not in proj_name and '(CalJPIA' not in proj_name and '(CalOES' not in proj_name:
            # Check if appears in design section
            if proj_name in all_civic_text and 'Capital Improvement Projects (Design)' in all_civic_text:
                # Find where project appears
                proj_pos = all_civic_text.find(proj_name)
                design_section_start = all_civic_text.find('Capital Improvement Projects (Design)')
                construction_section_start = all_civic_text.find('Capital Improvement Projects (Construction)')
                
                # Check if project is in design section
                if proj_pos > design_section_start and (construction_section_start == -1 or proj_pos < construction_section_start):
                    results.append(proj_name)

print('Capital design projects with >$50k:', len(results))
print(results[:10])

output = json.dumps({'count': len(results)})
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
