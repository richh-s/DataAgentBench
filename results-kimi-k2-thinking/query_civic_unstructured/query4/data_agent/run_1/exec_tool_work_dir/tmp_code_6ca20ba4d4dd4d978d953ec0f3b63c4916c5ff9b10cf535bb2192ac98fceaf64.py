code = """import json

# Load the civic documents that mention 2022
civic_file = var_functions.query_db:70
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Load all funding data
funding_file = var_functions.query_db:71
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_data)))

# Extract Spring 2022 projects
spring_months = ['March', 'April', 'May', 'Spring']
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check if line contains 2022 and spring months
        if '2022' in line:
            has_spring = any(month in line for month in spring_months)
            if has_spring:
                # Look backwards for project name (up to 5 lines)
                for j in range(max(0, i-5), i):
                    prev_line = lines[j].strip()
                    # Heuristic: project names are capitalized, reasonable length, not headers
                    if (prev_line and len(prev_line) > 8 and prev_line[0].isupper() and
                        ':' not in prev_line and 'Page' not in prev_line and
                        'Item' not in prev_line and 'Agenda' not in prev_line):
                        spring_projects.add(prev_line)
                        break

print('Found %d unique Spring 2022 projects' % len(spring_projects))

# Create a lookup dictionary for funding by project name
funding_dict = {}
for fund in funding_data:
    funding_dict[fund['Project_Name'].lower()] = int(fund['Amount'])

# Match projects with funding
total_funding = 0
matched_projects = 0

for proj in spring_projects:
    proj_lower = proj.lower()
    # Try exact match or partial match
    for fund_name, amount in funding_dict.items():
        if proj_lower == fund_name or proj_lower in fund_name or fund_name in proj_lower:
            total_funding += amount
            matched_projects += 1
            break

result = {
    "spring_2022_project_count": len(spring_projects),
    "total_funding_usd": total_funding,
    "matched_with_funding": matched_projects,
    "example_projects": list(spring_projects)[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'City Hall Roof Replacement', 'Amount': '79000'}, {'Project_Name': 'City Hall Solar Project', 'Amount': '38000'}, {'Project_Name': 'City Traffic Signals Backup Power', 'Amount': '85000'}, {'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Amount': '10000'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Amount': '30000'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Amount': '64000'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Amount': '45000'}, {'Project_Name': 'Civic Center Way Improvements', 'Amount': '37000'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
