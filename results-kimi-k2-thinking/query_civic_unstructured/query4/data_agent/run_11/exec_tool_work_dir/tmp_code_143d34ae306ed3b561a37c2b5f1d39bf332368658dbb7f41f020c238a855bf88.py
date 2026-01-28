code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:0']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_data = locals()['var_functions.query_db:2']

spring_2022_projects = []
spring_patterns = ['2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May', 'March 2022', 'April 2022', 'May 2022']

for doc in civic_docs:
    text = doc.get('text', '')
    has_spring_2022 = any(pattern in text for pattern in spring_patterns)
    
    if has_spring_2022:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if not line_clean or len(line_clean) < 5:
                continue
            skip_patterns = ['Page ', 'Agenda Item', 'To:', 'From:', 'Subject:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:']
            if any(skip in line_clean for skip in skip_patterns):
                continue
            if line_clean[0].isupper() and not line_clean.endswith(('.', '!', '?')):
                context_start = max(0, i-5)
                context_end = min(len(lines), i+10)
                context = ' '.join(lines[context_start:context_end])
                if any(pattern in context for pattern in spring_patterns):
                    spring_2022_projects.append({'project_name': line_clean, 'source_file': doc.get('filename', '')})

unique_projects = []
seen_names = set()
for proj in spring_2022_projects:
    if proj['project_name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['project_name'])

project_funding = []
for proj in unique_projects:
    proj_name = proj['project_name']
    for fund in funding_data:
        if fund['Project_Name'] == proj_name:
            project_funding.append({
                'project_name': proj_name,
                'funding_id': fund['Funding_ID'],
                'funding_source': fund['Funding_Source'],
                'amount': int(fund['Amount'])
            })

total_projects = len(unique_projects)
total_funding = sum(f['amount'] for f in project_funding)

result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_details': project_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
