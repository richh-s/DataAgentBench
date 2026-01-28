code = """import json

# Get the list of projects that started in Spring 2022 from civic docs
civic_file = locals()['var_functions.query_db:148']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Get funding for these projects
funding_file = locals()['var_functions.query_db:150']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# List of Spring 2022 projects identified from civic documents
spring_2022_projects = [
    'Marie Canyon Green Streets',
    'PCH Median Improvements Project',
    'PCH Signal Synchronization System Improvements Project',
    'Westward Beach Road Improvements Project',
    'Bluffs Park Shade Structure',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'
]

# Calculate total funding
project_count = len(funding_data)
total_funding = sum(int(item['Amount']) for item in funding_data)

print('Projects that started in Spring 2022:', project_count)
print('Total funding:', total_funding)

result = {'count': project_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.execute_python:126': {'funding_projects': 500, 'spring_references': 4}, 'var_functions.query_db:148': 'file_storage/functions.query_db:148.json', 'var_functions.query_db:150': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Marie Canyon Green Streets', 'Amount': '50000'}, {'Project_Name': 'PCH Median Improvements Project', 'Amount': '56000'}, {'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'Amount': '16000'}, {'Project_Name': 'PCH at Trancas Canyon Road Right Turn Lane', 'Amount': '90000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Westward Beach Road Improvements Project', 'Amount': '29000'}]}

exec(code, env_args)
