code = """import json

# Get file paths
civic_path = var_functions.query_db:50
funding_path = var_functions.query_db:48

# Read data
with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_list = json.load(f)

# Find projects that started Spring 2022
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line:
            # Check if it mentions spring months
            has_spring = any(m in line for m in ['March', 'April', 'May', 'Spring'])
            if has_spring:
                # Look for project name before this line
                for j in range(max(0, i-8), i):
                    prev = lines[j].strip()
                    if prev and len(prev) > 8 and prev[0].isupper():
                        bad_words = ['Updates:', 'Schedule:', 'Agenda', 'Page']
                        if not any(b in prev for b in bad_words):
                            spring_projects.add(prev)
                            break

# Match with funding
project_funding = {}
total = 0

for proj in spring_projects:
    for fund in funding_list:
        name = fund['Project_Name']
        # Simple match by checking if one contains the other
        proj_clean = proj.lower().replace(' project', '')
        fund_clean = name.lower().replace(' project', '')
        if proj_clean in fund_clean or fund_clean in proj_clean:
            amt = int(fund['Amount'])
            project_funding[proj] = amt
            total += amt
            break

result = {
    'spring_2022_count': len(spring_projects),
    'total_funding': total,
    'examples': list(spring_projects)[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'City Hall Roof Replacement', 'Amount': '79000'}, {'Project_Name': 'City Hall Solar Project', 'Amount': '38000'}, {'Project_Name': 'City Traffic Signals Backup Power', 'Amount': '85000'}, {'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Amount': '10000'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Amount': '30000'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Amount': '64000'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Amount': '45000'}, {'Project_Name': 'Civic Center Way Improvements', 'Amount': '37000'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
