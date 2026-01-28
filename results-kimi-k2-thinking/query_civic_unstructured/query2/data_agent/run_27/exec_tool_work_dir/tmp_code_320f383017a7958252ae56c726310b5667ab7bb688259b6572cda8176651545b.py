code = """import json, re

# Load the civic documents from the file path
civic_docs_path = locals()['var_functions.query_db:16']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded %d civic documents' % len(civic_docs))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        # Check if this line mentions completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for project name in surrounding lines
            for j in range(max(0, i-5), min(len(lines), i+5)):
                nearby_line = lines[j].strip()
                # Check if this is a park-related project name
                if nearby_line and 'park' in nearby_line.lower() and len(nearby_line) > 5:
                    # Clean up the project name
                    clean_name = nearby_line.replace('•', '').replace('◦', '').strip()
                    # Remove common prefixes
                    clean_name = re.sub(r'^[A-Z]\.?\s+', '', clean_name)
                    if clean_name and clean_name not in park_projects_2022:
                        park_projects_2022.append(clean_name)
                        print('Found park project completed in 2022: %s' % clean_name)

print('\nTotal park projects found: %d' % len(park_projects_2022))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:85': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}]}

exec(code, env_args)
