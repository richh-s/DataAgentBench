code = """import json, pandas as pd

# Load funding data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(locals()['var_functions.query_db:12'], 'r') as f:
    civic_data = json.load(f)

# Create funding DataFrame with numeric amount
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects using simpler pattern matching
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Detect design section start
        if 'Capital Improvement Projects (Design)' in line_clean:
            in_design_section = True
            continue
            
        # Detect construction section start (end of design section)
        if 'Capital Improvement Projects (Construction)' in line_clean:
            in_design_section = False
            continue
            
        # Extract project names from design section
        if in_design_section and line_clean:
            # Project names are followed by '(cid:190)' marker
            if i < len(lines)-1 and '(cid:190)' in lines[i+1]:
                # Filter out section headers and markers
                if (not line_clean.startswith('Capital Improvement') and 
                    not line_clean.startswith('(') and
                    len(line_clean) > 10):
                    design_projects.append(line_clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Count capital design projects with funding > 50000
count = 0
matched_projects = []

for _, row in funding_df.iterrows():
    amount = row['Amount']
    if amount > 50000:
        project_name = row['Project_Name']
        
        # Check if exact match
        if project_name in design_projects:
            count += 1
            matched_projects.append(project_name)
        else:
            # Check base name (remove suffixes like "(FEMA Project)")
            base_name = project_name.split(' (')[0]
            for design_proj in design_projects:
                if base_name in design_proj or design_proj in project_name:
                    count += 1
                    matched_projects.append(project_name)
                    break

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matched_projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
