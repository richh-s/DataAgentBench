code = """import json, pandas as pd, re

# Load funding data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(locals()['var_functions.query_db:12'], 'r') as f:
    civic_data = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract design projects by parsing the document structure
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    design_pos = text.find(design_marker)
    construction_pos = text.find(construction_marker)
    
    if design_pos >= 0 and construction_pos > design_pos:
        # Extract design section
        design_section = text[design_pos:construction_pos]
        
        # Split into sections and find project names
        parts = design_section.split('\n\n')
        
        for part in parts:
            clean_part = part.strip()
            # Project names are typically title case, start with letters, reasonable length
            if (clean_part and 
                len(clean_part) > 10 and 
                len(clean_part) < 300 and
                not clean_part.startswith('Capital Improvement') and
                not clean_part.startswith('(cid') and
                clean_part[0].isalpha() and
                clean_part[0].isupper()):
                
                # Check if it has multiple capitalized words (project name characteristic)
                words = clean_part.split()[:8]
                capital_word_count = sum(1 for w in words if w and w[0].isupper())
                
                if capital_word_count >= 2:
                    design_projects.append(clean_part)

# Remove duplicates
unique_design = list(set(design_projects))

# Filter funding > 50000
high_funding = funding_df[funding_df['Amount'] > 50000]

# Match design projects with high funding
capital_design_count = 0
matched_names = []

for _, row in high_funding.iterrows():
    fund_name = row['Project_Name']
    amount = row['Amount']
    
    # Check exact match
    if fund_name in unique_design:
        capital_design_count += 1
        matched_names.append(fund_name)
    else:
        # Check base name match (remove suffix)
        base_name = fund_name
        if ' (' in base_name:
            base_name = base_name.split(' (')[0]
        
        # Look for partial matches
        for design_name in unique_design:
            if (base_name in design_name) or (design_name in fund_name):
                capital_design_count += 1
                matched_names.append(fund_name)
                break

print('__RESULT__:')
print(json.dumps({
    'capital_design_projects_with_over_50k_funding': capital_design_count,
    'matched_projects': matched_names
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}, 'var_functions.execute_python:40': {'design_projects_extracted': 2, 'funding_projects_over_50k': 276, 'matches': [], 'count': 0}}

exec(code, env_args)
