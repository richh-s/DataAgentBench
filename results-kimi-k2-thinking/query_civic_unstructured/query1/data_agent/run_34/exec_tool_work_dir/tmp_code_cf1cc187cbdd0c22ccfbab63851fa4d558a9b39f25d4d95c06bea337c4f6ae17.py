code = """import json
import pandas as pd
import re

# Get file paths from storage
funding_file_path = locals()['var_functions.query_db:5']
civic_file_path = locals()['var_functions.query_db:12']

# Load data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_file_path, 'r') as f:
    civic_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Extract projects from civic documents
design_projects = []

for doc in civic_data:
    text = doc['text']
    
    # Look for 'Capital Improvement Projects (Design)' section
    design_section_match = re.search(
        r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|$)',
        text,
        re.DOTALL
    )
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Find project names - they appear as bold/standalone lines in the design section
        # Pattern: project name followed by '(cid:190)' marker
        project_matches = re.findall(
            r'\n\n([A-Z][^\n]{5,100}?)(?=\n\n\(cid:190\)|\Z)',
            design_section
        )
        
        for proj in project_matches:
            proj_clean = proj.strip()
            if proj_clean and len(proj_clean) < 150:  # Filter out noise
                design_projects.append({
                    'Project_Name': proj_clean,
                    'status': 'design'
                })

# Create DataFrame of design projects
design_df = pd.DataFrame(design_projects)

print('__RESULT__:')
print(json.dumps({
    'design_projects_found': len(design_df),
    'sample_design_projects': design_df['Project_Name'].head(10).tolist()
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
