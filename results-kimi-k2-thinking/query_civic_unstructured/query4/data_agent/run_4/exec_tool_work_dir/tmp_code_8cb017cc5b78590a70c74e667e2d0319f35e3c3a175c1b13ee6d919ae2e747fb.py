code = """import json
import re

# Load data from stored variables
civic_docs = json.load(open(locals()['var_functions.query_db:50']))
funding_data = json.load(open(locals()['var_functions.query_db:60']))

# Create funding lookup
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name','')
    if name:
        funding_lookup[name] = int(rec.get('Amount',0))

# Find Spring 2022 projects
spring2022 = set()
project_funding = {}

for doc in civic_docs:
    text = doc.get('text','')
    if 'Spring 2022' in text or '2022-Spring' in text:
        for fund_name in funding_lookup:
            if fund_name in text:
                spring2022.add(fund_name)
                project_funding[fund_name] = funding_lookup[fund_name]

# Also try pattern matching for project names
project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Road', 'Park', 'Drainage', 'System']
for doc in civic_docs:
    text = doc.get('text','')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 10 < len(line) < 150 and any(k in line for k in project_keywords):
                if not line.startswith('(') and not line.startswith('To:'):
                    # Try to match this line with funding
                    for fund_name in funding_lookup:
                        if fund_name not in project_funding:
                            if line.lower() in fund_name.lower() or fund_name.lower() in line.lower():
                                spring2022.add(fund_name)
                                project_funding[fund_name] = funding_lookup[fund_name]
                                break

count = len(project_funding)
total = sum(project_funding.values())

result = {'project_count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
