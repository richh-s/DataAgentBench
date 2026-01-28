code = """import json

# Load funding data > $50,000
f_file = var_functions.query_db:50
with open(f_file) as f:
    funding_data = json.load(f)

# Load civic document
c_file = var_functions.query_db:28
with open(c_file) as f:
    civic_docs = json.load(f)

# Extract capital design projects from civic document
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Find the design section
    start_pos = text.lower().find('capital improvement projects (design)')
    if start_pos >= 0:
        # Get section until next major heading
        section = text[start_pos:start_pos+2000]
        end_pos = len(section)
        for marker in ['capital improvement projects (construction)', 'disaster recovery projects']:
            pos = section.lower().find(marker)
            if pos > 0:
                end_pos = pos
        
        design_section = section[:end_pos]
        # Extract project names (lines not starting with common markers)
        for line in design_section.split('\n'):
            clean_line = line.strip()
            if len(clean_line) > 10 and not any(s in clean_line.lower()[:30] for s in ['capital improvement', 'design', 'updates:', 'project schedule']):
                if clean_line not in ['•', '●', '■', '□']:
                    # Remove leading numbers/bullets
                    while clean_line and (clean_line[0].isdigit() or clean_line[0] in ['•', '-', '.', '■']):
                        clean_line = clean_line[1:]
                    clean_line = clean_line.strip()
                    if len(clean_line) > 8:
                        design_projects.append(clean_line)

# Filter funding to > $50,000
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]

# Match design projects with funding
matches = set()
for design in design_projects:
    design_lower = design.lower()
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        # Simple substring matching
        if design_lower in fund_name or fund_name in design_lower or design_lower == fund_name:
            matches.add(design)
            break

# Return just the count
result = len(matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': [{'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '87000'}, {'Amount': '81000'}, {'Amount': '93000'}, {'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '64000'}, {'Amount': '53000'}, {'Amount': '54000'}, {'Amount': '68000'}, {'Amount': '58000'}, {'Amount': '80000'}, {'Amount': '90000'}, {'Amount': '56000'}, {'Amount': '94000'}, {'Amount': '91000'}, {'Amount': '56000'}, {'Amount': '57000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '78000'}, {'Amount': '69000'}, {'Amount': '91000'}, {'Amount': '81000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '93000'}, {'Amount': '60000'}, {'Amount': '92000'}, {'Amount': '81000'}, {'Amount': '84000'}, {'Amount': '84000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '86000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '77000'}, {'Amount': '80000'}, {'Amount': '78000'}, {'Amount': '92000'}, {'Amount': '65000'}, {'Amount': '68000'}, {'Amount': '90000'}, {'Amount': '91000'}, {'Amount': '87000'}, {'Amount': '77000'}, {'Amount': '94000'}, {'Amount': '94000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '63000'}, {'Amount': '90000'}, {'Amount': '99000'}, {'Amount': '73000'}, {'Amount': '93000'}, {'Amount': '64000'}, {'Amount': '99000'}, {'Amount': '69000'}, {'Amount': '81000'}, {'Amount': '69000'}, {'Amount': '77000'}, {'Amount': '86000'}, {'Amount': '66000'}, {'Amount': '74000'}, {'Amount': '80000'}, {'Amount': '70000'}, {'Amount': '91000'}, {'Amount': '76000'}, {'Amount': '90000'}, {'Amount': '79000'}, {'Amount': '98000'}, {'Amount': '100000'}, {'Amount': '62000'}, {'Amount': '79000'}, {'Amount': '63000'}, {'Amount': '63000'}, {'Amount': '84000'}, {'Amount': '83000'}, {'Amount': '71000'}, {'Amount': '55000'}, {'Amount': '59000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '87000'}, {'Amount': '65000'}, {'Amount': '53000'}, {'Amount': '96000'}, {'Amount': '61000'}, {'Amount': '69000'}, {'Amount': '78000'}, {'Amount': '60000'}, {'Amount': '82000'}, {'Amount': '92000'}, {'Amount': '69000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '58000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '93000'}, {'Amount': '93000'}, {'Amount': '95000'}, {'Amount': '82000'}, {'Amount': '69000'}, {'Amount': '57000'}, {'Amount': '87000'}, {'Amount': '96000'}, {'Amount': '58000'}, {'Amount': '85000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '78000'}, {'Amount': '94000'}, {'Amount': '92000'}, {'Amount': '63000'}, {'Amount': '72000'}, {'Amount': '65000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '76000'}, {'Amount': '78000'}, {'Amount': '71000'}, {'Amount': '65000'}, {'Amount': '85000'}, {'Amount': '51000'}, {'Amount': '67000'}, {'Amount': '69000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '72000'}, {'Amount': '55000'}, {'Amount': '86000'}, {'Amount': '62000'}, {'Amount': '81000'}, {'Amount': '70000'}, {'Amount': '72000'}, {'Amount': '61000'}, {'Amount': '94000'}, {'Amount': '57000'}, {'Amount': '80000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '55000'}, {'Amount': '68000'}, {'Amount': '78000'}, {'Amount': '98000'}, {'Amount': '71000'}, {'Amount': '85000'}, {'Amount': '77000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '71000'}, {'Amount': '53000'}, {'Amount': '71000'}, {'Amount': '72000'}, {'Amount': '83000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '63000'}, {'Amount': '86000'}, {'Amount': '89000'}, {'Amount': '76000'}, {'Amount': '67000'}, {'Amount': '66000'}, {'Amount': '85000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '94000'}, {'Amount': '67000'}, {'Amount': '86000'}, {'Amount': '100000'}, {'Amount': '99000'}, {'Amount': '68000'}, {'Amount': '97000'}, {'Amount': '90000'}, {'Amount': '94000'}, {'Amount': '82000'}, {'Amount': '98000'}, {'Amount': '99000'}, {'Amount': '79000'}, {'Amount': '66000'}, {'Amount': '86000'}, {'Amount': '65000'}, {'Amount': '51000'}, {'Amount': '96000'}, {'Amount': '83000'}, {'Amount': '96000'}, {'Amount': '76000'}, {'Amount': '66000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '72000'}, {'Amount': '70000'}, {'Amount': '62000'}, {'Amount': '51000'}, {'Amount': '62000'}, {'Amount': '73000'}, {'Amount': '94000'}, {'Amount': '80000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '61000'}, {'Amount': '75000'}, {'Amount': '79000'}, {'Amount': '62000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '66000'}, {'Amount': '99000'}, {'Amount': '90000'}, {'Amount': '80000'}, {'Amount': '80000'}, {'Amount': '100000'}, {'Amount': '63000'}, {'Amount': '71000'}, {'Amount': '80000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '63000'}, {'Amount': '74000'}, {'Amount': '85000'}, {'Amount': '94000'}, {'Amount': '78000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '79000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '59000'}, {'Amount': '62000'}, {'Amount': '70000'}, {'Amount': '58000'}, {'Amount': '94000'}, {'Amount': '93000'}, {'Amount': '73000'}, {'Amount': '85000'}, {'Amount': '66000'}, {'Amount': '77000'}, {'Amount': '68000'}, {'Amount': '93000'}, {'Amount': '89000'}, {'Amount': '60000'}, {'Amount': '52000'}, {'Amount': '96000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '79000'}, {'Amount': '89000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '51000'}, {'Amount': '55000'}, {'Amount': '65000'}, {'Amount': '62000'}, {'Amount': '97000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '97000'}, {'Amount': '73000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '95000'}, {'Amount': '69000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '64000'}, {'Amount': '59000'}, {'Amount': '71000'}], 'var_functions.list_db:62': ['civic_docs'], 'var_functions.query_db:66': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}], 'var_functions.query_db:70': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Malibu Bluffs Park South Walkway'}, {'Project_Name': 'Storm Drain Master Plan'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs'}, {'Project_Name': 'project_41'}, {'Project_Name': 'project_36'}, {'Project_Name': 'project_33'}, {'Project_Name': 'project_4'}, {'Project_Name': 'project_37'}, {'Project_Name': 'project_31'}, {'Project_Name': 'project_35'}, {'Project_Name': 'project_17'}, {'Project_Name': 'project_49'}, {'Project_Name': 'project_50'}, {'Project_Name': 'project_28'}, {'Project_Name': 'project_32'}, {'Project_Name': 'project_26'}, {'Project_Name': 'project_8'}, {'Project_Name': 'project_48'}, {'Project_Name': 'project_2'}, {'Project_Name': 'project_42'}, {'Project_Name': 'project_21'}, {'Project_Name': 'project_38'}, {'Project_Name': 'project_5'}, {'Project_Name': 'project_29'}, {'Project_Name': 'project_20'}, {'Project_Name': 'project_46'}, {'Project_Name': 'project_18'}]}

exec(code, env_args)
