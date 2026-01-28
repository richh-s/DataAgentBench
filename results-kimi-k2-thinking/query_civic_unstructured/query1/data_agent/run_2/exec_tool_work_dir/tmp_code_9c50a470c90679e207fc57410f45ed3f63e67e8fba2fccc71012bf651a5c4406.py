code = """import json
import re

# Read the funding data with Amount > 50000
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for easy lookup: project_name -> amount
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name.lower()] = amount

# Read the civic documents
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for "Capital Improvement Projects (Design)" section
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(|Disaster Recovery Projects|$)', 
                               text, re.DOTALL | re.IGNORECASE)
    
    if design_section:
        section_text = design_section.group(1)
        # Find project names - they typically appear as separate lines
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and common status/update lines
            if (line and 
                not line.startswith('(') and 
                not line.startswith('cid:') and 
                not line.startswith('Updates:') and
                not line.startswith('Project Schedule') and
                not line.startswith('Complete Design') and
                'Project Schedule' not in line and
                'Updates' not in line and
                len(line) > 10):  # Filter out short lines
                
                # Clean up common prefixes and markers
                project_name = line.strip('*-• ').strip()
                if project_name:
                    capital_design_projects.add(project_name.lower())

# Now match with funding data and count those > $50,000
count = 0
matched_projects = []

for project_name_lower in capital_design_projects:
    # Direct match
    if project_name_lower in funding_lookup:
        amount = funding_lookup[project_name_lower]
        if amount > 50000:
            count += 1
            matched_projects.append(project_name_lower)
    else:
        # Try partial matching for variations
        for funding_name, amount in funding_lookup.items():
            if project_name_lower in funding_name or funding_name in project_name_lower:
                if amount > 50000:
                    count += 1
                    matched_projects.append(project_name_lower)
                    break

# Prepare result
result = {
    'count': count,
    'sample_matches': matched_projects[:15]  # Show first 15 for verification
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
