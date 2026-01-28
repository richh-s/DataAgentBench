code = """import json
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_path = locals()['var_functions.query_db:12']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design project names from civic documents
design_project_names = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        
        # Split into lines
        lines = design_section.split('\n')
        for i in range(len(lines) - 1):
            current_line = lines[i].strip()
            next_line = lines[i+1].strip()
            
            # Check if this is a project name: not empty, reasonable length, not a marker,
            # and followed by the update marker
            if (current_line and 
                10 <= len(current_line) <= 200 and
                not current_line.startswith('(') and
                not current_line.startswith('Capital Improvement') and
                '(cid:190)' in next_line):
                
                # Clean up the project name
                clean_name = re.sub(r'[^A-Za-z0-9 &\-\.,\(\)]', '', current_line)
                if clean_name:
                    design_project_names.append(clean_name)

# Remove duplicates
design_project_names = list(set(design_project_names))

# Filter for capital projects (filter out disaster projects)
capital_design_projects = [name for name in design_project_names if 
                          'disaster' not in name.lower() and 
                          'fema' not in name.lower() and
                          'fire' not in name.lower()]

# Match with funding data and filter for amount > 50000
matched_projects = []

for _, row in funding_df.iterrows():
    amount = row['Amount']
    project_name = row['Project_Name']
    
    if amount > 50000:
        # Check for exact match or base name match
        if project_name in capital_design_projects:
            matched_projects.append({
                'Project_Name': project_name,
                'Amount': amount,
                'Funding_Source': row['Funding_Source']
            })
        else:
            # Check if base name (without suffix) matches
            base_name = project_name.split(' (')[0]
            for design_name in capital_design_projects:
                if base_name == design_name or design_name in project_name:
                    matched_projects.append({
                        'Project_Name': project_name,
                        'Amount': amount,
                        'Funding_Source': row['Funding_Source']
                    })
                    break

# Remove duplicates from matched projects
unique_matched = {proj['Project_Name']: proj for proj in matched_projects}
matched_projects = list(unique_matched.values())

print('__RESULT__:')
print(json.dumps({
    'count': len(matched_projects),
    'projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
