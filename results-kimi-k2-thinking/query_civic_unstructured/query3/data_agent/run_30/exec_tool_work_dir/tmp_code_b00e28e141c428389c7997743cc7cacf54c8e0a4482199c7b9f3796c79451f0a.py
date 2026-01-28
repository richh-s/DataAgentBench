code = """import json
import re

# Load data from files
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

results = []

# Step 1: Find funding records with FEMA or emergency
for item in funding_data:
    proj_name = item['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

# Step 2: Process civic documents
funding_dict = {item['Project_Name']: item for item in funding_data}

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Skip headers (using simpler check)
        lower_line = line.lower()
        if 'capital improvement' in lower_line or 'disaster recovery' in lower_line:
            continue
        if 'status report' in lower_line or 'project schedule' in lower_line:
            continue
        if line.startswith('Page') or line.startswith('Item #'):
            continue
        
        if 'FEMA' in line or 'emergency' in lower_line:
            project_name = ''
            if 10 <= len(line) <= 150 and not line.startswith('('):
                clean_line = re.sub(r'\s+', ' ', line).strip()
                clean_line = re.sub(r'^[•\-\*\d\.\)]+\s*', '', clean_line)
                project_name = clean_line
            
            if not project_name and i > 0:
                prev_line = lines[i-1].strip()
                if 10 <= len(prev_line) <= 150:
                    clean_prev = re.sub(r'\s+', ' ', prev_line).strip()
                    clean_prev = re.sub(r'^[•\-\*\d\.\)]+\s*', '', clean_prev)
                    project_name = clean_prev
            
            if project_name:
                status = 'unknown'
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'design' in next_line:
                        status = 'design'
                        break
                    elif 'construction' in next_line:
                        status = 'construction'
                        break
                    elif 'completed' in next_line:
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                
                if project_name in funding_dict:
                    funding = funding_dict[project_name]
                    results.append({
                        'Project_Name': project_name,
                        'Funding_Source': funding['Funding_Source'],
                        'Amount': int(funding['Amount']),
                        'Status': status,
                        'Topic': 'FEMA,emergency'
                    })

# Remove duplicates and finalize
unique_dict = {}
for proj in results:
    unique_dict[proj['Project_Name']] = proj

final_results = []
for name, proj in unique_dict.items():
    final_results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': proj['Status'],
        'Topic': proj['Topic']
    })

final_results.sort(key=lambda x: x['Project_Name'])

print('Projects found:', len(final_results))
print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
