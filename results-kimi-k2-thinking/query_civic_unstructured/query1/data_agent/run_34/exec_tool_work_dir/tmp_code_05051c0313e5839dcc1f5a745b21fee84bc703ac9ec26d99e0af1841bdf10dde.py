code = """import json
import pandas as pd

# Load data from files
funding_path = locals()['var_functions.query_db:5']
civic_path = locals()['var_functions.query_db:12']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Process funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design project names systematically
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find start and end positions
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        
        # Look for project names (they appear before the cid markers)
        lines = design_section.split('\n')
        for i in range(len(lines) - 1):
            current_line = lines[i].strip()
            next_line = lines[i + 1].strip()
            
            # Check if current line is a project name
            if (current_line and 
                next_line.startswith('(cid:190)') and
                not current_line.startswith('Capital Improvement') and
                not current_line.startswith('(') and
                len(current_line) > 10):
                design_projects.append(current_line)

# Remove duplicates
unique_design = list(set(design_projects))

# Filter for high funding and match with design projects
count = 0
matched_names = []

high_funding = funding_df[funding_df['Amount'] > 50000]

for _, row in high_funding.iterrows():
    fund_name = row['Project_Name']
    amount = row['Amount']
    
    # Direct match
    if fund_name in unique_design:
        count += 1
        matched_names.append(fund_name)
    else:
        # Base name match for variations like "Project (FEMA)"
        base_name = fund_name
        if '(' in base_name:
            base_name = base_name.split('(')[0].strip()
        
        for design_proj in unique_design:
            if base_name in design_proj:
                count += 1
                matched_names.append(fund_name)
                break

# Filter to keep only capital projects (exclude disaster/FEMA projects)
capital_matched = [name for name in matched_names if 'fema' not in name.lower() and 'disaster' not in name.lower()]

result = {
    'count': len(capital_matched),
    'capital_design_projects': capital_matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
