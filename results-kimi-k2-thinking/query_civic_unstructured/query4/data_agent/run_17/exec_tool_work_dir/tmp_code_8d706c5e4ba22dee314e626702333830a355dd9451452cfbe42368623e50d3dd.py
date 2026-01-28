code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:5']
funding_path = locals()['var_functions.query_db:20']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_dict = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_dict[project_name] = funding_dict.get(project_name, 0) + amount

spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 100:
            continue
        
        # Skip headers and labels
        if any(word in line for word in ['Projects (', 'Page', 'To:', 'From:', 'Subject:', 'Date:', 'Updates:', 'Schedule:']):
            continue
        
        if line.isupper():
            continue
        
        # Check for date patterns nearby
        context = ' '.join(lines[max(0,i-5):min(len(lines),i+10)])
        
        if '2022' in context:
            # Check for spring indicators
            spring_indicators = ['Spring 2022', 'March 2022', 'April 2022', 'May 2022', 'Spring']
            if any(indicator.lower() in context.lower() for indicator in spring_indicators):
                if 'Project Schedule:' in context or 'Updates:' in context or '(cid:' in context:
                    spring_2022_projects.add(line)

# Match with funding
matches = {}
for project in spring_2022_projects:
    for funded in funding_dict:
        # Create a simple matching score
        project_words = set(project.lower().split())
        funded_words = set(funded.lower().split())
        
        # Check overlap
        common = project_words.intersection(funded_words)
        if len(common) >= 2 or (len(project_words) <= 3 and len(common) >= 1):
            matches[project] = funding_dict[funded]
            break

result = {
    'count': len(matches),
    'total_funding': sum(matches.values()),
    'details': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
