code = """import json
import pandas as pd

# Load data from files
funding_path = locals()['var_functions.query_db:5']
civic_path = locals()['var_functions.query_db:12']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects from civic documents
all_design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        
        # Split by double newlines to get paragraphs
        paragraphs = design_section.split('\n\n')
        
        for para in paragraphs:
            clean_para = para.strip()
            # Heuristic: project names are reasonable length, start with capital letter, not markers
            if (clean_para and 
                10 < len(clean_para) < 200 and 
                not clean_para.startswith('Capital Improvement') and
                not clean_para.startswith('(cid') and 
                clean_para[0].isupper()):
                
                # Check if likely a project name (has multiple capitalized words)
                words = clean_para.split()
                capitalized_count = sum(1 for w in words[:5] if w and w[0].isupper())
                
                if capitalized_count >= 2 and len(words) <= 15:
                    all_design_projects.append(clean_para)

# Remove exact duplicates
all_design_projects = list(set(all_design_projects))

# Count funding matches > $50,000
count = 0
matched_projects = []

for _, row in funding_df.iterrows():
    if row['Amount'] > 50000:
        project_name = row['Project_Name']
        
        # Check if project is in design list or base name matches
        if project_name in all_design_projects:
            count += 1
            matched_projects.append(project_name)
        else:
            # Try base name matching (remove suffixes)
            base_name = project_name.split(' (')[0]
            for design_proj in all_design_projects:
                if base_name in design_proj or design_proj in project_name:
                    count += 1
                    matched_projects.append(project_name)
                    break

print('__RESULT__:')
print(json.dumps({
    'design_projects_found': len(all_design_projects),
    'funding_matches': count,
    'matched_project_names': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
