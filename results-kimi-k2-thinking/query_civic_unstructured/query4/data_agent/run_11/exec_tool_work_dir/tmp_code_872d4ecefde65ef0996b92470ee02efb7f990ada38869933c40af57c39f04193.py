code = """import json

# Load civic documents to verify the 2022 projects
civic_docs_file = locals()['var_functions.query_db:48']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Define Spring 2022 indicators
spring_indicators = [
    '2022-Spring',
    'Spring 2022',
    '2022-March',
    '2022-April',
    '2022-May',
    'March 2022',
    'April 2022',
    'May 2022'
]

# Check if documents mention these projects with Spring 2022
target_projects = [
    '2022 Annual Street Maintenance',
    '2022 Morning View Resurfacing & Storm Drain Improvements'
]

verified_projects = []
for project_name in target_projects:
    project_found = False
    spring_found = False
    
    for doc in civic_docs:
        text = doc.get('text', '')
        
        # Check if project name appears
        if project_name in text:
            project_found = True
            
            # Check if Spring 2022 appears in same document
            if any(indicator in text for indicator in spring_indicators):
                spring_found = True
                break
    
    verified_projects.append({
        'project_name': project_name,
        'project_mentioned': project_found,
        'spring_2022_mentioned': spring_found
    })

print('__RESULT__:')
print(json.dumps(verified_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:18': {'documents_with_spring_2022': 5, 'sample_filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:45': 'file_storage/functions.query_db:45.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:49': 'file_storage/functions.query_db:49.json', 'var_functions.execute_python:52': {'spring_2022_count': 1, 'funded_2022_projects': 2, 'sample_projects': ['2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements']}, 'var_functions.execute_python:54': {'number_of_projects': 2, 'total_funding': 83000, 'projects': [{'project_name': '2022 Annual Street Maintenance', 'amount': 45000}, {'project_name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}]}}

exec(code, env_args)
