code = """import json

# Load funding data
funding_data = locals()['var_functions.query_db:2']

# Load civic documents
civic_file = locals()['var_functions.query_db:32']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(civic_docs)} documents and {len(funding_data)} funding records')

# Search for Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for Spring 2022 date patterns
    if ('2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text)):
        # Look for specific Spring 2022 mentions
        if '2022-Spring' in text or 'Spring 2022' in text:
            spring_2022_projects.append({
                'filename': filename,
                'has_spring_2022': True
            })
        # Also check for month-year patterns  
        elif '2022-March' in text or 'March 2022' in text or '2022-April' in text or 'April 2022' in text or '2022-May' in text or 'May 2022' in text:
            spring_2022_projects.append({
                'filename': filename,
                'has_spring_2022': True
            })

print(f'Documents mentioning Spring 2022: {len(spring_2022_projects)}')
print('Sample filenames:', [p['filename'] for p in spring_2022_projects[:10]])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:18': {'documents_with_spring_2022': 5, 'sample_filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
