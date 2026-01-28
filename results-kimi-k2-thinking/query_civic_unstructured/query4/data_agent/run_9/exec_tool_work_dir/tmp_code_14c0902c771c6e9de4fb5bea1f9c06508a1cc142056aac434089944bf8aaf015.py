code = """import json

# Load data
civic_file = locals()['var_functions.query_db:32']
funding_file = locals()['var_functions.query_db:33']

if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Create funding lookup map
funding_map = {}
for f in funding_data:
    name = f['Project_Name']
    amt = int(f['Amount'])
    funding_map[name] = amt
    
    # Add base name without parentheses
    base_name = name.split('(')[0].strip()
    if base_name != name:
        funding_map[base_name] = funding_map.get(base_name, 0) + amt

# Extract Spring 2022 projects using simple text search
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Find lines with 2022 and spring months
        has_2022 = '2022' in line
        has_spring = any(x in line for x in ['Spring', 'spring', 'March', 'April', 'May', 'Mar', 'Apr'])
        
        if has_2022 and has_spring:
            # Look backward for project name
            for j in range(max(0, i-5), i):
                prev = lines[j].strip()
                
                # Check if it looks like a project name
                if len(prev) > 10 and prev[0].isupper():
                    if not any(skip in prev for skip in ['Agenda', 'Page', 'To:', 'From:', 'Prepared', 'Approved']):
                        words = prev.split()
                        cap_words = [w for w in words if w and w[0].isupper()]
                        
                        if len(cap_words) >= 2:
                            spring_projects.add(prev)

# Match with funding
results = []
total = 0

for project in spring_projects:
    amt = 0
    match = None
    
    # Direct match
    if project in funding_map:
        amt = funding_map[project]
        match = project
    else:
        # Partial match
        for fund_name in funding_map:
            if project.lower() in fund_name.lower() or fund_name.lower() in project.lower():
                if len(project) > 15:  # Avoid too short matches
                    amt = funding_map[fund_name]
                    match = fund_name
                    break
    
    if amt > 0:
        results.append({'project': project, 'funding': match, 'amount': amt})
        total += amt

# Sort by amount
results.sort(key=lambda x: x['amount'], reverse=True)

final_result = {
    'projects_matched': len(results),
    'total_funding': total,
    'details': results[:15]
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
