code = """import json
import re

# Load the funding data
funding_result = locals()['var_functions.query_db:6']
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load the civic docs data
civic_result = locals()['var_functions.query_db:8']
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

# Initialize list to store disaster projects that started in 2022
disaster_projects_2022 = []

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    project_start_date = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and obvious non-project lines
        if not line or len(line) < 10:
            continue
            
        # Check if this is a project name line
        # Look for indicators like (FEMA Project), (CalOES Project), etc.
        if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
            # This is likely a disaster project
            current_project = line
            
            # Look for schedule information in the next few lines
            next_lines = '\n'.join(lines[i:i+10])
            
            # Look for start/begin dates
            begin_match = re.search(r'Begin[^\n]*?(\d{4}[^\n]*)', next_lines)
            if begin_match:
                date_str = begin_match.group(1)
                project_start_date = date_str.strip()
            else:
                # Look for any 2022 date references
                year_match = re.search(r'(\d{4}[-\s]\w+|\d{4})', next_lines)
                if year_match:
                    project_start_date = year_match.group(1)
            
            # Check if this is a 2022 project
            if project_start_date and '2022' in project_start_date:
                disaster_projects_2022.append({
                    'name': current_project,
                    'st': project_start_date
                })

print("\nFound disaster projects that started in 2022:", len(disaster_projects_2022))

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for project in disaster_projects_2022:
    project_name = project['name']
    
    # Direct match
    if project_name in funding_map:
        amount = funding_map[project_name]
        total_funding += amount
        matched_projects.append((project_name, amount))
    else:
        # Try to find a close match
        # Remove parenthetical suffixes for matching
        base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
        
        for fund_name, amount in funding_map.items():
            # Check if base name matches
            if base_name in fund_name or fund_name in base_name:
                # Additional check to avoid false matches
                if abs(len(base_name) - len(fund_name)) < 30:
                    total_funding += amount
                    matched_projects.append((project_name, amount, fund_name))
                    break

print("\nMatched projects:", len(matched_projects))
print("Total funding:", total_funding)

# Print matched projects for verification
for proj in matched_projects:
    if len(proj) == 2:
        print(f"  {proj[0]}: ${proj[1]:,}")
    else:
        print(f"  {proj[0]} -> {proj[2]}: ${proj[1]:,}")

# Prepare final result
result = {
    "total_funding": total_funding,
    "matched_projects_count": len(matched_projects),
    "projects": matched_projects
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
