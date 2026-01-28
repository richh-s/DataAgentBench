code = """import json

civic_docs_file = '/tmp/civic_docs.json'
funding_file = '/tmp/funding.json'

# Load data
civic_docs = json.load(open(civic_docs_file))
funding = json.load(open(funding_file))

spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Look for Spring 2022 patterns
    if 'spring 2022' in text.lower() or '2022-spring' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if len(line_clean) > 15 and line_clean[0].isupper() and not line_clean.startswith('Page') and not line_clean.startswith('Item'):
                if 'PUBLIC WORKS' not in line_clean and 'COMMISSION' not in line_clean:
                    spring_2022_projects.add(line_clean)

# Count funding
total_funding = sum(int(f['Amount']) for f in funding if '2022' in f['Project_Name'])

result = {'count': len(spring_2022_projects), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}], 'var_functions.execute_python:64': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.query_db:70': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}

exec(code, env_args)
