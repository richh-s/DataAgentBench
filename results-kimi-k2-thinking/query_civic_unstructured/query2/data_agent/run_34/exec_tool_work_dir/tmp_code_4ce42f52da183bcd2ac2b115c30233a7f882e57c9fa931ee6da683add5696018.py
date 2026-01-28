code = """import json
import re

civic_docs_file = var_functions.query_db:0
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

park_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        # Simple pattern to find park projects completed in 2022
        pattern = 'park'
        for line in text.split('\n'):
            if 'park' in line.lower() and len(line) < 100:
                # Check if this project was completed in 2022
                if '2022' in text and 'completed' in text.lower():
                    park_projects_2022.append(line.strip())
                break

# Remove duplicates
unique_projects = list(set(park_projects_2022))
result = {'count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
