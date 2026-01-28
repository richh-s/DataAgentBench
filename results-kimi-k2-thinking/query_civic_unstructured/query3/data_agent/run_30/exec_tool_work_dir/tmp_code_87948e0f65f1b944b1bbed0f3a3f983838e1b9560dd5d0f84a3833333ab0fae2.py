code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

results = []

# Add projects with FEMA/emergency in name from funding data
for item in funding_data:
    name = item['Project_Name']
    if 'FEMA' in name or 'emergency' in name.lower():
        results.append({
            'Project_Name': name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = item

# Process civic documents
for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip short lines and headers
        if len(line) < 10:
            continue
        lower = line.lower()
        if 'capital improvement' in lower or 'status report' in lower:
            continue
        if line.startswith('Page'):
            continue
        
        # Check for FEMA or emergency
        if 'FEMA' in line or 'emergency' in lower:
            # Find project name
            project_name = ''
            if len(line) <= 150 and not line.startswith('('):
                project_name = line
            elif i > 0:
                prev = lines[i-1].strip()
                if len(prev) <= 150:
                    project_name = prev
            
            if project_name:
                # Clean name
                project_name = re.sub(r'\s+', ' ', project_name).strip()
                
                # Get status
                status = 'unknown'
                for j in range(i+1, min(i+10, len(lines))):
                    nxt = lines[j].strip().lower()
                    if 'design' in nxt:
                        status = 'design'
                        break
                    if 'construction' in nxt:
                        status = 'construction'
                        break
                    if 'completed' in nxt:
                        status = 'completed'
                        break
                
                # Add if has funding
                if project_name in funding_lookup:
                    fund = funding_lookup[project_name]
                    results.append({
                        'Project_Name': project_name,
                        'Funding_Source': fund['Funding_Source'],
                        'Amount': int(fund['Amount']),
                        'Status': status,
                        'Topic': 'FEMA,emergency'
                    })

# Remove duplicates
unique = {}
for r in results:
    unique[r['Project_Name']] = r

final = []
for name in sorted(unique.keys()):
    p = unique[name]
    final.append({
        'Project_Name': p['Project_Name'],
        'Funding_Source': p['Funding_Source'],
        'Amount': p['Amount'],
        'Status': p['Status'],
        'Topic': p['Topic']
    })

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
