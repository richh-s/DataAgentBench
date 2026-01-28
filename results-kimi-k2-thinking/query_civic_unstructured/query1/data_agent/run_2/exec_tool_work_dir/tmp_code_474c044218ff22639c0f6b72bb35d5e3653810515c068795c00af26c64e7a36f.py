code = """import json

# Access storage variables
funding_var = locals()['var_functions.query_db:5']
civic_var = locals()['var_functions.query_db:2']

# Load JSON data from file paths if they're strings
if isinstance(funding_var, str):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

if isinstance(civic_var, str):
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

# Create funding lookup
funding_dict = {}
for record in funding_data:
    funding_dict[record['Project_Name'].lower()] = int(record['Amount'])

# Extract capital design projects systematically
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Find design section
    idx = lower_text.find('capital improvement projects (design)')
    if idx == -1:
        continue
    
    # Find section end
    end_idx = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = lower_text.find(marker, idx + 10)
        if pos > idx and pos < end_idx:
            end_idx = pos
    
    # Extract project names from this section
    section = text[idx:end_idx]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if 10 < len(line) < 100:
            # Skip non-project lines
            skip_terms = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', '()']
            if not any(term in line for term in skip_terms) and not line.startswith('(') and not line.startswith('cid:'):
                # Clean up the name
                clean_name = line.strip('•*- ').strip()
                if clean_name and ' ' in clean_name:
                    design_projects.add(clean_name.lower())

# Count projects with funding > $50,000
count = 0
total_funded_projects = len([amt for amt in funding_dict.values() if amt > 50000])

for proj in design_projects:
    # Direct match
    if proj in funding_dict and funding_dict[proj] > 50000:
        count += 1
    else:
        # Partial match
        for fund_name in funding_dict:
            if (proj in fund_name or fund_name in proj) and funding_dict[fund_name] > 50000:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
