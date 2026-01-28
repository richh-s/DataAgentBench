code = """import json
import re

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {item['Project_Name'].lower().strip(): item for item in funding_data}

# Find park projects completed in 2022
completed_2022_park_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line contains a park project name
        lower_line = line.lower()
        if 'park' in lower_line and len(line) < 80:
            # Look ahead to find completion status and date
            segment = '\n'.join(lines[i:i+8])
            
            # Check if completed in 2022
            if '2022' in segment and ('completed' in segment.lower() or 'construction was completed' in segment.lower()):
                # Clean up the project name
                project_name = line.strip()
                
                # Skip if it's a header or metadata
                skip_words = ['Capital', 'Disaster', 'Public Works', 'Commission', 'RECOMMENDED', 'DISCUSSION']
                if any(word in project_name for word in skip_words):
                    continue
                
                # Find completion date
                completion_match = re.search(r'(?:completed|construction was completed)[\s,]*([A-Za-z\d\-\s,]+2022[A-Za-z\d\-\s,]*)', segment, re.IGNORECASE)
                completion_date = completion_match.group(1).strip() if completion_match else '2022'
                
                completed_2022_park_projects.append({
                    'project_name': project_name,
                    'completion_date': completion_date
                })

# Find unique projects
unique_projects = {}
for proj in completed_2022_park_projects:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

completed_2022_park_projects = list(unique_projects.values())

# Match with funding data and sum amounts
matched_projects = []
total_funding = 0

for project in completed_2022_park_projects:
    proj_name = project['project_name']
    
    # Try exact match first
    if proj_name.lower() in funding_lookup:
        funding_info = funding_lookup[proj_name.lower()]
        amount = int(funding_info['Amount'])
        total_funding += amount
        matched_projects.append({
            'project_name': proj_name,
            'funding_amount': amount,
            'completion_date': project['completion_date']
        })
    else:
        # Try partial matching for variations
        for fund_name, fund_info in funding_lookup.items():
            # Check if the core project name matches
            core_name = proj_name.lower().replace('project', '').strip()
            if core_name in fund_name or fund_name in core_name:
                amount = int(fund_info['Amount'])
                total_funding += amount
                matched_projects.append({
                    'project_name': proj_name,
                    'funding_amount': amount,
                    'completion_date': project['completion_date']
                })
                break

print('__RESULT__:')
result = {
    'completed_2022_park_projects_found': len(completed_2022_park_projects),
    'matched_with_funding': len(matched_projects),
    'total_funding_for_2022_completed_parks': total_funding,
    'matched_projects': matched_projects
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:12': {'park_funding_projects_count': 20, 'sample_park_projects': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}]}, 'var_functions.execute_python:18': {'total_park_projects': 20, 'total_funding_all_parks': 1033000, 'sample_projects': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}]}}

exec(code, env_args)
