code = """import json
import re

# Load the data files
civic_docs_file = var_functions.query_db_28
funding_file = var_functions.query_db_29

civic_docs = json.loads(open(civic_docs_file).read())
funding_data = json.loads(open(funding_file).read())

# Create funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find disaster-related projects from funding
print('Funding dict has', len(funding_dict), 'projects')

# Check for FEMA/CalOES/CalJPIA in project names
disaster_projects = []
for project_name in funding_dict.keys():
    if any(keyword in project_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA']):
        disaster_projects.append(project_name)

print('Found', len(disaster_projects), 'disaster-related projects in funding data')
print('First few:', disaster_projects[:5])

# Combine all civic document text
all_text = ' '.join([doc.get('text', '') for doc in civic_docs])
print('Total document text length:', len(all_text))

# For simplicity, let's just total all disaster project funding first
total_disaster_funding = sum(funding_dict[name] for name in disaster_projects)
result = f"Total funding for disaster-related projects: ${total_disaster_funding:,}"
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['Funding'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json'}

exec(code, env_args)
