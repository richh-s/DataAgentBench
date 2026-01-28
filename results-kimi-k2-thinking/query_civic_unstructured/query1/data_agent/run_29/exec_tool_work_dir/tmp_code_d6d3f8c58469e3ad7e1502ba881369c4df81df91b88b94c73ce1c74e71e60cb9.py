code = """import json
import pandas as pd

# Load funding data
funding_file = 'file_storage/functions.query_db:5.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Load all civic documents
civic_file = 'file_storage/functions.query_db:9.json'
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Simple approach - extract project names from design sections
project_names = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    if '(Design)' in text:
        parts = text.split('(Design)')
        if len(parts) > 1:
            design_part = parts[1]
            # Stop at next major section
            for marker in ['(Construction)', '(Not Started)', 'DISASTER RECOVERY']:
                if marker in design_part:
                    design_part = design_part.split(marker)[0]
            
            # Extract lines that look like project names
            lines = design_part.split('\n')
            for line in lines:
                line = line.strip()
                # Skip short lines, bullets, and known headers
                if len(line) > 10 and len(line) < 200:
                    if not any(skip in line for skip in ['cid:', 'Updates', 'Schedule', 'Advertise', 'Construction', 'Page', 'Agenda', 'Discussion', 'Action', '----']):
                        if not line.startswith('(') and not line.startswith('•') and not line.isupper():
                            project_names.add(line)

# Convert to list for processing
design_projects = [{'Project_Name': name, 'Status': 'design', 'Type': 'capital'} for name in project_names]

# Now join with funding data
# Create a mapping of project names to funding amounts
funding_map = dict(zip(df_funding['Project_Name'], df_funding['Amount']))

# Find matches between design projects and funding
matched_projects = []
for proj in design_projects:
    proj_name = proj['Project_Name']
    # Look for exact match or partial match
    if proj_name in funding_map:
        amount = funding_map[proj_name]
        if amount > 50000:
            matched_projects.append({
                'Project_Name': proj_name,
                'Amount': amount,
                'Status': 'design'
            })
    else:
        # Try to find partial matches (e.g., without suffixes)
        for fund_name, amount in funding_map.items():
            if amount > 50000:
                # Check if project name is contained in funding name or vice versa
                if proj_name in fund_name or fund_name in proj_name:
                    matched_projects.append({
                        'Project_Name': proj_name,
                        'Funded_As': fund_name,
                        'Amount': amount,
                        'Status': 'design'
                    })

print('__RESULT__:')
print(json.dumps({
    'design_projects_found': len(design_projects),
    'matched_with_funding': len(matched_projects),
    'sample_matches': matched_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
