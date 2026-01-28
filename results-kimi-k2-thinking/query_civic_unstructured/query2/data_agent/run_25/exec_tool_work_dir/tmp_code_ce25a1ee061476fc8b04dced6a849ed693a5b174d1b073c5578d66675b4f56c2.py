code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

completed_park_projects = []
for doc in civic_docs:
    doc_text = doc.get('text', '')
    lines = doc_text.split(chr(10))
    for i in range(len(lines)):
        line = lines[i]
        if 'park' in line.lower() and len(line.strip()) > 10:
            if 'capital improvement' not in line.lower() and 'agenda report' not in line.lower():
                for j in range(i, min(i+15, len(lines))):
                    next_line = lines[j].lower()
                    if 'completed' in next_line and '2022' in next_line:
                        if line.strip() not in completed_park_projects:
                            completed_park_projects.append(line.strip())
                        break

funding_matches = []
total_funding = 0
for project in completed_park_projects:
    if project in funding_dict:
        funding_matches.append({'project': project, 'amount': funding_dict[project]})
        total_funding += funding_dict[project]
    else:
        for funding_project, amount in funding_dict.items():
            if 'park' in funding_project.lower():
                if project.split()[0].lower() in funding_project.lower():
                    funding_matches.append({'project': funding_project, 'amount': amount})
                    total_funding += amount
                    break

result = {'completed_park_projects': completed_park_projects, 'funding_matches': funding_matches, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:14': {'park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'all_completed_2022': [], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'amount': 21000}, {'project': 'Permanent Skate Park', 'amount': 97000}], 'total_funding': 118000}}

exec(code, env_args)
