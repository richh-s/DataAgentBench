code = """import json

# Load all funding data > $50,000
funding_file = var_functions.query_db:50
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic document to extract design projects
civic_file = var_functions.query_db:28
with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract capital design projects from civic documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the "Capital Improvement Projects (Design)" section
    design_section_start = text.lower().find('capital improvement projects (design)')
    if design_section_start >= 0:
        # Get section up to next major heading
        section_end = len(text)
        for marker in ['capital improvement projects (construction)', 'disaster recovery projects', 'capital improvement projects (not started)']:
            pos = text.lower().find(marker, design_section_start)
            if pos > design_section_start and pos < section_end:
                section_end = pos
        
        design_section = text[design_section_start:section_end]
        
        # Extract project names (lines that look like project names)
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip headers and markers
            lower_line = line.lower()
            if any(skip in lower_line for skip in ['capital improvement', 'design', 'updates:', 'project schedule', 'subject:', 'recommended action', 'date prepared']):
                continue
            
            # Check if this is a project name (followed by project details)
            if i + 1 < len(lines):
                next_line = lines[i+1].strip().lower()
                if 'updates:' in next_line or 'project schedule' in next_line or next_line.startswith('('):
                    # Clean up the project name
                    clean_name = line.lstrip('0123456789.-• ')
                    if len(clean_name) > 8:
                        design_projects.append(clean_name)

# Filter funding to only amounts > $50,000
high_funding = []
for record in funding_data:
    try:
        amount = int(record['Amount'])
        if amount > 50000:
            high_funding.append({
                'project_name': record['Project_Name'],
                'amount': amount
            })
    except:
        pass

# Match design projects with funding records
matches = set()
for design_name in design_projects:
    design_lower = design_name.lower()
    
    for fund in high_funding:
        fund_lower = fund['project_name'].lower()
        
        # Check for direct match or containment
        if (design_lower in fund_lower or 
            fund_lower in design_lower or
            design_lower == fund_lower):
            matches.add(design_name)
            break
        
        # Check for partial matches on key terms
        design_words = set([w.lower() for w in design_name.split() if len(w) > 4])
        fund_words = set([w.lower() for w in fund['project_name'].split() if len(w) > 4])
        
        # If they share at least 3 key terms, it's a match
        if len(design_words.intersection(fund_words)) >= 3:
            matches.add(design_name)
            break

# Return the count
result = len(matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': [{'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '87000'}, {'Amount': '81000'}, {'Amount': '93000'}, {'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '64000'}, {'Amount': '53000'}, {'Amount': '54000'}, {'Amount': '68000'}, {'Amount': '58000'}, {'Amount': '80000'}, {'Amount': '90000'}, {'Amount': '56000'}, {'Amount': '94000'}, {'Amount': '91000'}, {'Amount': '56000'}, {'Amount': '57000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '78000'}, {'Amount': '69000'}, {'Amount': '91000'}, {'Amount': '81000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '93000'}, {'Amount': '60000'}, {'Amount': '92000'}, {'Amount': '81000'}, {'Amount': '84000'}, {'Amount': '84000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '86000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '77000'}, {'Amount': '80000'}, {'Amount': '78000'}, {'Amount': '92000'}, {'Amount': '65000'}, {'Amount': '68000'}, {'Amount': '90000'}, {'Amount': '91000'}, {'Amount': '87000'}, {'Amount': '77000'}, {'Amount': '94000'}, {'Amount': '94000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '63000'}, {'Amount': '90000'}, {'Amount': '99000'}, {'Amount': '73000'}, {'Amount': '93000'}, {'Amount': '64000'}, {'Amount': '99000'}, {'Amount': '69000'}, {'Amount': '81000'}, {'Amount': '69000'}, {'Amount': '77000'}, {'Amount': '86000'}, {'Amount': '66000'}, {'Amount': '74000'}, {'Amount': '80000'}, {'Amount': '70000'}, {'Amount': '91000'}, {'Amount': '76000'}, {'Amount': '90000'}, {'Amount': '79000'}, {'Amount': '98000'}, {'Amount': '100000'}, {'Amount': '62000'}, {'Amount': '79000'}, {'Amount': '63000'}, {'Amount': '63000'}, {'Amount': '84000'}, {'Amount': '83000'}, {'Amount': '71000'}, {'Amount': '55000'}, {'Amount': '59000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '87000'}, {'Amount': '65000'}, {'Amount': '53000'}, {'Amount': '96000'}, {'Amount': '61000'}, {'Amount': '69000'}, {'Amount': '78000'}, {'Amount': '60000'}, {'Amount': '82000'}, {'Amount': '92000'}, {'Amount': '69000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '58000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '93000'}, {'Amount': '93000'}, {'Amount': '95000'}, {'Amount': '82000'}, {'Amount': '69000'}, {'Amount': '57000'}, {'Amount': '87000'}, {'Amount': '96000'}, {'Amount': '58000'}, {'Amount': '85000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '78000'}, {'Amount': '94000'}, {'Amount': '92000'}, {'Amount': '63000'}, {'Amount': '72000'}, {'Amount': '65000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '76000'}, {'Amount': '78000'}, {'Amount': '71000'}, {'Amount': '65000'}, {'Amount': '85000'}, {'Amount': '51000'}, {'Amount': '67000'}, {'Amount': '69000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '72000'}, {'Amount': '55000'}, {'Amount': '86000'}, {'Amount': '62000'}, {'Amount': '81000'}, {'Amount': '70000'}, {'Amount': '72000'}, {'Amount': '61000'}, {'Amount': '94000'}, {'Amount': '57000'}, {'Amount': '80000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '55000'}, {'Amount': '68000'}, {'Amount': '78000'}, {'Amount': '98000'}, {'Amount': '71000'}, {'Amount': '85000'}, {'Amount': '77000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '71000'}, {'Amount': '53000'}, {'Amount': '71000'}, {'Amount': '72000'}, {'Amount': '83000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '63000'}, {'Amount': '86000'}, {'Amount': '89000'}, {'Amount': '76000'}, {'Amount': '67000'}, {'Amount': '66000'}, {'Amount': '85000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '94000'}, {'Amount': '67000'}, {'Amount': '86000'}, {'Amount': '100000'}, {'Amount': '99000'}, {'Amount': '68000'}, {'Amount': '97000'}, {'Amount': '90000'}, {'Amount': '94000'}, {'Amount': '82000'}, {'Amount': '98000'}, {'Amount': '99000'}, {'Amount': '79000'}, {'Amount': '66000'}, {'Amount': '86000'}, {'Amount': '65000'}, {'Amount': '51000'}, {'Amount': '96000'}, {'Amount': '83000'}, {'Amount': '96000'}, {'Amount': '76000'}, {'Amount': '66000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '72000'}, {'Amount': '70000'}, {'Amount': '62000'}, {'Amount': '51000'}, {'Amount': '62000'}, {'Amount': '73000'}, {'Amount': '94000'}, {'Amount': '80000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '61000'}, {'Amount': '75000'}, {'Amount': '79000'}, {'Amount': '62000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '66000'}, {'Amount': '99000'}, {'Amount': '90000'}, {'Amount': '80000'}, {'Amount': '80000'}, {'Amount': '100000'}, {'Amount': '63000'}, {'Amount': '71000'}, {'Amount': '80000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '63000'}, {'Amount': '74000'}, {'Amount': '85000'}, {'Amount': '94000'}, {'Amount': '78000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '79000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '59000'}, {'Amount': '62000'}, {'Amount': '70000'}, {'Amount': '58000'}, {'Amount': '94000'}, {'Amount': '93000'}, {'Amount': '73000'}, {'Amount': '85000'}, {'Amount': '66000'}, {'Amount': '77000'}, {'Amount': '68000'}, {'Amount': '93000'}, {'Amount': '89000'}, {'Amount': '60000'}, {'Amount': '52000'}, {'Amount': '96000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '79000'}, {'Amount': '89000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '51000'}, {'Amount': '55000'}, {'Amount': '65000'}, {'Amount': '62000'}, {'Amount': '97000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '97000'}, {'Amount': '73000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '95000'}, {'Amount': '69000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '64000'}, {'Amount': '59000'}, {'Amount': '71000'}], 'var_functions.list_db:62': ['civic_docs'], 'var_functions.query_db:66': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}]}

exec(code, env_args)
