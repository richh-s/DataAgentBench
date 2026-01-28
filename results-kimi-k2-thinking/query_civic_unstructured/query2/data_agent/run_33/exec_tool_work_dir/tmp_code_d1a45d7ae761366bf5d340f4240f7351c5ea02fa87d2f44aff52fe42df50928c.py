code = """import json

# Get file paths
civic_file = locals()['var_functions.query_db:34']
funding_file = locals()['var_functions.query_db:8']

# Load data
with open(civic_file) as cf:
    civic_docs = json.load(cf)
with open(funding_file) as ff:
    funding_data = json.load(ff)

# Find all park projects completed in 2022 from civic documents
park_projects = []

for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Construction was completed' in txt and '2022' in txt:
        lines = txt.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for lines with park/playground that have completion info nearby
            if ('park' in line.lower() or 'playground' in line.lower()):
                # Check following lines for completion in 2022
                for j in range(i+1, min(i+4, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'construction was completed' in next_line and '2022' in next_line:
                        if line and not line.startswith('(') and len(line) < 150:
                            park_projects.append(line)
                        break

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding data
found = []
total = 0

for park in park_projects:
    for fund in funding_data:
        if park == fund['Project_Name']:
            amt = int(fund['Amount'])
            found.append({'project': park, 'amount': amt})
            total += amt
            break

result = json.dumps({
    'projects': park_projects,
    'funded_projects': found,
    'total_funding': total
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'has_funding': False, 'has_civic': False}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
