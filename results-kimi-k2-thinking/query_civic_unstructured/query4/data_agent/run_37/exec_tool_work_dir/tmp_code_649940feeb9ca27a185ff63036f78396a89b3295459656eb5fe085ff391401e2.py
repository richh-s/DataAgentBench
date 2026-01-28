code = """import json, os

# Load funding data from file
funding_file = "/tmp/tmp4n6h1h4h.json"
funding_list = []
if os.path.exists(funding_file):
    f = open(funding_file, 'r')
    funding_list = json.load(f)
    f.close()

print('Funding count=' + str(len(funding_list)))

# Load civic documents from file  
civic_file = "/tmp/tmp4p5a1c3b.json"
civic_list = []
if os.path.exists(civic_file):
    f = open(civic_file, 'r')
    civic_list = json.load(f)
    f.close()

print('Civic docs count=' + str(len(civic_list)))

# Find Spring 2022 projects
spring_projects = []

for doc in civic_list:
    text = doc.get('text','')
    for line in text.splitlines():
        clean_line = line.strip()
        if len(clean_line) > 5 and '2022' in clean_line:
            if not clean_line.startswith('(') and not clean_line.startswith('Page'):
                # Check for Spring
                if 'Spring' in clean_line or 'spring' in clean_line:
                    spring_projects.append(clean_line)

# Remove duplicates
unique_projects = list(set(spring_projects))
print('Spring projects=' + str(len(unique_projects)))

# Match funding
matched = []
for fund in funding_list:
    fund_name = fund.get('Project_Name','').lower()
    for proj in unique_projects:
        if fund_name in proj.lower() and len(fund_name) > 5:
            matched.append(int(fund.get('Amount',0)))
            break

print('Matches=' + str(len(matched)))
print('Total=' + str(sum(matched)))

result = {'projects': len(unique_projects), 'funding': sum(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'status': 'checked'}, 'var_functions.execute_python:36': {'checked': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'count': '500', 'total_funding': '28094000'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
