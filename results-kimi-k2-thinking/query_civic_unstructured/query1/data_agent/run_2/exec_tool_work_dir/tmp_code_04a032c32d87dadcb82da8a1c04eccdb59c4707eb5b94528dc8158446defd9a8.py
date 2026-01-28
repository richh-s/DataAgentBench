code = """import json
import re

# Read the funding data
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Create lookup dictionary
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name.lower()] = amount

# Read civic documents
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(|Disaster Recovery Projects|$)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section = match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Filters to identify actual project names
            if len(line) > 10 and not line.startswith('(') and not line.startswith('cid:'):
                if 'Updates' not in line and 'Project Schedule' not in line:
                    if 'Complete Design' not in line and 'Advertise' not in line:
                        # Remove bullet markers
                        clean_line = line.strip('*- ').strip()
                        if clean_line:
                            design_projects.add(clean_line.lower())

# Match with funding
matches = []
for proj in design_projects:
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        if amount > 50000:
            matches.append(proj)
    else:
        # Partial match check
        for fund_name in funding_lookup:
            if proj in fund_name or fund_name in proj:
                amount = funding_lookup[fund_name]
                if amount > 50000:
                    matches.append(proj)
                    break

result = {
    'count': len(matches),
    'examples': matches[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
