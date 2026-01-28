code = """import json

# Load all data
civic_docs_file = locals()['var_functions.query_db:48']
funding_file = locals()['var_functions.query_db:49']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find projects with 2022 in their name from funding data
projects_2022 = []
total_funding = 0

for fund in funding_data:
    if '2022' in fund['Project_Name']:
        projects_2022.append({
            'project_name': fund['Project_Name'],
            'amount': int(fund['Amount'])
        })
        total_funding += int(fund['Amount'])

# Search civic docs for Spring 2022 mentions
spring_mentions = 0
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'Spring' in text:
        spring_mentions += 1

result = {
    'number_of_projects': len(projects_2022),
    'total_funding': total_funding,
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:18': {'documents_with_spring_2022': 5, 'sample_filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:45': 'file_storage/functions.query_db:45.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:52': {'spring_2022_count': 1, 'funded_2022_projects': 2, 'sample_projects': ['2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements']}}

exec(code, env_args)
