code = """import json
civic_docs = json.load(open(var_functions.query_db:0))
park_projects = []
for doc in civic_docs:
    for line in doc['text'].split('\n'):
        if 'park' in line.lower() and '2022' in doc['text']:
            if 'completed' in line.lower():
                park_projects.append(line.strip())
            else:
                # Check nearby lines
                lines = doc['text'].split('\n')
                idx = lines.index(line)
                for j in range(idx, min(idx+10, len(lines))):
                    if 'completed' in lines[j].lower() and '2022' in lines[j].lower():
                        park_projects.append(line.strip())
                        break

unique = list(set(park_projects))
result = json.dumps({'count': len(unique), 'projects': unique[:50]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
