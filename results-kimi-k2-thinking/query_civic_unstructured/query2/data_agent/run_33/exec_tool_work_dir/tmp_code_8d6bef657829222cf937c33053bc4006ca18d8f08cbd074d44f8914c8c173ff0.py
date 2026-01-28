code = """import json

# Load the data from the stored files
civic_file = locals()['var_functions.query_db:26']
funding_file = locals()['var_functions.query_db:8']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    if 'text' in doc:
        text = doc['text']
        if 'Construction was completed' in text and '2022' in text and ('park' in text.lower() or 'playground' in text.lower()):
            # Extract project names from lines that mention parks/playgrounds
            lines = text.split('\n')
            for i in range(len(lines)):
                line = lines[i].strip()
                lower_line = line.lower()
                if ('park' in lower_line or 'playground' in lower_line) and 'construction was completed' not in line.lower():
                    # Check next few lines for completion in 2022
                    for j in range(i+1, min(i+4, len(lines))):
                        next_line = lines[j].lower()
                        if 'construction was completed' in next_line and '2022' in next_line:
                            park_projects_2022.append(line)
                            break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding data
matching_projects = []
total_funding = 0

for proj in park_projects_2022:
    # Search funding data
    for fund in funding_data:
        if proj.lower() in fund['Project_Name'].lower() or fund['Project_Name'].lower() in proj.lower():
            matching_projects.append({'project': fund['Project_Name'], 'amount': int(fund['Amount'])})
            total_funding += int(fund['Amount'])
            break

# Print result
print('__RESULT__:')
print(json.dumps({
    'park_projects': park_projects_2022,
    'matches': matching_projects,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'has_funding': False, 'has_civic': False}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
