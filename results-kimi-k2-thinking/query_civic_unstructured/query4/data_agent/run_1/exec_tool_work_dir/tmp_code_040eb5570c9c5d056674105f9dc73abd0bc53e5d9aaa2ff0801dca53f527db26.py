code = """import json
import os

# Get the file paths from the locals() dictionary
civic_docs_path = locals().get('var_functions.query_db:92')
funding_path = locals().get('var_functions.query_db:93')

# Check if we have the file paths
if not civic_docs_path or not funding_path:
    # Try alternative approach - read directly from temp files
    try:
        civic_docs = json.load(open('/tmp/tmpt0l6v2gk.json'))
        funding_data = json.load(open('/tmp/tmpo2f_7tij.json'))
    except:
        result = {'error': 'Cannot access data files'}
        print('__RESULT__:')
        print(json.dumps(result))
        exit(0)
else:
    # Load from the file paths
    try:
        civic_docs = json.load(open(civic_docs_path))
        funding_data = json.load(open(funding_path))
    except Exception as e:
        result = {'error': str(e)}
        print('__RESULT__:')
        print(json.dumps(result))
        exit(0)

# Process the data
spring_months = ['March', 'April', 'May', 'Spring']
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if '2022' in line and any(month in line for month in spring_months):
            # Look backwards for project name (up to 5 lines back)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if (prev_line and len(prev_line) > 8 and prev_line[0].isupper() and
                    ':' not in prev_line and 'Page' not in prev_line and
                    'Item' not in prev_line and 'Agenda' not in prev_line):
                    spring_projects.add(prev_line)
                    break

# Create a mapping of project names to funding amounts
funding_map = {}
for fund in funding_data:
    funding_map[fund['Project_Name'].lower()] = int(fund['Amount'])

# Calculate total funding for Spring 2022 projects
total_funding = 0
matched_projects = 0

for proj in spring_projects:
    proj_lower = proj.lower()
    # Try to match with funding data
    for fund_name, amount in funding_map.items():
        if (proj_lower == fund_name or 
            proj_lower in fund_name or 
            fund_name in proj_lower):
            total_funding += amount
            matched_projects += 1
            break

result = {
    'spring_2022_project_count': len(spring_projects),
    'total_funding_usd': total_funding,
    'projects_with_funding': matched_projects,
    'unfunded_projects': len(spring_projects) - matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'City Hall Roof Replacement', 'Amount': '79000'}, {'Project_Name': 'City Hall Solar Project', 'Amount': '38000'}, {'Project_Name': 'City Traffic Signals Backup Power', 'Amount': '85000'}, {'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Amount': '10000'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Amount': '30000'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Amount': '64000'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Amount': '45000'}, {'Project_Name': 'Civic Center Way Improvements', 'Amount': '37000'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:93': 'file_storage/functions.query_db:93.json'}

exec(code, env_args)
