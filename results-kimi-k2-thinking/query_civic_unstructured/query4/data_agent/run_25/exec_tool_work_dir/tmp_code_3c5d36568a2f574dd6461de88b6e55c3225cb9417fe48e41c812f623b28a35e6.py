code = """import json, os, re

# Read the file paths
civic_file = locals()['var_functions.query_db:38']
funding_file = locals()['var_functions.query_db:28']

# Load data
civic_docs = json.load(open(civic_file, 'r'))
funding_data = json.load(open(funding_file, 'r'))

# Create funding map
funding_map = {}
for rec in funding_data:
    name = rec['Project_Name']
    amt = int(str(rec['Amount']))
    funding_map[name] = amt

# Find Spring 2022 projects and their funding
spring_2022_projects = []
total_funding = 0

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for Spring 2022 mentions and nearby project names
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if '2022' in line_lower and 'spring' in line_lower:
            # Look backwards for the project name (typically uppercase)
            for j in range(i-1, max(-1, i-5), -1):
                prev_line = lines[j].strip()
                if prev_line.isupper() and len(prev_line) > 10:
                    proj_name = prev_line
                    # Get funding
                    if proj_name in funding_map:
                        funding = funding_map[proj_name]
                        total_funding += funding
                        spring_2022_projects.append({
                            'name': proj_name,
                            'funding': funding
                        })
                    break

result = {
    'count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': spring_2022_projects
}

print(json.dumps({'result': result}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.execute_python:26': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:28': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
