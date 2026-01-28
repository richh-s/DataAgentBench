code = """import json

funding_path = 'var_functions.query_db:6'
civic_path = 'var_functions.query_db:64'

# Load data manually using the storage keys approach
funding_data = locals()['var_functions.query_db:92']  # Smaller query result
civic_data = locals()['var_functions.query_db:64']

# Step 1: Get funding projects > $50,000 (using the smaller sample set)
high_funding_names = set(r['Project_Name'] for r in funding_data)

# Step 2: Extract design capital projects from civic documents
design_projects = []
for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Extract design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1].split('DISCUSSION')[0]
        for line in design_section.split('\n'):
            line = line.strip()
            # Filter for project names
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                    if 'Subject:' not in line and 'RECOMMENDED' not in line:
                        if len(line) > 5 and line[0].isupper():
                            design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Count matches
matched = 0
for proj in unique_design:
    for fund_name in high_funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:80': ['civic_docs'], 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json', 'var_functions.query_db:96': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}]}

exec(code, env_args)
