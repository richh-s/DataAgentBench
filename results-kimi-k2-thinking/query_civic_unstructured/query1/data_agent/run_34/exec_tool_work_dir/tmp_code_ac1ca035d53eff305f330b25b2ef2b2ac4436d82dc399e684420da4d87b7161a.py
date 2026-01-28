code = """import json, pandas as pd, re

# Load data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_functions.query_db:12'], 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects more comprehensively
all_design_projects = []

for doc in civic_data:
    text = doc['text']
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        
        # Split into paragraphs
        paragraphs = design_section.split('\n\n')
        for para in paragraphs:
            clean_para = para.strip()
            # Project names are typically title case and followed by a marker
            if (clean_para and 
                len(clean_para) > 10 and 
                len(clean_para) < 200 and
                not clean_para.startswith('Capital') and
                not clean_para.startswith('(') and
                sum(1 for c in clean_para if c.isupper()) > 5):  # Has multiple uppercase letters
                all_design_projects.append(clean_para)

# Remove exact duplicates
all_design_projects = list(set(all_design_projects))

# Map to find matches between funding and design projects
matches = []
for idx, row in funding_df.iterrows():
    if row['Amount'] > 50000:
        funding_name = row['Project_Name']
        # Check if base name is in any design project (handle suffixes)
        base_name = funding_name.split(' (')[0]  # Remove suffixes like " (FEMA Project)"
        
        for design_proj in all_design_projects:
            if base_name in design_proj or design_proj in funding_name:
                matches.append({
                    'funding_name': funding_name,
                    'design_name': design_proj,
                    'amount': row['Amount']
                })
                break

print('__RESULT__:')
print(json.dumps({
    'design_projects_found': len(all_design_projects),
    'design_projects': all_design_projects,
    'funding_over_50k': len(funding_df[funding_df['Amount'] > 50000]),
    'matches_count': len(matches),
    'matches': matches
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
