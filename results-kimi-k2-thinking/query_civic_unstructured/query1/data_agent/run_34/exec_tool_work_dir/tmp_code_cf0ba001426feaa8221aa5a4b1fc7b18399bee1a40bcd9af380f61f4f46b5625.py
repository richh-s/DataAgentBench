code = """import json
import pandas as pd
import re

# Load funding data
funding_file = locals()['var_functions.query_db:5']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:12']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Process funding data
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects from civic documents
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        
        # Split into sections by looking for patterns
        sections = design_section.split('\n\n')
        
        for section in sections:
            clean_section = section.strip()
            # A project name typically: starts with uppercase, not a marker, reasonable length, has multiple uppercase characters
            if (clean_section and 
                len(clean_section) > 10 and 
                len(clean_section) < 300 and
                not clean_section.startswith('Capital Improvement') and
                not clean_section.startswith('(cid') and
                sum(c.isupper() for c in clean_section[:30]) >= 3):
                
                # Found a potential project name
                design_projects.append(clean_section)

# Remove exact duplicates
design_projects = list(set(design_projects))

# Filter funding for design projects with amount > 50000
matching_funding = []
for _, row in funding_df.iterrows():
    amount = row['Amount']
    if amount > 50000:
        project_name = row['Project_Name']
        
        # Check for exact match
        if project_name in design_projects:
            matching_funding.append(row.to_dict())
        else:
            # Check for similar match (base name without suffix)
            base_name = project_name.split(' (')[0]
            for design_proj in design_projects:
                if base_name in design_proj or design_proj in project_name:
                    matching_funding.append(row.to_dict())
                    break

print('__RESULT__:')
print(json.dumps({
    'design_projects_count': len(design_projects),
    'matching_projects': len(matching_funding),
    'projects': matching_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
