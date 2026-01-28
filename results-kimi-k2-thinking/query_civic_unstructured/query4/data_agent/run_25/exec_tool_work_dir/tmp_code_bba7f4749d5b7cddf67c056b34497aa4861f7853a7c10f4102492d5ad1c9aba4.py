code = """import json, os

# Read civic documents
civic_file = 'file_storage/functions.query_db:38.json'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project names that started in Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        if '2022' in line_lower and 'spring' in line_lower:
            spring_2022_projects.append(line.strip())

# Read funding data
funding_file = 'file_storage/functions.query_db:28.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding map
funding_map = {}
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
    except:
        amount = 0
    funding_map[record.get('Project_Name', '')] = amount

# Try to match and calculate funding
total_funding = 0
matched = []

for project_line in spring_2022_projects:
    # Look for project name in the same line or nearby
    # This is a simplified approach - in real data, we'd need better parsing
    if '2022 Morning View' in project_line:
        total_funding += funding_map.get('2022 Morning View Resurfacing & Storm Drain Improvements', 0)
        matched.append('2022 Morning View Resurfacing & Storm Drain Improvements')

print('__RESULT__:')
print(json.dumps({
    'project_lines': spring_2022_projects,
    'matched': matched,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.execute_python:26': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:28': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
